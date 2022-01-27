# Generated by Django 1.11.16 on 2018-11-12 13:57
import django.db.models.deletion
import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0032_increase_webhook_maxsize'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnvironmentVariable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(help_text='Name of the environment variable', max_length=128)),
                ('value', models.CharField(help_text='Value of the environment variable', max_length=256)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='environmentvariable',
            name='project',
            field=models.ForeignKey(help_text='Project where this variable will be used', on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
    ]
