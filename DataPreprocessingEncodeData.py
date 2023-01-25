import pandas as pd

#****************************
class DataPreprocessingEncodeData(DataPreprocessingImputeMissingData):
    def __init__(self, data_ingestion_object, categorical_columns, continuous_columns):
        """
        Initializes a DataPreprocessingEncodeData object with a DataIngestion object, a list of categorical columns, and a list of continuous columns.
        Which will be used to extract the data, remove rare values, impute missing data and one hot encode categorical data in the dataset.
        
        Parameters:
            - data_ingestion_object (DataIngestion): A DataIngestion object containing the necessary credentials to connect to the SQL server.
            - categorical_columns (list): list of categorical columns in the dataset.
            - continuous_columns (list): list of continuous columns in the dataset.
        """
        super().__init__(data_ingestion_object, categorical_columns, continuous_columns)
        
    def one_hot_encode(self):
        """
        One-hot encodes the categorical columns in the dataset.
        
        Returns:
            - A pandas DataFrame with one-hot encoded categorical columns.
        """
        self.data = pd.get_dummies(self.data, columns=self.categorical_columns)
        self.preprocessing_steps += "One-hot encoded categorical variables.\n"
        return self.data
    
    def summarize(self):
        """
        Prints a string describing a statistical summary of the dataset before and after one-hot encoding categorical variables.
        """
        print("Dataset Summary before One-Hot Encoding:\n", self.data_ingestion_object.data.describe())
        print("Dataset Summary after One-Hot Encoding:\n", self.data.describe())

# Use this class as follows
dp = DataPreprocessingEncodeData(data_ingestion_object, categorical_columns, continuous_columns)
dp.remove_missing_values()
dp.remove_rare_values()
dp.impute_missing_values()
dp.one_hot_encode()
dp.summarize()
dp.print_steps()
