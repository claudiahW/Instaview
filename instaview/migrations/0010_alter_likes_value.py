# Generated by Django 3.2.9 on 2021-12-08 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaview', '0009_auto_20211208_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='value',
            field=models.CharField(choices=[('Like', 'Like'), ('Dislike', 'Dislike')], default='like', max_length=10),
        ),
    ]
