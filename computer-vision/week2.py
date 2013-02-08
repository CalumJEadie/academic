# coding: utf-8

## Required imports.
import cv2, numpy as np, os


## Exercise 1 ----------------------------------------------------------------------


## TODO: Complete this for exercise 1a
def ComputeGradients(image):

  # TODO: define the kernels
  dxKernel        = np.array([[1]], dtype='float32');
  dyKernel        = np.array([[1]], dtype='float32');
  dx2Kernel       = np.array([[1]], dtype='float32');
  dy2Kernel       = np.array([[1]], dtype='float32');
  laplacianKernel = np.array([[1]], dtype='float32');

  # Apply the kernels to the image.
  dx = cv2.filter2D(image, cv2.CV_32F, dxKernel)
  dy = cv2.filter2D(image, cv2.CV_32F, dyKernel)

  # TODO: Calculate the gradient magnitude.
  gradMag = np.zeros_like(image)

  # Apply the second-order kernels.
  dx2       = cv2.filter2D(image, cv2.CV_32F, dx2Kernel)
  dy2       = cv2.filter2D(image, cv2.CV_32F, dy2Kernel)
  laplacian = cv2.filter2D(image, cv2.CV_32F, laplacianKernel)

  return dx, dy, gradMag, dx2, dy2, laplacian


## TODO: Complete this for exercise 1b
def ComputeEdges(dx, dy, gradientMagnitude):

  # TODO: Threshold the images at magnitude over 0.075.

  return dx, dy, gradientMagnitude


## TODO: Complete this for exercise 1c
def ComputeCanny(image):

  # TODO: Compute Canny edges (using second-order gradient).

  return image


## Exercise 2 ----------------------------------------------------------------------


## TODO: Complete this for exercise 2
def scaleSpaceEdges(image):

  # TODO: Calculate Gaussian-blurred images (using sigma = 1, 1.6, 2.56).
  gauss1 = np.zeros_like(image);
  gauss2 = np.zeros_like(image);
  gauss3 = np.zeros_like(image);

  # Calculate the edges using code from previous exercises.
  dx1, dy1, gradEdges1 = ComputeGradients(image)[:3]
  dx2, dy2, gradEdges2 = ComputeGradients(gauss1)[:3]
  dx3, dy3, gradEdges3 = ComputeGradients(gauss2)[:3]
  dx4, dy4, gradEdges4 = ComputeGradients(gauss3)[:3]

  # Normalise and write out to disk.
  dxEdges1, dyEdges1, gradEdges1 = ComputeEdges(dx1, dy1, gradEdges1)
  dxEdges2, dyEdges2, gradEdges2 = ComputeEdges(dx2, dy2, gradEdges2)
  dxEdges3, dyEdges3, gradEdges3 = ComputeEdges(dx3, dy3, gradEdges3)
  dxEdges4, dyEdges4, gradEdges4 = ComputeEdges(dx4, dy4, gradEdges4)

  # Overlay text about sigma and edge type.
  cv2.putText(dxEdges1,   'sigma = 0',       (10,20), cv2.FONT_HERSHEY_COMPLEX, 0.5, 1.0)
  cv2.putText(dxEdges2,   'sigma = 1',       (10,20), cv2.FONT_HERSHEY_COMPLEX, 0.5, 1.0)
  cv2.putText(dxEdges3,   'sigma = 1.6',     (10,20), cv2.FONT_HERSHEY_COMPLEX, 0.5, 1.0)
  cv2.putText(dxEdges4,   'sigma = 2.56',    (10,20), cv2.FONT_HERSHEY_COMPLEX, 0.5, 1.0)
  cv2.putText(dxEdges1,   'dx edges',       (170,20), cv2.FONT_HERSHEY_COMPLEX, 0.5, 1.0)
  cv2.putText(dyEdges1,   'dy edges',       (170,20), cv2.FONT_HERSHEY_COMPLEX, 0.5, 1.0)
  cv2.putText(gradEdges1, 'Grad Mag Edges', (100,20), cv2.FONT_HERSHEY_COMPLEX, 0.5, 1.0)
  
  # Concatenate the output images.
  separator = np.ones((dxEdges.shape[0], 2))
  row1 = np.concatenate((dxEdges1, separator, dyEdges1, separator, gradEdges1), axis = 1)
  row2 = np.concatenate((dxEdges2, separator, dyEdges2, separator, gradEdges2), axis = 1)
  row3 = np.concatenate((dxEdges3, separator, dyEdges3, separator, gradEdges3), axis = 1)
  row4 = np.concatenate((dxEdges4, separator, dyEdges4, separator, gradEdges4), axis = 1)

  scaleSpace = np.concatenate((row1, row2, row3, row4), axis = 0)
  cv2.imwrite(os.path.expanduser("scaleSpace.png"), np.uint8(255 * scaleSpace))

  # Return the Gaussians for the next exercise.
  return gauss1, gauss2, gauss3


## Exercise 3 ----------------------------------------------------------------------


