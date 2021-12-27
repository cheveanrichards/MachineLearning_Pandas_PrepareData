import pandas as pd
from sqlalchemy import create_engine


data = {
    'Country': ['Belgium', 'India', 'Brazil'],
    'Capital': ['Brussels', 'New Delhi', 'Brasilia'],
    'Population': [11190846, 130171035, 207847528]
}

Data_Table = pd.DataFrame(data, columns=['Country', 'Capital', 'Population'])
print(Data_Table)
Data_Table_After_RemoveingColumn = Data_Table.drop(['Capital', 'Population'], axis=1) 
print("\n")
print(Data_Table_After_RemoveingColumn)

Data_Table_Sorted =  Data_Table.sort_index()
print("\n")
print(Data_Table_Sorted)

Data_Table_Sorted_ByValue = Data_Table.sort_values(by='Country')
print("\n")
print(Data_Table_Sorted_ByValue)

Data_Table_Rank = Data_Table.rank()
print("\n")
print(Data_Table_Rank)
print('*************************CSV**************************')

# Starting to use CSV now with Pandas 
DataReadIn = pd.read_csv('data.csv',header=None)
Data_ReadIn_removetabs = DataReadIn.replace("\t","  ", regex=True)
print(DataReadIn)
print("\n")
print(Data_ReadIn_removetabs)
Data_ReadIn_removetabs.to_csv('modified_data.csv')

# Starting to use SQL Database with Pandas 
engine = create_engine('sqlite:///:memory:')
Data_Table.to_sql('my_table', engine)
Sql_ReadIn_all=  pd.read_sql("SELECT * FROM my_table;", engine)
Sql_ReadIn_Country_Capital =  pd.read_sql("SELECT Country, Capital FROM my_table;", engine)

print("\n")
print("************SQL Query*****************" + "\n")
print(Sql_ReadIn_all)
print("\n")
print(Sql_ReadIn_Country_Capital)
