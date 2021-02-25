from django import forms
from . import models
from . import views


class PostForm(forms.ModelForm):
    class Meta:
        fields = ("message", "group")
        model = models.Post

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["group"].queryset = (models.Forum.objects.filter(pk__in=user.forums.values_list("group__pk")))
