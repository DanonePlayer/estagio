# Generated by Django 4.2.3 on 2023-08-26 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0004_emailcandidato'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dadoscandidato',
            name='data_nasc_candidato',
        ),
        migrations.AlterField(
            model_name='emailcandidato',
            name='email_candidato',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='DadosCandidato2',
        ),
    ]
