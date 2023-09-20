from django import forms
from bankapp.models import  Branch,Sbranch
class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    dob = forms.DateField()
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    phone_number = forms.CharField(max_length=15)
    mail_id = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    district = forms.ModelChoiceField(queryset=Branch.objects.all(), empty_label=None)
    branch = forms.ModelChoiceField(queryset=Sbranch.objects.none(), empty_label=None) # You can use a CharField here
    account_type = forms.ChoiceField(choices=[('savings', 'Savings Account'), ('current', 'Current Account')])
    materials_provide = forms.MultipleChoiceField(
        choices=[('debit_card', 'Debit Card'), ('credit_card', 'Credit Card'), ('cheque_book', 'Cheque Book')],
        widget=forms.CheckboxSelectMultiple,
    )
