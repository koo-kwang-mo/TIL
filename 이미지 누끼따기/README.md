# jpg or png 파이썬 코드를 통해 누끼 따기
pip install rembg
pip install -U Pillow

###
from rembg import remove
from PIL import Image

input = Image.open('testImg.jpg') # load image
output = remove(input) # remove background
output.save('rembg.PNG') # save image
###

TBB 에러가 발생할 경우
혹시나 하단의 TBB 에러가 발생할 수 있는데요.

CE_VERSION = 9107. The TBB threading layer is disabled.

아래와 같은 명령어로 tbb를 업그레이드해주면 해결됩니다.

pip install --upgrade tbb