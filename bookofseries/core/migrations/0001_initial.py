# Generated by Django 3.2 on 2022-04-27 23:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Nome')),
                ('last_name', models.CharField(max_length=100, verbose_name='Sobre nome')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='data de nascimento')),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Data de falecimento')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='CatalogItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('summary', models.TextField(max_length=1000, verbose_name='Resumo')),
                ('classification_type', models.CharField(blank=True, choices=[('u', 'unknown'), ('s', 'series'), ('m', 'Movie'), ('o', 'OVA')], default='u', max_length=1, verbose_name='Tipo')),
                ('season', models.CharField(max_length=50, verbose_name='Temporada')),
                ('episodes', models.IntegerField(verbose_name='Episodios Diponiveis')),
                ('watched', models.IntegerField(verbose_name='Episodios Vistos')),
                ('release', models.DateField(verbose_name='Data de lan??amento')),
                ('in_producing', models.BooleanField(blank=True, verbose_name='Nova Temporada')),
                ('new_season_preview', models.BooleanField(blank=True, verbose_name='Nova Temporada')),
                ('new_season_in', models.DateField(verbose_name='Nova temporada em')),
                ('image', models.ImageField(height_field=800, upload_to='', verbose_name='Capa', width_field=600)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.author')),
                ('genre', models.ManyToManyField(to='core.Genre', verbose_name='Genero')),
            ],
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.catalogitem', verbose_name='Titulo')),
            ],
        ),
    ]
