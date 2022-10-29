from django.forms import ModelForm
from Cedva1.models import *
from django.contrib.auth.models import User
from django import forms

class FormularioPago(ModelForm):
    folio = forms.CharField(label='Folio', widget=forms.TextInput(attrs={'type': 'text','class': 'form-control'}), required=True)
    tipoPago = forms.CharField(label='Tipo de Pago', widget=forms.TextInput(attrs={'type': 'text','class': 'form-control'}), required=True)
    monto = forms.CharField(label='Monto', widget=forms.TextInput(attrs={'type': 'text','class': 'form-control'}), required=True)
    fechaPago = forms.CharField(label='Fecha de Pago', widget=forms.TextInput(attrs={'type': 'date','class': 'form-control  datetimepicker'}), required=True)
    horapago = forms.CharField(label='Hora de Pago', widget=forms.TextInput(attrs={'type': 'time','class': 'form-control  datetimepicker'}), required=True)
    mesPagado = forms.CharField(label='Mes a pagar', widget=forms.TextInput(attrs={'type': 'text','class': 'form-control'}), required=True)

    class Meta:
        model = Pago
        fields = ('folio', 'tipoPago', 'monto', 'fechaPago', 'mesPagado', 'horapago')

