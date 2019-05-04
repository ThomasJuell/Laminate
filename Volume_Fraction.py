from PIL import Image 
from scipy.misc import imsave
import numpy as np

im = Image.open("sfrp_fiber1.png").convert('1')  
# convert image to binary image
# where the pixel values are either true (white) or false (black)
a = np.asarray(im)  # returns the pixel values as a numpy array
imageshape = a.shape     # returns a tuple of (lines,columns)
totpix = imageshape[0]*imageshape[1]   # computing the total number of pixels
white = np.count_nonzero(a)   # this is for the fiber in the current case

print('The image shape is',imageshape,'where the total no of pix=',totpix,'and no. of black pix =',white)
print('Fiber volume fraction is',white/totpix)
