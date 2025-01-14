# Generated by Django 4.2.1 on 2023-06-05 22:47

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FormLetters',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=256)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(max_length=1000, verbose_name='عنوان نامه')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='زمان ارسال نامه')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'نامه',
                'verbose_name_plural': 'نامه ها',
            },
        ),
    ]
