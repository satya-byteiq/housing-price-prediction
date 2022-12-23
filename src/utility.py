import yaml


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
