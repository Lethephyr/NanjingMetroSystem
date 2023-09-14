import time
import requests
import urllib
from urllib import parse
# 定义请求头
headers = {
    'Host': 'www.njmetro.com.cn',
    'Cookie': 'JSESSIONID=51B99C05A9D6930A9B72C1A32D4E5F95; JSESSIONID=F66A86F9D6458074976E1021716CF43D; Hm_lvt_8d42de8d1552f264e412bb016d24eb5b=1694169379; Hm_lpvt_8d42de8d1552f264e412bb016d24eb5b=1694169416',
    'Content-Length': '103',
    'Sec-Ch-Ua': '"(Not(A:Brand";v="8", "Chromium";v="100"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'Sec-Ch-Ua-Platform': '"macOS"',
    'Origin': 'https://www.njmetro.com.cn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.njmetro.com.cn/njdtweb/portal/get-lineList.do?parentId=root&tag=0jl',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'close'
}

# 定义请求数据
data = 'starts=%25E5%2590%2589%25E7%25A5%25A5%25E5%25BA%25B5&ends=%25E4%25B8%25AD%25E5%258D%258E%25E9%2597%25A8'

# 发送POST请求
url = 'https://www.njmetro.com.cn/njdtweb/mobileTicketAction/getPrice.do'
response = requests.post(url, headers=headers, data=data)

stations = {
        1: "八卦洲大桥南",2: "笆斗山",3: "燕子矶",4: "吉祥庵",5: "晓庄",6: "迈皋桥",7: "红山动物园",8: "南京站",9: "新模范马路",10: "玄武门",11: "鼓楼",12: "珠江路",13: "新街口",14: "张府园",15: "三山街",16: "中华门",17: "安德门",18: "天隆寺",19: "软件大道",20: "花神庙",21: "南京南站",22: "双龙大道",23: "河定桥",24: "胜太路",25: "百家湖",26: "小龙湾",27: "竹山路",28: "天印大道",29: "龙眠大道",30: "南医大江苏经贸学院",31: "南京交院",32: "中国药科大学",33: "鱼嘴",34: "天保街",35: "青莲街",36: "螺塘路",37: "油坊桥",38: "雨润大街",39: "元通",40: "奥体东站",41: "兴隆大街",42: "集庆门大街",43: "云锦路",44: "莫愁湖",45: "汉中门",46: "上海路",47: "新街口",48: "大行宫",49: "西安门",50: "明故宫",51: "苜蓿园",52: "下马坊",53: "孝陵卫",54: "钟灵街",55: "马群",56: "金马路",57: "仙鹤门",58: "学则路",59: "仙林中心",60: "羊山公园",61: "南大仙林校区",62: "经天路",63: "林场",64: "星火路",65: "东大成贤学院站",66: "泰冯路",67: "天润城",68: "柳洲东路",69: "上元门",70: "五塘广场",71: "小市",72: "南京站",73: "南京林业大学新庄",74: "鸡鸣寺",75: "浮桥",76: "大行宫",77: "常府街",78: "夫子庙",79: "武定门",80: "雨花门",81: "卡子门",82: "大明路",83: "明发广场",84: "南京南站",85: "宏运大道",86: "胜太西路",87: "天元西路",88: "九龙湖",89: "诚信大道",90: "东大九龙湖校区",91: "秣周东路",92: "仙林湖",93: "西岗桦墅",94: "孟北",95: "东流",96: "灵山",97: "汇通路",98: "金马路",99: "徐庄",100: "聚宝山",101: "王家湾",102: "蒋王庙",103: "岗子村",104: "九华山",105: "鸡鸣寺",106: "鼓楼",107: "云南路",108: "草场门",109: "龙江",110: "仙新路",111: "尧化门",112: "尧化新村",113: "丁家庄南",114: "丁家庄",115: "万寿",116: "晓庄",117: "幕府山",118: "五塘广场",119: "幕府西路",120: "雨山路",121: "文德路",122: "龙华路",123: "南京工业大学",124: "浦口万汇城",125: "临江",126: "江心洲",127: "绿博园",128: "梦都大街",129: "奥体中心",130: "元通",131: "中胜",132: "小行",133: "安德门",134: "空港新城江宁",135: "禄口机场",136: "翔宇路南",137: "翔宇路北",138: "正方中路",139: "吉印大道",140: "河海大学佛城西路",141: "翠屏山",142: "南京南站",143: "南京南站",144: "景明佳园",145: "铁心桥",146: "春江路",147: "贾西",148: "油坊桥",149: "永初路",150: "平良大街",151: "吴侯街",152: "高庙路",153: "天保",154: "刘村",155: "马骡圩",156: "兰花塘",157: "双垅",158: "石碛河",159: "桥林新城",160: "林山",161: "高家冲",162: "马群",163: "百水桥站",164: "麒麟门站",165: "东郊小镇站",166: "古泉站",167: "南京猿人洞站",168: "汤山站",169: "泉都大街站",170: "黄梅站",171: "童世界站",172: "华阳站",173: "崇明站",174: "句容站",175: "空港新城江宁",176: "柘塘",177: "空港新城溧水",178: "群力",179: "卧龙湖",180: "溧水",181: "中山湖",182: "幸庄",183: "无想山",184: "长江大桥北",185: "毛纺厂路",186: "泰山新村",187: "泰冯路",188: "高新开发区",189: "信息工程大学",190: "卸甲甸",191: "大厂",192: "葛塘",193: "长芦",194: "化工园",195: "六合开发区",196: "龙池",197: "雄州",198: "凤凰山公园",199: "方州广场",200: "沈桥",201: "八百桥",202: "金牛湖",203: "翔宇路南",204: "铜山",205: "石湫",206: "明觉",207: "团结圩",208: "高淳",
        }

