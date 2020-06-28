import pandas as pd
import math
#Load data
data_set = pd.read_csv('./giong_cay.csv', header=0).values
test_set = pd.read_csv('./giong_cay_test.csv', header=0).values

# print(data_set)
# print(test_set)

def cosinAB(a, b):  
  # Cosin = E(Ai * Bi)/(E(Ai^2) * E(Bi^2))
  sumAB = sum(a * b)
  sum_squareA = math.sqrt(sum([i * i for i in a]))    
  sum_squareB = math.sqrt(sum([i * i for i in b]))
  cosin = sumAB / (sum_squareA * sum_squareB)
  return cosin

for test in test_set:
  print('Case #{}: {}'.format(int(test[0]), tuple(test[1:])))
  maxCosin, neighbor = -1, None
  for data in data_set:    
    cosin = cosinAB(data[1:], test[1:])
    print('Cosine similarity with tag {}: {}'.format(data[0], cosin))
    if(cosin > maxCosin):
      maxCosin = cosin
      neighbor = data[0]
  print('Neighbor: {}'.format(neighbor))
