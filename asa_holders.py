import requests
import pandas as pd

df = pd.read_csv('asa_ids.csv')
asa_ids = df['0'].values.tolist()

address = []

count = len(asa_ids)
print(count)

for x in range(count):
    asaID = str(asa_ids[x])
    url = "https://algoindexer.algoexplorerapi.io/v2/assets/" + asaID + "/balances?currency-greater-than=0"
    
    resp = requests.get(url)
    data = resp.json()
    results = data['balances']
    values = results[0]
    address.append(values['address'])
    print(x)
    addr_df = pd.DataFrame(address)
    addr_df.drop_duplicates(keep='first',inplace=True)
    addr_df.to_csv('holder_addr.csv', index=False)


