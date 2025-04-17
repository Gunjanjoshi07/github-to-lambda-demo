import pandas as pd

def lambda_handler(event, context):
    d = {'col1': [7,8], 'col2': [9,10]}
    df = pd.DataFrame(data=d)
    print(df)
    print('third change')