from datetime import datetime
from django.utils.deprecation import MiddlewareMixin

class BenchmarkMiddleware(object):
    
    def __init__(self, next_layer=None):
        """We allow next_layer to be None because old-style middlewares
        won't accept any argument.
        """
        
        self.get_response = next_layer
        
        
        
    def process_request(self, request):
        request._request_time = datetime.now()

    def process_template_response(self, request, response):
        response_time = datetime.now() - request._request_time
        response.context_data['response_time'] = response_time
        return response
    
    
    def __call__(self, request):
        """Handle new-style middleware here."""
        print(123)
        response = self.process_request(request)
        if response is None:
            # If process_request returned None, we must call the next middleware or
            # the view. Note that here, we are sure that self.get_response is not
            # None because this method is executed only in new-style middlewares.
            response = self.get_response(request)

        response = self.process_response(request, response)
        return response