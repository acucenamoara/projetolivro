"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from financas.views import *

urlpatterns = [
    path('', home, name='home'),
    path('config/<int:pk>', config, name='auth.config'),

    path('objetivos/', goal_index, name='goal.index'),
    path('objetivo/novo/', goal_create, name='goal.create'),
    path('objetivo/<int:pk>/e', goal_edit, name='goal.edit'),
    path('objetivo/<int:pk>/d', goal_delete, name='goal.delete'),

    path('despesas/', expense_index, name='expense.index'),
    path('despesa/novo/', expense_create, name='expense.create'),
    path('despesa/<int:pk>/e', expense_edit, name='expense.edit'),
    path('despesa/<int:pk>/d', expense_delete, name='expense.delete'),

    path('saldos/', balance_index, name='balance.index'),
    path('saldo/novo/', balance_create, name='balance.create'),
    path('saldo/<int:pk>/e', balance_edit, name='balance.edit'),
    path('saldo/<int:pk>/d', balance_delete, name='balance.delete'),

    path('bancos/', bank_index, name='bank.index'),
    path('banco/novo/', bank_create, name='bank.create'),
    path('banco/<int:pk>/e', bank_edit, name='bank.edit'),
    path('banco/<int:pk>/d', bank_delete, name='bank.delete'),


]
