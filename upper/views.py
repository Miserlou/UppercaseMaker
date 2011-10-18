from django.shortcuts import render_to_response

def home(request, input="No input supplied"):
    output = input.upper()
    return render_to_response('home.html', {'output': output})
