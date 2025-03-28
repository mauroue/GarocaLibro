# Generated by Django 4.2.16 on 2024-10-27 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_leitor_options_leitor_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leitor',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Ativo?'),
        ),
        migrations.AlterField(
            model_name='leitor',
            name='criado',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação'),
        ),
        migrations.AlterField(
            model_name='leitor',
            name='modificado',
            field=models.DateTimeField(auto_now=True, verbose_name='Data de Atualização'),
        ),
        migrations.AlterField(
            model_name='leitor',
            name='telefone',
            field=models.CharField(max_length=15, verbose_name='Telefone'),
        ),
    ]
