# Generated by Django 4.1.7 on 2023-04-21 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0016_alter_joblisting_employment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblisting',
            name='employment_status',
            field=models.CharField(choices=[('Part Time', 'Part Time'), ('Полное', 'Полное'), ('Freelance', 'Freelancer')], max_length=10),
        ),
    ]