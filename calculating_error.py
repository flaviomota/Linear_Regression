def get_y(m, b, x):
    y = m*x + b
    return y

# print(get_y(1, 0, 7) == 7)
# print(get_y(5, 10, 3) == 25)

def calculate_error(m, b, point):
  x_point, y_point = point
  y = m*x_point + b
  distance = abs(y - y_point)
  return distance

# print(calculate_error(1, 0, (3, 3)))
# print(calculate_error(1, 0, (3, 4)))
# print(calculate_error(1, -1, (3, 3)))
# print(calculate_error(-1, 1, (3, 3)))

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]

def calculate_all_erro(m, b, datapoints):
    total_error = 0
    for point in datapoints:
        point_error = calculate_error(m, b, point)
        total_error += point_error
    return total_error

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
smallest_error = float("inf")
best_m = 0
best_b = 0

for m in possible_ms:
    for b in possible_bs:
   	 error = calculate_all_error(m, b, datapoints)
   	 if error < smallest_error:
   		 best_m = m
   		 best_b = b
   		 smallest_error = error
       	 
print(best_m, best_b, smallest_error)

get_y(0.3, 1.7, 6)