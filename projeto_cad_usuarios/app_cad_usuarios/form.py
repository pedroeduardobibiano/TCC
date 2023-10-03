from django import forms
from .models import TCC


class TCCForm(forms.ModelForm):
    class Meta:
        model = TCC
        fields = ('nome_autores', 'ano', 'tema', 'descricao', 'curso_graduacao', 'arquivo_tcc')
