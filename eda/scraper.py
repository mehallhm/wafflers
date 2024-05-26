"""
TODO
"""

import requests
import pandas as pd
import numpy as np

def parse_df_from_eurostat(values: dict[str: str], tables: list[str], rows: list[str], cols: list[str], label:str="", col_label:str="") -> list[pd.DataFrame]:
	"""
	Given a dict of indexed scaler values and the label lists, parse into a list of dataframes
	Note: Across all tables, the size (row x col) should be the same!

	:param values: A dict with indexed scaler values, ie {'572': 145.5} where the index is the cell that value occupies
	:param tables: A list of the table labels
	:param rows: A list of row labels
	:param cols: A list of column labels 
	:param label: The optional column label for the row keys
	:param col_label: The optional label for the column header group
	:returns: A dataframe with multiindexes for each table
	"""
	calc_index = lambda i, j, k: k + (j * len(cols)) + (i * (len(cols) * len(rows)))
	data_3d = []
	for i in range(len(tables)):
		data_2d = []
		for j in range(len(rows)):
			builder_row = []
			for k in range(len(cols)):
				if str(calc_index(i, j, k)) in values:
					builder_row.append(values[str(calc_index(i, j, k))])
				else:
					builder_row.append(np.NaN)
			data_2d.append(builder_row)
		data_3d.append(data_2d)
	

	dataframes = []
	for table in data_3d:
		df = pd.DataFrame(table)
		dataframes.append(df)
	
	df = pd.concat(dataframes, axis=1)
	cols = [l[0] for l in cols]
	df.columns = pd.MultiIndex.from_product([tables, cols], names=["table", col_label])
	if label:
		df[label] = [i[0] for i in rows]

	return df


def scrape_sdg_07_40() -> tuple[pd.DataFrame, list[str]]:
	"""
	Scrapes the `sdg_07_40` dataset from eurostat.

	Title: Share of renewable energy in gross final energy consumption
	  by sector
	Description: The indicator measures the share of renewable energy
	  consumption in gross final energy consumption according to the Renewable
	  Energy Directive. The gross final energy consumption is the energy used
	  by end-consumers (final energy consumption) plus grid losses and 
	  self-consumption of power plants.
	
	:returns: A tuple with the dataframe and a list of tables
	"""
	url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data" 
	params = "format=JSON&lang=EN"
	dataset = "sdg_07_40"
	res = requests.get(f"{url}/{dataset}?{params}")
	raw = res.json()

	values = raw["value"]
	rows = list(raw["dimension"]["geo"]["category"]["label"].items())
	cols = list(raw["dimension"]["time"]["category"]["label"].items())
	tables = [i[0] for i in raw["dimension"]["nrg_bal"]["category"]["label"].items()]

	return parse_df_from_eurostat(values, tables, rows, cols, label="country", col_label="time"), tables


# def parse_from_eurostat_raw(raw:dict, tables: list[str]) -> pd.DataFrame:
# 	"""
# 	Parses a dataframe from the raw eurostat output

# 	:param raw: The raw API output as a parsed dict
# 	:param tables: A list of the table names
# 	:returns: A dataframe from `parse_df_from_eurostat`
# 	"""
# 	rows = list(raw["dimension"]["geo"]["category"]["label"].items())
# 	cols = list(raw["dimension"]["time"]["category"]["label"].items())

# 	return parse_df_from_eurostat(raw["value"], tables, rows, cols, label="country", col_label="time")