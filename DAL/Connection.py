import pyodbc

def ConnectionSQL():
    Server = "DESKTOP-T7D96U5"
    Database = "DB01" 
    cnx = pyodbc.connect(
                         "DRIVER={ODBC Driver 17 for SQL Server};"
                         +"SERVER="+Server+";"
                         +"DATABASE="+Database+";"
                         +"Trusted_Connection=yes")   
    return cnx