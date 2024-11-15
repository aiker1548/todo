# Generated by Django 5.0.3 on 2024-03-07 20:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='state',
        ),
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
        migrations.CreateModel(
            name='Labels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
                ('state', models.CharField(choices=[('Not started', 'Not started'), ('In progress', 'In progress'), ('Complete', 'Complete')], default='Not started', max_length=20)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('labels', models.ManyToManyField(to='todo.labels')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='State',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
