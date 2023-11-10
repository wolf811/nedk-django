from django import forms
from mainapp.models import Service, Feedback

class MessageForm(forms.Form):
    your_name = forms.CharField(required=False)
    your_phone = forms.CharField(required=False)
    your_email = forms.EmailField(required=True)
    thema = forms.ModelChoiceField(
        queryset=Service.objects.all(),
        empty_label="",
        required=True,
    )
    message = forms.CharField(widget=forms.Textarea, required=True)
    

class FeedbackCreateForm(forms.ModelForm):
    """
    Форма отправки обратной связи
    """

    class Meta:
        model = Feedback
        fields = ('subject', 'phone', 'email', 'service', 'content')

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {'class': 'form-control', 'autocomplete': 'off'})
