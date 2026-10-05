import os
from django.shortcuts import render, redirect

FILE_PATH = 'resultado.txt'

def obtener_acumulado():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as f:
            try:
                return int(f.read().strip())
            except ValueError:
                return 0
    return 0

def index(request):
    if request.method == 'POST':
        num1 = int(request.POST.get('num1') or 0)
        num2 = int(request.POST.get('num2') or 0)
        
        total_anterior = obtener_acumulado()
        nuevo_total = total_anterior + num1 + num2
        
        with open(FILE_PATH, 'w') as f:
            f.write(str(nuevo_total))
            
        return redirect('resultado')
        
    return render(request, 'index.html')

def resultado(request):
    total = obtener_acumulado()
    return render(request, 'resultado.html', {'total': total})