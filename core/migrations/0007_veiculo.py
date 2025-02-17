# Generated by Django 5.0.6 on 2024-07-12 11:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_remove_modelo_carca_modelo_marca_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Veiculo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("descricao", models.CharField(max_length=100)),
                ("ano", models.IntegerField(blank=True, default=0, null=True)),
                ("preco", models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                (
                    "acessorios",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="modelos",
                        to="core.acessorio",
                    ),
                ),
                (
                    "cor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="modelos",
                        to="core.cor",
                    ),
                ),
                (
                    "modelo",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="modelos",
                        to="core.modelo",
                    ),
                ),
            ],
        ),
    ]
