from django.db import migrations, models

# Adiciona os campos de foto e de visibilidade na tabela de contatos.
class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='picture',
            field=models.ImageField(blank=True, upload_to='pictures/%Y/%m/'),
        ),
        migrations.AddField(
            model_name='contact',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]
