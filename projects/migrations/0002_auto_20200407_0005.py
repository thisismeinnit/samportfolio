# Generated by Django 3.0.4 on 2020-04-06 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='summary',
            field=models.CharField(default='nil', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(default=0, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ProjectPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.CharField(max_length=200)),
                ('project', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='projects.Project')),
            ],
        ),
    ]
