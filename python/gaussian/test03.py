import numpy as np
import scipy.misc
import scipy.signal
from scipy import stats

w = scipy.misc.imread("test_in_04.png")
p = scipy.misc.imread("test_out_04.png")

temp1 = scipy.signal.convolve(w.transpose(),w)
temp2 = temp1[::-1]
temp3 = scipy.signal.convolve(temp2,w.transpose())
v = scipy.signal.convolve(temp3,p)

tem1 = scipy.signal.convolve(p.transpose(),p)
tem2 = tem1[::-1]
tem3 = scipy.signal.convolve(tem2,p.transpose())
final = scipy.signal.convolve(tem3,v)

print final
# np.savetxt('png04_in_01.txt',w,fmt='%3d')
# np.savetxt('png04_out_01.txt',final,fmt='%3d')
# scipy.misc.imsave('outfile.png', final)