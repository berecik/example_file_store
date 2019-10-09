# Generated by Django 2.2.6 on 2019-10-09 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('file', models.FileField(upload_to='files_valut')),
                ('hash', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=255, null=True)),
                ('date_to', models.DateField(null=True)),
                ('file_name', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
