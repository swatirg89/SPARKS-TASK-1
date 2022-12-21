from django.shortcuts import render

# Create your views here.
def usersList(request):
    return render(request , 'userlist.html')

def transfermoney(request):
    return render(request , 'moneytransfer.html')

def payments(request):
    return render(request , 'payments.html')