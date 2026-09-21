from django import forms

class InvertebrateForm(forms.Form):
    name = forms.CharField(label='Nombre común', required=True, max_length=50)
    scientific_name = forms.CharField(label='Nombre científico', required=True, max_length=50)
    taxon_class = forms.CharField(label='Clase', required=True, max_length=50)
    taxon_order = forms.CharField(label='Orden', required=True, max_length=50)
    facts = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
    image = forms.ImageField(required=True)