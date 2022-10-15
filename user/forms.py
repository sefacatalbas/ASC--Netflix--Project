from dataclasses import field
from django.forms import ModelForm # Varan 57 
from .models import * # Varan 58

class ProfileForm(ModelForm): #Varan 59 
    class Meta:
        model = Profile
        fields = ['isim', 'resim']
    
    def __init__(self, *args, **kwargs):  #Varan 61
        super(ProfileForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control mt-2'}) #sınırsız class eklenebilir
        self.fields['isim'].widget.attrs.update({'placeholder': 'isim giriniz'}) #tekini sadece değiştirmek için

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['resim', 'tel']
        
        
        def __init__(self, *args, **kwargs):  #Varan 61
            super(AccountForm, self).__init__(*args, **kwargs)
            for name, field in self.fields.items():
                field.widget.attrs.update({'class': 'form-control mt-2'}) #sınırsız class eklenebilir
            