# Import libraries
import codecademylib  # This might be specific to Codecademy's environment
from matplotlib import pyplot as plt

# Data for plotting
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# Number of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]

# Generate x-axis values
x_values = range(len(months))

# Create the figure with two subplots
plt.figure(figsize=(12, 8))  # Set figure size

# First subplot: Visits per month
ax1 = plt.subplot(1, 2, 1)  # Create the first subplot
plt.plot(x_values, visits_per_month, marker='o')
plt.xlabel('Months')
plt.ylabel('Visits per Month')
ax1.set_xticks(x_values)  # Set x-ticks to align with months
ax1.set_xticklabels(months)  # Set x-tick labels to month names
plt.title("Visits per Month")
plt.savefig('Visits_per_Month.png')  # Save the first plot

# Second subplot: Limes per month
ax2 = plt.subplot(1, 2, 2)  # Create the second subplot
ax2.set_xticks(x_values)  # Set x-ticks to align with months
ax2.set_xticklabels(months)  # Set x-tick labels to month names
plt.plot(x_values, key_limes_per_month, marker='v', color='red')
plt.plot(x_values, persian_limes_per_month, marker='x', color='blue')
plt.plot(x_values, blood_limes_per_month, marker='p', color='green')
plt.legend(['Key', 'Persian', 'Blood'], loc=1)  # Place legend in upper right corner
plt.title("Limes per Month")
plt.savefig('Limes_per_Month.png')  # Save the second plot

plt.show()
