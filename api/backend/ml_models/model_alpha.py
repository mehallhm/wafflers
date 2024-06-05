"""
The Train, Test, and Predict functions for the CO2 Emission Linear Regression
ML Model
"""

import numpy as np
import pandas as pd
import pandasdmx as sdmx
import train_helpers
from sklearn.metrics import r2_score

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
	melted_emissions_df = train_helpers.melt_smdx_dataframe(emission_df)

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
	melted_household_energy_df = train_helpers.melt_smdx_dataframe(household_energy_df)

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
	melted_gas_df = train_helpers.melt_smdx_dataframe(gas_df)

	merged_df = train_helpers.merge_dataframes([melted_emissions_df,
											  melted_household_energy_df,
											  melted_gas_df])
	merged_df.columns = ["year", "geo", "emissions", "energy", "gas"]
	merged_df = merged_df.drop(merged_df[(merged_df.geo == "EU27_2020") |
									   (merged_df.geo == "EU20")].index)
	merged_df = merged_df.drop("year", axis=1)
	standard_df = train_helpers.standardize(merged_df)

	df_dummies = pd.get_dummies(standard_df, dtype=int, columns=["geo"])
	df_dummies = df_dummies.fillna(0)

	#X = np.pad(df_dummies.iloc[:, 1:].to_numpy(dtype=np.float64),
	# ((0,0), (1,0)), mode="constant", constant_values=1)
	X = np.pad(standard_df.iloc[:,1:3].to_numpy(dtype=np.float64),
			 ((0,0), (1,0)), mode="constant", constant_values=1)
	y = np.array(df_dummies["emissions"], dtype=np.float64)

	m = np.matmul(np.linalg.inv(np.matmul(X.T, X)), np.matmul(X.T, y))

	return m


def test(X: np.array, y: np.array) -> any:
	"""
	Tests the CO2 emissions regression model

	:param X: The padded X features
	:param y: The y features
	:returns: The R2 value of the model w/ LOO-CV
	"""
	np_remove = lambda a, i: np.concatenate([a[:i,], a[i + 1:,]])
	lin_reg = lambda X, Y: np.matmul(np.linalg.inv(np.matmul(X.T, X)),
								   np.matmul(X.T, Y))

	y_pred = []
	for i in range(len(X)):
		holdout_X = X[i]
		
		loo_X = np_remove(X, i)
		loo_y = np_remove(y, i)
		loo_b = lin_reg(loo_X, loo_y)

		y_hat = np.matmul(holdout_X, loo_b)
		y_pred.append(y_hat)
	
	r2 = r2_score(y, y_pred)

	return r2
	

def predict(feats:list[float], beta:list[float]) -> float:
	"""
	Predicts the Greenhouse Gas Emissions for an inividual user in ktonnes.

	:param feats: The unpadded input features from the user:
		- Motor Gassoline in ktoes
		- Household Energy in TJ
	:param beta: The slopes (and intercept) for the trained model of shape: (3,)
	:returns: The predicted greenhouse gass emission in CO2 equiventlents
		measured in ktonnes
	"""
	x = np.pad(np.array(feats, dtype=np.float64), ((0, 0), (1, 0)),
			 mode="constant", constant_values=1)
	beta = np.array(beta, dtype=np.float64)
	y_hat = np.matmul(x, beta)

	return y_hat[0]