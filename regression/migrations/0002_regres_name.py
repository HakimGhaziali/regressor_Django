# Generated by Django 4.1 on 2022-08-30 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regression', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='regres',
            name='name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='esme', to='regression.esm'),
            preserve_default=False,
        ),
    ]
