from django.shortcuts import render, redirect
from django.shortcuts import redirect
from django.urls import reverse
from .models import Category
def scheme_view(request):
    category_path = request.session.get('category_path', [])
    context = {'category_path': category_path,}
    return render(request, "main/scheme.html", context=context)

def main_view(request):
    return render(request, "main/index.html")

def admin_redirect(request):
    return redirect(reverse('admin:index'))