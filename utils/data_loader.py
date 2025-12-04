import yaml
import os

def load_yaml_data(file_name: str):
    """Loads data from a YAML file."""
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', file_name)
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)