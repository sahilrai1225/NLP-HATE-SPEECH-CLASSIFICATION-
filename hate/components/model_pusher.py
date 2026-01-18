import sys
from hate.logger import logging
from hate.exception import CustomException
from hate.configuration.gcloud_syncer import GCloudSync
from hate.entity.config_entity import ModelPusherConfig
from hate.entity.artifact_entity import ModelPusherArtifacts


class ModelPusher:
    def __init__(self,model_pusher_config:ModelPusherConfig):
        """
        param model_pusher_config; Configuration for model pusher
        """

        self.model_pusher_config=model_pusher_config
        self.gcloud=GCloudSync()



    def initiate_model_pusher(self) -> ModelPusherArtifacts:
        """
        Method Name : initiate model_pusher
        Descr: This method initiate model_pusher

        output: model pusher Artifacts


        """
        logging.info("Enetered the initiate model_pusher of ModelTrainer class")

        try:
            #uploading the model to gcloud storage
            self.gcloud.sync_folder_to_gcloud(
                self.model_pusher_config.BUCKET_NAME,
                self.model_pusher_config.TRAINED_MODEL_PATH,
                self.model_pusher_config.MODEL_NAME
            )

            # saving the model pusher artifacts

            model_pusher_artifact=ModelPusherArtifacts(
                bucket_name=self.model_pusher_config.BUCKET_NAME
            )

            logging.info("Exited the initiate model_pusher_artifacts")

            return model_pusher_artifact


        except Exception as e:
            raise CustomException(e,sys )from e