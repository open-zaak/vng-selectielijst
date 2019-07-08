# Generated by Django 2.1.4 on 2019-02-27 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("selectielijst", "0008_resultaat_procestermijn_opmerking")]

    operations = [
        migrations.AlterField(
            model_name="resultaat",
            name="procestermijn_opmerking",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Voorbeeld: '25 jaar', '30 jaar, '5 of 10 jaar'",
                max_length=20,
                verbose_name="procestermijn opmerking",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="resultaat",
            name="waardering",
            field=models.CharField(
                choices=[
                    (
                        "blijvend_bewaren",
                        "Het zaakdossier moet bewaard blijven en op de Archiefactiedatum overgedragen worden naar een archiefbewaarplaats.",
                    ),
                    (
                        "vernietigen",
                        "Het zaakdossier moet op of na de Archiefactiedatum vernietigd worden.",
                    ),
                ],
                max_length=50,
                verbose_name="waardering",
            ),
        ),
    ]
