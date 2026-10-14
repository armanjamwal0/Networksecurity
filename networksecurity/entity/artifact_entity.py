from dataclasses import dataclass


"""
    dataclass module is introduced in Python 3.7 as a utility tool to make structured classes specially for storing data. 
    These classes hold certain properties and functions to deal specifically with the data and its representation.
    """


@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path: str
    