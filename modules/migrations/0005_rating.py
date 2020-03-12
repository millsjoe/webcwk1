# Generated by Django 3.0.4 on 2020-03-10 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0004_delete_rating'),
    ]

    operations = [
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
