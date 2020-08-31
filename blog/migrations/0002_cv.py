# Generated by Django 2.2.15 on 2020-08-31 13:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('dob', models.DateTimeField(default=django.utils.timezone.now)),
                ('email', models.CharField(max_length=200)),
                ('phoneNo', models.CharField(max_length=15)),
                ('profile', models.TextField()),
                ('objective', models.TextField()),
                ('SkillsAndA', models.TextField()),
                ('education', models.TextField()),
                ('workE', models.TextField()),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]