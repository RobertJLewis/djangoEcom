from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('catalog:index')
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('catalog:index')
    

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("home")

@login_required

def profile_view(request):
    profile= request.user.profile
    addresses = request.user.addresses.all()
    orders = request.user.orders.all() [:5]
    return render(request, "accounts/profile.html", {
        "profile": profile,
        "addresses": addresses,
        "orders": orders
    })