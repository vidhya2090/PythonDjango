from django.db import models

# Create your models here.

class Persons(models.Model):
    personid = models.AutoField(db_column='PersonID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'persons'

class Studentdata(models.Model):
    num = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    emailid = models.CharField(max_length=255, blank=True, null=True)
    qualification = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'studentdata'

class Sales(models.Model):
    region = models.TextField(db_column='Region', blank=True, null=True)  # Field name made lowercase.
    country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
    item_type = models.TextField(db_column='Item Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_channel = models.TextField(db_column='Sales Channel', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    order_priority = models.TextField(db_column='Order Priority', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    order_date = models.TextField(db_column='Order Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    order_id = models.BigIntegerField(db_column='Order ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ship_date = models.TextField(db_column='Ship Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    units_sold = models.BigIntegerField(db_column='Units Sold', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unit_price = models.FloatField(db_column='Unit Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unit_cost = models.FloatField(db_column='Unit Cost', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_revenue = models.FloatField(db_column='Total Revenue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_cost = models.FloatField(db_column='Total Cost', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_profit = models.FloatField(db_column='Total Profit', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    new_column = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'sales'

