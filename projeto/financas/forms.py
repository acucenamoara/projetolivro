from django.utils.translation import gettext_lazy as _
from django import forms
from .models import *

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['description', 'cost', 'type', 'payment_method']
        labels = {
            'description': _('Descrição'),
            'cost': _('Custo'),
            'type': _('Tipo de despesa'),
            'payment_method': _('Método de pagamento'),
        }
        

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['goal', 'value', 'date', 'income', 'saved_value']
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'autocomplete': 'off'
                },
            )
        }
        
        labels = {
            'goal': _('Objetivo'),
            'value': _('Valor'),
            'date': _('Data'),
            'income': _('Rendimento (%)'),
            'saved_value': _('Valor economizado'),
        }
        help_texts = {
            'goal': _('O que almeja com esse dinheiro?'),
            'income': _('Exemplo: 2,9.'),
        }
        error_messages = {
            'goal': {
                'max_length': _("Este campo tem muitos caracteres"),
            },
        }

class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['institution', 'type']
        labels = {
            'institution': _('Instituição'),
            'type': _('Tipo de conta'),
        }

class BalanceForm(forms.ModelForm):
    class Meta:
        model = Balance
        fields = ['value', 'income', 'bank']
        labels = {
            'value': _('Valor'),
            'income': _('Rendimento (%)'),
            'bank': _('Banco'),
        }  
        help_texts = {
            'income': _('Exemplo: 2,9.'),
        }
