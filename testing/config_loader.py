import yaml
import os

def load_config(file_path):
    # Resolve absolute path
    abs_path = os.path.abspath(file_path)

    with open(abs_path, 'r') as f:
        config = yaml.safe_load(f)

    return config