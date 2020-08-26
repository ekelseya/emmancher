from django.db import models


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

class PatternView(models.Model):
    view = models.CharField(max_length=10)
    pattern = models.ForeignKey('Pattern', on_delete=models.CASCADE)
    pattern_type = models.ManyToManyField('PatternType', null=True)

    class Meta:
        ordering = ['view']

    def __str__(self):
        return f'{self.pattern} {self.view}'
