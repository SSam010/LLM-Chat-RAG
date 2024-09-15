import asyncio
import matplotlib.pyplot as plt
from db_alchemy.first_db.models import User

data = list(asyncio.run(User.get_str_count_abs()))

plt.hist(
    data,
    bins=15,
    edgecolor="k",
    color='skyblue',
    alpha=0.7
)

plt.title("Histogram of Data Distribution")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()
