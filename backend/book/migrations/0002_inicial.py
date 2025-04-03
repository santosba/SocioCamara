from django.db import migrations, models
from django.utils import timezone

class Migration(migrations.Migration):
    dependencies = [
        ('book', '0001_initial'),  # Adjust based on your last migration
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='published',
            field=models.DateTimeField(auto_now_add=True, default=timezone.now),
            preserve_default=False,
        ),
    ]