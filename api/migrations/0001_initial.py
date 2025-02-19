# Generated by Django 3.2.16 on 2023-01-31 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(db_index=True)),
                ('service_name', models.CharField(blank=True, max_length=1024)),
                ('client_id', models.CharField(blank=True, max_length=1024)),
                ('ip_address', models.CharField(blank=True, max_length=128)),
                ('actor_user_id', models.UUIDField(null=True)),
                ('actor_role', models.CharField(blank=True, max_length=1024)),
                ('target_user_id', models.UUIDField(null=True)),
                ('target_profile_id', models.UUIDField(null=True)),
                ('target_type', models.CharField(blank=True, max_length=1024)),
                ('operation', models.CharField(blank=True, max_length=1024)),
            ],
        ),
    ]
