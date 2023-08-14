from django.shortcuts import render, redirect
from django.shortcuts import redirect
from django.urls import reverse

def scheme_view(request):
    return render(request, "main/scheme.html")

def main_view(request):
    return render(request, "main/index.html")

def admin_redirect(request):
    return redirect(reverse('admin:index'))