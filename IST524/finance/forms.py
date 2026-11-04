from django import forms
from finance.models import Finance

class FinanceForm(forms.ModelForm):
    class Meta:
        model = Finance
        fields = "__all__"