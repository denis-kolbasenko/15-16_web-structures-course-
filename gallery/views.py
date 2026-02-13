from django.shortcuts import render
from .models import Asset # Импортируем модель, чтобы спрашивать данные
from django.shortcuts import render, redirect # Добавляем redirect
from .forms import AssetForm # Импортируем нашу новую форму
from django.contrib import messages # ДЗ 5ЛР

def home(request):
# all() возвращает хаос.
# order_by('-created_at') сортирует по полю created_at.
# Минус (-) означает "по убыванию" (DESC).
    assets = Asset.objects.all().order_by('-created_at')
    context_data = {
        'page_title': 'Главная Галерея',
        'assets': assets,
    }
    return render(request, 'gallery/index.html', context_data)

def about(request):
    return render(request, 'gallery/about.html')

def upload(request):
	if request.method == 'POST':
		form = AssetForm(request.POST, request.FILES)
		
		if form.is_valid():
			# Если все поля заполнены верно - сохраняем в БД
			form.save()
			messages.success(request, 'Спасибо, файл загружен!') # ДЗ 5ЛР
			# И перекидываем пользователя на главную
			return redirect('home')
	else:
		# Сценарий: Пользователь просто зашел на страницу (GET)
		form = AssetForm() # Создаем пустую форму


		# Отдаем шаблон, передавая туда форму (заполненную ошибками или пустую)
	return render(request, 'gallery/upload.html', {'form': form})
