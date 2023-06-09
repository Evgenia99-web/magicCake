# Generated by Django 4.2 on 2023-05-08 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakeapp', '0004_alter_order_status_alter_post_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('1', 'Обрабатывается'), ('2', 'Принят'), ('3', 'Выполняется'), ('4', 'Готов')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('1', 'Черновик'), ('2', 'Опубликовано'), ('3', 'На модерации')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('1', 'Черновик'), ('2', 'Опубликовано'), ('3', 'На модерации')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='status',
            field=models.CharField(choices=[('1', 'Черновик'), ('2', 'Опубликовано'), ('3', 'На модерации')], default='1', max_length=1),
        ),
    ]
