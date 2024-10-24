#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'calculator/home.html')

def calculate(request):
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operation = request.POST['operation']

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = 'Error: Division by zero!'
        else:
            result = 'Error: Invalid operation'

        return render(request, 'calculator/result.html', {'result': result})

    return render(request, 'calculator/home.html')
