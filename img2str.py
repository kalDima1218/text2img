from PIL import Image

def main(img_name):
	image = Image.open(img_name)
	width, height = image.size
	pix = image.load()
	message = ""
	for x in range(width):
		for y in range(height):
			for i in range(3):
				message+=chr(int(pix[x, y][i]))
	message.replace("\x00", "")

	print(message)

if __name__ == "__main__":
	image = 'token.png'
	main(image)