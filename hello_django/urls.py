"""
URL configuration for hello_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def greeting(request):
    return HttpResponse("Hello Whiskey")

def square(request, base):
    area = base ** 2
    return HttpResponse(area)

def triangle(request, base, height):
    area = base * height * .5
    return HttpResponse(area)

def rectangle_area(request, height, width):
    area = height * width
    return HttpResponse(area)

def rectangle_perimeter(request, height, width):
    perimeter = (2 * height) + (2 * width)
    return HttpResponse(perimeter)

def circle_area(request, radius):
    area = 3.14 * radius ** 2
    return HttpResponse(area)

def circle_perimeter(request, radius):
    perimeter = 2 * 3.14 * radius ** 2
    return HttpResponse(perimeter)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', greeting),
    path('square/<int:base>/', square),
    path('triangle/base/<int:base>/height/<int:height>/', triangle),
    path('rectangle/area/<int:height>/<int:width>/', rectangle_area),
    path('rectanage/perimeter/<int:height>/<int:width>/', rectangle_perimeter),
    path('circle/area/<int:radius>/', circle_area),
    path('circle/perimeter/<int:radius>/', circle_perimeter),
]
