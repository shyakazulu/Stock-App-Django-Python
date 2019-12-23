from django import forms
from .models import quote

class quoteForm(forms.ModelForm):
    class Meta:
        model = quote
        fields = ["ticker"]