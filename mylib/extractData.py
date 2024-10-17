import requests
import pandas as pd
import os
from io import StringIO

# Function to extract, clean, split, and save data from GitHub URL
def extractData(
    url="https://raw.githubusercontent.com/viraterletska/Impact_of_Remote_Work_on_Mental_Health/main/data/Impact_of_Remote_Work_on_Mental_Health.csv",
    csvFile1="Data/EmployeeData.csv",
    csvFile2="Data/MentalHealthData.csv"
):
    # Step 1: Extract the data from the URL
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to download file. Status code: {response.status_code}")

    csv_data = response.text
    csv_file = StringIO(csv_data)

    # Step 2: Read and process the data in chunks
    df_employeedata_list = []
    df_mentalhealth_list = []
    chunk_size = 1000  # Adjust based on dataset size

    for chunk in pd.read_csv(csv_file, chunksize=chunk_size):
        df_employeedata = chunk[['Employee_ID', 'Age', 'Job_Role', 'Industry', 'Years_of_Experience', 'Work_Location']].copy()
        df_mentalhealth = chunk[['Employee_ID', 'Hours_Worked_Per_Week', 'Mental_Health_Condition', 'Access_to_Mental_Health_Resources']].copy()

        # Step 3: Clean the employee data
        df_employeedata['Age'] = pd.to_numeric(df_employeedata['Age'], errors='coerce')
        df_employeedata['Years_of_Experience'] = pd.to_numeric(df_employeedata['Years_of_Experience'], errors='coerce')
        df_employeedata.dropna(inplace=True)

        # Step 4: Clean the mental health data
        df_mentalhealth['Access_to_Mental_Health_Resources'] = df_mentalhealth['Access_to_Mental_Health_Resources'].map({'Yes': True, 'No': False})
        df_mentalhealth['Hours_Worked_Per_Week'] = pd.to_numeric(df_mentalhealth['Hours_Worked_Per_Week'], errors='coerce')
        df_mentalhealth.dropna(inplace=True)

        # Step 5: Append cleaned chunks to the lists
        df_employeedata_list.append(df_employeedata)
        df_mentalhealth_list.append(df_mentalhealth)

    # Step 6: Concatenate all chunks into final DataFrames (limit to 100 rows)
    n = 100
    df_employeedata = pd.concat(df_employeedata_list).head(n).copy()
    df_mentalhealth = pd.concat(df_mentalhealth_list).head(n).copy()

    # Step 7: Save the DataFrames into CSV files
    os.makedirs(os.path.dirname(csvFile1), exist_ok=True)
    df_employeedata.to_csv(csvFile1, index=False)

    os.makedirs(os.path.dirname(csvFile2), exist_ok=True)
    df_mentalhealth.to_csv(csvFile2, index=False)

    print(f"Data has been saved into two CSV files: '{csvFile1}' and '{csvFile2}'")

