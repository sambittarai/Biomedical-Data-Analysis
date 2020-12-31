# Task 1 - Read a single dicom file
import imageio
import matplotlib.pyplot as plt
import numpy as np
import os


im = imageio.imread("chest-220.dcm")
print(im.shape) # (512, 512)

#metadata can be quite rich in medical images and can include: [1] patient demographics (name, age, sex, ...), [2] Acquisition Information (image shape,, modality, ...)
print(im.meta.keys()) #Dict([('TransferSyntaxUID', '1.2.840.10008.1.2'), ('SOPClassUID', '1.2.840.10008.5.1.4.1.1.2'), ('SOPInstanceUID', '1.3.6.1.4.1.14519.5.2.1.5168.1900.290866807370146801046392918286'), ('StudyDate', '20040529'), ('SeriesDate', '20040515'), ('ContentDate', '20040515'), ('StudyTime', '115208'), ('SeriesTime', '115254'), ('ContentTime', '115325'), ('Modality', 'CT'), ('Manufacturer', 'GE MEDICAL SYSTEMS'), ('StudyDescription', 'PET CT with registered MR'), ('SeriesDescription', 'CT IMAGES - RESEARCH'), ('PatientName', 'STS_007'), ('PatientID', 'STS_007'), ('PatientBirthDate', ''), ('PatientSex', 'F '), ('PatientWeight', 82.0), ('StudyInstanceUID', '1.3.6.1.4.1.14519.5.2.1.5168.1900.381397737790414481604846607090'), ('SeriesInstanceUID', '1.3.6.1.4.1.14519.5.2.1.5168.1900.315477836840324582280843038439'), ('SeriesNumber', 2), ('AcquisitionNumber', 1), ('InstanceNumber', 57), ('ImagePositionPatient', (-250.0, -250.0, -180.62)), ('ImageOrientationPatient', (1.0, 0.0, 0.0, 0.0, 1.0, 0.0)), ('SamplesPerPixel', 1), ('Rows', 512), ('Columns', 512), ('PixelSpacing', (0.976562, 0.976562)), ('BitsAllocated', 16), ('BitsStored', 16), ('HighBit', 15), ('PixelRepresentation', 0), ('RescaleIntercept', -1024.0), ('RescaleSlope', 1.0), ('PixelData', b'Data converted to numpy array, raw data removed to preserve memory'), ('shape', (512, 512)), ('sampling', (0.976562, 0.976562))])

plt.imshow(im, cmap="gray")
#plt.imshow(im, vmin=-200, vmax=200, cmap="gray")
plt.axis("off")
plt.show()

#1 N number of dicom images, being stacked as array
im1 = imageio.imread('chest-000.dcm')
im2 = imageio.imread('chest-001.dcm')
im3 = imageio.imread('chest-002.dcm')

vol_arr = np.stack([im1, im2, im3])
vol_arr.shape # (3, 512, 512)

#2 Loading volumes directly from the disk
'''
imageio.volread() 
	* read multi-dimensional data directly
	* assemble a volume from multiple images
'''
os.listdir('chest-data') #['chest-000.dcm', 'chest-001.dcm', ..., 'chest-049.dcm']

vol = imageio.volread('chest-data')
#vol.meta - prints all the meta data
#vol.meta.keys() - prints all the keys of the meta data

#Plotting multiple images at once
fig, axes = plt.subplots(nrows=1, ncols=3)
axes[0].imshow(vol[0], cmap="gray")
axes[1].imshow(vol[10], cmap="gray")
axes[2].imshow(vol[20], cmap="gray")

for ax in axes:
	ax.axis('off')
plt.show()

#array shape
n0, n1, n2 = vol.shape #(50, 512, 512)
#Sampling rate - physical space covered by each element
d0, d1, d2 = vol.meta['sampling'] 
#Field of view (FOV) - Total amount of space covered along each axis by the image
FOV = (n0*d0, n1*d1, n2*d2)

#3 Modifying the aspect ratio
#This will result in a properly proportioned image, failing to adjust this aspect ratio will result in a distorted image.
im = vol[:,:,100]
d0, d1, d2 = vol.meta['sampling']
asp = d0/d1
plt.imshow(im, cmap="gray", aspect=asp)
plt.show()





