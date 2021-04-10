from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
import math
import time
import matplotlib.animation as anim
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

blobs = []

class blob():
	def __init__(self,x,y,offset,vel = 3,amp = 0.5):
		self.x = x -3
		self.y = y - 3
		self.z = 0
		self.vel = vel
		self.offset = offset
		self.amp = amp

		blobs.append(self)

	def __str__(self):
		return f'({self.x} , {self.y} , {self.z})'

	def plot_update(self, dt):
		self.z = self.amp * math.cos(self.vel*dt + self.offset)
# Blob ( x ,y , vel, off)

blob15 = blob(1,5,0)	
blob24 = blob(2,4,0)
blob33 = blob(3,3,0)
blob42 = blob(4,2,0)	
blob51 = blob(5,1,0)

blob14 = blob(1,4,1)
blob23 = blob(2,3,1)
blob32 = blob(3,2,1)
blob41 = blob(4,1,1)
blob25 = blob(5,2,-1)
blob34 = blob(3,4,-1)
blob43 = blob(4,3,-1)
blob52 = blob(5,2,-1)

blob13 = blob(1,3,2)
blob22 = blob(2,2,2)
blob31 = blob(3,1,2)
blob35 = blob(3,5,-2)
blob44 = blob(4,4,-2)
blob53 = blob(5,3,-2)

blob12 = blob(1,2,3)
blob21 = blob(2,1,3)
blob45 = blob(4,5,-3)
blob54 = blob(5,4,-3)

blob11 = blob(1,1,4)
blob55 = blob(5,5,-4)


k = 3.5
def update(i):
	ax1.clear()
	ax1.scatter(k,k,k)
	ax1.scatter(-k,-k,-k)

	for b in blobs:
		b.plot_update(time.time())
		ax1.scatter(b.x, b.y, b.z)



a = anim.FuncAnimation(fig, update, frames=500, repeat=False)
plt.show()
	