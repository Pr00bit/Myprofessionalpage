from django.db import models
#from django_markdown.models import MarkdownField

#dodany model aby mozna bylo dodac kategorie#
class Category(models.Model):
    #name = models.CharField('Nazwa Kategorii', max_length=100, null=True, blank=True)
    #slug = models.SlugField('Odnosnik', unique=True, max_length=100, null=True, blank=True)
    #icon = models.ImageField('Ikonka Kategorii', upload_to='icons',      blank=True#)

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategoria"

    def __unicode__(self):
        return self.name
 #-----------------------------------------------------#
from froala_editor.fields import FroalaField
class Post(models.Model):
    title = models.CharField(max_length = 140)
    bodyszort = FroalaField()
    body = FroalaField()
    date = models.DateTimeField()
    #category = models.ManyToManyField(Category, verbose_name='Kategoria')
    img = models.ImageField(upload_to='admina',null=True, blank=True)
    is_published = models.BooleanField(default=True, blank=True)


    def __str__(self):
        return self.title
