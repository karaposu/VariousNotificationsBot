from abc import ABC, abstractmethod

class BaseService(ABC):
    def __init__(self, request, dependencies=None):
        self.request = request
        self.dependencies = dependencies
        self.preprocessed_data = None
        self.compatible=False
        self.response = None

        self.preprocess_request_data()
        self.process_request()


    @abstractmethod
    def preprocess_request_data(self):
        """Unpack and validate the incoming request.and
         edit self.preprocessed_data. self.preprocessed_data is a dict.  """
        """check compatibility of data and edit self.compatible """

        pass

    @abstractmethod
    def check_compatibility(self, img=None, text=None):
        """Check if the request is compatible with the service's requirements."""
        pass

    @abstractmethod
    def process_request(self):
        """Process the request and produce a response."""
        pass
