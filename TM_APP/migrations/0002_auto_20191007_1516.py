# Generated by Django 2.2.1 on 2019-10-07 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TM_APP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='coursres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attatchment', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.FileField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='comments',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.RemoveField(
            model_name='posts',
            name='comments',
        ),
        migrations.AddField(
            model_name='posts',
            name='comments',
            field=models.ManyToManyField(to='TM_APP.comments'),
        ),
        migrations.RemoveField(
            model_name='posts',
            name='id',
        ),
        migrations.AddField(
            model_name='posts',
            name='id',
            field=models.AutoField(auto_created=True, default=2, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TM_APP.coursres')),
            ],
        ),
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=26, unique=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TM_APP.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=26, unique=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TM_APP.questions')),
            ],
        ),
    ]