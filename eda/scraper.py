"""
Gets and parses data from Eurostat through their `statistics` API
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


def get_eurostat_dataframe(dataset:str, tables:any) -> tuple[pd.DataFrame, list[str]]:
	"""
	Gets the eurostat dataframe from a given dataset id and tables function.

	:param dataset: The dataset id to scrape and parse
	:param tables: A function that takes in the raw response and returns
		a list of tables that the dataset contains
	:returns: A tuple with the dataframe and an array of the tables
	"""
	url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data" 
	params = "format=JSON&lang=EN"
	res = requests.get(f"{url}/{dataset}?{params}")
	raw = res.json()

	values = raw["value"]
	rows = list(raw["dimension"]["geo"]["category"]["label"].items())
	cols = list(raw["dimension"]["time"]["category"]["label"].items())
	tables = tables(raw)

	return parse_df_from_eurostat(values, tables, rows, cols, label="country", col_label="time"), tables


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
	dataset = "sdg_07_40"
	tables = lambda raw: [i[0] for i in raw["dimension"]["nrg_bal"]["category"]["label"].items()]

	return get_eurostat_dataframe(dataset, tables)


def scrape_sdg_13_10() -> tuple[pd.DataFrame, list[str]]:
	"""
	Scrapes the `sdg_13_10` dataset from eurostat.

	Title: Net greenhouse gas emissions
	Description: The indicator measures total national emissions (from both ESD
	  and ETS sectors) including international aviation of the so called
	    ‘Kyoto basket’ of greenhouse gases, including carbon dioxide (CO2), 
		methane (CH4), nitrous oxide (N2O), and the so-called F-gases 
		(hydrofluorocarbons, perfluorocarbons, nitrogen triflouride (NF3) and
		sulphur hexafluoride (SF6)) from all sectors of the GHG emission
		inventories (including international aviation and indirect CO2).
		The indicator is presented in two forms: as net emissions including
		land use, land use change and forestry (LULUCF) as well as excluding
		LULUCF. Using each gas’ individual global warming potential (GWP),
		they are being integrated into a single indicator expressed in units
		of CO2 equivalents. The GHG emission inventories are submitted annually
		by the EU Member States to the United Nations Framework Convention on
		Climate Change (UNFCCC).
	
	:returns: A tuple with the dataframe and a list of tables
	"""
	dataset = "sdg_13_10"
	def tables(raw:str) -> list[str]:
		"""
		Generates tables list from raw response
	
		:param raw: The raw response from eurostat
		:returns: A list of the available tables
		"""
		t = []
		for j in raw["dimension"]["src_crf"]["category"]["label"].items():
			for k in raw["dimension"]["unit"]["category"]["label"].items():
				t.append(j[0] + "_" + k[0])
		return t

	return get_eurostat_dataframe(dataset, tables)