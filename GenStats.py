# Show overall downloads over time, excluding mirrors
import pypistats
import datetime

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

data = pypistats.overall("generiter", total=True, format="pandas")
data = data.groupby("category").get_group("without_mirrors").sort_values("date")

print("")

print(pypistats.overall("generiter"))

print("")

chart = data.plot(x="date", y="downloads", figsize=(10, 2))
chart.figure.show()
outfil = "Total_Downloads_" + str(tim) + ".png"

print("")

trig = input("Press any key to save and close chart: ")

print("")

chart.figure.savefig(outfil)  # alternatively

