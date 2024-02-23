# Create some helper functions to wrap the
# Pygame image functions

import pygame
import numpy

def getImage(filename):
  """
  Input: filename - string containing image filename to open
  Returns: 2d array of RGB values
  """
  image = pygame.image.load(filename)
  return pygame.surfarray.array3d(image).tolist()

def showImage(pixels, title):
    """
    Input:  pixels - 2d array of RGB values
            title - title of the window
    Output: show the image in a window
    """
    nparray = numpy.asarray(pixels)
    surf = pygame.surfarray.make_surface(nparray)
    (width, height, colours) = nparray.shape
    pygame.display.init()
    pygame.display.set_caption(title)
    screen = pygame.display.set_mode((width, height))
    screen.fill((225, 225, 225))
    screen.blit(surf, (0, 0))
    pygame.display.update()
