# Generated by Django 3.1 on 2020-08-12 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmallSemesterChild', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Belong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.IntegerField()),
                ('username', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Browse',
            fields=[
                ('browse_time', models.DateTimeField(auto_now=True)),
                ('browse_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('username', models.TextField()),
                ('doc_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('com_content', models.TextField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('com_author', models.TextField()),
                ('com_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('doc_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('demo_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('demo_content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('doc_name', models.TextField()),
                ('doc_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('doc_content', models.TextField()),
                ('introduction', models.TextField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('doc_groupid', models.IntegerField(blank=True, null=True)),
                ('doc_creater', models.IntegerField(blank=True, null=True)),
                ('isin_recycle', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_id', models.IntegerField()),
                ('username', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('creater', models.TextField()),
                ('groupid', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('group_name', models.TextField()),
                ('introduction', models.TextField()),
            ],
        ),
    ]
