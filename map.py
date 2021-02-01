from urllib.request import urlopen


class Map:
	def __init__(self, cords, size, layer, zoom=5):
		self.cords = list(map(str, cords))
		self.size = list(map(str, size))
		self.layer = layer
		self.zoom = zoom


	def load(self):
		url = f"https://static-maps.yandex.ru/1.x/?ll={','.join(self.cords)}&size={','.join(self.size)}&l={self.layer}&z={self.zoom}"
		res = urlopen(url).read()
		return 	res

	def update(self, **kwargs):
		if "zoom" in kwargs:
			if kwargs["zoom"] in range(24):
				self.zoom = kwargs["zoom"]
			

def test():
	return Map(['37.620070', '55.753630'], [450, 450], "map").load()
