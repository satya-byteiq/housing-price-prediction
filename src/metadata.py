"""

"""

import numpy as np
import pandas as pd
import os

from utility import read_yml_file


def get_meta(df, df_type):
    meta_data = pd.DataFrame(df.dtypes)
    meta_data['fill_rate'] = df.notna().sum() * 100 / df.shape[0]
    meta_data = meta_data.reset_index().rename(columns={'index': 'col_name',
                                                        0: 'datatype'})
    nuniq_dict = {}
    for col in df:
        nuniq_dict[col] = df[col].nunique()
    meta_data['nunique'] = meta_data['col_name'].map(nuniq_dict)
    meta_data['dataset_type'] = df_type
    return meta_data


def save_metadata():
    config_path = "../config/dataset_info.yml"
    data_info_dict = read_yml_file(config_path)
    raw_data_path = data_info_dict['raw_data_path']
    metadata_path = data_info_dict['metadata_path']
    train_file = data_info_dict['train_file']
    test_file = data_info_dict['test_file']
    train_data = pd.read_csv(os.path.join(raw_data_path, train_file))
    test_data = pd.read_csv(os.path.join(raw_data_path, test_file))
    train_metadata = get_meta(train_data, 'train')
    test_metadata = get_meta(test_data, 'test')
    col_set = [i for i in test_data.columns if i in train_data.columns]
    comm_train = train_data[col_set]
    comm_test = test_data[col_set]
    merged_data = pd.concat([comm_train, comm_test])
    merged_meta = get_meta(merged_data, 'merged')
    metadata = pd.concat([train_metadata, test_metadata, merged_meta])
    metadata.to_csv(os.path.join(metadata_path, 'metadata.csv'), index=False)


if __name__ == '__main__':
    save_metadata()
