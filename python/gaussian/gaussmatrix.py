import numpy as np
from scipy import stats
x = stats.norm(0, 0.84089642).pdf(np.arange(-3, 4))
g = np.outer(x, x)