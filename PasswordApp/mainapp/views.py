from django.shortcuts import render
import random
import string
from .forms import PasswordGeneratorForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = PasswordGeneratorForm(request.POST)
        if form.is_valid():
            length = form.cleaned_data['length']
            include_numbers = form.cleaned_data['include_numbers']
            include_special_characters = form.cleaned_data['include_special_characters']
            
            characters = string.ascii_letters
            if include_numbers:
                characters += string.digits
            if include_special_characters:
                characters += string.punctuation
            
            password = ''.join(random.choice(characters) for _ in range(length))
            
            return render(request, 'mainapp/index.html', {'form': form, 'password': password, 'title': "Password Generator"})
    else:
        form = PasswordGeneratorForm()
    
    return render(request, 'mainapp/index.html', {'form': form,'title': "Password Generator"})