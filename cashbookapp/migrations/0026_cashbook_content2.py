# Generated by Django 4.0.4 on 2022-10-01 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashbookapp', '0025_alter_cashbook_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashbook',
            name='content2',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]