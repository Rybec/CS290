import pygame

# Bindings between specific event types
# and a text name for that event type
bindings = {
	pygame.QUIT : "quit",
#	"up":None,
}

# Bindings between the text name for events
# and the handlers for those events
handlers = {
	"quit":None,
}

def register(event, handler):
	''' Registers event handlers

	event -- the event name in 'handlers' and 'bindings'
	handler -- event handler that takes a single argument
	'''

	if event in handlers:
		handlers[event] = handler
	else:
		raise Exception("No such event: " + str(event))

def run():
	'''Check for events and run the appropriate handlers'''
	for event in pygame.event.get():
		if event.type in bindings:
			handlers[bindings[event.type]](event)
