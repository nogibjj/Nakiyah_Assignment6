import requests
import pandas as pd
import os
from io import StringIO

# Function to extract data from GitHub URL as a string
def extractData(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to download file. Status code: {response.status_code}")

# Function to clean and split the data while reading in chunks
def cleanAndSplitData(url):
    csv_data = extractData(url)
    csv_file = StringIO(csv_data)

    # Read and processing the data in chunks
    df_employeedata_list = []
    df_mentalhealth_list = []
    chunk_size = 1000  # Adjust based on dataset size
    for chunk in pd.read_csv(csv_file, chunksize=chunk_size):

        df_employeedata = chunk[['Employee_ID', 'Age', 'Job_Role', 'Industry', 'Years_of_Experience', 'Work_Location', 'Hours_Worked_Per_Week']].copy()
        df_mentalhealth = chunk[['Employee_ID', 'Mental_Health_Condition', 'Access_to_Mental_Health_Resources']].copy()
        
        # Cleaning the employee data
        df_employeedata['Age'] = pd.to_numeric(df_employeedata['Age'], errors='coerce')
        df_employeedata['Years_of_Experience'] = pd.to_numeric(df_employeedata['Years_of_Experience'], errors='coerce')
        df_employeedata['Hours_Worked_Per_Week'] = pd.to_numeric(df_employeedata['Hours_Worked_Per_Week'], errors='coerce')
        df_employeedata.dropna(inplace=True)
        
        # Cleaning the mental health data
        df_mentalhealth['Access_to_Mental_Health_Resources'] = df_mentalhealth['Access_to_Mental_Health_Resources'].map({'Yes': True, 'No': False})
        df_mentalhealth.dropna(inplace=True)
        
        # Append the cleaned chunk data to the respective lists
        df_employeedata_list.append(df_employeedata)
        df_mentalhealth_list.append(df_mentalhealth)
    
    # Concatenate all chunks into final DataFrames
    df_employeedata = pd.concat(df_employeedata_list).head(100).copy()  # Limit to 100 rows
    df_mentalhealth = pd.concat(df_mentalhealth_list).head(100).copy()
    
    return df_employeedata, df_mentalhealth


def processData(url):
    df_employeedata, df_mentalhealth = cleanAndSplitData(url)
    
    #Employee Data
    os.makedirs(os.path.dirname(csvFile1), exist_ok=True)
    df_employeedata.to_csv(csvFile1, index=False)

    #MentalHealth of Employee Data
    os.makedirs(os.path.dirname(csvFile2), exist_ok=True)
    df_mentalhealth.to_csv(csvFile2, index=False)
    
    print(f"Data has been saved into two CSV files: '{csvFile1}' and '{csvFile2}'")


url = "https://raw.githubusercontent.com/viraterletska/Impact_of_Remote_Work_on_Mental_Health/main/data/Impact_of_Remote_Work_on_Mental_Health.csv"
csvFile1 = "Data/EmployeeData.csv"
csvFile2 = "Data/MentalHealthData.csv"
processData(url)

def logQuery(query):
    """adds to a query markdown file"""
    with open("queryLog.md", "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")