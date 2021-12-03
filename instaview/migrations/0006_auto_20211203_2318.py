# Generated by Django 3.2.9 on 2021-12-03 20:18

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instaview', '0005_auto_20211203_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('title', models.CharField(max_length=100)),
                ('caption', models.TextField(max_length=100)),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('like_count', models.IntegerField(default=0)),
                ('comment_count', models.IntegerField(default=0)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='comments',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instaview.image'),
        ),
        migrations.AlterField(
            model_name='likes',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instaview.image'),
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]