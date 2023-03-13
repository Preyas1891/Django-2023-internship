import django.forms as Form
from .models import Product,Category

class ProductForm(Form.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
  
class CategoryForm(Form.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'    
