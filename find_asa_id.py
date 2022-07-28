from algosdk.v2client import indexer
import json
import csv
import pandas as pd


indexer_address = "https://mainnet-algorand.api.purestake.io/idx2"
indexer_token = ""
headers = {
  "X-API-Key": ""
}

indexer_client = indexer.IndexerClient(indexer_token, indexer_address, headers)

creator = 'A62XRVE7ZWSXLAA4YDDI7GUMCHML2TT3JXFT3OWTVQAKOZSBGNT7FX5YQU'
limit = 4000

unit = "WWC#"
asset_ids = []

for x in range(32):
    unit_name = unit + str(x)
    print(unit_name)
    response = indexer_client.search_assets(unit= unit_name, limit=2000)
    data = response['assets']
    size = len(data)
    for x in range(size):
      index_query = data[x]
      asset_ids.append(index_query['index'])

df = pd.DataFrame(asset_ids)
df.drop_duplicates(keep='first',inplace=True)
df.to_csv('asa_ids.csv', index=False)

