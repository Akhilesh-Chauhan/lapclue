from django import forms
from .models import AllProducts

class ProductForm(forms.ModelForm):
   class Meta:
       model = AllProducts
       fields = ('cname','modelno','image','category','price','screen','processor','graphics','memory','storage','ioports','dimensions','description')