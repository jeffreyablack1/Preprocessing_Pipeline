import tensorflow as tf
import pandas as pd

#****************************
class DataPreprocessingRemove:
    def __init__(self, data_ingestion_object):
        """
        Initializes a DataPreprocessingRemove object with a DataIngestion object, which will be used to extract the data.
        
        Parameters:
            - data_ingestion_object (DataIngestion): A DataIngestion object containing the necessary credentials to connect to the SQL server.
        """
        self.data_ingestion_object = data_ingestion_object
        self.data = self.data_ingestion_object.extract_data()
        self.preprocessing_steps = ""

    def remove_missing_values(self, missing_threshold=0.1):
        """
        Removes features that have more than missing_threshold (default = 0.1) missing values.
        
        Parameters:
            - missing_threshold (float): The threshold of missing values beyond which a feature will be removed.
        
        Returns:
            - A pandas DataFrame with features that have more than missing_threshold missing values removed.
        """
        missing_values_count = self.data.isnull().sum()
        missing_values_count = missing_values_count[missing_values_count > missing_threshold * len(self.data)]
        self.data = self.data.drop(missing_values_count.index, axis=1)
        self.preprocessing_steps += f"Removed features with more than {missing_threshold}% missing values.\n"
        return self.data

    def summarize(self):
        """
        Prints a string describing a statistical summary of the dataset before and after removing any features.
        """
        print("Dataset Summary before Preprocessing:\n", self.data_ingestion_object.data.describe())
        print("Dataset Summary after Preprocessing:\n", self.data.describe())
        
    def print_steps(self):
        """
        Prints a string describing all preprocessing steps performed in detail.
        """
        print("Preprocessing Steps:\n", self.preprocessing_steps)

# Use this class as follows
dp = DataPreprocessingRemove(data_ingestion_object)
dp.remove_missing_values()
dp.summarize()
dp.print_steps()
