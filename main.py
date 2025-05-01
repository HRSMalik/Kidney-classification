from CNNClassifier import logger
from CNNClassifier.pipeline.stage02_prep_base_model import PrepareBaseModelPipeline
from CNNClassifier.pipeline.stage03_modeltrain import ModelTrainingPipeline
from CNNClassifier.pipeline.stage01_data_ingestion import DataIngestionPipeline



if __name__ == "__main__":
        STAGE_NAME = "Data Ingestion stage"

        try:
            logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
            obj = DataIngestionPipeline()
            obj.main()
            logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
        except Exception as e:
            logger.exception(e)
            raise e
        
        STAGE_NAME = "Prepare Base Model stage"
        try:
            logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
            obj = PrepareBaseModelPipeline()
            obj.main()
            logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
        except Exception as e:
            logger.exception(e)
            raise e
        
        STAGE_NAME = "Model Training stage"
        try:
            logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
            obj = ModelTrainingPipeline()
            obj.main()
            logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
        except Exception as e:
            logger.exception(e)
            raise e
