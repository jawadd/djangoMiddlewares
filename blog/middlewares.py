# def my_custom_middleware(get_response):
#     print("Code here will be executed only one time, i.e, this place is used for one time initialization")

#     def my_function(request):
#         print("Code here will be executed before reaching the view")

#         respnose= get_response(request)
#         print("Code here will be executed after the view")
#         return respnose
#     return my_function

class MyCustomMiddleware:
    def __init__(self, get_response):
        # One-time configuration and initialization
        self.get_response = get_response
        print("Code here will be executed only one time, i.e, this place is used for one time initialization")

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("Code here will be executed before reaching the view")

        # Call the view or the next middleware
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        print("Code here will be executed after the view")

        return response
