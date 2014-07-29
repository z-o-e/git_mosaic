from PIL import Image

class mosaic:
	# @param targetImg, an image file
	# @param tileSize, a tuple
	def __init__(self, targetImg, imgSize, tileSize):
		self.im = Image.open(tagetImg)
		self.canvas = Image.new("RGB", self.im.size, "white")
		self.tileSize = tileSize
		x, y = math.ceil(1.0*self.im.size[0]/tileSize[0]), math.ceil(1.0*self.im.size[1]/tileSize[1])
		self.tiles = np.zeros((x,y))

		for i in range(x):
			for j in range(y):
				window = self.im.crop(i*tileSize[0], j*tileSize[1], (i+1)*tileSize[0], (j+1)*tileSize[1])
				self.tile[i][j] = self.calRGB(window)
	 
	# @param im, an image
	# @return [r,g,b], an numpy array
	def calRGB(self, img):
		arr = np.array(img.getdata())
		return arr.mean(axis=0)
		
	# @param imgA and imgB, numpy arrays [r,g,b]
	# @return diff, an integer
	def imgDiff(self,imgA, imgB):
		s = (imgA - imgB)**2
		return math.sqrt(s.sum)
		
	# @param origImg, an image
	# @param position, a 4-tuple
	def pasteThumbnail(self, origImg, position):
		imgSmall = origImg.thumbnail(self.tileSize)
		self.canvas.paste(imgSmall, position)

	
		
		
