from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    content = forms.CharField(label='内容', widget=forms.Textarea())
    image = forms.ImageField(label='イメージ画像', required=False) # 追加
    date = forms.DateTimeField(label='日時',required=True,widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),input_formats=['%Y-%m-%dT%H:%M'])