from django import forms
from finance.models import Conta, Categoria


class ContaForm(forms.ModelForm):
    class Meta:
        model = Conta
        fields = "__all__"
        widgets = {"data_vencimento": forms.DateInput(attrs={"type": "date"})}


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = "__all__"
