from django import forms
from .models import PerfilUtilizador

class PerfilUtilizadorForm(forms.ModelForm):
    confirmarPalavraPasse = forms.CharField(widget=forms.PasswordInput(attrs={
        'style': 'margin-left: 30px; height: 20px; width: 400px;',
    }), label="Confirmar Palavra Passe")
    
    class Meta:
        model = PerfilUtilizador
        fields = ['username', 'email', 'palavraPasse', 'confirmarPalavraPasse']

        widgets = {
            'username': forms.TextInput(attrs={
                'style': 'margin-left: 30px; height: 20px; width: 400px;',
            }),
            'email': forms.EmailInput(attrs={
                'style': 'margin-left: 30px; height: 20px; width: 400px;',
            }),
            'palavraPasse': forms.PasswordInput(attrs={
                'style': 'margin-left: 30px; height: 20px; width: 400px;',
            }),
            'palavraPasse': forms.PasswordInput(attrs={
                'style': 'margin-left: 30px; height: 20px; width: 400px;',
            }),            
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("palavraPasse")
        confirm_password = cleaned_data.get("confirmarPalavraPasse")

        if password != confirm_password:
            raise forms.ValidationError("As palavras passe não coincidem.")
        return cleaned_data
