from django import forms

from .models import Customer

class DateInput(forms.DateInput):
    input_type = 'date'
    
class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Nome',
        error_messages={'max_length': 'Nome não pode ter mais que 30 caracteres'},
    )
    last_name = forms.CharField(
        label='Sobrenome',
        error_messages={'max_length': 'Sobre nome não pode ter mais que 50 caracteres'},
    )
    email = forms.EmailField(label='E-mail')
    birth_date = forms.DateField(label='dt. Nasc.', widget=DateInput())
    area_code = forms.RegexField(
        label='DDD',
        regex=r'^\+?1?[0-9]{2}$',
        error_messages={'invalid': 'Número de DDD inválido.'},
    )
    phone_number = forms.RegexField(
        label='Telefone',
        regex=r'^\+?1?[0-9]{9,15}$',
        error_messages={'invalid': 'Número de DDD inválido.'},
    )
    country = forms.CharField(label='Endereço')
    state = forms.CharField(label='Estado')
    city = forms.CharField(label='Cidade')
    cep = forms.CharField(label='Cep')
    
    class Meta:
        model = Customer
        fields = (
            "first_name",
            "last_name",
            "email",
            "area_code",
            "phone_number",
            "country",
            "state",
            "city",
            "cep"
        )
