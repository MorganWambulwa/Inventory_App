from django.shortcuts import render, redirect, get_object_or_404
from django_daraja.mpesa.core import MpesaClient
from Admin.models import Product

# Create your views here.
def admin(request):
    products = Product.objects.all()
    return render(request, 'admin.html', {'products': products})

def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        brand = request.POST.get('brand')
        category = request.POST.get('category')
        quantity = request.POST.get('quantity')
        
        Product.objects.create(name=name, price=price, description=description, brand=brand, category=category, quantity=quantity)
        return redirect('admin')
    return render(request, 'add_item.html')

def delete_item(request,id):
    product = get_object_or_404(Product,id=id)
    product.delete()
    return redirect('admin')

def update_item(request, id):
    product = get_object_or_404(Product, id=id)
    
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.description = request.POST.get('description')
        product.brand = request.POST.get('brand')
        product.category = request.POST.get('category')
        product.quantity = request.POST.get('quantity')
        
        product.save()
        return redirect('admin')
    return render(request, 'update_item.html', {'product': product})

def mpesa_pay(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        amount = int(request.POST.get('amount'))
        
        client = MpesaClient()
        
        account_ref = 'EMobilis Tech Institute'
        desc = 'school fees payment'
        
        callback_url = 'https://callback.com/url'
        
        response = client.stk_push(phone,amount,account_ref,desc,callback_url)
        return render(request, "payment_form.html",{"message":"STK Push sent!"})
    return render(request, 'payment_form.html')
