# Import libraries
from re import U
import pandas as pd
import numpy as np
import matplotlib as plt
import os
from os.path import exists

class test_data:
    # import excel sheet
    def __init__(self, test_type, file_name):
        file_dir = os.getcwd() + '/java_foil_data'
        test_dir = '/' + test_type + '_data'
        file_dir += test_dir
        self.file_path = file_dir + '/' + file_name

        self.df = pd.read_excel(self.file_path)


if __name__ == '__main__':
    aoa_4d_test = test_data('aoa', '4d-velocity-data.xlsx')
    print('Hello World')