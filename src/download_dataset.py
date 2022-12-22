"""
This module is for downloading the dataset from kaggle.
Problem statement: Housing price prediction using advanced regression
Dataset url: https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques

Functions:

1. load_env_variable: I have stored kaggle api credentials inside .env file. By using python-dotenv
I have loaded those as environment variable in this function.

2. read_yml_file: I have the configuration related to dataset inside config/dataset_info.yml, using
this function, I read the constants.

3. unzip file: If the dataset is going to be downloaded as zip file, we can use this function to
unzip the downloaded file.

4. download_dataset: To download the dataset with appropriate arguments like command to download and
dataset storage path.

5. main: To assemble all the functions and call one by one.
"""

import os
from zipfile import ZipFile
from dotenv import load_dotenv
import yaml


def load_env_variables():
    """
    Load the environment variable
    :return: None
    """
    load_dotenv()
    print("env variable loaded successfully!")


def read_yml_file(path_name, key='dataset'):
    """
    Will read the dataset_info.yml file and return the info about dataset
    :return:
    """
    with open(path_name, "r") as stream:
        try:
            dataset_info = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return dataset_info[key]


def download_dataset(dataset_info):
    """
    Download the dataset into a directory
    :param dataset_info: dataset info dictionary
    :return: None
    """
    raw_data_dir = dataset_info['data-directory-path']
    download_command = f"{dataset_info['download-command']} -c {dataset_info['name']} -p " \
                       f"{raw_data_dir}"
    if not os.path.exists(raw_data_dir):
        print("directory absence! creating directory...")
        os.mkdir(raw_data_dir)
    try:
        os.system(download_command)
        print("downloading started!")
    except OSError as e:
        print(e.args)


def unzip_file(path, file_name, type_file='zip'):
    """
    To unzip the given file into the current direction
    :param path: the given path to the zip file
    :param file_name: zip file name
    :param type_file: type  of zip file
    :return: None
    """
    try:
        print("unzipping started!")
        with ZipFile(os.path.join(path, file_name), 'r') as zObject:
            zObject.extractall(path=path)
        zObject.close()
    except OSError as e:
        print(e.args)


def main():
    """
    Perform certain steps to have all the dataset files. Steps are: download, unzip
    and removing the zip file

    :return: None
    """
    load_env_variables()
    dataset_config_path = "../config/dataset_info.yml"
    dataset_info = read_yml_file(dataset_config_path)
    # download the dataset to the given directory
    download_dataset(dataset_info)
    name_of_dataset = dataset_info['name']
    target_path = dataset_info['data-directory-path']
    ls_files = [i for i in os.listdir(target_path) if name_of_dataset in i]
    zip_file = None
    if len(ls_files) != 0:
        print("dataset downloaded!")
        extension = ls_files[0].split(os.path.sep)[-1]
        unzip_file(target_path, ls_files[0], extension)
        print("Zip file extracted!")
        zip_file = [i for i in ls_files if name_of_dataset in i and extension in i][0]
    ls_files = os.listdir(target_path)
    if len(ls_files) > 1:
        os.remove(os.path.join(target_path, zip_file))


if __name__ == "__main__":
    main()
