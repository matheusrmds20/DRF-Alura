# Generated by Django 5.1.7 on 2025-03-16 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Escola', '0004_alter_curso_codigo_alter_estudante_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='codigo',
            field=models.CharField(max_length=10),
        ),
    ]
