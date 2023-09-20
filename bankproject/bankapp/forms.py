from django import forms
from bankapp.models import  Branch,Sbranch,RegForm
class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    dob = forms.DateField(widget = forms.SelectDateWidget)
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    phonenumber = forms.CharField(max_length=15)
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    district = forms.ModelChoiceField(queryset=Branch.objects.all(), empty_label=None)
    # branch = forms.ModelChoiceField(queryset=Sbranch.objects.none(), empty_label=None) # You can use a CharField here
    accounttype = forms.ChoiceField(choices=[('savings', 'Savings Account'), ('current', 'Current Account')])
    materialsprovide = forms.MultipleChoiceField(
        choices=[('debit_card', 'Debit Card'), ('credit_card', 'Credit Card'), ('cheque_book', 'Cheque Book')],
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = RegForm
        fields=['name','dob','gender','phone_number','email','address','district','accounttype','materailsprovided']