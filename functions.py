import pygame 
import sys,os

def load_image(fileName,colorKey = -1):
  """Loads an image from a file"""
  fullName = os.path.join("assets/cards",fileName)
  try:
    image = pygame.image.load(fullName).convert()
    if colorKey == -1:
      colorKey = image.get_at((0,0))
      image.set_colorkey(colorKey)
    return image
  except:
    print("Load image opeartion failed: check the filepath and file permissions to make sure that the image is available")
    
 

