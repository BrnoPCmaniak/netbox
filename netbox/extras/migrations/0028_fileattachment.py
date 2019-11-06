# Generated by Django 2.2.6 on 2019-11-06 10:31

from django.db import migrations, models
import django.db.models.deletion
import extras.models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('extras', '0027_webhook_additional_headers'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('object_id', models.PositiveIntegerField()),
                ('file', models.FileField(upload_to=extras.models.file_upload)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ['name'],
            },
	),
    ]

