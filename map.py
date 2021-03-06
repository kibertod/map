from urllib.request import urlopen
import requests


class Map:
	def __init__(self, cords, size, layer, zoom=5):
		self.cords = cords
		self.size = size
		self.layer = layer
		self.zoom = zoom

	def load(self):
		url = "https://static-maps.yandex.ru/1.x/?"
		url += f"ll={','.join(list(map(str, self.cords)))}"
		url += f"&size={','.join(list(map(str, self.size)))}"
		url += f"&l={self.layer}"
		url += f"&z={self.zoom}"
		res = urlopen(url).read()
		return res

	def update(self, **kwargs):
		if "zoom" in kwargs:
			if self.layer == 'sat':
				if kwargs['zoom'] in range(20):
					self.zoom = kwargs['zoom']
			elif kwargs["zoom"] in range(24):
				self.zoom = kwargs["zoom"]
		if "cords" in kwargs:
			if -90 < kwargs["cords"][1] < 90 and -180 < kwargs["cords"][0] < 180:
				self.cords = kwargs["cords"]
			elif -180 > kwargs["cords"][0]:
				self.cords = [360 + kwargs["cords"][0], kwargs["cords"][1]]
			elif 180 < kwargs["cords"][0]:
				self.cords = [kwargs["cords"][0] - 360, kwargs["cords"][1]]
		if "layer" in kwargs:
			self.layer = kwargs['layer']
			if self.layer == 'sat' and self.zoom not in range(20):
				self.zoom = 19

	def find(self, address_name):
		response = requests.get('https://geocode-maps.yandex.ru/1.x/?geocode={}'
								'&apikey=40d1649f-0493-4b70-98ba-98533de7710b&format=json'.format(address_name))
		json_responce = response.json()
		return json_responce['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']

	def point_func(self, cords):
		pass

	def clear_point_func(self):
		pass



def test():
	return Map([37.620070, 55.753630], [450, 450], "map").load()
