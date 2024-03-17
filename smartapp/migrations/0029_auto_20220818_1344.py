# Generated by Django 3.2.4 on 2022-08-18 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smartapp', '0028_userprofile_nic'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='prime_subscription',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(null=True)),
                ('email', models.CharField(max_length=300, null=True)),
                ('amount', models.FloatField(max_length=5, null=True)),
                ('tr_id', models.CharField(max_length=20, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='smartapp.userprofile')),
            ],
        ),
    ]