import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("books.csv")

rating_count = df["Rating"].value_counts()

rating_count.plot(kind="bar")

plt.title("Book Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Books")

plt.savefig("rating_chart.png")
plt.show()