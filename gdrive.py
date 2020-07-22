import gdown
import time

url ='https://drive.google.com/uc?id=1ENUnOgRwcPoigIS8bwZsWt9Y4zH4MZmH'
output='VGG16_ImageNet.pt'
time.sleep(100)
gdown.download(url, output, quiet=False)
