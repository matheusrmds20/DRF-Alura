# Generated by Django 5.1.7 on 2025-03-13 20:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Escola', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Periodo', models.CharField(choices=[('M', 'Matutino'), ('V', 'Vespertino'), ('N', 'Noturno')], default='M', max_length=1)),
                ('Curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Escola.curso')),
                ('Estudante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Escola.estudante')),
            ],
        ),
    ]
