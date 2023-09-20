from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from . models import Branch,Sbranch,RegForm,UserProfile
from django.contrib import messages
from .forms import UserForm

# Create your views here.
def home(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def inside(request):
    return render(request,"inside.html")
def rough(request):
    return render(request,"rough.html")
def form(request):
    if request.method == "POST":
        try:
            name = request.POST.get('name', )
            dob = request.POST.get('dob', )
            email = request.POST.get('email', )
            phonenumber = request.POST.get('phonenumber', )
            address = request.POST.get('address', )
            # city = request.POST.get('city', )
            # district = request.POST.get('district', )
            regform = RegForm(name=name, dob=dob, email=email, phonenumber=phonenumber,address=address)
            regform.save()
            messages.success(request, 'Application accepted')
            return redirect('bankapp:rough')
        except:
            messages.success(request, 'missed one data. please fill it again')
            return redirect('bankapp:form')
    return render(request,'form.html')

def MBranch(request,c_slug=None):
    c_page = None
    products = None

    if c_slug != None:
         c_page = get_object_or_404(Branch, slug=c_slug)
         products = Sbranch.objects.all().filter(branch=c_page, available=True)
         branches = Branch.objects.all()

    else:
        products = Sbranch.objects.all().filter(available=True)

    return render(request,"ind.html",{'branch': c_page,'products': products})


# def Update(request,id):
#     up=get_object_or_404(UserProfile, id=id)
#     form=UserForm(request.POST or None,instance=up)
#     if form.is_valid():
#         form.save()
#         messages.success(request, 'Application accepted')
#         return redirect('/')
#
#     return render(request,"user_form.html",{'form':form,'up':up})




















from django.http import JsonResponse


# from django.views.generic import ListView, CreateView, UpdateView
# from django.urls import reverse_lazy
# from .models import RegForm
# from .forms import  BranchForm
#
# class PersonListView(ListView):
#     model = RegForm
#
#     context_object_name = 'registration'
#
# class PersonCreateView(CreateView):
#     model = RegForm
#     form_class = BranchForm
#     success_url = reverse_lazy('bankapp:person_changelist')
#
# class PersonUpdateView(UpdateView):
#     model = RegForm
#     form_class = BranchForm
#     success_url = reverse_lazy('bankapp:person_changelist')
#
# def load_cities(request):
#     country_id = request.GET.get('district')
#     cities = Sbranch.objects.filter(id=country_id).order_by('name')
#     return render(request, 'form.html', {'cities': cities})
#
# class PersonCreateView(CreateView):
#     model = RegForm
#     fields = ('name','dob','email','phonenumber','address','district','city')
#     success_url = reverse_lazy('bankapp:person_changelist')
#
# class PersonUpdateView(UpdateView):
#     model = RegForm
#     fields = ('name','dob','email','phonenumber','address','district','city')
#     success_url = reverse_lazy('bankapp:person_changelist')