from DAL.scc import Scc as SccDAL

class Scc:
	def __init__(self):
		self.scc = SccDAL()
	def post(self, json_data):
		print "BLL"
		return self.scc.post(json_data)