# Generated by Django 2.1.7 on 2019-07-11 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0018_small_fixes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('rent', 'rent'), ('extra', 'extra')], default='rent', max_length=32, verbose_name='type'),
        ),
    ]
