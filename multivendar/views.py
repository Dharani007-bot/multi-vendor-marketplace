from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Vendor, Product
from .form import VendorForm, ProductForm

def home(request):
    return render(request, 'home.html')

# CUSTOMER REGISTER
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# CUSTOMER LOGIN
def user_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if Vendor.objects.filter(user=user).exists():
                return redirect('customer_dashboard')
            login(request, user)
            return redirect('customer_dashboard')
        else:
            error = 'Invalid username or password'
    return render(request, 'customer_login.html', {'error': error})

# VENDOR LOGIN
def vendor_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and Vendor.objects.filter(user=user).exists():
            login(request, user)
            return redirect('vendor_dashboard')
        else:
            error = 'Invalid credentials or not a vendor account'
    return render(request, 'vendor_login.html', {'error': error})

# CUSTOMER DASHBOARD
@login_required
def customer_dashboard(request):
    if Vendor.objects.filter(user=request.user).exists():
        return redirect('customer_login')
    return render(request, 'customer_dashboard.html')

# VENDOR DASHBOARD
@login_required
def vendor_dashboard(request):
    if not Vendor.objects.filter(user=request.user).exists():
        return redirect('vendor_dashboard')
    vendor = Vendor.objects.get(user=request.user)
    products = Product.objects.filter(vendor=vendor)
    context = {
        'vendor': vendor,
        'products': products,
        'product_count': products.count()
    }
    return render(request, 'vendor_dashboard.html', context)

# ADD VENDOR (linked to logged-in user)
@login_required
def add_vendor(request):
    if request.method == 'POST':
        form = VendorForm(request.POST, request.FILES)
        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.user = request.user  # link vendor to current user
            vendor.save()
            return redirect('vendor_list')
    else:
        form = VendorForm()
    return render(request, 'vendor.html', {'form': form})

# ADD PRODUCT
@login_required
def add_product(request):
    if not Vendor.objects.filter(user=request.user).exists():
        return redirect('customer_dashboard')
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = Vendor.objects.get(user=request.user)
            product.save()
            return redirect('vendor_dashboard')
    else:
        form = ProductForm()
    return render(request, 'product.html', {'form': form})

# VENDOR LIST
def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendor_list.html', {'vendors': vendors})

# PRODUCT LIST
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

# ADMIN STYLE DASHBOARD
@login_required
def dashboard(request):
    context = {
        'vendor_count': Vendor.objects.count(),
        'product_count': Product.objects.count()
    }
    return render(request, 'vendor_dashboard.html', context)

# LOGOUT
def user_logout(request):
    logout(request)
    return redirect('home')