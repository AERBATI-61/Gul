# Generated by Django 4.0.5 on 2022-06-20 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TibCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tibCategory', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Tib Category',
            },
        ),
        migrations.CreateModel(
            name='Tib',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('tib_image', models.ImageField(blank=True, null=True, upload_to='tib_image/')),
                ('tib_Video', models.FileField(blank=True, null=True, upload_to='tib_Video/')),
                ('description', models.TextField()),
                ('active', models.BooleanField()),
                ('publicatetime', models.DateTimeField()),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Tib_Category', to='tib.tibcategory')),
            ],
            options={
                'verbose_name': 'Tib',
                'verbose_name_plural': 'Tib',
                'ordering': ['-publicatetime'],
            },
        ),
    ]