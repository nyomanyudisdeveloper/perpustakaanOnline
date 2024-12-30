from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, render
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect

class LoginRequireMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        # test = 123
        # Preparation ops

        # Retrieving the response
        # response = self.get_response(request)
        if not request.user.is_authenticated:
            return redirect("/pinjamBuku")
        # return response

        # Updating the response

        # Returning the response
        # return response
        
    # def process_request(self,request):
    #     if not request.user.is_authenticated:
    #         return redirect(settings.LOGIN_URL)