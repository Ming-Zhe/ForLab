import numpy as np
import scipy.misc
import scipy.signal
from scipy import stats
img1 = scipy.misc.imread("test_in_04.png")
x = stats.norm(0, 0.84089642).pdf(np.arange(-3, 4))
g = np.outer(x, x)

# jpg2 = np.convolve(jpg1,g)
img2 = scipy.signal.convolve(img1,g)
scipy.misc.imsave('test_out_04.png', img2)