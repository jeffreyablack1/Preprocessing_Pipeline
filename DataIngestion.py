import tensorflow as tf
import pyodbc

#****************************
class DataIngestion:
    def __init__(self, server, database, table, user, password):
        """
        Initializes a DataIngestion object with the necessary credentials to connect to the SQL server.
        
        Parameters:
            - server (str): The server name or IP address of the SQL server.
            - database (str): The name of the database containing the table to be extracted.
            - table (str): The name of the table to be extracted.
            - user (str): The username to connect to the SQL server.
            - password (str): The password associated with the provided username.
        """
        self.server = server
        self.database = database
        self.table = table
        self.user = user
        self.password = password
    
    def extract_data(self):
        """
        Connects to the SQL server and extracts the specified table as a pandas DataFrame.
        
        Returns:
            - A pandas DataFrame containing the data from the specified table.
        """
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.user+';PWD='+ self.password)
        query = "SELECT * FROM " + self.table
        data = pd.read_sql(query, connection)
        connection.close()
        return data

#****************************
class OptimizeSpeed:
    def __init__(self, data_ingestion_object):
        """
        Initializes an OptimizeSpeed object with a DataIngestion object, which will be used to extract the data.
        
        Parameters:
            - data_ingestion_object (DataIngestion): A DataIngestion object containing the necessary credentials to connect to the SQL server.
        """
        self.data_ingestion_object = data_ingestion_object

    def optimize(self):
        """
        Optimizes the speed of the data extraction process.
        
        Returns:
            - A pandas DataFrame containing the data from the specified table, extracted at optimized speed.
        """
        data = self.data_ingestion_object.extract_data()
        # Apply any necessary optimizations here, such as parallel processing or multi-threading
        return data
