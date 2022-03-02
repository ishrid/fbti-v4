# Generated by Django 4.0.3 on 2022-03-02 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlbiDOro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('attivo', models.BooleanField(default=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='albiDoro/img')),
                ('pdf', models.FileField(upload_to='albiDoro/pdf')),
            ],
        ),
        migrations.CreateModel(
            name='Calendari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('attivo', models.BooleanField(default=True)),
                ('anno', models.IntegerField(blank=True, null=True)),
                ('pdf', models.FileField(upload_to='calendari')),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('attivo', models.BooleanField(default=True)),
                ('anno', models.IntegerField(blank=True, null=True)),
                ('pdf', models.FileField(upload_to='categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Classifiche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('attivo', models.BooleanField(default=True)),
                ('anno', models.IntegerField(blank=True, null=True)),
                ('pdf', models.FileField(upload_to='classifiche')),
            ],
        ),
        migrations.CreateModel(
            name='Regolamenti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('attivo', models.BooleanField(default=True)),
                ('anno', models.IntegerField(blank=True, null=True)),
                ('pdf', models.FileField(upload_to='regolamenti')),
            ],
        ),
    ]
