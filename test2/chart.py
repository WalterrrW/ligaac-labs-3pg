import matplotlib.pyplot as plt
import random

# Data to plot
labels = 'Anger', 'Contempt', 'Disgust', 'Fear', 'Happiness', 'Neutral', "Sadnes", "Surprise"
sizes = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9),
         random.randint(0, 9), random.randint(0, 9), random.randint(0, 9),
         random.randint(0, 9), random.randint(0, 9)]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0.2, 0, 0.1, 0.2, 0.1, 0, 0.2)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()