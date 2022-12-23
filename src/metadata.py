"""

"""

import numpy as np
import pandas as pd
import os


class MetaData:
    def __init__(self,
                 train_data_path: str,
                 test_data_path: str,
                 train_dataset_type='csv',
                 test_dataset_type='csv'):

        self.train_data = pd.read_csv(train_data_path)
        self.test_data = pd.read_csv(test_data_path)

    def get_primary_metadata(self, df):
        """

        :param df:
        :return:
        """
        pass

    def numeric_meta(self, df):
        """

        :param df:
        :return:
        """
        pass

    def categorical_meta(self, df):
        """

        :param df:
        :return:
        """
        pass

    def date_meta(self, df):
        """

        :param df:
        :return:
        """
        pass

    def run(self):
        """

        :return:
        """
        