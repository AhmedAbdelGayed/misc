#Defination: This Python function builds an item to item collaboration filering based recommendations based on a correlation matrix which can be used for lookups.
#The matrix values are correlation values between values. The values are calculated based on pandas corr function that can be called using multile values and methods to calculate correlation
#The input is a dataframe of users and products/Services usage
#Application: The application of the function can be used to determine somehow the correlation between the products/services based on customer usage. It is useful to determine how a specific product/service change can impact other products 
import os 
import pyodbc
import pandas as pd 
import math

dirname = os.path.dirname(__file__)
CORR_FILE = dirname + "\CorrelationMatrix.csv"
dbconnection = pyodbc.connect(dsn='NZPROD')  

query = "select distinct USER_ID, SERVICE_ID from USAGE_TABLE "

def constructCORRMatrix(query, dbconnection):
    df_results = pd.DataFrame(['USER_ID','SERVICE_ID'])
    df_results = pd.read_sql(query, dbconnection)
    UNIQUE_USERS = df_results.USER_ID.unique()
    UNIQUE_SERVICES = df_results.TRAIL_ID.unique()
    df = pd.DataFrame(index = UNIQUE_USERS, columns = UNIQUE_SERVICES)
    df = df.fillna(value = 0)
    services_results = pd.DataFrame(['TRAIL_ID'])
    for user in UNIQUE_USERS:
        services_results = df_results['TRAIL_ID'].where(df_results['USER_ID'] == user)
        for i in services_results.iteritems():
            if not math.isnan(i[1]):
                 df.at[int(user),int(i[1])] +=1
    dfCORR = df.corr()
    #dfCORR = df.corr(method='pearson', min_periods=5)
    dfCORR.to_csv(CORR_FILE, sep='\t', encoding=None, index=True)
    return dfCORR


constructCORRMatrix(query, dbconnection)
