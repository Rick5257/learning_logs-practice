from django import forms

from .models import Topic,Entry


class TopicForm(forms.ModelForm):
    """定义主题的表单"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}

class EntryForm(forms.ModelForm):
    """定义笔记条目表单的类"""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}
