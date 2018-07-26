from PIL import Image
import math

path_to_image = "imgs_camera_180/"
img_name = "bus2.jpg"
inputImg = Image.open(path_to_image+img_name)
nX, nY = inputImg.size

print("Input size: ", nX, nY)

n = min(nX, nY)

# tranform input image to square
if(nX != nY):
	if(nX > nY):
		left = int(math.ceil((max(nX, nY)-n)/2))
		top = 0
	elif(nY > nX):
		top = int(math.ceil((max(nX, nY)-n)/2))
		left = 0
	right = left+n
	bottom = top+n
	inputImg = inputImg.crop((left, top, right, bottom))

print("Input new size: ", inputImg.size)
#inputImg.show()

outNX = 5000

outNY = 1000

outputImg = Image.new('RGB', (outNX, outNY), color = 'black')

print("Output size: ", outputImg.size)

for i in range(n):
	for j in range(n):
		outX = int(round((math.atan2(i-(n/2),j-(n/2))*180/math.pi + 180)*(outNX-1)/360))
		outY = int(round(math.sqrt(math.pow(i-(n/2),2)+math.pow(j-(n/2),2))*math.sqrt(2)*(outNY-1)/n))
		#print("Indice: ",outX, outY)
		outputImg.putpixel((outX, outY), inputImg.getpixel((j, i)))

outputImg.show()
outputImg.save(path_to_image+'out'+img_name)


#Image.putpixel(xy, value)