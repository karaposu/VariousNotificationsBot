

import os
import sys
from pathlib import Path
from collections import OrderedDict
import logging

script_dir = os.path.dirname(__file__)
sys.path.append(script_dir)  # Appe

sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

# from celery_app import async_text_to_image_service




class RequestHandler:
    #def __init__(self, iie,ch, et=False):
    def __init__(self):
        self.package_content = None
        self.requester_id = None
        self.package_sent_time = None
        self.response = None
        # self.iie=iie
        # self.ch=ch
        self.DATA_IS_VALID = None
        self.META_IS_VALID = None
        self.USER_HAS_PERMISSION = None

        self.REQUEST_IS_VALID=None
        self.error_code=None

        logger = logging.getLogger(__name__)

        logger.setLevel(logging.DEBUG)
        logger.debug(" ------ ")
        self.logger= logger

        #self.elapsed_time =et
        self.elapsed_time=None
        if not self.elapsed_time:

            self.elapsed_time= OrderedDict()

        # self.elapsed_time = OrderedDict()

        # self.elapsed_time["start_time"] = time.time()
    def op_validity(self,meta_data):

        is_permitted=self.check_metadata_validity(meta_data)
        if is_permitted:
            return True
        else:
           # raise HTTPException(status_code=400, detail="user doesnt have permission for this operation")
            return False

    def check_metadata_validity(self, meta_data):
        return True


    # def handle_register_request_request(self, request: RegisterPostRequest) -> RegisterPost200Response:
    #
    #
    #         business_logic= RegisterService(request)
    #         api_key=business_logic.response
    #
    #            # ops = OperationStatus(success="true", error_code="", debug_log="", package_sent_time="", counter=12)
    #         return RegisterPost200Response(api_key=api_key)

    # def handle_send_notification_request(self, request: ImageGenerationRequest) -> ImageGenerationResponse:
    #     op_valid=self.op_validity(request.operation)
    #     if not op_valid:
    #         ops = OperationStatus(success="false", error_code="", debug_log="", package_sent_time="", counter=12)
    #         images_data =""
    #     else:
    #         business_logic= TextToImageService(request)
    #         images_data=business_logic.response
    #
    #         ops = OperationStatus(success="true", error_code="", debug_log="", package_sent_time="", counter=12)
    #     return ImageGenerationResponse(operation=ops, data=images_data)


    # def handle_source_monitoring_request(self):
    #
    #     # service = SourceMonitoringService()
    #     # return service.response
    #     return SourceMonitoringService(None).prepare_response_for_source_monitoring()
    #
    #
    #
    #
    # # app_version: str = Field(alias="appVersion")
    #
    # def handle_report_bug_request(self, request: BugReportRequest) -> RegisterUser200Response:
    #     # app_version: str = Field(alias="appVersion")
    #     # installation_id: str = Field(alias="installationId")
    #     # timestamp: datetime = Field(alias="timestamp")
    #     # locale: str = Field(alias="locale")
    #     # platform: RegisterUserRequestPlatform = Field(alias="platform")
    #
    #     # business_logic = RegisterOperation(request)
    #     # user_id = business_logic.user_id
    #     return ""
    #
    # def handle_register_user_request(self, request: RegisterUserRequest) -> RegisterUser200Response:
    #     # app_version: str = Field(alias="appVersion")
    #     # installation_id: str = Field(alias="installationId")
    #     # timestamp: datetime = Field(alias="timestamp")
    #     # locale: str = Field(alias="locale")
    #     # platform: RegisterUserRequestPlatform = Field(alias="platform")
    #
    #         # business_logic= RegisterService(request)
    #         # user_id=business_logic.user_id
    #
    #         user_id= ""
    #         return RegisterUser200Response(message="successful", user_id=user_id)
    #
    #
    # def handle_increase_user_limit_request(self, request: IncreaseUserLimitRequest) -> IncreaseUserLimit200Response:
    #     # op_valid=self.op_validity(request.operation)
    #     # if not op_valid:
    #     #     ops = OperationStatus(success="false", error_code="", debug_log="", package_sent_time="", counter=12)
    #     # else:
    #         business_logic= IncreaseLimitService(request)
    #         success=business_logic.response
    #
    #         print("1 **********")
    #         if success:
    #             print("success handle_increase_user_limit_request **********")
    #             return IncreaseUserLimit200Response(message="succesful", newLimit=100)
    #
    # def handle_image_manipulation_request(self, request: MANDOMIMAGEPostRequest) -> ImageManipulationResponse:
    #     op_valid=self.op_validity(request.operation)
    #     if not op_valid:
    #         ops = OperationStatus(success="false", error_code="", debug_log="", package_sent_time="", counter=12)
    #         images_data =""
    #     else:
    #         business_logic= ImageManipulationService(request)
    #         images_data=business_logic.response
    #
    #         ops = OperationStatus(success="true", error_code="", debug_log="", package_sent_time="", counter=12)
    #     return ImageManipulationResponse(operation=ops, data=images_data)
    #
    # def handle_usr_image_manipulation_request(self, request: MANUSRIMAGEPostRequest) -> UserImageManipulationResponse:
    #     op_valid = self.op_validity(request.operation)
    #     if not op_valid:
    #         ops = OperationStatus(success="false", error_code="", debug_log="", package_sent_time="", counter=12)
    #         images_data = ""
    #     else:
    #         p = UsrImageManipulationService(request)
    #         data = p.response
    #         ops = OperationStatus(success="true", error_code="", debug_log="", package_sent_time="", counter=12)
    #     return UserImageManipulationResponse(operation=ops, data=data)
    #
    #