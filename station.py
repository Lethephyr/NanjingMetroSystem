import math
cnt = 0
def add_station(station_name):
    global cnt
    cnt = cnt + 1
    print(f"{cnt}: \"{station_name}\",", end="")
# 1
add_station("八卦洲大桥南")
add_station("笆斗山")
add_station("燕子矶")
add_station("吉祥庵")
add_station("晓庄")
add_station("迈皋桥")
add_station("红山动物园")
add_station("南京站")
add_station("新模范马路")
add_station("玄武门")
add_station("鼓楼")
add_station("珠江路")
add_station("新街口")
add_station("张府园")
add_station("三山街")
add_station("中华门")
add_station("安德门")
add_station("天隆寺")
add_station("软件大道")
add_station("花神庙")
add_station("南京南站")
add_station("双龙大道")
add_station("河定桥")
add_station("胜太路")
add_station("百家湖")
add_station("小龙湾")
add_station("竹山路")
add_station("天印大道")
add_station("龙眠大道")
add_station("南医大·江苏经贸学院")
add_station("南京交院")
add_station("中国药科大学")

# 2
add_station("鱼嘴")
add_station("天保街")
add_station("青莲街")
add_station("螺塘路")
add_station("油坊桥")
add_station("雨润大街")
add_station("元通")
add_station("奥体东")
add_station("兴隆大街")
add_station("集庆门大街")
add_station("云锦路")
add_station("莫愁湖")
add_station("汉中门")
add_station("上海路")
add_station("新街口")
add_station("大行宫")
add_station("西安门")
add_station("明故宫")
add_station("苜蓿园")
add_station("下马坊")
add_station("孝陵卫")
add_station("钟灵街")
add_station("马群")
add_station("金马路")
add_station("仙鹤门")
add_station("学则路")
add_station("仙林中心")
add_station("羊山公园")
add_station("南大仙林校区")
add_station("经天路")

# 3 
add_station("林场")
add_station("星火路")
add_station("东大成贤学院")
add_station("泰冯路")
add_station("天润城")
add_station("柳洲东路")
add_station("上元门")
add_station("五塘广场")
add_station("小市")
add_station("南京站")
add_station("南京林业大学·新庄")
add_station("鸡鸣寺")
add_station("浮桥")
add_station("大行宫")
add_station("常府街")
add_station("夫子庙")
add_station("武定门")
add_station("雨花门")
add_station("卡子门")
add_station("大明路")
add_station("明发广场")
add_station("南京南站")
add_station("宏运大道")
add_station("胜太西路")
add_station("天元西路")
add_station("九龙湖")
add_station("诚信大道")
add_station("东大九龙湖校区")
add_station("秣周东路")

# 4
add_station("仙林湖")
add_station("西岗桦墅")
add_station("孟北")
add_station("东流")
add_station("灵山")
add_station("汇通路")
add_station("金马路")
add_station("苏宁总部·徐庄")
add_station("聚宝山")
add_station("王家湾")
add_station("蒋王庙")
add_station("岗子村")
add_station("九华山")
add_station("鸡鸣寺")
add_station("鼓楼")
add_station("云南路")
add_station("草场门·南艺·二师")
add_station("龙江")

# 7
add_station("仙新路")
add_station("尧化门")
add_station("尧化新村")
add_station("丁家庄南")
add_station("丁家庄")
add_station("万寿")
add_station("晓庄")
add_station("幕府山")
add_station("五塘广场")
add_station("幕府西路")

# 10
add_station("雨山路")
add_station("文德路")
add_station("龙华路")
add_station("南京工业大学")
add_station("浦口万汇城")
add_station("临江·青奥体育公园")
add_station("江心洲")
add_station("绿博园")
add_station("梦都大街")
add_station("奥体中心")
add_station("元通")
add_station("中胜")
add_station("小行")
add_station("安德门")

# s1
add_station("空港新城江宁")
add_station("禄口机场")
add_station("翔宇路南")
add_station("翔宇路北")
add_station("正方中路")
add_station("吉印大道")
add_station("河海大学·佛城西路")
add_station("翠屏山")
add_station("南京南站")

# s3
add_station("南京南站")
add_station("景明佳园")
add_station("铁心桥")
add_station("春江路")
add_station("贾西")
add_station("油坊桥")
add_station("永初路")
add_station("平良大街")
add_station("吴侯街")
add_station("高庙路")
add_station("天保")
add_station("刘村")
add_station("马骡圩")
add_station("兰花塘")
add_station("双垅")
add_station("石碛河")
add_station("桥林新城")
add_station("林山")
add_station("高家冲")

# s6
add_station("马群")
add_station("白水桥")
add_station("麒麟门")
add_station("东郊小镇")
add_station("古泉")
add_station("南京猿人洞")
add_station("汤山")
add_station("泉都大街")
add_station("黄梅")
add_station("童世界")
add_station("华阳")
add_station("崇明")
add_station("句容")

# s7
add_station("空港新城江宁")
add_station("柘塘")
add_station("空港新城溧水")
add_station("群力")
add_station("卧龙湖")
add_station("溧水")
add_station("中山湖")
add_station("幸庄")
add_station("无想山")

#s8
add_station("长江大桥北")
add_station("毛纺厂路")
add_station("泰山新村")
add_station("泰冯路")
add_station("高新开发区")
add_station("信息工程大学")
add_station("卸甲甸")
add_station("大厂")
add_station("葛塘")
add_station("长芦")
add_station("化工园")
add_station("六和开发区")
add_station("龙池")
add_station("雄州")
add_station("凤凰山公园")
add_station("方州广场")
add_station("沈桥")
add_station("八百桥")
add_station("金牛湖")

# s9
add_station("翔宇路南")
add_station("铜山")
add_station("石湫")
add_station("明觉")
add_station("团结圩")
add_station("高淳")
