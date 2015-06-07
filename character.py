class Character():
	def __init__(self, name, hp):
		self.name = name
		self.hp = hp

	def damage_taken(self, hit):
		self.hp -= hit

	def healing_taken(self, healing):
		if self.hp > 0:
			self.hp += healing

	def damage_done(self, hit):
		pass

	def healing_done(self, healing):
		pass	
