import json
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

class Day:
	def __init__(self, day_dict):
		self.minutes = day_dict['minuteCount']
		self.pickups = day_dict['pickupCount']
		self.date = day_dict['date'].split('T')[0] # %Y-%M-%D
		self.is_weekday = datetime.strptime(self.date, '%Y-%M-%d').weekday() < 5

	def __repr__(self):
		return f'''minutes: {self.minutes}, pickups: {self.pickups}, 
			date: {self.date}'''

with open('data/moment.json') as f:
	data = json.load(f)

day_data = next(iter(data.values()))

days = [Day(d) for d in day_data]
# filter out non 2018
days = [d for d in days if '2018' in d.date]

# what is the average time spent on my phone across all days?
# wht is the standard deviation?
# plot a histogram/frequency chart of num hours on y axis and frequency on the x axis
# what was the most/least usage week/month?

# distinguish between weekends and weekdays

# what day of the week do i normally use my phone the most?
# create a plot of day of week on x axis and usage on x axis

# create a plot for weeks and months

minute_data = [d.minutes for d in days]
mean_time, time_var = np.mean(minute_data), np.std(minute_data)
bins = [i for i in range(0, max(minute_data) + 60, 60)]
n, bins, _ = plt.hist([minute_data], bins=bins)
plt.xlabel('Minutes of Phone Usage')
plt.xticks(bins)
plt.ylabel('Frequency (# of Days)')
plt.title('Histogram of Phone Usage Time')
plt.text(300, 50, r'$\mu={0:.2f},\ \sigma={1:.2f}$'.format(mean_time, time_var))
plt.grid(True)
# plt.show()

# pickups

pickups = [d.pickups for d in days]
print(pickups)
mean_num_picks, pick_var = np.mean(pickups), np.std(pickups)
print(mean_num_picks, pick_var)






