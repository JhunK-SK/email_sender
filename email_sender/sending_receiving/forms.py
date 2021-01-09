from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField(max_length=50)
    
    def __str__(self):
        return self.email