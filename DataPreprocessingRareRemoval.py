import tensorflow as tf
import pandas as pd

#****************************
class DataPreprocessingRareRemoval(DataPreprocessingRemove):
    def __init__(self, data_ingestion_object,categorical_columns):
        """
        Initializes a DataPreprocessingRareRemoval object with a DataIngestion object and a list of categorical columns.
        Which will be used to extract the data and remove rare values in the dataset.
        
        Parameters:
            - data_ingestion_object (DataIngestion): A DataIngestion object containing the necessary credentials to connect to the SQL server.
            - categorical_columns (list): list of categorical columns in the dataset.
        """
        super().__init__(data_ingestion_object)
        self.categorical_columns = categorical_columns
        
    def remove_rare_values(self, rare_threshold=0.05):
        """
        Removes rows with discrete data points that occur less than rare_threshold (default = 0.05) of the time.
        
        Parameters:
            - rare_threshold (float): The threshold of rarity beyond which a discrete data point will be removed.
        
        Returns:
            - A pandas DataFrame with rows containing discrete data points that occur less than rare_threshold removed.
        """
        for col in self.categorical_columns:
            value_counts = self.data[col].value_counts()
            rare_values = value_counts[value_counts < rare_threshold * len(self.data)]
            self.data = self.data[~self.data[col].isin(rare_values.index)]
        self.preprocessing_steps += f"Removed rows with discrete data points that occur less than {rare_threshold}% of the time.\n"
        return self.data
    
    def summarize(self):
        """
        Prints a string describing a statistical summary of the dataset before and after removing rare values.
        """
        print("Dataset Summary before Removing Rare values:\n", self.data_ingestion_object.data.describe())
        print("Dataset Summary after Removing Rare values:\n", self.data.describe())
        
    def print_steps(self):
        """
        Prints a string describing all preprocessing steps performed in detail.
        """
        print("Preprocessing Steps:\n", self.preprocessing_steps)

# Use this class as follows
dp = DataPreprocessingRareRemoval(data_ingestion_object, categorical_columns)
dp.remove_missing_values()
dp.remove_rare_values()
dp.summarize()
dp.print_steps()
