# Generated by Django 5.1.4 on 2024-12-17 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=100)),
                ('published_date', models.DateField()),
                ('summary', models.TextField()),
                ('genre', models.CharField(max_length=50)),
            ],
        ),
    ]
