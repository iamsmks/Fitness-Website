# Generated by Django 4.1.7 on 2023-04-01 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StayFit', '0003_userpreference_delete_workout'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserPreference',
        ),
        migrations.AddField(
            model_name='gexercise',
            name='video_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
