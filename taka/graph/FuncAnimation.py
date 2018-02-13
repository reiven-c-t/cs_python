import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

def plot(data):
    plt.cla()
    # 現在描画されているグラフの消去
    rand = np.random.randn(100)
    im = plt.plot(rand)

ani = animation.FuncAnimation(fig, plot, interval=100)
plt.show()