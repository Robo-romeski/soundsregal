from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View

class indexView(View): 

		def get(self, request):
			return render(request, 'index.html', {'email':'roborome@mail.com', 'password':'password'})

