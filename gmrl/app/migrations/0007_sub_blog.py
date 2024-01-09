# Generated by Django 3.2.12 on 2024-01-08 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub_blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img')),
                ('name', models.CharField(max_length=50)),
                ('heading1', models.CharField(max_length=500)),
                ('description1', models.CharField(max_length=500)),
                ('heading2', models.CharField(max_length=500)),
                ('description2', models.CharField(max_length=500)),
                ('heading3', models.CharField(max_length=500)),
                ('description3', models.CharField(max_length=500)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.blog')),
            ],
        ),
    ]