prices = [[0 for i in range(209)] for j in range(209)]

errers = []

# 以C语言格式输出prices数组

f = open("prices.txt", "w")

f.write("u8 prices[209][209] = {\n")
for i in range(0, 209):
    f.write("{")
    if i == 0:
        for j in range(0, 209):
            f.write(f"{prices[i][j]}, ")
    else:
        for j in range(209):
            f.flush()
            if j == 0:
                f.write(f"{prices[i][j]}, ")
            elif j == 208:
                try:
                    data = 'starts=' + parse.quote(parse.quote(stations[i])) + '&ends=' + parse.quote(parse.quote(stations[j]))
                    response = requests.post(url, headers=headers, data=data, timeout=0.1)
                    if response.status_code == 200:
                        prices[i][j] = response.json()['price']
                        f.write(f"{prices[i][j]}")
                    else:
                        # f.write("error in", i, stations[i], j, stations[j], data)
                        f.write(f"233")
                        # 添加到错误列表
                        errers.append([i, j, stations[i], stations[j]])
                except requests.exceptions.Timeout:
                    f.write(f"233")
                    # 添加到错误列表
                    errers.append([i, j, stations[i], stations[j]])
                except requests.exceptions.RequestException as e:
                    f.write(f"233")
                    # 添加到错误列表
                    errers.append([i, j, stations[i], stations[j], e])
            else:
                try:
                    data = 'starts=' + parse.quote(parse.quote(stations[i])) + '&ends=' + parse.quote(parse.quote(stations[j]))
                    response = requests.post(url, headers=headers, data=data, timeout=0.1)
                    if response.status_code == 200:
                        prices[i][j] = response.json()['price']
                        f.write(f"{prices[i][j]}, ")
                    else:
                        # f.write("error in", i, stations[i], j, stations[j], data)
                        f.write(f"233, ")
                        # 添加到错误列表
                        errers.append([i, j, stations[i], stations[j]])
                except requests.exceptions.Timeout:
                    f.write(f"233, ")
                    # 添加到错误列表
                    errers.append([i, j, stations[i], stations[j]])
                except requests.exceptions.RequestException as e:
                    f.write(f"233, ")
                    # 添加到错误列表
                    errers.append([i, j, stations[i], stations[j], e])
    f.write("},\n")
f.write("};\n")

f.write("errors:\n")
for i in errers:
    f.write(i+"\n")