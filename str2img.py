from PIL import Image, ImageDraw

def main(message, img_name):
	for i in range(len(message) % 3): message+="\x00"
	for i in range(int((len(message)//3) ** 0.5), 0, -1):
		if len(message)//3 % i == 0: h, w = [i, (len(message)//3)//i]
	img = Image.new("RGB", (w, h))
	draw = ImageDraw.Draw(img)
	for i in range(w): 
		for j in range(h):
			draw.point((i, j), (ord(message[i*h*3 + j*3 + 0]), ord(message[i*h*3 + j*3 + 1]), ord(message[i*h*3 + j*3 + 2])))

	img.save(img_name)

if __name__ == "__main__":
	message = """Hello World!"""
	image = "token.png"
	main(message, image)