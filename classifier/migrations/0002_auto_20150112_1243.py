# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classifier',
            options={'ordering': ['-sort', 'translit'], 'verbose_name_plural': '\u041a\u043b\u0430\u0441\u0441\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440'},
        ),
        migrations.AddField(
            model_name='classifier',
            name='classifiers',
            field=models.ManyToManyField(related_name='classifiers_rel_+', to='classifier.Classifier', blank=True),
            preserve_default=True,
        ),
    ]
