from dataclasses import dataclass


"""
    dataclass module is introduced in Python 3.7 as a utility tool to make structured classes specially for storing data. 
    These classes hold certain properties and functions to deal specifically with the data and its representation.
    """


@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path: str

@dataclass
class DataValidationArtifact:
    validation_status: bool
    valid_train_file_path : str 
    valid_test_file_path: str
    invalid_train_file_path :str 
    invalid_test_file_path :str 
    drift_report_file_path : str