# by Albert Zeyer, 2011

class Document:
	MarkdownTxtType = 0
	def __init__(self):
		self.type = None

def foregroundDocument(): return Document()
def waitFocusChangeEvent():
	# TODO ...
	import time
	time.sleep(1)

class Window:
	def showMarkdown(self, txt):
		pass

while True:
	doc = foregroundDocument()
	if doc.type == MarkdownTxtType:
		win = Window()
		win.showMarkdown(doc.txt)
	waitFocusChangeEvent()
