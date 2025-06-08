from django import forms
from ..models import Post, Tag

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        label='Tags',
        required=False,
        help_text='Enter comma-separated tags.'
    )

    class Meta:
        model = Post
        fields = ('title', 'content')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Set initial value for tags field
            self.initial['tags'] = ', '.join(t.name for t in self.instance.tags.all())

    def save(self, commit=True):
        # Save the Post instance
        instance = super(PostForm, self).save(commit=False)

        # Process tags
        def save_tags():
            tag_names = self.cleaned_data.get('tags', '').split(',')
            instance.tags.clear()
            for tag_name in tag_names:
                tag_name = tag_name.strip()
                if tag_name:
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    instance.tags.add(tag)

        if commit:
            instance.save()
            save_tags()
        else:
            # Handle the case where commit=False
            self.save_m2m = save_tags

        return instance
