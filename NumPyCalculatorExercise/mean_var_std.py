import numpy as np

list = ([0, 1, 2, 3, 4, 5, 6, 7, 8])
calculations = {}


def calculate(list):
  if (len(list) == 9):
    a = np.array(list)
    b = np.array(list)
    a = a.reshape(3, 3)
    mean = np.mean(a, axis=0)
    variance = np.var(a, axis=0)
    stddev = np.std(a, axis=0)
    max = np.max(a, axis=0)
    min = np.min(a, axis=0)
    sum = np.sum(a, axis=0)
    mean0 = np.mean(a, axis=1)
    variance0 = np.var(a, axis=1)
    stddev0 = np.std(a, axis=1)
    max0 = np.max(a, axis=1)
    min0 = np.min(a, axis=1)
    sum0 = np.sum(a, axis=1)
    mean1 = np.mean(b, axis=0)
    variance1 = np.var(b, axis=0)
    stddev1 = np.std(b, axis=0)
    max1 = np.max(b, axis=0)
    min1 = np.min(b, axis=0)
    sum1 = np.sum(b, axis=0)
    calculations = {
      'mean': [mean.tolist(), mean0.tolist(), mean1],
      'variance': [variance.tolist(), variance0.tolist(), variance1],
      'standard deviation': [stddev.tolist(), stddev0.tolist(), stddev1],
      'max': [max.tolist(), max0.tolist(), max1],
      'min': [min.tolist(), min0.tolist(), min1],
      'sum': [sum.tolist(), sum0.tolist(), sum1]
    }
  else:
    raise ValueError("List must contain nine numbers")

  return calculations
