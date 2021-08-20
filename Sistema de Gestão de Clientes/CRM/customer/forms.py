from django import forms
from .models import Customer

class DateInput(forms.DateInput):
    input_type = "date"

class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(
        label="Primeiro Nome",
        error_messages={"max_length": "O nome não pode ter mais de 30 caractéres"}
    )
    last_name = forms.CharField(
        label="Sobrenome",
        error_messages={"max_length": "O sobrenome não pode ter mais de 30 caractéres"}
    )
    email = forms.EmailField(label="E-Mail")
    birth_date = forms.DateField(label="Data de Nascimento", widget=DateInput())
    area_code = forms.RegexField(
        label="DDD",
        regex=r"^\+?1?[0-9]{2}$",
        error_messages={"invalid": "DDD Inválido!"}
    )
    phone_number = forms.RegexField(
        label="Telefone/Celular",
        regex=r"^\+?1?[0-9]{8}$",
        error_messages={"invalid": "O Numero de Telefone é inválido!"}    
    )
    country = forms.CharField(label="País")
    state = forms.CharField(label="Estado")
    city = forms.CharField(label="Cidade")

    class Meta:
        model = Customer
        fields = (
            "first_name",
            "last_name",
            "email",
            "birth_date",
            "area_code",
            "phone_number",
            "country",
            "state",
            "city"
        )