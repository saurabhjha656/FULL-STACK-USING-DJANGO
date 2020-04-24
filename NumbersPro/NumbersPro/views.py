from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def num(request):
    xx = []
    xx = request.GET.get('Numbbers', 'default')
    req = request.GET.get('nummmm', 'off')
    req1 = request.GET.get('less_than10', 'off')
    req2 = request.GET.get('more_than10', 'off')
    xx1 = []

    if req == 'on':
        xx1 = set(xx)

        numm = {'manipulation': 'IS DONE', 'Numbersss': xx1}
        return render(request, 'Ind.html', numm)

    elif req1 == 'on':
        xx2 = []
        xx1 = list(xx)
        for i in xx1:
            if(xx1[i] > 10):
                i = i+1
            else:
                xx2.append(xx1[i])

        numm = {'manipulation': 'IS DONE', 'Numbersss': xx1}
        return render(request, 'Ind.html', numm)

    elif req2 == 'on':
        xx2 = []
        xx1 = list(xx)
        for i in xx1:
            if(xx1[i] < 10):
                i = i+1
            else:
                xx2.append(xx1[i])

        numm = {'manipulation': 'IS DONE', 'Numbersss': xx1}
        return render(request, 'Ind.html', numm)

    else:
        return HttpResponse('VALUE or CHECKBOX ERROR')
