# Generated by Django 4.2.16 on 2025-01-17 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('cpf', models.CharField(max_length=12, unique=True)),
            ],
            options={
                'db_table': 'developer',
            },
        ),
        migrations.CreateModel(
            name='LevelDeveloper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='Default Description', max_length=20, unique=True)),
            ],
            options={
                'db_table': 'level_developer',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField()),
                ('update_at', models.CharField()),
                ('code', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='StatusDeveloper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='Default Description', max_length=20, unique=True)),
            ],
            options={
                'db_table': 'status_developer',
            },
        ),
        migrations.CreateModel(
            name='StatusProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='Default Description', max_length=20, unique=True)),
            ],
            options={
                'db_table': 'status_project',
            },
        ),
        migrations.CreateModel(
            name='StatusTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='Default Description', max_length=20, unique=True)),
            ],
            options={
                'db_table': 'status_task',
            },
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('alias', models.CharField(max_length=12, unique=True)),
            ],
            options={
                'db_table': 'technology',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.FloatField(default=0.0)),
                ('description', models.CharField(default='Default Description', unique=True)),
                ('developer_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects_manager.developer')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects_manager.project')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects_manager.statustask')),
            ],
            options={
                'db_table': 'task',
            },
        ),
        migrations.CreateModel(
            name='ProjectTechnology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects_manager.project')),
                ('technology_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects_manager.technology')),
            ],
            options={
                'db_table': 'project_technology',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects_manager.statusproject'),
        ),
        migrations.CreateModel(
            name='DeveloperTechnology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('developer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects_manager.developer')),
                ('technology_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects_manager.technology')),
            ],
            options={
                'db_table': 'developer_technology',
            },
        ),
        migrations.AddField(
            model_name='developer',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects_manager.leveldeveloper'),
        ),
        migrations.AddField(
            model_name='developer',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects_manager.statusdeveloper'),
        ),
    ]
