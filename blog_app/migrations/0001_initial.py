# Generated by Django 4.1.5 on 2023-01-15 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('hobby', models.CharField(max_length=20)),
                ('email_id', models.CharField(max_length=20)),
                ('phone_num', models.IntegerField(default=0)),
            ],
        ),
    ]