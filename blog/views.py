from django.shortcuts import render, redirect
from .forms import AutorForm, CategoriaForm, PostForm, BuscarForm
from .models import Post

def index(request):
    return render(request, 'blog/index.html')

def crear_autor(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'blog/autor_form.html', {'form': form})

def crear_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'blog/categoria_form.html', {'form': form})

def crear_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'blog/post_form.html', {'form': form})

def buscar_post(request):
    form = BuscarForm()
    resultados = None
    if request.method == 'POST':
        form = BuscarForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            resultados = Post.objects.filter(titulo__icontains=query)
    return render(request, 'blog/resultados.html', {'form': form, 'resultados': resultados})
