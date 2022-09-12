# Generated by Django 4.1.1 on 2022-09-12 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('celular', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('numPaciente', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('fechaNacimiento', models.DateField()),
                ('idPaciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Paciente', to='persona.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('numFamiliar', models.AutoField(primary_key=True, serialize=False)),
                ('parentesco', models.CharField(max_length=45)),
                ('correo', models.CharField(max_length=45)),
                ('idFamiliar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Familiar', to='persona.persona')),
                ('pacienteAsig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Paciente', to='persona.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='persona.persona')),
                ('registro', models.SmallIntegerField(unique=True)),
                ('especialidad', models.CharField(max_length=45)),
                ('idDoctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Doctor', to='persona.persona')),
            ],
            bases=('persona.persona',),
        ),
    ]
