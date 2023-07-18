# Generated by Django 4.2.3 on 2023-07-16 21:17

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
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(default='images/none/noimg.jpg', upload_to='images')),
                ('rating', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=200)),
                ('cat', models.CharField(max_length=200)),
            ],
        ),
    ]