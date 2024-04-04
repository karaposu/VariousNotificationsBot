from sqlalchemy.orm import Session
from database_setup import User, APIKey, engine  # Ensure these are correctly imported

import logging

# Basic configuration for logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
logger = logging.getLogger(__name__)

class SendNotificationService:
    def __init__(self, request, dependencies=None):
        self.request = request
        self.dependencies = dependencies
        self.preprocessed_data = None
        self.compatible = False
        self.response = None
        logger.debug("SendNotificationService instance created")

    @classmethod
    async def create(cls, request, dependencies=None):
        # Create an instance of the class
        logger.info("Creating SendNotificationService instance")
        self = cls(request, dependencies)

        # Perform preprocessing and request processing
        self.preprocess_request_data()
        await self.process_request()  # This can now be awaited
        return self

    def check_compatibility(self, api_key=None, message=None):
        # logger.info(f"Check compatibility: {compatible}")
        return True, ""

    def preprocess_request_data(self):
        logger.info("Preprocessing request data")
        session = Session(bind=engine)
        try:
            # Query the database for the API key
            api_key_obj = session.query(APIKey).filter(APIKey.api_key == self.request.api_key).first()
            if api_key_obj is not None:
                # If the API key exists, get the associated user's telegram_id
                telegram_id = api_key_obj.user.telegram_id
                COMPATIBLE, details = self.check_compatibility(api_key=self.request.api_key,
                                                               message=self.request.message)
                unpacked = {"COMPATIBLE": COMPATIBLE, "api_key": self.request.api_key, "message": self.request.message,
                            "telegram_id": telegram_id}
                self.preprocessed_data = {"COMPATIBLE": COMPATIBLE, "api_key": self.request.api_key, "message": self.request.message, "telegram_id": telegram_id}
            else:
                logger.error("API key not found.")
                COMPATIBLE, details = False, "API key not found."
                unpacked = {"COMPATIBLE": COMPATIBLE, "api_key": self.request.api_key, "message": self.request.message,
                            "telegram_id": None}

            self.preprocessed_data = unpacked
        except Exception as e:
            logger.error("Error during preprocessing", exc_info=True)
            session.rollback()
            raise e
        finally:
            session.close()


    async def send_notification(self):
        if self.preprocessed_data["COMPATIBLE"]:
            from handlers import send_notification
            telegram_id=self.preprocessed_data["telegram_id"]
            telegram_id=int(telegram_id)
            # 572163035
            message = self.preprocessed_data["message"]
            logger.info(f"Sending notification to {telegram_id} with message: {message}")
            await send_notification(telegram_id, self.preprocessed_data["message"])
        else:
            pass  # Handle incompatibility

    async def process_request(self):
        logger.info("Processing request")
        await self.send_notification()
