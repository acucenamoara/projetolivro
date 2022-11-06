from django.db import models
from customauth.models import MyUser
from datetime import date as datetime
# Create your models here.

# User: Sexo = models.CharField(max_length=45) 

# Despesa
class Expense(models.Model):
    PAYMENT_METHODS = (
        ("Pix", "Pix"),
        ("Espécie", "Espécie"),
        ("Cartão", "Cartão"),
    )
    TYPES = (
        ("Essencial", "Essencial"),
        ("Não essencial", "Não essencial"),
    )
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    cost = models.FloatField() # custo
    description = models.CharField(max_length=45) # descrição
    type = models.CharField(max_length=45, choices=TYPES) # tipo - essencial e não essencial
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHODS) # método de pagamento - carteira, a vista e parceladod
    def __str__(self):
        return self.description

# Objetivo/meta
class Goal(models.Model):    
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    goal = models.CharField(max_length=45) # objetivo/nome
    value = models.FloatField() # valor
    date = models.DateField() # data 
    income = models.FloatField() # rendimento
    saved_value = models.FloatField() # valor guardado/economizado    
    def __str__(self):
        return self.goal

    @property
    def time_left(self):
        today = datetime.today()
        result = self.date - today
        return result.days
        

# Banco
class Bank(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    TYPES = (
        ("Conta corrente", "Conta corrente"),
        ("Conta poupança", "Conta poupança"),
        ("Carteira", "Carteira"),
    )
    institution = models.CharField(max_length=45) # instituição
    type = models.CharField(max_length=45, choices=TYPES) # tipo - conta corrente, conta poupança e carteira
    def __str__(self):
        return self.institution

# Saldo
class Balance(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    value = models.FloatField() # valor
    income = models.FloatField() # rendimento
    def __str__(self):
        return self.value + ' em ' + self.bank.institution