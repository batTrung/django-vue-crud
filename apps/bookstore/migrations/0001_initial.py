# Generated by Django 3.0.3 on 2020-06-22 02:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=60)),
                ('status', models.CharField(choices=[('D', 'Draft'), ('P', 'Published')], default='D', max_length=1)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('photo', models.URLField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
