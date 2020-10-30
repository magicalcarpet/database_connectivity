import yaml
import os
import sys

class Environment:
    @classmethod
    def database_key_name(cls, key_name):
        path_to_file = os.path.realpath(__file__)
        directory = os.path.dirname(path_to_file)
        yaml_file = os.path.join(directory, 'database.yml')
        with open(yaml_file) as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            return (data['database'][key_name])
    

# print(Environment.database_key_name('password'))
# print(Environment.database_key_name('password'))
    