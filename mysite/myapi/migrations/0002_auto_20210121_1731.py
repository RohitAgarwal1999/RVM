# Generated by Django 3.1.5 on 2021-01-21 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='employ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('sirname', models.CharField(max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='Hero',
        ),
    ]