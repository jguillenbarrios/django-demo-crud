from django.db import models

# Create your models here.
class Source(models.Model):
  source_id = models.AutoField(primary_key=True)
  source = models.CharField(max_length=100)

  def __str__(self):
    return self.source

class BusinessUnit(models.Model):
  business_unit_id = models.AutoField(primary_key=True)
  business_unit = models.CharField(max_length=100)

  def __str__(self):
    return self.business_unit

class Dashboard(models.Model):
  dashboard_id = models.AutoField(primary_key=True)
  dashboard_name = models.CharField(max_length=100)
  dashboard_description = models.CharField(max_length=200)
  dashboard_link = models.URLField(max_length=200)
  dashboard_tag = models.CharField(max_length=300)
  dashboard_source = models.ForeignKey(Source, on_delete=models.CASCADE)
  dashboars_business_unit = models.ForeignKey(BusinessUnit, on_delete=models.CASCADE)
  created_at = models.DateField(auto_now_add=True)
  # I want here the user who is adding the record
  #models.ForeignKey(settings.AUTH_USER_MODEL, ondelete=models.CASCADE)
  dashboard_owner = models.EmailField(max_length=100)
  internal_only = models.BooleanField(default=False)
  #override the Save to assign a custom value to the "tag link" using the url & dashboard name
  def save(self, *args, **kwargs):
    self.dashboard_tag =  '<a target="_blank" href="{}">{}</a>'.format(self.dashboard_link, self.dashboard_name)
    super(Dashboard, self).save(*args, **kwargs)
