from  django import forms

from .models import Auto


class AddFormAuto(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['engine'].empty_label = 'Двигатель не выбран' # вместо прочерков в форме будет запись
        self.fields['transmission'].empty_label = 'Трансмиссия не выбрана'

    class Meta:
        model = Auto
        fields = '__all__' # выбирает все поля формы , если не нужно прописываем в кортеже
#
# class EasyForm(forms.Form):
#     name = forms.CharField(max_length=50)