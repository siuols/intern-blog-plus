# Generated by Django 2.0.4 on 2018-04-22 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
