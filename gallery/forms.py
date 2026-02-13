from django import forms
from django.core.exceptions import ValidationError
import os
from .models import Asset


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        # Указываем, какие поля дать заполнить пользователю.
        # created_at мы не включаем, так как оно заполняется само.
        fields = ['title', 'file']
        # Небольшая косметика для HTML (добавляем CSS классы)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 
            'Название модели'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }
    
    # Валидация отдельного поля пишется как clean_ИМЯ_ПОЛЯ
    def clean_file(self):
        file = self.cleaned_data['file']
        # Получаем расширение файла (превращаем имя в нижний регистр)
        ext = os.path.splitext(file.name)[1].lower()
        # Список разрешенных форматов
        valid_extensions = ['.glb', '.gltf']  # .jpg или документ .pdf . Наш 3D-движок
        if ext not in valid_extensions:
            raise ValidationError('Неподдерживаемый формат. Пожалуйста, загрузите .glb или .gltf')
        return file