from django import forms
from .models import CustomerMessage


class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerMessage
        fields = ('contact', 'text', 'position')
        labels = {
            'text': 'your message',
            'contact': 'contact (email/mobile number)',
            'position': 'select subject',
        }

    def __int__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['text'].required = False

