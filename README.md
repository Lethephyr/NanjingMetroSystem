# 地铁售票模拟系统

XXXXXXXX XXX
2023/9/8

## 一、设计要求
### 1.1 功能描述

用于模仿地铁售票的自动售票，完成地铁售票的核心控制功能。

### 1.2 功能要求及验收要点

- [ ] 地铁售票机有两个进币孔，可以输入硬币和纸币，售货机有两个进币孔，一个是输入硬币，一个是输入纸币，硬币的识别范围是1 元的硬币，纸币的识别范围是5 元，10 元，20元。乘客可以连续多次投入钱币。
- [ ] 以南京市轨道交通1/2/3/4号线为基准进行设计考虑。站点数较多，需自行编码。
- [ ] 系统可以通过按键设定当前站点为4条线路中任意一站。
- [ ] 乘客买票时可以有两种选择，第一种，乘客已经知道所需费用，直接选择票价，如2元、3元或4元或更多。第二种，不知道票价，选择出站口，系统以目的地与当前站的站数来进行计算价格，计算方式参考南京市轨道交通计价标准。请注意，由于换乘站的存在导致两地之间有可能有多种价格的，以最低价格为准。
- [ ] 得到票价单价后，选择所需购买的票数，然后进行投币，投入的钱币达到所需金额时，售票机自动出票，并一次性找出余额，本次交易结束，等待下一次的交易。在投币期间，乘客可以按取消键取消本次操作，钱币自动一次性退出。


## 2. 项目特色

### 2.1 
## 3. 项目结构

1. 票价查询脚本[metro.py](metro.py)，报头信息请自行抓包填写，使用方法如下：

   ```shell
   python metro.py > result.txt
   ```
2. 

## 4. 项目运行


## 5. 项目功能




## 6. 项目成员


