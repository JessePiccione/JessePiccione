# Generated by Django 5.0 on 2024-03-05 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technologies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
            ],
        ),
    ]
