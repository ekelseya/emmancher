# Generated by Django 3.1 on 2020-08-26 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the pattern name or number', max_length=100)),
                ('size', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['company', 'name'],
            },
        ),
        migrations.CreateModel(
            name='PatternCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'PatternCompanies',
                'ordering': ['company_name'],
            },
        ),
        migrations.CreateModel(
            name='PatternType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(help_text='Enter the pattern type, such as "Outerwear" or "Tops"', max_length=100)),
            ],
            options={
                'ordering': ['type'],
            },
        ),
        migrations.CreateModel(
            name='PatternView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view', models.CharField(max_length=10)),
                ('fabric_req', models.CharField(help_text='Enter the fabric requirements in yards', max_length=20)),
            ],
            options={
                'ordering': ['view'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fabric', models.CharField(max_length=100)),
            ],
        ),
    ]