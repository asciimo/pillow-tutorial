from PIL import Image

def main():
    im = Image.open("src/badge.png")
    im.save("dist/badge_out.png")

if __name__ == "__main__":
    main()
