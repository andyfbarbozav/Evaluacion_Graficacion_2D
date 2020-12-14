import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

figure, axes = plt.subplots()
draw_circle = plt.Circle((0.5, 0.5), 0.1,fill=False)

#rectangulo y circulo
axes.set_aspect(1)
axes.add_artist(draw_circle)
plt.title('Circle')

someX, someY = 0.3, 0.5
currentAxis = plt.gca()
currentAxis.add_patch(Rectangle((someX - .2, someY - .2), 0.8, 0.4, fill=None, alpha=1))

#rectangulo secundario
someX, someY = 1.1, 0.5
currentAxis = plt.gca()

currentAxis.add_patch(Rectangle((someX - .6, someY - .4), 0.8, 0.4, fill=None, alpha=1))
