import requests
from io import BytesIO
from PIL import Image
import hashlib

sess = requests.session()
c = 2000


for i in range(c):
    cap = sess.get("http://cas.swust.edu.cn/authserver/captcha")
    imgBuf = BytesIO(cap.content)
    with Image.open(imgBuf) as im:
        _id = hashlib.md5(cap.content).hexdigest()
        name = f"temp/{_id}.jpg"
        print(name)
        im.save(name)
