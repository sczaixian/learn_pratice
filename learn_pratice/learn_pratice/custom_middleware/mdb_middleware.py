
def polls_middleware(get_response):
    print('----------')
    def middleware(request):
        print('-------------2--------')
        response = get_response(request)
        print('-----------------3-------')
        return response
    return middleware