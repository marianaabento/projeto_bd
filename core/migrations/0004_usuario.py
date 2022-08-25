# Generated by Django 4.1 on 2022-08-25 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_genero_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Usuario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=45)),
                ("email", models.EmailField(max_length=254)),
                ("senha", models.CharField(max_length=15)),
                ("dt_nasc", models.DateField()),
            ],
        ),
    ]
