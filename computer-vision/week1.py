# coding: utf-8

## Required imports.
import cv2, numpy as np, os

## Exercise 1
def basic_convolution(image, kernel, verbose=False):
  'Computes the convolution of an image with a kernel.'

  ## TODO
  
  return image


## Exercise 2
def padded_convolution(image, kernel, verbose=False):
  'Computes the convolution of an image with a kernel, with clamp-to-edge.'

  ## TODO

  return image


## Exercise 3
def basic_convolution_dft(image, kernel, verbose=False):
  'Computes the convolution of an image with a kernel using a basic DFT-based approach.'
   
  ## TODO

  return image
  

## Exercise 4
def padded_convolution_dft(image, kernel, verbose=False):
  'Computes the convolution of an image with a kernel using a DFT-based approach (clamp-to-edge).'

  ## TODO
  
  return image


if __name__ == '__main__':

  verbose = True
  
  ## Start background thread for event handling of windows.
  if verbose:
    cv2.namedWindow("image")
    cv2.namedWindow("result")
    cv2.startWindowThread()
  
  ## Read in example image (greyscale, float, half-size).
  image = cv2.imread("/usr/share/doc/opencv-doc/examples/c/baboon.jpg", 0) / 255.0
  image = cv2.resize(image, (256, 256))
  if verbose: cv2.imshow("image", image)
  
  ## Prepare small convolution kernel (good for naive convolution).
  kernel = np.ones((5,5))
  kernel = kernel / kernel.sum() # normalise kernel
  
  ## Prepare large convolution kernel (good for DFT-based convolution).
  #sigma = 10
  #gauss = cv2.getGaussianKernel(2 * 3 * sigma + 1, sigma)
  #kernel = np.outer(gauss, gauss)

  if verbose: print "kernel = %i x %i" % kernel.shape
  result1 = basic_convolution(image, kernel, verbose=verbose)
  result2 = padded_convolution(image, kernel, verbose=verbose)
  result3 = basic_convolution_dft(image, kernel, verbose=verbose)
  result4 = padded_convolution_dft(image, kernel, verbose=verbose)
  
  ## Save images to disk for comparison.
  cv2.imwrite(os.path.expanduser("image-input.png"), np.uint8(255 * image))
  cv2.imwrite(os.path.expanduser("image-basic_convolution.png"), np.uint8(255 * result1))
  cv2.imwrite(os.path.expanduser("image-padded_convolution.png"), np.uint8(255 * result2))
  cv2.imwrite(os.path.expanduser("image-basic_convolution-dft.png"), np.uint8(255 * result3))
  cv2.imwrite(os.path.expanduser("image-padded_convolution-dft.png"), np.uint8(255 * result4))

#  ## Time different implementations of convolution.
#  import timeit
#  for kernelSize in range(1, 40):
#    kernel = np.ones((kernelSize,kernelSize)) / (1.0 * kernelSize * kernelSize)

#    print "kernel %2ix%2i:" % kernel.shape,
#    if kernelSize < 4: print "%.3f s (own naive)," % timeit.timeit("padded_convolution(image, kernel)", "from __main__ import image, kernel, padded_convolution", number=1),
#    else: print "-.--- s (own naive),",
#    print "%.3f s (own DFT)," % (timeit.timeit("padded_convolution_dft(image, kernel)", "from __main__ import image, kernel, padded_convolution_dft", number=20) / 20),
#    print "%.3f s (OpenCV's filter2D)" % (timeit.timeit("cv2.filter2D(image, -1, kernel, borderType=cv2.BORDER_REPLICATE)", "from __main__ import image, kernel, cv2", number=20) / 20)
  
  ## show filtered image
  if verbose: cv2.imshow("result", result1)
  
  ## wait for keyboard input or windows to close
  if verbose: cv2.waitKey(0)
