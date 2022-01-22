import argparse
from pprint import pprint  
import datetime

import pypistats

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

#if __name__ == "__main__":
#    parser = argparse.ArgumentParser(
#        description="Example use of pypistats",
#        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
#   )
#   args = parser.parse_args()

#   print(
#       pypistats.overall(
#           "generiter", start_date="2021-10-31", end_date="2022-01-22", total=True
#       )
#   )

data = pypistats.overall("generiter", start_date="2021-10-31", end_date="2022-01-22", total=True, format = "pandas")

data = data.groupby("category").get_group("without_mirrors").sort_values("date")

print("")

print(data)

print("")

Total = 3645 + data['downloads'].sum()

print("Total Estimate Non-Mirror Downloads: ", Total)

print("")

print("Stats For Generiter Module")

print("")

chart = data.plot(x="date", y="downloads", figsize=(10, 2))
chart.figure.show()
outfil = "Total_Downloads_" + str(tim) + ".png"

print("")

trig = input("Press any key to save and close chart: ")

print("")

chart.figure.savefig(outfil)  # alternatively

