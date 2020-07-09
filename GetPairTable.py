from novadax import request_client as NovaClient
from Login import *
import pandas as pd
import matplotlib

# EDIT DATA FRAME TO JSON
# with open('file.json') as data_file:
#    json = json.load(data_file)


novaClient = NovaClient(getAccessKey(), getPrivateKey())


def getTableAssets():
    tickers = novaClient.list_tickers()
    df = pd.DataFrame(tickers['data'])
    df = df.sort_values(by=['symbol'])
    df = df[['symbol', 'lastPrice', 'ask', 'bid', 'low24h', 'open24h', 'quoteVolume24h', 'high24h', 'baseVolume24h',
             'timestamp']]
    df = df.reset_index()
    df = df.drop(['index'], axis=1)
    df.to_html('temp.html')
    print(df)
    return df


def getCoinsList():
    table = getTableAssets()
    coinList = table['symbol']
    return coinList


print(getTableAssets())
