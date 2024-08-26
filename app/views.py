from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    s={'name':'radha','age':30}
    return render(request,'jinja.html',context=s)