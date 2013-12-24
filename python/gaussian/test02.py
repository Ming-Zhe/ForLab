import numpy as np
import scipy.misc
import scipy.signal
from scipy import stats

img1 = scipy.misc.imread("test_in_04.png")
img2 = scipy.misc.imread("test_out_04.png")


temp1 = scipy.signal.convolve(img1.transpose(),img1)
temp2 = temp1[::-1]

temp3 = scipy.signal.convolve(temp2,img1.transpose())
temp4 = scipy.signal.convolve(temp3,img2)

print temp4
# np.savetxt('png04_result_01.txt',temp4,fmt='%3d')