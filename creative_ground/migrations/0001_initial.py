# Generated by Django 3.2.7 on 2021-10-29 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BackGroundImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='MoreImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images_field2', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='TextElements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OfferImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('background_image', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='creative_ground.backgroundimage')),
                ('extra_images', models.ManyToManyField(to='creative_ground.MoreImages')),
                ('main_text', models.ManyToManyField(to='creative_ground.TextElements')),
            ],
        ),
    ]
