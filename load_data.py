# This module will provide the functions necessary for loading data from various sources, such as CSV files, databases, and APIs. It will include functions for reading data, cleaning it, and transforming it into a format suitable for analysis.
import pandas as pd
import os

class DataLoader:
    """
    This class is responsible for loading data. 
    It provides methods to read data from csv sources, clean it, and transform it into a usable format for analysis.
    It is required that the data be in a csv format.
    
    Methods:
    get_data_dictionary: Returns a dictionary containing files mapped to their respective dataFrames. 
    add_data: Adds a new data source to the data dictionary.
    get_specific_dataframe: Retrieves a specific DataFrame from the data dictionary based on the file name.
    get_count: Returns the count of data sources currently loaded in the data dictionary.

    Future implementations:
    delete_data
    update_data
    """
    # ATTRIBUTES
    # data_dictionary: A dictionary that maps file names to their corresponding pandas DataFrames.
    # number_data_sources: An integer that keeps track of the number of data sources currently loaded in the data dictionary.
    def __init__(self):
        """
        Initializes the DataLoader class with an empty data dictionary and a count of zero data sources.
        """
        self.data_dictionary = {}
        self.number_data_sources = 0
    
    def get_data_dictionary(self):
        """
        Returns the current `data_dictionary` of the DataLoader. 
        """
        return self.data_dictionary 
    
    def add_data(self, source: list[str]):
        """
        Adds each csv file from source into data_dictionary. If there is a duplicate, it will be ignored. 

        Preconditions:
            `source`: a list of strings. Requires that these strings are paths to valid csv files that exist. 
        """
        for file in source: 
            if not os.path.basename(file) in self.data_dictionary:
                self.number_data_sources += 1
            self.data_dictionary[os.path.basename(file)] = pd.read_csv(file)
    
    def get_specific_dataframe(self, file: str):
        """
        Returns the dataframe of a specific file. Throws an error if file is not in the dictionary. 
        
        Preconditions:
            `file`: A str that corresponds to a valid csv file path that exists in the data_dictionary.
        """
        return self.data_dictionary[os.path.basename(file)]

    def get_count(self):
        """
        Returns the number of entries in data_dictionary. 
        """
        return self.number_data_sources