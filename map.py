from urllib.request import urlopen


class Map:
	def __init__(self, cords, size, layer):
		self.cords = map(str, cords)
		self.size = map(str, size)
		self.layer = layer


	def load(self):
		res =   urlopen(
					f"https://static-maps.yandex.ru/1.x/?ll={','.join(self.cords)}&size={','.join(self.size)}&l={self.layer}"
				).read()
		return 	res
			

def test():
	return Map(['37.620070', '55.753630'], [450, 450], "map").load()
