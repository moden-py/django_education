

class PrintMiddleware:

    def process_request(self, request):
        print(request)
