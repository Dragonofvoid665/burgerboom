# Generated by Django 5.2.1 on 2025-07-01 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_alter_food_options_alter_stories_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food',
            options={'verbose_name': 'Блюда', 'verbose_name_plural': 'Блюды'},
        ),
        migrations.RenameField(
            model_name='stories',
            old_name='image2',
            new_name='circle',
        ),
        migrations.AddField(
            model_name='table_creat_order',
            name='first_name',
            field=models.CharField(default='wrvrv', max_length=150),
        ),
        migrations.AddField(
            model_name='tableorderitem',
            name='first_name',
            field=models.CharField(default='wrvrv', max_length=150),
        ),
    ]
