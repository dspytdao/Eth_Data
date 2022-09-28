"""script to get data from dune analytics queries"""
import os
from duneanalytics.duneanalytics import DuneAnalytics
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

dune = DuneAnalytics(os.getenv('login'), os.getenv('password'))

# try to login
dune.login()

# fetch token
dune.fetch_auth_token()

QUERY=815

result_id = dune.query_result_id(query_id=QUERY)

data = dune.query_result(result_id)
data = data['data']['get_result_by_result_id']

df = pd.DataFrame(data)

final_df = pd.DataFrame(df.data.tolist(), index=df.index)
final_df.to_csv(f'bitlyWithdrawalsWeekly{QUERY}.csv', index=False)
