"""
"""

import numpy as np
import pandas as pd
import pandasdmx as sdmx
import train_helpers
from sklearn.metrics import r2_score

def train():
	"""
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
	emission_df = resp.to_pandas(datetime={'dim': 'TIME_PERIOD'}).droplevel(level=['unit', 'freq', 'src_crf', 'airpol'], axis=1)
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
	household_energy_df = resp.to_pandas(datetime={'dim': 'TIME_PERIOD', 'freq': 'freq'}).droplevel(level=["siec", "unit", "nrg_bal"], axis=1)
	melted_household_energy_df = train_helpers.melt_smdx_dataframe(household_energy_df)

	merged_df = train_helpers.merge_dataframes([melted_emissions_df, melted_household_energy_df])
	merged_df = merged_df.drop(merged_df[(merged_df.geo == "EU27_2020") | (merged_df.geo == "EU20")].index)
	merged_df = merged_df.drop("year", axis=1)
	standard_df = train_helpers.standardize(merged_df)

	df_dummies = pd.get_dummies(standard_df, dtype=int, columns=["geo"])
	df_dummies = df_dummies.fillna(0)

	#X = np.pad(df_dummies.iloc[:, 1:].to_numpy(dtype=np.float64), ((0,0), (1,0)), mode="constant", constant_values=1)
	X = np.pad(standard_df.iloc[:,1:3].to_numpy(dtype=np.float64), ((0,0), (1,0)), mode="constant", constant_values=1)
	y = np.array(df_dummies["emissions"], dtype=np.float64)

	m = np.matmul(np.linalg.inv(np.matmul(X.T, X)), np.matmul(X.T, y))

	return m

def test(X: np.array, y: np.array) -> any:
	"""
	"""
	np_remove = lambda a, i: np.concatenate([a[:i,], a[i + 1:,]])
	lin_reg = lambda X, Y: np.matmul(np.linalg.inv(np.matmul(X.T, X)), np.matmul(X.T, Y))

	y_pred = []
	for i in range(len(X)):
		holdout_X = X[i]
		
		loo_X = np_remove(X, i)
		loo_y = np_remove(Y, i)
		loo_b = lin_reg(loo_X, loo_y)

		y_hat = np.matmul(holdout_X, loo_b)
		y_pred.append(y_hat)
	
	r2 = r2_score(y, y_pred)

	return r2
	

def predict(feats:np.array, beta:np.array) -> float:
	"""
	Predict the 

	:param feats: The unpadded input features from the user
	:param beta: The slopes (and intercept) for the trained model
	:returns: The predicted value
	"""
	x = np.pad(feats, ((0, 0), (1, 0)), mode="constant", constant_values=1)
	y_hat = np.matmul(x, beta)

	return y_hat[0]