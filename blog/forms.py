from django import forms
from product.widgets import CustomClearableFileInput

from .models import BlogPost

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class BlogPostForm(forms.ModelForm):
    """
    The form for the blog post model.
    """

    class Meta:
        model = BlogPost
        fields = ('status', 'title', 'content',
                  'featured_image', 'tags', 'category')
        widgets = {
            'content': SummernoteWidget(),
        }

    featured_image = forms.ImageField(
        label='Featured Image',
        required=False,
        widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-primary rounded'
