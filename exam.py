class exam():
	level = r""""""         # class variable shared by all instances
	titre = r""""""
	dateOfExam = r""""""
	leftHead= r"""Nom : \\ Prénom :"""
	rightHead = r""""""
	leftFoot = r""""""
	rightFoot = r""""""
	centerHead = r""""""
	centerFoot = r""""""
	session = r"""2023-24"""
	firstpagefooter = [r"""LPO G. BRASSENS""" , r"""Page \thepage\ / \numpages""" , r"""Session """+session ]
	runningfooter = [ r"""LPO G. BRASSENS""" , r"""Page \thepage\ / \numpages""", r"""Session """+session ]
	runningheadrule = True
	runningfootrule = True
	duree=r""""""
	points=r""""""
	bonus=r""""""

	def __init__(self, level="", titre="", date="" ):
		self.level = level
		self.titre = titre

	def __str__(self):
		return( self.level+"-"+self.titre )

