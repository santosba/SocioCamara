from django import forms
from .models import Article

class UnifiedArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'is_published', 'author', 'image', 'article_type']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'article_type': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False

    def clean(self):
        cleaned_data = super().clean()
        article_type = cleaned_data.get('article_type')
        image = cleaned_data.get('image')

        # No need to check image dimensions here, as it's handled in the model
        if not image:
            raise forms.ValidationError("Articles must have an image")

        return cleaned_data