# Generated by Django 4.1 on 2022-09-26 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_remove_artistas_titulo"),
    ]

    operations = [
        migrations.AddField(
            model_name="artistas",
            name="titulo",
            field=models.ManyToManyField(related_name="Artistas", to="core.filmes"),
        ),
        migrations.RemoveField(
            model_name="filmes",
            name="nome_genero",
        ),
        migrations.AddField(
            model_name="filmes",
            name="nome_genero",
            field=models.ManyToManyField(related_name="Filmes", to="core.genero"),
        ),
    ]
