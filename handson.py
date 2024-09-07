import time
import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(n):
    x = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            x = x + 1
    return x

# Part 2
# Timing the function for various n
n_values = list(range(1, 1001))  # From 1 to 1000
times = []

for n in n_values:
    start_time = time.time()
    f(n)
    end_time = time.time()
    times.append(end_time - start_time)

# Plot "time" vs "n"
plt.plot(n_values, times, label='Time vs n')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity of Function f(n)')
plt.show()

#Part 3
# Fitting a polynomial curve (degree 2)
coeffs = np.polyfit(n_values, times, 2)
p = np.poly1d(coeffs)

# Plot fitted curve
plt.plot(n_values, times, label='Time vs n')
plt.plot(n_values, p(n_values), label='Fitted Curve (Degree 2)', linestyle='--')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity of Function f(n) with Fitted Curve')
plt.legend()
plt.show()

# Part 4 
# Zooming in to find n_0
plt.plot(n_values, times, label='Time vs n')
plt.plot(n_values, p(n_values), label='Fitted Curve (Degree 2)', linestyle='--')
plt.xlim(0, 50)  # Zoom in on small values of n
plt.ylim(0, max(times[:50]))  # Adjust y-axis to match zoomed x-axis
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Zoomed Plot to Find n_0')
plt.legend()
plt.show()
