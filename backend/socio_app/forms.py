from django import forms

from .models import Socio, Artigo, Categoria,Contacto,Comentario


class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ['nome', 'email', 'telefone', 'morada', 'data_registo', 'actividade','forma', 'tipo_socio']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control','style': 'width: 300px;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'morada': forms.Textarea(attrs={'class': 'form-control'}),
            'data_registo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'actividade': forms.Select(attrs={'class': 'form-control'}),
            'forma': forms.Select(attrs={'class': 'form-control'}),
            'tipo_socio': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome da Empresa',
            'email': 'Endereço de Email',
            'telefone': 'Telefone',
            'morada': 'Morada',
            'data_registo': 'Data de Registo',
            'actividade': 'Atividade',
            'forma': 'Forma',
            'tipo_socio': 'Tipo de Sócio',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['telefone'].required = False


class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ['titulo', 'conteudo',  'image', 'categoria']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
            'conteudo': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'titulo': 'Título',
            'conteudo': 'Conteúdo',
            'image': 'Imagem',
            'categoria': 'Categoria',
        }
class CategoriaForm(forms.ModelForm):
    class Meta:
        model= Categoria
        fields = [ 'nome','descricao']
        widgets ={
            'nome':forms.TextInput(attrs={'class':'form-control'}),
            'descricao':forms.Textarea(attrs={'class':'form-control'})
        }

        labels ={
            'nome': 'Nome da Categoria',
            'descricao': 'Descrição da Categoria'
        }


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto

        fields =['nome','email','mensagem']
        widgets ={
            'nome':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'mensagem':forms.Textarea(attrs={'class':'form-control'})
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comentario

        fields = ['conteudo']

        widgets ={  
            'Comentario':forms.Textarea(attrs={'class':'form-control'})
        }

        