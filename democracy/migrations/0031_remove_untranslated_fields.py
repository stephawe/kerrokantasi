# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-12-08 15:40
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.translation import ugettext_lazy as _


class Migration(migrations.Migration):

    dependencies = [
        ('democracy', '0030_migrate_translatable_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactperson',
            name='title',
            field=models.CharField(verbose_name=_('title'), max_length=255, default='', null=True),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='contactperson',
            name='title',
        ),
        migrations.RemoveField(
            model_name='hearing',
            name='borough',
        ),
        migrations.AlterField(
            model_name='hearing',
            name='title',
            field=models.CharField(verbose_name=_('title'), max_length=255, default='', null=True),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='hearing',
            name='title',
        ),
        migrations.RemoveField(
            model_name='label',
            name='label',
        ),
        migrations.RemoveField(
            model_name='section',
            name='abstract',
        ),
        migrations.RemoveField(
            model_name='section',
            name='content',
        ),
        migrations.AlterField(
            model_name='section',
            name='title',
            field=models.CharField(verbose_name=_('title'), max_length=255, default='', null=True),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='section',
            name='title',
        ),
        migrations.RemoveField(
            model_name='sectionimage',
            name='caption',
        ),
        migrations.AlterField(
            model_name='sectionimage',
            name='title',
            field=models.CharField(verbose_name=_('title'), max_length=255, default='', null=True),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='sectionimage',
            name='title',
        ),
    ]