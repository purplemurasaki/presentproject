# Generated by Django 3.1.4 on 2021-02-17 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentpost', '0002_memorymodel_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memorymodel_1',
            name='content_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='memorymodel_1',
            name='content_3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='memorymodel_1',
            name='images_2',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='memorymodel_1',
            name='images_3',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='memorymodel_1',
            name='images_4',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='memorymodel_1',
            name='images_5',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='memorymodel_1',
            name='images_comment_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='memorymodel_1',
            name='images_comment_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='memorymodel_1',
            name='images_comment_3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='memorymodel_1',
            name='images_comment_4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='memorymodel_1',
            name='images_comment_5',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]