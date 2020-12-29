import requests, base64, json
from PIL import Image

class CardRecognition():
    def get_info(self, img_path, lang='auto', color='color'):
        if img_path is None:
            print("No image input")

        key = '5bb7d36c-a70b-4689-93fd-e6fa9bd87c08'
        url = 'http://api.hanvon.com/rt/ws/v1/ocr/bcard/recg?key=%s&code=91f6a58d-e418-4e58-8ec2-61b583c55ba2' % key
        base64img = ""
        img = Image.open(img_path)
        img = img.convert('L')
        img.save(img_path)
        # base64img需要是utf-8格式的字符串
        base64img = base64.b64encode(open(img_path, 'rb').read())

        data = {"uid": '', "lang": 'auto', "gray": 'color', "image": base64img.decode()}

        headers = {"Content-Type": "application/octet-stream"}
        resp = requests.post(url, data=json.dumps(data), headers=headers)
        print(resp.text)
        return json.loads(resp.text)