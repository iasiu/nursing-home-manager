# Generated by Django 3.2.2 on 2021-05-24 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_alter_adresy_poczty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adresy',
            name='poczty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.poczty'),
        ),
        migrations.AlterField(
            model_name='domyseniora',
            name='adresy',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='database.adresy'),
        ),
        migrations.AlterField(
            model_name='kartyzdrowia',
            name='seniorzy',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='database.seniorzy'),
        ),
        migrations.AlterField(
            model_name='leki',
            name='domyseniora',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.domyseniora'),
        ),
        migrations.AlterField(
            model_name='leki',
            name='rodzajelekow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.rodzajelekow'),
        ),
        migrations.AlterField(
            model_name='lozka',
            name='pokoje',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.pokoje'),
        ),
        migrations.AlterField(
            model_name='pracownicy',
            name='adresy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.adresy'),
        ),
        migrations.AlterField(
            model_name='pracownicy',
            name='domyseniora',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.domyseniora'),
        ),
        migrations.AlterField(
            model_name='pracownicy',
            name='stanowiska',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.stanowiska'),
        ),
        migrations.AlterField(
            model_name='seniorzy',
            name='domyseniora',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.domyseniora'),
        ),
        migrations.AlterField(
            model_name='seniorzy',
            name='lozka',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='database.lozka'),
        ),
        migrations.AlterField(
            model_name='wynagrodzenia',
            name='pracownicy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.pracownicy'),
        ),
    ]