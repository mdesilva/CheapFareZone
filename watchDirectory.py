import pyinotify
from splinter import Browser


#read pyinotify documentation at http://seb.dbzteam.org/pyinotify/
#splinter.readthedocs.io
browser = Browser() #initiate browser instance
wm = pyinotify.WatchManager () #initiate Watch Manager
mask = pyinotify.IN_MODIFY #watched events

browser.visit("file:///home/manuja/Desktop/CheapFareZone/index.html") #visit page

class EventHandler(pyinotify.ProcessEvent):
	def process_IN_MODIFY(self, event):
	    browser.reload() #takes no arguments, reloads page defined in visit()

handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)

watch = wm.add_watch('/home/manuja/Desktop/CheapFareZone/', mask, rec=True) #path to watch, mask of type of changes to watch

notifier.loop()
