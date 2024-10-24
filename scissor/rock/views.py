import random
from django.shortcuts import render, redirect

def games(request):
    if 'userscore' not in request.session:
        request.session['userscore'] = 0
        request.session['computerscore'] = 0

    result = ''
    if request.method == 'POST':
        userchoice = request.POST.get('choice')
        computerchoice = random.choice(['rock', 'paper', 'scissors'])

        if userchoice == computerchoice:
            result = "It's a tie!"
        elif (userchoice == 'rock' and computerchoice == 'scissors') or \
             (userchoice == 'paper' and computerchoice == 'rock') or \
             (userchoice == 'scissors' and computerchoice == 'paper'):
            result = "You win!"
            request.session['userscore'] += 1
        else:
            result = "You lose!"
            request.session['computerscore'] += 1

        return render(request, 'home.html', {
            'result': result,
            'userchoice': userchoice,
            'computerchoice': computerchoice,
            'userscore': request.session['userscore'],
            'computerscore': request.session['computerscore'],
        })

    return render(request, 'home.html')

def reset(request):
    request.session.flush()
    return redirect('games')
