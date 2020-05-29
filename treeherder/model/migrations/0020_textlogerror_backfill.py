from django.db import migrations, transaction


def backfill_job(apps, schema_editor):
    TextLogError = apps.get_model('model', 'TextLogError')
    with transaction.atomic():
        for row in TextLogError.objects.only('job', 'step').iterator():
            row.job_id = row.step_id
            row.save()


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0019_textlogerror_job'),
    ]

    operations = [
        migrations.RunPython(backfill_job),
    ]
