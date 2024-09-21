def my_custom_middleware(get_response):
    print("Code here will be executed only one time, i.e, this place is used for one time initialization")

    def my_function(request):
        print("Code here will be executed before reaching the view")

        respnose= get_response(request)
        print("Code here will be executed after the view")
        return respnose
    return my_function