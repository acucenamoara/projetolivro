from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from customauth.forms import *

# Create your views here.
@login_required(login_url='auth.login')
def home(request):
    return redirect('bank.index')

@login_required(login_url='auth.login')
def config(request, pk):    
    user = MyUser.objects.get(pk=pk)
    if user.id == request.user.id:
        form = UserChangeForm(request.POST or None, instance=user)
        if form.is_valid():            
            form.save()
            return redirect('./'+str(request.user.id))
            
        return render(request,'auth/config.html', {'form':form})
    return redirect('home')

# Objetivo
@login_required(login_url='auth.login')
def goal_index(request):    
    goals = Goal.objects.filter(user=request.user)
    return render(request, 'goal/index.html', {'goals':goals})

@login_required(login_url='auth.login')
def goal_create(request):
    form = GoalForm(request.POST or None)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('goal.index')
        
    return render(request,'goal/create.html', {'form':form})

@login_required(login_url='auth.login')
def goal_edit(request, pk):
    goal = Goal.objects.get(pk=pk)
    if request.user != goal.user:
        return redirect('goal.index')

    form = GoalForm(request.POST or None, instance=goal)
    if form.is_valid():
        form.save()
        return redirect('goal.index')
        
    return render(request,'goal/edit.html', {'form':form, 'goal': goal})

@login_required(login_url='auth.login')
def goal_delete(request, pk):
    goal = Goal.objects.get(pk=pk)
    if request.user == goal.user:
        goal.delete()
    return redirect('goal.index')

# Despesa
@login_required(login_url='auth.login')
def expense_index(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'expense/index.html', {'expenses':expenses})

@login_required(login_url='auth.login')
def expense_create(request):
    form = ExpenseForm(request.POST or None)

    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('expense.index')
        
    return render(request,'expense/create.html', {'form':form})

@login_required(login_url='auth.login')
def expense_edit(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.user != expense.user:
        return redirect('expense.index')

    form = ExpenseForm(request.POST or None, instance=expense)
    if form.is_valid():
        form.save()
        return redirect('expense.index')
        
    return render(request,'expense/edit.html', {'form':form, 'expense': expense})

@login_required(login_url='auth.login')
def expense_delete(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.user == expense.user:
        expense.delete()
    return redirect('expense.index')


# Saldo
@login_required(login_url='auth.login')
def balance_index(request):
    balances = Balance.objects.filter(user=request.user)
    return render(request, 'balance/index.html', {'balances':balances})

@login_required(login_url='auth.login')
def balance_create(request):
    form = BalanceForm(request.POST or None)

    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('balance.index')

    return render(request,'balance/create.html', {'form':form})

@login_required(login_url='auth.login')
def balance_edit(request, pk):
    balance = Balance.objects.get(pk=pk)
    if request.user != balance.user:
        return redirect('balance.index')
        
    form = BalanceForm(request.POST or None, instance=balance)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('balance.index')
        
    return render(request,'balance/edit.html', {'form':form, 'balance': balance})

@login_required(login_url='auth.login')
def balance_delete(request, pk):
    balance = Balance.objects.get(pk=pk)
    if request.user == balance.user:
        balance.delete()
    return redirect('balance.index')

# Banco
@login_required(login_url='auth.login')
def bank_index(request):
    banks = Bank.objects.filter(user=request.user)
    return render(request, 'bank/index.html', {'banks':banks})

@login_required(login_url='auth.login')
def bank_create(request):
    form = BankForm(request.POST or None)

    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('bank.index')
        
    return render(request,'bank/create.html', {'form':form})

@login_required(login_url='auth.login')
def bank_edit(request, pk):
    bank = Bank.objects.get(pk=pk)
    if request.user != bank.user:
        return redirect('bank.index')

    form = BankForm(request.POST or None, instance=bank)
    if form.is_valid():
        form.save()
        return redirect('bank.index')
        
    return render(request,'bank/edit.html', {'form':form, 'bank': bank})

@login_required(login_url='auth.login')
def bank_delete(request, pk):
    bank = Bank.objects.get(pk=pk)
    if request.user == bank.user:
        bank.delete()
    return redirect('bank.index')
