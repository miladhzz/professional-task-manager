# Generated by Django 3.2.7 on 2022-04-08 09:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import todo.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_id', models.CharField(blank=True, default=todo.models.group_id_creator, editable=False, max_length=20, primary_key=True, serialize=False, unique=True)),
                ('link', models.CharField(blank=True, default=todo.models.group_link_creator, editable=False, max_length=30, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('members', models.ManyToManyField(related_name='group_members', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('C', 'Created'), ('D', 'Doing'), ('F', 'Finished')], default='C', max_length=1)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('finished_date', models.DateTimeField(blank=True)),
                ('duration', models.CharField(blank=True, max_length=200)),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='todo.group')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=80)),
                ('avatar', models.ImageField(upload_to=todo.models.user_avatar)),
                ('biograhpy', models.CharField(blank=True, max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
