import requests, time

gonghao = ""
shoujihao = ""
nianling = ""

if(gonghao == "" or shoujihao == ""):
    gonghao = input("-")
    shoujihao = input("-")
    nianling = input("-")

def main():
    url="http://xg.sqxy.edu.cn/xgh5/openData"
    r = requests.Session()
    riqi=time.strftime('%Y-%m-%d',time.localtime(time.time())) #年-月-日   格式的当天日期
    #riqi="2020-01-06"的形式
    params="command=XGXT&param=%7B%22cmd%22%3A%22yqsbFormSave%22%2C%22xh%22%3A%22"+gonghao+"%22%2C%22sbsj%22%3A%22"+riqi+"%22%2C%22nl%22%3A%22"+nianling+"%22%2C%22lxfs%22%3A%22"+shoujihao+"%22%2C%22jzdq%22%3A%22411402%22%2C%22jzdq_xxdz%22%3A%22%E5%95%86%E4%B8%98%E5%AD%A6%E9%99%A2%22%2C%22tw%22%3A%2236.5%22%2C%22sflx%22%3A%220%22%2C%22jcbr%22%3A%220%22%2C%22zyzz%22%3A%221%2C%22%2C%22fbrq%22%3A%22%22%2C%22zyzzms%22%3A%22%22%2C%22bz%22%3A%22%22%2C%22bz1%22%3A%22%22%2C%22wcjtgj%22%3A%22%22%2C%22wcjtgjxq%22%3A%22%22%2C%22wcdq%22%3A%22%22%2C%22wcdqxxdz%22%3A%22%22%2C%22lkdate%22%3A%22%22%2C%22fhdate%22%3A%22%22%2C%22zszt%22%3A%22%22%7D"
    xiangying=r.post(url, params = params)
    jieguo=xiangying.text #dict形式，但是是str格式
    jieguo=eval(jieguo) #字符串转字典类型，就可以使用dict方法操作
    print(riqi)
    print(jieguo["message"])
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    return 1
    

if __name__ == "__main__":
    main()
