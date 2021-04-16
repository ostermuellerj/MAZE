import cv2
import numpy as np

#img=cv2.imread("maze.png")

numPics=1

for i in range(numPics):
	print("%.3d.png" % i)
	# img=cv2.imread("input/%.3d.png" % i)
	img=cv2.imread("output/generated/maze_800_800.png")
	# "output/generated/maze_%s_%s.png"
	
	
	def solve(h,w):
		x0=0
		y0=0

		current=[y0,x0]
		stack=[]
		direction="east"

		#trailColor=(1,0,254)
		#exploredColor=(100,100,253)

		trailColor=(254, 200, 0) #orange
		exploredColor=(150, 240, 254) #blue

		img[current[1]*2+1,current[0]*2+1]=trailColor

		def turn(d):
			cardinals=["east","south","west","north"]
			direction=cardinals[(cardinals.index(d)+1)%len(cardinals)]
			return direction

		def move(y,x,d):
			
			if d == "east":
				current[0]=x+1
				current[1]=y
				setColor(y*2+1,x*2+2,y*2+1,x*2+1)
			if d == "south":	
				current[0]=x
				current[1]=y+1
				setColor(y*2+2,x*2+1,y*2+1,x*2+1)
			if d == "west": 
				current[0]=x-1
				current[1]=y
				setColor(y*2+1,x*2,y*2+1,x*2+1)
			if d == "north": 
				current[0]=x
				current[1]=y-1
				setColor(y*2,x*2+1,y*2+1,x*2+1)
			#setColor(y*2+1,x*2+1)
			
		def setColor(Y,X,y1,x1):
			if img[Y,X,2]==0: #if it's trailcolor
				img[Y,X]=exploredColor
				img[y1,x1]=exploredColor
			if img[Y,X,2]==255: #if it's white
				img[Y,X]=trailColor
				img[y1,x1]=trailColor		

		def checkDir(y,x,d):
			if d == "east" and x<w-1 and img[y*2+1,x*2+2,0]>0: 
				return True
			elif d == "south" and y<h-1 and img[y*2+2,x*2+1,0]>0: 
				return True
			elif d == "west" and img[y*2+1,x*2,0]>0: 
				return True
			elif d == "north" and img[y*2,x*2+1,0]>0: 
				return True
			else:
				return False
				
		while current!=[w-1,h-1]:
			if checkDir(current[1],current[0],turn(direction)):
				move(current[1],current[0],turn(direction))
				direction=turn(direction)
				#print("right")
			elif checkDir(current[1],current[0],direction):
				move(current[1],current[0],direction)	
				#print("fwd")
			elif checkDir(current[1],current[0],turn(turn(turn(direction)))):
				move(current[1],current[0],turn(turn(turn(direction))))
				direction=turn(turn(turn(direction)))
				#print("left")
			else:
				img[current[1]*2+1,current[0]*2+1]=exploredColor
				move(current[1],current[0],turn(turn(direction)))
				direction=turn(turn(direction))
				#print("back")

		img[(h-1)*2+1,(w-1)*2+1]=trailColor
				
#		cv2.imshow("grid", img)
#		cv2.waitKey(0)
		
		cv2.imwrite("output/solved/solved_%.3d.png" % i,img)
#		cv2.imwrite("mazeSolved.png",img)
#		cv2.destroyAllWindows()

		""" 
		while not at end
			try turn left
			try forward
			try turn right
			try back
		"""
	
	#print(int((img.shape[0]-1)/2))
	#print(int((img.shape[1]-1)/2))
	#h,w
	#solve(40,30)
	solve((img.shape[0]-1)//2,(img.shape[1]-1)//2)

