from django.shortcuts import render
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
