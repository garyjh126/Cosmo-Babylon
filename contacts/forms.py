from django import forms


from .models import Message

class ContactForm(forms.ModelForm):
    # name = forms.CharField(max_length=100)
    # email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'placeholder': 'Your email', 'class': 'form-control'}))
    # message_content = forms.TextField(max_length=10000)

    name = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True)
    content = forms.Textarea()

    class Meta:
        model = Message
        fields = ['name', 'email', 'content']

    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'type': 'text',
            'class': 'form-control',
            'id': 'name',
            'placeholder': 'Name',
        })
        self.fields['email'].widget.attrs.update({
            'type': 'email',
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Your Email',
        })
        self.fields['content'].widget.attrs.update({
            'type': 'text',
            'class': 'form-control',
            'id': 'message',
            'placeholder': 'Message',
            'style': 'resize:none'
        })
    
    def clean(self, *args, **kwargs):

        data = self.cleaned_data

        name = data.get("name")
        email = data.get("email")
        content = data.get("content")

        data['name'] = " ".join([ n[0].upper() + n[1:] for n in name.split() ])

        

        