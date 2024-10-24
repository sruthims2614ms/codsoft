
import random
import string
from django.shortcuts import render

def generated(request):
    password = ""
    if request.method == "POST":
        length = int(request.POST.get('length'))
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) 
        for _ in range(length))
    
    return render(request, 'generator.html', {'password': password})
