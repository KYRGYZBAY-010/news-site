from django.db import models


class HomeNews(models.Model):
    img = models.ImageField(upload_to='img', null=True, blank=True)
    title = models.CharField('Название', max_length=90)
    description = models.TextField('Описание')
    date = models.DateTimeField('Дата и время публикации')



    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Новости на главном странице'
        verbose_name_plural = 'Новости на главном странице'


class About(models.Model):
    title = models.CharField('Название', max_length=90)
    photo = models.ImageField(upload_to='img', null=True, blank=True)
    texts = models.TextField('Текст про нас', null=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Добавить текст на страницу "Про нас"'
        verbose_name_plural = 'Добавить текст на страницу "Про нас"'