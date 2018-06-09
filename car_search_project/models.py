
from django.db import models


class Vehicle(models.Model):
	# id = models.IntegerField()
	make_id = models.IntegerField()
	make_desc = models.CharField(max_length=128)
	model_id = models.IntegerField()
	model_desc = models.CharField(max_length=128)
	variant_id = models.IntegerField()
	variant_desc = models.CharField(max_length=128)
	motor_flag = models.CharField(max_length=128)
	fuel_type_id = models.IntegerField()
	fuel_type_desc = models.CharField(max_length=128)
	seating_capacity = models.IntegerField()
	vehicle_image = models.CharField(max_length=128)
	search_string = models.CharField(max_length=128, db_index=True, unique=True)
	search_count = models.IntegerField(default=0, db_index=True)

	def __str__(self):
		return ("{} : {} ".format(self.search_string, self.search_count))