## TODO: Complete this for exercise 
def DifferenceOfGaussiansLaplacian(gauss1, gauss2, gauss3):

  # TODO: Calculate the Laplacian of gauss1 and gauss2.
  Laplacian1 = np.zeros_like(gauss1)
  Laplacian2 = np.zeros_like(gauss1)

  # TODO: Calculate the difference of Gaussians (DoG).
  DoG1 = np.zeros_like(gauss1)
  DoG2 = np.zeros_like(gauss1)

  # Normalise and write out to disk
  Laplacian1 = normalise(Laplacian1)
  Laplacian2 = normalise(Laplacian2)
  DoG1       = normalise(DoG1)
  DoG2       = normalise(DoG2)

  # Overlay additional information.
  cv2.putText(Laplacian1, 'Laplacian', (10,20), cv2.FONT_HERSHEY_COMPLEX, 0.5, 1.0)
  cv2.putText(DoG1, 'Difference of Gaussians', (10,20), cv2.FONT_HERSHEY_COMPLEX, 0.5, 1.0)

  row1           = np.concatenate((Laplacian1, DoG1), axis = 1)
  row2           = np.concatenate((Laplacian2, DoG2), axis = 1)
  laplacianVsDoG = np.concatenate((row1, row2),       axis = 0)
  cv2.imwrite(os.path.expanduser("laplacianVsDoG.png"), np.uint8(255 * laplacianVsDoG))


## Utility functions (no need to edit them) ----------------------------------------


# Normalisation
def normalise(image):
  'Normalises the image so that the values lie from 0 to 1.'

  output = image - image.min();
  if(output.max() != 0):
    output = output / output.max();
  
  return output


# Writing out the gradient images
def WriteOutGradients(dx, dy, gradMag, dx2, dy2, laplacian):

  # Normalising the images so they can be saved
  dxOut        = normalise(dx);
  dyOut        = normalise(dy);
  gradMagOut   = normalise(gradMag);
  dx2Out       = normalise(dx2);
  dy2Out       = normalise(dy2);
  laplacianOut = normalise(laplacian);

  font = cv2.FONT_HERSHEY_COMPLEX
  cv2.putText(dxOut,        'dx',                 (10,20), font, 0.5, (1.0))
  cv2.putText(dyOut,        'dy',                 (10,20), font, 0.5, (1.0))
  cv2.putText(dx2Out,       'dx2',                (10,20), font, 0.5, (1.0))
  cv2.putText(dy2Out,       'dy2',                (10,20), font, 0.5, (1.0))
  cv2.putText(gradMagOut,   'Gradient Magnitude', (10,20), font, 0.5, (1.0))
  cv2.putText(laplacianOut, 'Laplacian',          (10,20), font, 0.5, (1.0))
  
  row1 = np.concatenate((dxOut,  dyOut,  gradMagOut),   axis = 1)
  row2 = np.concatenate((dx2Out, dy2Out, laplacianOut), axis = 1)
  combinedEdges = np.concatenate((row1, row2), axis = 0)

  ## Save images to disk for comparison.
  cv2.imwrite(os.path.expanduser("combinedGradients.png"), np.uint8(255 * combinedEdges))


# Writing out the edge images
def OutputEdges(dxEdges, dyEdges, gradEdges, cannyEdges):

  cv2.putText(dxEdges,   'dx edges',       (10,20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (1.0))
  cv2.putText(dyEdges,   'dy edges',       (10,20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (1.0))
  cv2.putText(gradEdges, 'grad mag edges', (10,20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (1.0))

  # convert to a floating point first (as canny returns uint8)
  cannyEdges = cannyEdges / 255.0
  cv2.putText(cannyEdges, 'Canny', (10,20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (1.0))

  combinedEdges = np.concatenate((dxEdges, dyEdges, gradEdges, cannyEdges), axis=1)

  # Save the edge images
  cv2.imwrite(os.path.expanduser("combinedEdges.png"), np.uint8(255 * combinedEdges))


if __name__ == '__main__':

  verbose = True
  
  ## Start background thread for event handling of windows.
  #if verbose:
  #  cv2.namedWindow("image")
  #  cv2.namedWindow("result")
  #  cv2.startWindowThread()
  
  ## Read in example image (greyscale, float, resize).
  image = cv2.imread("/usr/share/doc/opencv-doc/examples/c/lena.jpg", 0)
  imageUint8 = cv2.pyrDown(image);

  # See the image we're working on
  cv2.imwrite(os.path.expanduser("image-input.png"), imageUint8)

  imageF32 = np.array(imageUint8 / 255.0, dtype='float32');

  ## Apply them to an image
  dx, dy, gradMag, dx2, dy2, laplacian = ComputeGradients(imageF32)

  # Write them to disc
  WriteOutGradients(dx, dy, gradMag, dx2, dy2, laplacian)
 
  # Second part of the exercise, actually getting the edges
  dxEdges, dyEdges, gradMagEdges = ComputeEdges(dx, dy, gradMag)  

  # A more exciting edge detector
  canny = ComputeCanny(imageUint8)

  OutputEdges(dxEdges, dyEdges, gradMagEdges, canny)

  # Exercise 2 - edge detection in scale space
  gauss1, gauss2, gauss3 = scaleSpaceEdges(imageF32)

  # Exercise 3 - Approximating Laplacian as difference of Gaussians
  DifferenceOfGaussiansLaplacian(gauss1, gauss2, gauss3)

