from django import forms

class PasswordGeneratorForm(forms.Form):
    length = forms.IntegerField(label='Longitud de la contraseña', min_value=8, max_value=32)
    include_numbers = forms.BooleanField(label='Incluir números', required=False)
    include_special_characters = forms.BooleanField(label='Incluir caracteres especiales', required=False)
