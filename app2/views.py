from django.shortcuts import render

# Create your views here.
def jinja_print2(request):
    s={'radha':'krushna'}
    return render(request,'jinja2.html',s)