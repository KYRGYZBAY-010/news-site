# Generated by Django 4.0.5 on 2022-06-09 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_about_photo_about_texts_about_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('text', models.CharField(max_length=255)),
            ],
        ),
    ]
