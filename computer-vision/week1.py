# coding: utf-8

## Required imports.
import cv2, numpy as np, os

import progressbar

## Exercise 1
def basic_convolution(image, kernel, verbose=False):
  '''
  Computes the convolution of an image with a kernel.
  
  :type image: numpy.ndarray
  :param kernel: normalised kernel
  :type kernel: numpy.ndarray
  :rtype: numpy.ndarray
  '''
  
  result = np.zeros_like(image)
  
  iend, jend = image.shape
  mend, nend = kernel.shape
  
  if verbose:
    pbar = progressbar.ProgressBar(widgets=[progressbar.ETA(), progressbar.Percentage(), progressbar.Bar()], maxval=(iend-mend)*(jend-nend)).start()
  
  # Outer loop iterates over every cell in result.
  for i in range(mend, iend): 
    for j in range(nend, jend):
      sum = 0
      # Inner loop iterates over every possible position of the kernel.
      for m in range(0, mend):
        for n in range(0, nend):
          sum += kernel[m, n] * image[i-m, j-n]
      # Do not need to normalise with /mend*nend as assume normalised.
      result[i, j] = sum
      if verbose:
        pbar.update((i-mend)*(jend-nend) + (j-nend))
        
  if verbose:
    pbar.finish()
      
  return result

## Exercise 2
def padded_convolution(image, kernel, verbose=False):
  '''Computes the convolution of an image with a kernel, with clamp-to-edge.
  
  :type image: numpy.ndarray
  :param kernel: normalised kernel
  :type kernel: numpy.ndarray
  :rtype: numpy.ndarray
  '''
  
  result = np.zeros_like(image)
  
  iend, jend = image.shape
  mend, nend = kernel.shape
  
  if verbose:
    pbar = progressbar.ProgressBar(widgets=[progressbar.ETA(), progressbar.Percentage(), progressbar.Bar()], maxval=(iend-mend)*(jend-nend)).start()
  
  # Outer loop iterates over every cell in result.
  for i in range(mend, iend): 
    for j in range(nend, jend):
      sum = 0
      # Inner loop iterates over every possible position of the kernel.
      for m in range(0, mend):
        for n in range(0, nend):
          sum += kernel[m, n] * image[i-m, j-n]
      # Do not need to normalise with /mend*nend as assume normalised.
      result[i, j] = sum
      if verbose:
        pbar.update((i-mend)*(jend-nend) + (j-nend))
        
  if verbose:
    pbar.finish()
    
  # Handle border effets using clamp to edge.
  # Pixel at the edge of image is repeated.
  resultClampedToEdge = np.zeros_like(result)
  resultClampedToEdge = cv2.copyMakeBorder(result[mend:, nend:], mend, mend, nend, nend, cv2.BORDER_REPLICATE)

  return resultClampedToEdge


def convolveWithDFT(a, b, verbose=False):
  '''
  Returns a convolved with b. Uses DFT and Convolution Theorem.
  
  :type a: numpy.ndarray
  :type b: numpy.ndarray
  :rtype: numpy.ndarray
  '''
  
  if verbose:
    pbar = progressbar.ProgressBar(widgets=[progressbar.Percentage(), progressbar.Bar()], maxval=4).start() 
 
  # Based on: docs.opencv.org/modules/core/doc/operations_on_arrays.html#dft
  
  # Create result and work out correct size.
  a_rows, a_cols = a.shape
  b_rows, b_cols = b.shape 
  result = np.empty((abs(a_rows-b_rows)+1, abs(a_cols-b_cols)+1))
  
  # Calculate size for DFT
  dft_width = cv2.getOptimalDFTSize((a_cols-b_cols)+1)
  dft_height = cv2.getOptimalDFTSize((a_rows-b_rows)+1)
  
  # Tranform a and b to fourier domain.
  # Complexity: O(n**2 * log2(n)
  
  # Create temporary buffers.
  temp_a = np.zeros((dft_height, dft_width))
  temp_b = np.zeros((dft_height, dft_width))
  
  # Copy a and b to top left conerns of temporary buffers.
  temp_a[0:a_cols, 0:a_rows] = a
  temp_b[0:b_cols, 0:b_rows] = b
  
  # Transform padded a&b in place.
  # Use nonzeroRows hint for faster processing.
  cv2.dft(temp_a, temp_a, 0, a_rows)
  if verbose:
    pbar.update(1)
  cv2.dft(temp_b, temp_b, 0, b_rows)
  if verbose:
    pbar.update(2)
  
  # By convolution theorem multiplication in fourier domain is equivalent to convolution
  # in original domain.
  # Perform per element multiplication.
  # Complexity: O(n**2)
  temp_a = cv2.mulSpectrums(temp_a, temp_b, False)
  if verbose:
    pbar.update(3)
  
  # Transform result from fourier domain to original domain.
  # Only need first abs(image_rows-kernel_rows)+1 rows of result.
  # Complexity: O(n**2 * log2(n)
  cv2.dft(temp_a, temp_a, cv2.DFT_INVERSE + cv2.DFT_SCALE, result.shape[1])

  result = temp_a[0:result.shape[0], 0:result.shape[1]]
  
  if verbose:
    pbar.finish()
  
  return result

