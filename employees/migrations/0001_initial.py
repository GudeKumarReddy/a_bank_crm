# Generated by Django 5.0.3 on 2024-03-26 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('branch', models.CharField(max_length=150)),
                ('role', models.CharField(choices=[('manager', 'Manager'), ('ast_manager', 'Ast Manager'), ('clerk', 'Clerk')], default='clerk', max_length=50)),
                ('verified', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Employees',
            },
        ),
        migrations.CreateModel(
            name='FileStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('file', models.FileField(upload_to='uploads/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
