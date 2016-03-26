print "Hello Python"

class WasRun(object):
	def __init__(self, name):
		self.WasRun = None
	def testMethod(self):
		pass

test = WasRun("testMethod")
print test.WasRun
test.testMethod()
print test.WasRun


