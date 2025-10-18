from django import forms
from .models import Autor, Categoria, Post

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class BuscarForm(forms.Form):
    query = forms.CharField(label='Buscar por título', max_length=100)