"""
"""

import pandas as pd
import numpy as np
from functools import reduce

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

	merged_df = reduce(lambda l, r: pd.merge(l, r, left_on=["year", "geo"], right_on=["year", "geo"]), dataframes)
	return merged_df

def fill_holes(df: pd.DataFrame) -> pd.DataFrame:
	"""
	"""
	lin_reg = lambda X, Y: np.matmul(np.linalg.inv(np.matmul(X.T, X)), np.matmul(X.T, Y))

	dfs = []

	for name, group in df.groupby('geo'):
		cols = [[name for _ in range(len(group.index))]]
		for i in range(1, len(group.columns)):
			d = group.iloc[:, i:i+1].to_numpy()

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

			x_present = np.pad(np.arange(len(d))[present_mask].reshape(-1, 1), ((0, 0), (1, 0)), mode="constant", constant_values=1)
			y_present = d[present_mask]

			w = lin_reg(x_present, y_present)

			x_missing = np.pad(np.arange(len(d))[missing_mask].reshape(-1, 1), ((0, 0), (1, 0)), mode="constant", constant_values=1)
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
		if feat == "geo": continue
		df_standard[f'{feat}'] = ((df[feat] - df[feat].mean()) / df[feat].std())
	df_standard["geo"] = df["geo"]

	return df_standard