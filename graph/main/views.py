import os
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import subprocess

def run_script(request):
    try:
        # Получаем значения чисел из запроса
        number1 = request.GET.get('number1')
        number2 = request.GET.get('number2')
        number3 = request.GET.get('number3')
        # Сохраняем значения в файл numbers.txt
        file_path = os.path.join(os.path.dirname(__file__),'/home/rumin/Documents/Code/Web/graph/War/numbers.txt')
        with open(file_path, 'w') as file:
            file.write(f'{number1}\n{number2}\n{number3}')

        # Выполняем скрипт
        result = subprocess.check_output(['python', '/home/rumin/Documents/Code/Web/graph/Scripts/plot.py'], text=True)
        return JsonResponse({'result': result})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def index(request):
    return render(request, 'main/home.html')

