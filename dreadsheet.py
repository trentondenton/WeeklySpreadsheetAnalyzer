import pandas as pd
import matplotlib.pyplot as plt

"""|--------------------------------------------------|
   | 1. Read & Sort Data                              |
   |--------------------------------------------------|"""
# Read Data
dreadsheet = pd.read_csv('performance.csv')
 # Index by Date
dreadsheet = dreadsheet.set_index('created_at') 
# Convert to Date/Time
dreadsheet.index = pd.to_datetime(dreadsheet.index)
# Sort by Date/Time
dreadsheet = dreadsheet.sort_index()  


"""|--------------------------------------------------|
   | 1. Calculate & Plot Tickets Per Day              |
   |--------------------------------------------------|"""
# Calculate Tickets Per Day
dates = dreadsheet.index
dates = dates.to_series().dt.date
dates = dates.value_counts()
# Tickets/Day Bar Chart
plt.bar(dates.index, dates.values)
plt.title('Tickets/Day')
plt.xlabel('Date')
plt.ylabel('Tickets')


"""|--------------------------------------------------|
   | 2. Calculate & Plot Tickets Per Mentor Per Day   |
   |--------------------------------------------------|"""
# Get Tickets/Mentor/Day
mentors = dreadsheet['mentor_email']
mentors = mentors.groupby([mentors.index.date, mentors]).count()

# Tickets/Mentor/Day Bar Chart
mentors.unstack().plot(kind='barh', stacked=True, subplots=True, figsize=(10, 10))

# Total Tickets Per Mentor
for i, ax in enumerate(plt.gcf().axes):
    for bar in ax.patches:
        ax.annotate(str(bar.get_width()), (bar.get_width(), bar.get_y() + bar.get_height() / 2), 
                    xytext=(5, 0), textcoords='offset points', ha='left', va='center')

plt.xlabel('Tickets')
plt.ylabel('Date')

"""|--------------------------------------------------|
   | 3. Calculate Tickets by Organization             |
   |--------------------------------------------------|"""
# Get Tickets by Organization
orgs = dreadsheet['organization']
orgs = orgs.groupby([orgs.index.date, orgs]).count()

# Tickets by Organization Bar Chart
orgs.unstack().plot(kind='barh', stacked=True, subplots=True, figsize=(10, 10))

# Total Tickets by Organization
for i, ax in enumerate(plt.gcf().axes):
    for bar in ax.patches:
        ax.annotate(str(bar.get_width()), (bar.get_width(), bar.get_y() + bar.get_height() / 2), 
                    xytext=(5, 0), textcoords='offset points', ha='left', va='center')

plt.xlabel('Tickets')
plt.ylabel('Date')
plt.show()

"""|--------------------------------------------------|
   | 4. Response Times per Day                        |
   |--------------------------------------------------|"""



"""|--------------------------------------------------|
   | 5. Response Times Per Day Per Organization       |
   |--------------------------------------------------|"""



