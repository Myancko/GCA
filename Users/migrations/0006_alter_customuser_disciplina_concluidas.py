# Generated by Django 4.1.6 on 2023-02-05 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0008_disciplina_status'),
        ('Users', '0005_customuser_disciplina_concluidas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='disciplina_concluidas',
            field=models.ManyToManyField(blank=True, related_name='Disciplina_cluidas', to='administrador.disciplina', verbose_name='Disciplina Concluidas'),
        ),
    ]
