# name: File path of the pgm image file
# Output is a 2D list of integers
from math import sqrt
def readpgm(name):
	image = []
	with open(name) as f:
		lines = list(f.readlines())
		if len(lines) < 3:
			print("Wrong Image Format\n")
			exit(0)

		count = 0
		width = 0
		height = 0
		for line in lines:
			if line[0] == '#':
				continue

			if count == 0:
				if line.strip() != 'P2':
					print("Wrong Image Type\n")
					exit(0)
				count += 1
				continue

			if count == 1:
				dimensions = line.strip().split(' ')
				print(dimensions)
				width = dimensions[0]
				height = dimensions[1]
				count += 1
				continue

			if count == 2:	
				allowable_max = int(line.strip())
				if allowable_max != 255:
					print("Wrong max allowable value in the image\n")
					exit(0)
				count += 1
				continue

			data = line.strip().split()
			data = [int(d) for d in data]
			image.append(data)
	return image	

# img is the 2D list of integers
# file is the output file path
def writepgm(img, file):
	with open(file, 'w') as fout:
		if len(img) == 0:
			pgmHeader = 'p2\n0 0\n255\n'
		else:
			pgmHeader = 'P2\n' + str(len(img[0])) + ' ' + str(len(img)) + '\n255\n'
			fout.write(pgmHeader)
			line = ''
			for i in img:
				for j in i:
					line += str(j) + ' '
			line += '\n'
			fout.write(line)

def Averaging_filter(image):
	h=len(image)
	w=len(image[0])
	new_image=[[0 for i in range(w)] for j in range(h)]
	for i in range(h):
		for j in range(w):
			if i==0 or i==h-1:
				new_image[i][j]=image[i][j]
			elif j==0 or j==w-1:
				new_image[i][j]=image[i][j]
			else:
				new_image[i][j]=(image[i-1][j-1]+image[i-1][j]+image[i-1][j+1]+image[i][j-1]+image[i][j]+image[i][j+1]+image[i+1][j-1]+ image[i+1][j]+image[i+1][j+1])/9
	return new_image

def Edge_detection(image):
	h=len(image)
	w=len(image[0])
	gradient=[[0 for i in range(w)] for j in range(h)]
	edgy=[['k' for i in range(w)] for j in range(h)]
	for i in range(h):		
		for j in range(w):
			if i==0 and j!=0 and j!=w-1 and i!=h-1:
				hdif = 2*(image[i][j-1]-image[i][j+1]) + (image[i+1][j-1]-image[i+1][j+1])
				vdif = 0
				grad = sqrt(hdif*hdif + vdif*vdif)
				gradient[i][j]=grad						
			elif j==0 and i!=0 and i!=h-1 and j!=w-1:

				hdif = 0
				vdif = 2*(image[i-1][j]-image[i+1][j]) + (image[i-1][j+1]-image[i+1][j+1])
				grad = sqrt(hdif*hdif + vdif*vdif)
				gradient[i][j]=grad
								
			elif i==h-1 and j!=0 and j!=w-1 and i!=0:
				hdif = (image[i-1][j-1]-image[i-1][j+1]) + 2*(image[i][j-1]-image[i][j+1]) 
				vdif = 0
				grad = sqrt(hdif*hdif + vdif*vdif)
				gradient[i][j]=grad				
			elif j==w-1 and i!=0 and i!=h-1 and j!=0:
				hdif = 0
				vdif = (image[i-1][j-1]-image[i+1][j-1]) + 2*(image[i-1][j]-image[i+1][j])
				grad = sqrt(hdif*hdif + vdif*vdif)				
				gradient[i][j]=grad				
			elif j!=w-1 and i!=0 and i!=h-1 and j!=0:
				hdif = (image[i-1][j-1]-image[i-1][j+1]) + 2*(image[i][j-1]-image[i][j+1]) + (image[i+1][j-1]-image[i+1][j+1])
				vdif = (image[i-1][j-1]-image[i+1][j-1]) + 2*(image[i-1][j]-image[i+1][j]) + (image[i-1][j+1]-image[i+1][j+1])
				grad = sqrt(hdif*hdif + vdif*vdif)
				gradient[i][j]=grad
	return gradient

def least_Enery_Path(image):
	edge=Edge_detection(image)
	h=len(edge)
	w=len(edge[0])
	def MinEnergy(i,j):
		if j==w-1 and i!=0:
			return edge[i][j] + min(MinEnergy(i-1,j-1), MinEnergy(i-1,j))
		elif j==0 and i!=0:				
			return edge[i][j] + min(MinEnergy(i-1,j), MinEnergy(i-1,j+1))
		elif i==0:		
			return edge[0][j]
		else:			
			return edge[i][j] + min(MinEnergy(i-1,j-1), MinEnergy(i-1,j), MinEnergy(i-1,j+1))
	Min_energy_matrix=[[0 for i in range(w)] for i in range(h)]
	for i in range(h):
		for j in range(w):
			Min_energy_matrix[i][j]=MinEnergy(i,j)
	a1=min(Min_energy_matrix[h-1])
	a1_index=0
	for i in range(w):
		if Min_energy_matrix[h-1][i]==a1:
			a1_index+=i
	l=[]
	p=a1
	i=h-1
	while i>=0:
		for k in range(w):
			if Min_energy_matrix[i][k]==p:
				l.append(k)
				if j==w-1 and i!=0:
					p = min(Min_energy_matrix[i-1][j-1], Min_energy_matrix[i-1][j])
				elif j==0 and i!=0:				
					p = min(Min_energy_matrix[i-1][j], Min_energy_matrix[i-1][j+1])
				elif i==0:		
					p = Min_energy_matrix[0][j]
				else:			
					p = min(Min_energy_matrix[i-1][j-1], Min_energy_matrix[i-1][j], Min_energy_matrix[i-1][j+1])
				i=i-1
	for i in range(len(l)):
		for k in range(h):
			Min_energy_matrix[h-1-k][l[i]]=225
	return Min_energy_matrix

########## Function Calls ##########
x = readpgm('flower_gray.pgm')			# test.pgm is the image present in the same working directory
writepgm(x, 'test_o.pgm')
writepgm(Averaging_filter(x), 'average.pgm')
writepgm(Edge_detection(x), 'edge.pgm')
writepgm(least_Enery_Path(x), 'Least_enery_path.pgm')
		# x is the image to output and test_o.pgm is the image output in the same working directory
###################################