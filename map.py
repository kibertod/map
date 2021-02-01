from urllib.request import urlopen


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
		return 	res

	def update(self, **kwargs):
		if "zoom" in kwargs:
			if kwargs["zoom"] in range(24):
				self.zoom = kwargs["zoom"]
		if "cords" in kwargs:
			self.cords = kwargs["cords"]
			

def test():
	return Map([37.620070, 55.753630], [450, 450], "map").load()
