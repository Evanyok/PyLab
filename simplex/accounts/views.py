from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .models import TUser

def index(request):
    # list = TUser.objects.order_by('id')
    list = get_list_or_404(TUser)
    return render(request, 'accounts/index.html', {'users': list})

def detail(request, uid):
    # try:
    #     user = TUser.objects.get(pk=uid)
    # except TUser.DoesNotExist:
    #     raise Http404("User does not exist.")
    user = get_object_or_404(TUser, pk=uid)
    return render(request, 'accounts/detail.html', {'user': user})

def results(request):
    return HttpResponse("results")

def verify(request):
    if 'verify' in request.POST.keys():
        list = request.POST['verify']
        for i in list:
            user = get_object_or_404(TUser, pk=i)
            user.validated = True
            user.save()
    return HttpResponseRedirect(reverse('index'))

def sign_up(request):
    return HttpResponse("sign up")

def sign_in(request):
    return HttpResponse("sign in")