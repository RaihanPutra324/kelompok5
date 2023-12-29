# Generated by Django 4.2.7 on 2023-12-29 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AplikasiLayananUMKM', '0005_rename_esjeruk_esbuah'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bakwan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_menu', models.CharField(max_length=255)),
                ('deskripsi', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Batagor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_menu', models.CharField(max_length=255)),
                ('deskripsi', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_menu', models.CharField(max_length=255)),
                ('deskripsi', models.TextField()),
                ('gambar', models.ImageField(null=True, upload_to='img/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
