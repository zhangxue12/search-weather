
#查询天气
import requests

def input_judge(find):
	flag = 0
	while True:
		url = "http://wthrcdn.etouch.cn/weather_mini?city=%s"%find
		req = requests.get(url)
		judge = re.search(r"[A-z]+|[0-9]+",find)
		if judge == None and req.status_code == 200 and len(find)>1:
			break
		else:
			print("无法查询该城市的天气！")
			c_city = input("请重新输入你要查询的天气的城市：")
			find = c_city
	return req.text

while True:
	
	find = input("请输入你要查询的天气的城市：")
	
	data = input_judge(find)
	data1 = json.loads(data)
	content =data1["data"]
	print("你查询的是%s的天气！"%content["city"])
	content = content["forecast"]
	#print(content)
	for one in content:
		for k,v in one.items():
			print(k,v)
		print("=============")
	print("\n*********************\n")
	c = input("按任意键继续，\n退出请输入 2 \n")
	if c == "2":
		exit(0)
	else:
		continue
