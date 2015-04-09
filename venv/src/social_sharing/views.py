from django.shortcuts import render


# function -> home
def testhome(request):
    context = {}
    template = "donotuse.html"
    return render(request, template, context)



