# Generated by Django 5.1.4 on 2025-06-25 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_remove_stories_image_of_stories_alter_banner_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stories',
            options={'verbose_name': 'Сторис', 'verbose_name_plural': 'Сторисы'},
        ),
        migrations.RemoveField(
            model_name='stories',
            name='image2',
        ),
        migrations.AddField(
            model_name='stories',
            name='circle',
            field=models.ImageField(default='static/image/1.jpg', upload_to='static/image', verbose_name='Фотография истории'),
        ),
    ]
