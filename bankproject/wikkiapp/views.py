from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserForm

def user_form_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name', )
            dob = request.POST.get('dob', )
            email = request.POST.get('email', )
            phonenumber = request.POST.get('phonenumber', )
            address = request.POST.get('address', )
            city=request.POST.get('city', )
            district=request.POST.get('district')

            regform = UserForm(name=name, dob=dob, email=email, phonenumber=phonenumber, address=address,city=city,district=district)
            regform.save()
            messages.success(request, 'Application is accepted ')
        return redirect('bankapp:rough')
    else:
        form = UserForm()
        messages.success(request, 'missed one data. please fill it again')
        return redirect('wikkiapp:user_form_view')
    return render(request, 'user_form.html', {'form': form})

