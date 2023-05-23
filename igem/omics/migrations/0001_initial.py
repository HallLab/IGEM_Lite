# Generated by Django 4.2.1 on 2023-05-23 15:14

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="snpgene",
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
                (
                    "rsid",
                    models.CharField(max_length=15, unique=True, verbose_name="SNP ID"),
                ),
                ("observed", models.CharField(max_length=30, verbose_name="observed")),
                (
                    "genomicassembly",
                    models.CharField(max_length=20, verbose_name="Assembly"),
                ),
                ("chrom", models.CharField(max_length=5, verbose_name="Chromosome")),
                ("start", models.CharField(max_length=15, verbose_name="Start")),
                ("end", models.CharField(max_length=15, verbose_name="End")),
                ("loctype", models.CharField(max_length=5, verbose_name="Local Type")),
                (
                    "rsorienttochrom",
                    models.CharField(max_length=5, verbose_name="Orient Chrom"),
                ),
                (
                    "contigallele",
                    models.CharField(max_length=20, verbose_name="Contig Allele"),
                ),
                ("contig", models.CharField(max_length=20, verbose_name="Contig")),
                ("geneid", models.CharField(max_length=15, verbose_name="Gene ID")),
                (
                    "genesymbol",
                    models.CharField(max_length=30, verbose_name="Gene Symbol"),
                ),
            ],
        ),
    ]
