from django import forms
from .models import Post, Focal, Report, Paper


class FileForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['file']


class FileForm2(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['file2']


# class FileForm3(forms.ModelForm):
# 	class Meta:
# 		model = Post
# 		fields = ['file3']

class ImageForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['image']


# class ImageForm2(forms.ModelForm):
# 	class Meta:
# 		model = Post
# 		fields = ['image2']

class NameForm(forms.Form):
    Region = forms.CharField(label='Region', max_length=100)


class FocalForm(forms.ModelForm):
	class Meta:
		model = Focal
		fields = ['title', 'date', 'file']


class ReportForm(forms.ModelForm):
	class Meta:
		model = Report
		fields = ['title', 'date', 'file']

class PaperForm(forms.ModelForm):
	class Meta:
		model = Paper
		fields = ['title', 'link']
		
class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	email_address = forms.CharField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)