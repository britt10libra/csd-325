# Brittany Smith
# Module 4.2 Assignment
# Purpose: Edit the program so Sitka high or low temperatures
# are displayed based on user selection.
# Source: Matplotlib quick start guide, The Pragmatic Programmer concepts

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high temperatures, and low
    # temperatures from this file.
    dates, highs, lows = [], [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)

        high = int(row[5])
        highs.append(high)

        low = int(row[6])
        lows.append(low)

while True:
    print("\nSitka Weather Menu")
    print("1. High Temperatures")
    print("2. Low Temperatures")
    print("3. Exit")

    choice = input(" Enter your choice: ")

    if choice == '1':
        # Plot the high temperatures.
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')

        # Format plot.
        plt.title("Daily high temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()

    elif choice == '2':
        # Plot the low temperatures.
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')

        # Format plot.
        plt.title("Daily low temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()

    elif choice == '3':
        print("Thank you for using the Sitka Weather program. Goodbye!")
        sys.exit()
    else:
        print("Invalid selection. Please choose 1, 2, or 3.")
