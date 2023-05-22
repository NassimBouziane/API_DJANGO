class AuthHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'auth' in request.headers:
            auth_header_value = request.headers['auth']

            expected_value = 'test'
            if auth_header_value == expected_value:
                request.auth_valid = True
            else:
                request.auth_valid = False
        else:
            request.auth_valid = False

        response = self.get_response(request)

        return response
