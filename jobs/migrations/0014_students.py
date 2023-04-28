# Generated by Django 4.1.7 on 2023-04-21 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0013_auto_20201104_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('speciality', models.CharField(max_length=255)),
                ('contacts', models.CharField(max_length=255)),
                ('exp', models.TextField()),
                ('skills', models.TextField()),
            ],
        ),
    ]