# Generated by Django 4.1 on 2022-08-25 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_filmes_duracao"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="genero",
            options={"verbose_name_plural": "Generos"},
        ),
    ]
