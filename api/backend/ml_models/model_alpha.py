"""
The Train, Test, and Predict functions for the CO2 Emission Linear Regression
ML Model
"""

import numpy as np
import pandas as pd
import pandasdmx as sdmx
from sklearn.metrics import r2_score
from functools import reduce


def train() -> np.array:
    """
    Calculates the slopes for the CO2 emissions regression model.

    :returns: An array with the slopes in shape (3,)
    """
    estat = sdmx.Request("ESTAT")
    resp = estat.data(
        "ENV_AIR_GGE",
        key={
            "unit": "THS_T",
            "freq": "A",
            "src_crf": "TOTX4_MEMONIA",
            "airpol": "GHG"
        }
    )
    emission_df = (resp
                   .to_pandas(datetime={'dim': 'TIME_PERIOD'})
                   .droplevel(level=['unit', 'freq', 'src_crf', 'airpol'], axis=1))
    melted_emissions_df = melt_smdx_dataframe(emission_df)

    resp = estat.data(
        "NRG_D_HHQ",
        key={
            "siec": "TOTAL",
            "unit": "TJ",
            "nrg_bal": "FC_OTH_HH_E",
            "freq": "A",
        }
    )
    household_energy_df = (resp
                           .to_pandas(datetime={'dim': 'TIME_PERIOD', 'freq': 'freq'})
                           .droplevel(level=["siec", "unit", "nrg_bal"], axis=1))
    melted_household_energy_df = melt_smdx_dataframe(household_energy_df)

    resp = estat.data(
        "TEN00127",
        key={
            "unit": "KTOE",
            "freq": "A",
            "siec": "O4652XR5210B",
            "nrg_bal": "FC_TRA_ROAD_E"
        }
    )
    gas_df = (resp
              .to_pandas(datetime={'dim': 'TIME_PERIOD'})
              .droplevel(level=['unit', 'freq', 'siec', "nrg_bal"], axis=1))
    melted_gas_df = melt_smdx_dataframe(gas_df)

    merged_df = merge_dataframes([melted_emissions_df, melted_household_energy_df, melted_gas_df])
    merged_df.columns = ["year", "geo", "emissions", "energy", "gas"]
    merged_df = merged_df.drop(merged_df[(merged_df.geo == "EU27_2020") | (merged_df.geo == "EU20")].index)
    merged_df = merged_df.drop("year", axis=1)
    standard_df = standardize(merged_df)
    standard_df = standard_df.fillna(0)

    X = np.pad(standard_df.iloc[:, 1:3].to_numpy(dtype=np.float64),
               ((0, 0), (1, 0)), mode="constant", constant_values=1)
    y = np.array(standard_df["emissions"], dtype=np.float64)

    m = np.matmul(np.linalg.inv(np.matmul(X.T, X)), np.matmul(X.T, y))

    return m


def test(x: np.array, y: np.array) -> any:
    """
    Tests the CO2 emissions regression model

    :param x: The padded X features
    :param y: The y features
    :returns: The R2 value of the model w/ LOO-CV
     """
    np_remove = lambda a, i: np.concatenate([a[:i, ], a[i + 1:, ]])
    lin_reg = lambda X, Y: np.matmul(np.linalg.inv(np.matmul(X.T, X)),
                                     np.matmul(X.T, Y))

    y_pred = []
    for i in range(len(x)):
        holdout_x = x[i]

        loo_x = np_remove(x, i)
        loo_y = np_remove(y, i)
        loo_b = lin_reg(loo_x, loo_y)

        y_hat = np.matmul(holdout_x, loo_b)
        y_pred.append(y_hat)

    r2 = r2_score(y, y_pred)

    return r2


def predict(feats: list[float], beta: list[float]) -> float:
    """
    Predicts the Greenhouse Gas Emissions for an individual user in ktonnes.

    :param feats: The unpadded input features from the user:
        - Motor Gasoline in ktoes
        - Household Energy in TJ
    :param beta: The slopes (and intercept) for the trained model of shape: (3,)
    :returns: The predicted greenhouse gas emission in CO2 equiventlents
         measured in ktonnes
    """
    x = np.concatenate([np.array([1]), np.array(feats, dtype=np.float64)])
    beta = np.array(beta, dtype=np.float64)
    y_hat = np.matmul(x, beta)

    return y_hat


def melt_smdx_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Given an ESTAT smdx dataframe, convert the datetimes to years and melt

    :param df: The raw SDMX parsed dataframe from ESTAT
    :returns: A melted dataframe with the columns of:
        `year` - the year of the observation
        `geo` - the country of the observation
        `value` - the value of the observation
    """
    df = df.reset_index()
    df["year"] = df["TIME_PERIOD"].dt.year
    df = df.drop("TIME_PERIOD", axis=1)
    return pd.melt(df, id_vars="year")


def merge_dataframes(dataframes: list[pd.DataFrame]) -> pd.DataFrame:
    """
    """
    for i, df in enumerate(dataframes):
        df.columns = ["geo", "year", i]

    merged_df = reduce(lambda left, right: pd.merge(left, right, left_on=["year", "geo"], right_on=["year", "geo"]),
                       dataframes)
    return merged_df


def fill_holes(df: pd.DataFrame) -> pd.DataFrame:
    """
    """
    lin_reg = lambda X, Y: np.matmul(np.linalg.inv(np.matmul(X.T, X)), np.matmul(X.T, Y))

    dfs = []

    for name, group in df.groupby('geo'):
        cols = [[name for _ in range(len(group.index))]]
        for i in range(1, len(group.columns)):
            d = group.iloc[:, i:i + 1].to_numpy()

            missing_mask = np.isnan(d) | (d == 0)
            present_mask = ~missing_mask

            missing_mask = missing_mask.reshape(1, -1)[0]
            present_mask = present_mask.reshape(1, -1)[0]

            if not np.any(missing_mask):
                d = d.reshape(1, -1)[0]
                cols.append(d)
                continue

            if not np.any(present_mask):
                d = d.reshape(1, -1)[0]
                cols.append(d)
                continue

            x_present = np.pad(np.arange(len(d))[present_mask].reshape(-1, 1),
                               ((0, 0), (1, 0)), mode="constant", constant_values=1)
            y_present = d[present_mask]

            w = lin_reg(x_present, y_present)

            x_missing = np.pad(np.arange(len(d))[missing_mask].reshape(-1, 1),
                               ((0, 0), (1, 0)), mode="constant", constant_values=1)
            y_missing_pred = np.matmul(x_missing, w)

            d[missing_mask] = y_missing_pred
            d = d.reshape(1, -1)[0]

            cols.append(d)

        dfs.append(pd.DataFrame(cols).T)

    df_unswissed = pd.concat(dfs, axis=0)
    df_unswissed.columns = df.columns
    return df_unswissed


def standardize(df: pd.DataFrame) -> pd.DataFrame:
    """
    """
    df_standard = pd.DataFrame()
    for feat in df.columns:
        if feat == "geo":
            continue
        df_standard[f'{feat}'] = ((df[feat] - df[feat].mean()) / df[feat].std())
    df_standard["geo"] = df["geo"]

    return df_standard
