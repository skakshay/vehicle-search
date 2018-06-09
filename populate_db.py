import os, csv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'car_search_project.settings')

import django
django.setup()

from car_search_project.models import Vehicle


def populate():
	with open('query_result.csv', 'r') as f:
		reader = csv.reader(f)
		next(reader)
		for row in reader: 
			car = Vehicle()
			car.make_id = int(row[1])
			car.make_desc = row[2]
			car.model_id = int(row[3])
			car.model_desc = row[4]
			car.variant_id = int(row[5])
			car.variant_desc = row[6]
			car.motor_flag = row[7]
			car.fuel_type_id = int(row[8])
			car.fuel_type_desc = row[9]
			car.seating_capacity = int(row[10])
			car.vehicle_image = row[11]
			car.search_string = row[12]
			car.search_count = 0
			car.save()




if __name__=="__main__":
	print ("Populating DB")
	populate();