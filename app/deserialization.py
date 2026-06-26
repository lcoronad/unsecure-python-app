import pickle

import yaml


def load_pickle(data: bytes) -> object:
    """CWE-502: insecure pickle deserialization."""
    return pickle.loads(data)


def load_yaml(document: str) -> object:
    """CWE-502: unsafe yaml.load without SafeLoader."""
    return yaml.load(document)
