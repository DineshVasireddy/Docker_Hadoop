import matplotlib.pyplot as plt

dates = []
requests = []
with open("mapreduce_output.txt", "r") as file:
    for line in file:
        date, count = line.strip().split("\t")
        dates.append(date)
        requests.append(int(count))

plt.figure(figsize=(10, 6))
plt.bar(dates, requests)
plt.title("API Requests over Dates")
plt.xlabel("Date")
plt.ylabel("Number of API Requests")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.show()