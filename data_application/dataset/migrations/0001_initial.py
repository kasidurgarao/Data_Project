# Generated by Django 4.1.7 on 2023-05-08 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('data_file', models.FileField(upload_to='datasets')),
            ],
        ),
        migrations.CreateModel(
            name='PlottedData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_x', models.CharField(max_length=255)),
                ('column_y', models.CharField(max_length=255)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataset.dataset')),
            ],
        ),
        migrations.CreateModel(
            name='ComputedData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_name', models.CharField(max_length=255)),
                ('operation', models.CharField(max_length=3)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataset.dataset')),
            ],
        ),
    ]
