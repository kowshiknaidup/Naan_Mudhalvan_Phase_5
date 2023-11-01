import matplotlib.pyplot as plt

years = [2015, 2016, 2017, 2018, 2019]
avg_temperatures = [15.2, 15.8, 16.5, 16.3, 15.7]
plt.plot(years, avg_temperatures, marker='0')
plt.title('Average Temperature Trends')
plt.xlabel('Year')
plt.ylabel('Average Temperature (°C)')
plt.grid(True)
plt.show()