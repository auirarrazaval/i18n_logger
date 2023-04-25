from django.db import models

# Create your models here.


class i18nLog(models.Model):
    LOCALES = (
        ("en", "English"),
        ("es", "Spanish"),
    )

    id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=255)
    hits = models.IntegerField(default=0)
    misses = models.IntegerField(default=0)
    value = models.TextField(blank=True, null=True)
    locale = models.CharField(max_length=2, choices=LOCALES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.key

    class Meta:
        db_table = "i18n_log"
        verbose_name = "i18n Log"
        verbose_name_plural = "i18n Logs"
        # Unique condition on key and locale
        unique_together = ("key", "locale")
