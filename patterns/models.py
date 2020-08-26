from datetime import datetime

from django.conf import settings
from django.db import models
from django.urls import reverse


# Create your models here.
class PatternType(models.Model):
    """Defines the Pattern Type model"""
    type = models.CharField(max_length=100, help_text='Enter the pattern type, such as "Outerwear" or "Tops"')

    class Meta:
        ordering = ['type']

    def __str__(self):
        return self.type


class PatternCompany(models.Model):
    """Defines the Pattern Company model"""
    company_name = models.CharField(max_length=100)
    website = models.URLField

    class Meta:
        ordering = ['company_name']
        verbose_name_plural = 'PatternCompanies'

    def __str__(self):
        return self.company_name


class Pattern(models.Model):
    """Defines the Pattern model"""
    name = models.CharField(max_length=100, help_text='Enter the pattern name or number')
    company = models.ForeignKey('PatternCompany', on_delete=models.CASCADE)
    size = models.CharField(max_length=20)

    class Meta:
        ordering = ['company', 'name']

    def __str__(self):
        return f'{self.company} {self.name}'

    def get_absolute_url(self):
        """Returns the url to access the detail record for this pattern"""
        return reverse('pattern-detail', args=[str(self.id)])


class PatternView(models.Model):
    view = models.CharField(max_length=10)
    pattern = models.ForeignKey('Pattern', on_delete=models.CASCADE)
    pattern_type = models.ManyToManyField('PatternType')
    fabric_req = models.CharField(max_length=20, help_text='Enter the fabric requirements in yards')

    class Meta:
        ordering = ['view']

    def __str__(self):
        return f'{self.pattern} view {self.view}'


class Project(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    pattern = models.ForeignKey('PatternView', on_delete=models.CASCADE)
    fabric = models.CharField(max_length=100)
    start_date = models.DateField(default=datetime.now)
    finish_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['owner']

    def __str__(self):
        return f'{self.owner}\'s {self.pattern}'
