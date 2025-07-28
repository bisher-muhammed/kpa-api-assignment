from django.db import models

# Create your models here.

class WheelSpecification(models.Model):
    form_number = models.CharField(max_length=100)
    submitted_by = models.CharField(max_length=100)
    submitted_date = models.DateField()
    
    # Individual fields from "fields"
    axle_box_housing_bore_dia = models.CharField(max_length=100)
    bearing_seat_diameter = models.CharField(max_length=100)
    condemning_dia = models.CharField(max_length=100)
    intermediate_wwp = models.CharField(max_length=100)
    last_shop_issue_size = models.CharField(max_length=100)
    roller_bearing_bore_dia = models.CharField(max_length=100)
    roller_bearing_outer_dia = models.CharField(max_length=100)
    roller_bearing_width = models.CharField(max_length=100)
    tread_diameter_new = models.CharField(max_length=100)
    variation_same_axle = models.CharField(max_length=100)
    variation_same_bogie = models.CharField(max_length=100)
    variation_same_coach = models.CharField(max_length=100)
    wheel_disc_width = models.CharField(max_length=100)
    wheel_gauge = models.CharField(max_length=100)
    wheel_profile = models.CharField(max_length=100)

    def __str__(self):
        return self.form_number

