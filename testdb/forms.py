from django import forms
from .models import Post, Post2, Focal, Report, Paper


class FileForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['file']


class FileForm1(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['file1']

class FileForm11(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['file11']


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



class ImageForm1(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['image_h']



class ImageForm2(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['image_p']


class ImageForm3(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['image_z']



class NameForm(forms.Form):
	Region = forms.CharField(label='Region', max_length=100)
	MagnitudeMw = forms.CharField(label='MagnitudeMw', max_length=100)

#===========post2

class Post2FileForm(forms.ModelForm):
	class Meta:
		model = Post2
		fields = ['file']


class Post2FileForm1(forms.ModelForm):
	class Meta:
		model = Post2
		fields = ['file1']

class Post2FileForm11(forms.ModelForm):
	class Meta:
		model = Post2
		fields = ['file11']


class Post2FileForm2(forms.ModelForm):
	class Meta:
		model = Post2
		fields = ['file2']





# class FileForm3(forms.ModelForm):
# 	class Meta:
# 		model = Post
# 		fields = ['file3']

class Post2ImageForm(forms.ModelForm):
	class Meta:
		model = Post2
		fields = ['image']



class Post2ImageForm1(forms.ModelForm):
	class Meta:
		model = Post2
		fields = ['image_h']



class Post2ImageForm2(forms.ModelForm):
	class Meta:
		model = Post2
		fields = ['image_p']


class Post2ImageForm3(forms.ModelForm):
	class Meta:
		model = Post2
		fields = ['image_z']



class Post2NameForm(forms.Form):
	Region = forms.CharField(label='Region', max_length=100)
	MagnitudeMw = forms.CharField(label='MagnitudeMw', max_length=100)


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