## Exercise 3
def basic_convolution_dft(image, kernel, verbose=False):
  '''
  Computes the convolution of an image with a kernel using a basic DFT-based approach.
  
  :type image: numpy.ndarray
  :param kernel: normalised kernel
  :type kernel: numpy.ndarray
  :rtype: numpy.ndarray
  '''
  
  return convolveWithDFT(image, kernel, verbose)

## Exercise 4
def padded_convolution_dft(image, kernel, verbose=False):
  '''
  Computes the convolution of an image with a kernel using a DFT-based approach (clamp-to-edge).
  
  :type image: numpy.ndarray
  :param kernel: normalised kernel
  :type kernel: numpy.ndarray
  :rtype: numpy.ndarray
  '''
  
  mend, nend = kernel.shape

  result = convolveWithDFT(image, kernel, verbose)

  # Handle border effets using clamp to edge.
  # Pixel at the edge of image is repeated.
  resultClampedToEdge = np.zeros_like(result)
  resultClampedToEdge = cv2.copyMakeBorder(result[mend:, nend:], mend, mend, nend, nend, cv2.BORDER_REPLICATE)

  return resultClampedToEdge


if __name__ == '__main__':

  verbose = True
  
  ## Start background thread for event handling of windows.
  if verbose:
    cv2.namedWindow("image")
    cv2.namedWindow("result1")
    cv2.namedWindow("result2")
    cv2.namedWindow("result3")
    cv2.namedWindow("result4")
    cv2.startWindowThread()
  
  ## Read in example image (greyscale, float, half-size).
  # CV2 uses numpy arrays to represent images
  image = cv2.imread("/usr/share/doc/opencv-doc/examples/c/baboon.jpg", 0) / 255.0
  image = cv2.resize(image, (256, 256))
  if verbose: cv2.imshow("image", image)
  
  ## Prepare small convolution kernel (good for naive convolution).
  #kernel = np.ones((5,5))
  #kernel = kernel / kernel.sum() # normalise kernel
  
  ## Prepare large convolution kernel (good for DFT-based convolution).
  #sigma = 10
  sigma = 2
  gauss = cv2.getGaussianKernel(2 * 3 * sigma + 1, sigma)
  kernel = np.outer(gauss, gauss)

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

  ## Time different implementations of convolution.
  import timeit
  for kernelSize in range(1, 40):
    kernel = np.ones((kernelSize,kernelSize)) / (1.0 * kernelSize * kernelSize)

    print "kernel %2ix%2i:" % kernel.shape,
    if kernelSize < 4: print "%.3f s (own naive)," % timeit.timeit("padded_convolution(image, kernel)", "from __main__ import image, kernel, padded_convolution", number=1),
    else: print "-.--- s (own naive),",
    print "%.3f s (own DFT)," % (timeit.timeit("padded_convolution_dft(image, kernel)", "from __main__ import image, kernel, padded_convolution_dft", number=20) / 20),
    print "%.3f s (OpenCV's filter2D)" % (timeit.timeit("cv2.filter2D(image, -1, kernel, borderType=cv2.BORDER_REPLICATE)", "from __main__ import image, kernel, cv2", number=20) / 20)
  
  ## show filtered image
  if verbose: cv2.imshow("result1", result1)
  if verbose: cv2.imshow("result2", result2)
  if verbose: cv2.imshow("result3", result3)
  if verbose: cv2.imshow("result4", result4)
  
  ## wait for keyboard input or windows to close
  if verbose: cv2.waitKey(0)
