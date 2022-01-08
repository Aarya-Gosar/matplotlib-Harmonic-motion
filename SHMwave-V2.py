from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
import math
import time
import matplotlib.animation as anim

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')


Amp = 0.5
Freq = 3

def update_z(dt):
	for t , z in enumerate(zs):
		zs[t] = Amp * math.cos(Freq*dt + off[t])
	return zs

k = 3.5
def update(i):
	ax1.clear()
	ax1.scatter(k,k,k,s = 0.0001)
	ax1.scatter(-k,-k,-k , s = 0.0001)

	update_z(time.time())
	ax1.scatter(xs,ys,zs , c = off)

def get_arrs_of_n(n):
	if n % 2 == 0:
		print("n must be odd!!!")
		return

	base_arr_x = []
	base_arr_y = []
	base_arr_z = []

	offsets = []

	n_2 = (n-1)/2
	d = math.tau/(n-1)

	for i in range(n):
		for j in range(n):
			base_arr_x.append(i-n_2)
			base_arr_y.append(j-n_2)
			base_arr_z.append(0)
			offsets.append(round((i + j) * d , 3))

	return base_arr_x, base_arr_y , base_arr_z,  offsets 


n = int(input("Enter an ODD number: "))

try:
	xs , ys ,zs, off = get_arrs_of_n(n)

except:
	print("I Said ODD!!!")
	print("will take n as 9 by default")
	n = 9
	xs , ys ,zs, off = get_arrs_of_n(n)

a = anim.FuncAnimation(fig, update, frames=500, repeat=False)
plt.show()


