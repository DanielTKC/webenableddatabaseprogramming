# Generated by Django 4.2.7 on 2023-11-16 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepages', '0004_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='emp_skills',
            field=models.ManyToManyField(to='homepages.skill'),
        ),
    ]