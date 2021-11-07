# Generated by Django 3.2.9 on 2021-11-07 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=50, unique=True)),
                ('creation_date', models.DateField(auto_now=True)),
                ('author', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=1000)),
                ('creation_date_of_comments', models.DateField(auto_now_add=True)),
                ('id_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='main.author')),
            ],
        ),
        migrations.CreateModel(
            name='AmountOfUpvotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_of_upvotes', models.PositiveIntegerField(default=1)),
                ('id_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.author')),
            ],
        ),
    ]
