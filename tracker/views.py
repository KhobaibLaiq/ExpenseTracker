from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Transaction  
from django.db.models import Sum
def index(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = request.POST.get('amount')

        if not description:
            messages.info(request, "Description cannot be empty")
            return redirect('/')

        if not amount:
            messages.info(request, "Amount is required")
            return redirect('/')

        try:
            amount = float(amount)
        except ValueError:
            messages.info(request, "Amount should be a valid number")
            return redirect('/')

        # Create a new transaction with the given description and amount
        Transaction.objects.create(
            description=description,
            amount=amount
        )

        return redirect('/')
    
    context ={'transactions': Transaction.objects.all(),
              'balance': Transaction.objects.all().aggregate(total_balance = Sum('amount'))['total_balance'] or 0,
              'income': Transaction.objects.filter(amount__gte=0).aggregate(income = Sum('amount'))['income'] or 0,
              'expense': Transaction.objects.filter(amount__lte=0).aggregate(expense = Sum('amount'))['expense'] or 0,
              
              }
    return render(request, 'index.html', context)



def deleteTransacrion(request,uuid):
    Transaction.objects.get(uuid=uuid).delete()
    return redirect('/')
