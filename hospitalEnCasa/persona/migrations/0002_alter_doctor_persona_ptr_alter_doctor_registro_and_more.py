# Generated by Django 4.1.1 on 2022-09-12 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='persona_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='persona.persona'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='registro',
            field=models.SmallIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='fechaNacimiento',
            field=models.DateField(),
        ),
    ]
