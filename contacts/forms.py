from django import forms

from .models import Message

class ContactForm(forms.ModelForm):
    # name = forms.CharField(max_length=100)
    # email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'placeholder': 'Your email', 'class': 'form-control'}))
    # message_content = forms.TextField(max_length=10000)

    class Meta:
        model = Message
        fields = ['name', 'email', 'content']
         
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        qs = Message.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email already exists")
        return email