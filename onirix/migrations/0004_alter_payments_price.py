# Generated by Django 4.2.1 on 2023-05-06 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onirix', '0003_payments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='price',
            field=models.CharField(choices=[('$25', '$25'), ('$38', '$38')], default='', max_length=3),
        ),
    ]