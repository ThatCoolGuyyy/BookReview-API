# Generated by Django 4.0.6 on 2022-08-06 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookShop', '0003_alter_review_createdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='bookWebsite',
            field=models.CharField(max_length=100),
        ),
    ]
