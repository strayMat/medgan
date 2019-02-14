# class and method for patient

class patient(object):
	def __init__(self, codes, ix2codes, codes2hum):
		self.codes = [int(c) for c in codes if int(c) !=0]
		self.unmatching = [i for i in range(len(self.codes)) if ix2codes[i][2:] not in codes2hum.keys()]
		self.human_codes = [(c, codes2hum[ix2codes[i][2:]]) for i, c in enumerate(self.codes) if (i not in self.unmatching and c != 0)]


	def print(self):
		for nb, c in self.human_codes:
			print('{} {}'.format(nb, c))