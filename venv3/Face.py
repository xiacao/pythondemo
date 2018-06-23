import requests

from json import JSONDecoder

http_url ="https://api-cn.faceplusplus.com/facepp/v3/compare"

key ="Z5Dl_lp1Vgq4O9G7yc8hY3JVQTiyOiBO"

secret ="4VvslYJaKDnqP_XJQ_RMFE9FzQsoC0rj"

filepath1 ="D:\python\myspoils\\baifendemo\\2.jpg"

filepath2 ="D:\python\myspoils\\baifendemo\\3.jpg"
data = {"api_key":
 key, "api_secret": secret, "return_landmark": "0"}

files = {"image_file1":
 open(filepath1, "rb"),"image_file2": open(filepath2, "rb")}

response = requests.post(http_url,
 data=data, files=files)


req_con = response.content.decode('utf-8')

req_dict = JSONDecoder().decode(req_con)

print(req_dict)