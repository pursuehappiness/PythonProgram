from PIL import Image,ImageFilter

def testImage():

	im = Image.open('test.jpg')

	w,h = im.size

	print('Original size is %sx%s',(w,h))

	im.thumbnail((w/2,h/2))
	im.save('thumbnail.jpg','jpeg')

	imf = Image.open('test.jpg')

	im2 = imf.filter(ImageFilter.BLUR)
	im2.save('blur.jpg','jpeg')


if __name__ == '__main__':
	testImage()