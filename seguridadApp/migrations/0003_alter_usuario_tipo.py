# Generated by Django 3.2.4 on 2021-09-14 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguridadApp', '0002_alter_usuario_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipo',
            field=models.CharField(default='administrador', max_length=15, null=True),
        ),
    ]
