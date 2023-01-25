import tensorflow as tf
import pandas as pd
from sklearn.impute import KNNImputer

#****************************
class DataPreprocessingImputeMissingData(DataPreprocessingRareRemoval):
    def __init__(self, data_ingestion_object, categorical_columns, continuous_columns):
        """
        Initializes a DataPreprocessingImputeMissingData object with a DataIngestion object, a list of categorical columns, and a list of continuous columns.
        Which will be used to extract the data, remove rare values and impute missing data in the dataset.
        
        Parameters:
            - data_ingestion_object (DataIngestion): A DataIngestion object containing the necessary credentials to connect to the SQL server.
            - categorical_columns (list): list of categorical columns in the dataset.
            - continuous_columns (list): list of continuous columns in the dataset.
        """
        super().__init__(data_ingestion_object,categorical_columns)
        self.continuous_columns = continuous_columns
        
    def impute_missing_values(self, imputer = KNNImputer(n_neighbors=5)):
        """
        Imputes missing values in the data using the provided imputer object.
        The default imputer is KNNImputer with 5 neighbors.
        
        Parameters:
            - imputer : An object that implements the impute method to impute missing values.
        
        Returns:
            - A pandas DataFrame with missing values imputed.
        """
        self.data[self.continuous_columns] = imputer.fit_transform(self.data[self.continuous_columns])
        self.preprocessing_steps += "Imputed missing values using KNN.\n"
        return self.data
    
    def summarize(self):
        """
        Prints a string describing a statistical summary of the dataset before and after imputing missing values.
        """
        print("Dataset Summary before Imputing Missing Values:\n", self.data_ingestion_object.data.describe())
        print("Dataset Summary after Imputing Missing Values:\n", self.data.describe())
        
    def print_steps(self):
        """
        Prints a string describing all preprocessing steps performed in detail.
        """
        print("Preprocessing Steps:\n", self.preprocessing_steps)

# Use this class as follows
dp = DataPreprocessingImputeMissingData(data_ingestion_object, categorical_columns, continuous_columns)
dp.remove_missing_values()
dp.remove_rare_values()
dp.impute_missing_values()
dp.summarize
