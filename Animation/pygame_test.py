import os
import pygame		# Load the Pygame module
pygame.display.init()		# Initialize Pygame

screen = pygame.display.set_mode((768, 512))	# Open window
screen.fill((255, 255, 255))			# Fill the Surface with white
pygame.display.flip()				# Copy Surface to the screen

filename = os.path.join('img', 'eggs2.png')

image = pygame.image.load(filename)	# Load the image file
image.convert()		# Convert the Surface format to the same as screen
image.convert_alpha()	# Convert Surface alpha to optimized format for screen

screen.blit(image, (0, 0))	# Draws the image onto the screen at (0, 0)

pygame.display.flip()				# Copy Surface to the screen

quit = False
while(not quit):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit = True

pygame.quit()		# Shut down Pygame (uninitialize)

print "Thank you for visiting!"


