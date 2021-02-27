# Generated by Django 3.0.5 on 2021-02-20 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, verbose_name='Proje Adı')),
                ('speaker_name', models.CharField(max_length=1000, verbose_name='Speaker Name')),
                ('content', models.TextField(verbose_name='İçerik')),
                ('published_date', models.DateTimeField(verbose_name='Başlama Tarihi')),
                ('lesson_date', models.DateTimeField(blank=True, null=True, verbose_name='Bitiş Tarihi')),
                ('is_ended', models.BooleanField(verbose_name='Devam Eden')),
                ('speaker_image', models.FileField(blank=True, null=True, upload_to='', verbose_name='speaker photo')),
            ],
        ),
    ]
