import os
from django.shortcuts import render, redirect
from .models import ArchivoSubido

# Ruta para la calculadora existente
TXT_FILE_PATH = os.path.join(os.path.dirname(__file__), '../resultado.txt')

def index(request):
    return render(request, 'index.html')

def resultado(request):
    total = "0"
    if os.path.exists(TXT_FILE_PATH):
        with open(TXT_FILE_PATH, 'r', encoding='utf-8') as f:
            contenido = f.read().strip()
            if contenido:
                total = contenido
    return render(request, 'resultado.html', {'total': total})

def evacuacion_view(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        archivo = request.FILES.get('archivo')
        if titulo and archivo:
            ArchivoSubido.objects.create(titulo=titulo, archivo=archivo)
            return redirect('evacuacion')

    # Consulta los archivos subidos para mostrarlos en la página
    archivos = ArchivoSubido.objects.all().order_by('-fecha_subida')
    return render(request, 'calculadora/evacuacion.html', {'archivos': archivos})