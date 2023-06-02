from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'your name',
               
            }))

    class Meta:


        model = Contact
        fields = (
            'name',
            'email',
            'subject',
            'message'
        )
        widgets = {
            # 'name' : forms.TextInput(attrs={
            #     'class' : 'form-control',
            #     'placeholder' : 'Your name'
            # }),
            'email' : forms.EmailInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Your email'
            }),
            'subject' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Subject'
            }),
            'message' : forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Your message',
                 'cols' : "30",
                   'rows' : "7"
            })
            
        }

    def clean(self):
        value = self.cleaned_data['email']
        if not value.endswith('gmail.com'):
            raise forms.ValidationError('Email must be gmail.com')
        return self.cleaned_data
    
    def clean_name(self):
        value = self.cleaned_data.get('name')
        return value.lower()