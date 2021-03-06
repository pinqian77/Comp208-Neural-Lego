# Generated by Django 3.2.5 on 2022-04-24 11:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Users_data',
            fields=[
                ('udpk', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('data_id', models.IntegerField()),
            ],
            options={
                'db_table': 'users_data',
                'ordering': ['udpk'],
            },
        ),
        migrations.CreateModel(
            name='Users_project',
            fields=[
                ('uppk', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('project_id', models.IntegerField()),
            ],
            options={
                'db_table': 'users_project',
                'ordering': ['uppk'],
            },
        ),
        migrations.CreateModel(
            name='Users_template',
            fields=[
                ('utpk', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('project_id', models.IntegerField()),
            ],
            options={
                'db_table': 'users_template',
                'ordering': ['utpk'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=50)),
                ('project_directory', models.CharField(max_length=100)),
                ('discription', models.CharField(max_length=100)),
                ('last_save_time', models.DateTimeField(auto_now_add=True)),
                ('is_public', models.CharField(max_length=50)),
                ('star', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'project',
                'ordering': ['project_id'],
            },
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('dataset_id', models.AutoField(primary_key=True, serialize=False)),
                ('dataset_name', models.CharField(max_length=50)),
                ('dataset_directory', models.CharField(max_length=100)),
                ('discription', models.CharField(max_length=100)),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'data',
                'ordering': ['dataset_id'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_id', models.IntegerField()),
                ('content', models.CharField(max_length=70)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('like_count', models.IntegerField(default=0)),
                ('user_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_owner+', to=settings.AUTH_USER_MODEL)),
                ('user_target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_target+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'comment',
                'ordering': ['comment_id'],
            },
        ),
    ]
