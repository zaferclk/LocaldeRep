# Generated by Django 2.0.4 on 2018-04-21 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YazilarTabloAdiKlasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=120, verbose_name='Başlık')),
                ('metin', models.TextField(verbose_name='İçerik')),
                ('yayinlanma_tarihi', models.DateTimeField(auto_now_add=True, verbose_name='Yayınlanma Tarihi')),
                ('yuklenen_dosya', models.FileField(blank=True, null=True, upload_to='')),
                ('slug_alani_modelden', models.SlugField(editable=False, max_length=130, unique=True)),
            ],
            options={
                'ordering': ['-yayinlanma_tarihi', 'id'],
            },
        ),
    ]
