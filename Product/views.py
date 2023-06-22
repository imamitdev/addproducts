from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .models import Product
from .form import Productform

# Create your views here.


def product_list(request):

    products=Product.objects.all()

    return render(request,'index.html',{'products':products})

def product_view(request,product_id):
    products=get_object_or_404(Product,id=product_id)
    return render(request,'view.html',{"products":products})

def create_product(request):

    if request.method=="POST":

        print(request.method)

        form=Productform(request.POST)

        if form.is_valid():

            form.save()
            print(form)

        return redirect("Product:home")
    else:
        form=Productform()

    return render(request,'create.html',{"form":form})


def edit_product(request, product_id):

    products=get_object_or_404(Product,id=product_id)

    if request.method=="POST":     

        form=Productform(request.POST,instance=products)

        if form.is_valid():

            form.save()           

        return redirect("Product:home")
    else:

        form=Productform(instance=products)

    return render(request,'create.html', {"form":form})



def product_delete(request,id):

    products=Product.objects.get(id=id)    
    products.delete()

    return HttpResponse("Product delete Successfully")    
    

