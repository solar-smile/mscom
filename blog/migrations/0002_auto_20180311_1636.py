# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-11 13:36
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
