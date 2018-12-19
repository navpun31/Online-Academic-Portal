from datetime import datetime

def my_context(request):
    context_data = dict()
    response_time = datetime.now() - request._request_time
    context_data['response_time'] = response_time
    return context_data