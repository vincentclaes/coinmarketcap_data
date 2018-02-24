#!/Users/vincent/anaconda3/bin/python
import requests
import time
import json
import os
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

def _construct_db_path(file_path):
    return 'sqlite:///{}/coinmarketcap_data.db'.format(file_path)

def load_to_db(df, db_path):
    disk_engine = create_engine(db_path)
    df.to_sql('crypto_data', disk_engine, if_exists='append')

def get_data():

    url = "https://api.coinmarketcap.com/v1/ticker/"

    querystring = {"limit": "200"}

    headers = {
        'cache-control': "no-cache",
        'postman-token': "559e252d-ca13-c52c-7667-107f809d9520"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    parsed_response = json.loads(response.text)

    df = pd.DataFrame(parsed_response)
    now = datetime.now()
    df['date'] = str(now.date())
    df['hour'] = now.hour
    df['minute'] = now.minute
    df['uuid'] = int(time.time())

    file_path = 'Users/vincent/Workspace/coinmarketcap_data'
    db_path = _construct_db_path(file_path)
    print '{}'.format(db_path)
    try:
        load_to_db(df, db_path)
    except OperationalError:
        db_path = _construct_db_path(os.path.dirname(os.path.realpath(__file__)))
        load_to_db(df, db_path)


if __name__ == '__main__':
    get_data()