# Generated by Django 3.0.4 on 2020-03-10 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LecturerInfo',
            fields=[
                ('code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ModuleInfo',
            fields=[
                ('code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('year', models.CharField(max_length=4)),
                ('semester', models.IntegerField()),
                ('taughtBy', models.ManyToManyField(to='modules.LecturerInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('lecturer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='modules.LecturerInfo')),
                ('module', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='modules.ModuleInfo')),
            ],
        ),
    ]