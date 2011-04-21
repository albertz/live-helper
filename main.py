# by Albert Zeyer, 2011

class Document:
	MarkdownTxtType = 0
	def __init__(self):
		self.type = None

def foregroundDocument(): return Document()
def waitSystemEvent():
	# TODO ...
	import time
	time.sleep(1)

class Window:
	def placeNextTo(self, win):
		pass
	def showMarkdown(self, txt):
		pass

while True:
	doc = foregroundDocument()
	if doc.type == MarkdownTxtType:
		win = Window()
		win.placeNextTo(doc)
		win.showMarkdown(doc.txt)

	waitSystemEvent()
