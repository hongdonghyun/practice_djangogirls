from django import forms


class PostCreateForm(forms.Form):
    title = forms.CharField(
        label='제목',
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': '제목을 입력하세요.',
                'class': 'form-control',
            }
        )
    )
    text = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'placeholder': '내용을 입력하세요.',
                'class': 'form-control',
            }
        ),
        required=True
    )
