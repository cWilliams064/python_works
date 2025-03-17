def describe_car(manufacturer, model, **car_info):
  car_info['manufacturer'] = manufacturer
  car_info['model'] = model
  return car_info

car = describe_car('chevrolet', 'malibu', color='white', sunroof='false')
print(car)