# Generated by Django 3.2.8 on 2021-11-05 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, null=True, unique=True),
        ),
    ]
