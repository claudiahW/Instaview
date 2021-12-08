# Generated by Django 3.2.9 on 2021-12-08 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaview', '0008_auto_20211208_0828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='comment_count',
        ),
        migrations.AlterField(
            model_name='likes',
            name='value',
            field=models.CharField(choices=[('Dislike', 'Dislike'), ('Like', 'Like')], default='like', max_length=10),
        ),
    ]