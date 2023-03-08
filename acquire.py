# inside acquire.py script:
from env import user, password, host
import pandas as pd

def get_sql_url(schema, u=user, p=password, h=host):
    '''
    get_sql_url will pull the credentials present from any current env
    file in the same directory as this acquire script
    and will return a connection based on what schema as handed to the 
    function call
    '''
    return f'mysql+pymysql://{u}:{p}@{h}/{schema}'

def acquire_employee_head(schema, u=user, p=password, h=host):
    '''
    acquire_employee_head will grab the first 20 rows
    of the employees table from the employees schema and return it
    as a pandas dataframe.
    
    note that this function is dependent on the schema being passed
    as employees due to the query being defined in the scope of the function
    '''
    query = 'SELECT * FROM employees LIMIT 20'
    url = get_sql_url(schema, u=u,p=p,h=h)
    return pd.read_sql(query,url)