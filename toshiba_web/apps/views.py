from django.shortcuts import render
from .models import Product
from django.views.generic import TemplateView

def index(request):
    product = Product.objects.all()
    # print(product)
    a = {
        'mahsulot': product
    }
    return render(request, "products.html", context=a)


def product(request, pk):
    data = Product.objects.filter(id=pk).first()
    a = {
        'product':data
    }

    return render(request, 'product.html',context=a)


from django.shortcuts import render, get_object_or_404
from .models import Product  # Assuming the model is named Product

def product_detail(request):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product.html', {'fast': "fast"})


from django.shortcuts import render, redirect
from .forms import PaymentForm

def payment_view(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Process payment here
            return redirect('success_page')
    else:
        form = PaymentForm()

    return render(request, 'pay.html', {'form': form})

def con(request):
    return render(request, 'contact.html')


