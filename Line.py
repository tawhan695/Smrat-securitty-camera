import requests

def senLineNotify():
   
       LINE_ACCESS_TOKEN="C9lv6JMLqaMDG56IB42WGecJsv7lA8sAexiPPbsV5jf"
       url = "https://notify-api.line.me/api/notify"
       data = ({'message':"มีคนมาหาที่หน้าบ้าน !!"})
       file = {'imageFile':open('save/User.jpg','rb')}           
       LINE_HEADERS = {"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
       session = requests.Session()
       r=session.post(url, headers=LINE_HEADERS, files =file ,data=data)
       print(r.text)
