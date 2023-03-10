from django.shortcuts import render,redirect
from .models import Product,Category
from django.http import HttpResponse
from .forms import ProductForm
from .forms import ProductForm,CategoryForm

# Create your views here.
def getAllProducts(request):
    
    #select * from products
    product = Product.objects.all().values()
    #products = Product.objects.all().values_list('pName','pPrice','pQty')
    #products = Product.objects.all().values('pName','pPrice','pQty')
    #fetch single object
    # product =Product.objects.get(id=1)
    #price greater thn....
    #__ django orm lookups
    #products  = Product.objects.filter(pPrice__gte = 800).values()
    #products  = Product.objects.filter(pPrice__lte = 800).values()
    #products = Product.objects.filter(pName__startswith='i').values()
    #products = Product.objects.filter(pName__icontains='P').values()
    #orderby
    #products = Product.objects.all().order_by('-pName').values()
    print(product)
    return render(request,'product/allproducts.html',{'product':product})

def addProducts(request):
    #add product
    #productdict ={'pName':'mouse2','Price':100,'pQty':10,'pDesc':'mouse for laptop','pStatus':True,'pColor':'black'}
    product = Product(pname ="lloyd tv ",price=10000,pQty=100,pdescription="lloyd tv for the drawing room tv",pstatus=True,pColor="orange")
    #product = Product(productdict)
    product.save()
    print("product added")
    return render(request,'product/addproducts.html')


def deleteProduct(request,id):
    #delete product
    #id = 1
    product = Product.objects.get(id=id)
    product.delete()
    
    #return HttpResponse("product deleted")
    return render(request,'product/deleteproduct.html')
    
def updateProduct(request,id):
    #update product
    #id = 1
    
    product = Product.objects.get(id=id)
    product.pname = "lenovo laptop"
    product.price = 500000
    product.save()
    
    # product = Product.objects.get(id=id)
    # product.pName = "mouse"
    # product.save()
    #return HttpResponse("product updated")
    return render(request,'product/updateproduct.html')
    
    
def addProductWithForm(request):
    
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.save()
        return HttpResponse("product added")    
            
        
    return render(request,'product/addproductwithform.html',{'form':form})    
        
    
    # if request.method == "POST":
    #     pName = request.POST['pName']

def updateProductWithForm(request,id):
    
    #7
    product = Product.objects.get(id=id)
    form = ProductForm()
    
    print("post.....")
    form = ProductForm(request.POST or None,instance=product)    
    if form.is_valid():
        form.save()
        return redirect('getproducts')  
    
    return render(request,'product/updateproductwithform.html',{'form':form})  



def addCategory(request):
    form = CategoryForm()
    if request.method =="POST" :
        form = CategoryForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('getcategories')
    
    return render(request,'product/addcategory.html',{'form':form})    

def getAllCategories(request):
    categories = Category.objects.all().values()
    return render(request,'product/allcategories.html',{'categories':categories})
                
   
def deleteCategory(request,id):
    
    cat = Category.objects.get(id=id)
    cat.delete()
    return redirect('getcategories')
        
    
def updateCat(request,id):
    cat = Category.objects.get(id=id)
    form = CategoryForm(request.POST or None,instance=cat)
    if form.is_valid():
        cat.save()
        return redirect('getcategories')
    
    return render(request,'product/updatecategory.html',{'form':form})