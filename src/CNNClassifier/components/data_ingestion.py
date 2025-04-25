import os
import zipfile
import gdown
from CNNClassifier import logger
from CNNClassifier.utils.common import get_size
from CNNClassifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
 
    def download_file(self) -> str:
        """
        Download file from Google Drive
        """
        try:
            dataset_url = self.config.source_url
            zip_down_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading data from{dataset_url} into {zip_down_dir}")
            
            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?id='
            gdown.download(f"{prefix}{file_id}", zip_down_dir, quiet=False)
            
            logger.info(f"Downloaded data from {dataset_url} into {zip_down_dir}")
            
        except Exception as e:
            logger.exception(e)
            raise e
        
    def extract_zip_file(self):
        """
        Extract zip file
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f"Extracted file to {unzip_path}")
            