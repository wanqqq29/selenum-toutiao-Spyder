from selenium import webdriver
from lxml import etree
import time,requests
import test

def main(groupID):
    browser = webdriver.Chrome()
    browser.get("https://www.toutiao.com/c/user/token/"+groupID+"/?tab=article")
    time.sleep(5) ## 让页面加载完毕

    # title = browser.find_elements_by_xpath("//*[@id='root']/div/div[3]/div[1]/div/div[2]/div/div/div/div/div/div/a").text  用.text取值
    # href = browser.find_elements_by_xpath("//*[@id='root']/div/div[3]/div[1]/div/div[2]/div/div/div/div/div/div/a").get_attribute('href') 用.get_attribute()获取属性值

    title=[]
    href=[]
    List = browser.find_elements_by_xpath("//*[@id='root']/div/div[3]/div[1]/div/div[2]/div/div/div/div/div/div/a")

    for i in List:
        if len(i.text) !=0:
            title.append(i.text)
        else:
            title.append('')
        if len(i.get_attribute('href')) !=0:
            href.append(i.get_attribute('href'))
        else:
            href.append('')

    browser.close()

def req():
    burp0_url = "https://www.toutiao.com:443/a7011662797025051143/"
    burp0_cookies = {"__ac_signature": "_02B4Z6wo00f01TOeTywAAIDBMTmmhhl7U5Uzv0uAAC2t00",
                     "ttcid": "d7c088480cf949589056833420cf5be018",
                     "ttwid": "1%7CiHZsupiFeH47_vudwvPkDWnDq992klqk-xLqRqcwiqI%7C1632542463%7Cdb147b5e871a40dad24164318a16ba3c4bdf92a61f75001cd1d1772908f73418",
                     "MONITOR_WEB_ID": "dfacb733-6c31-4df4-afad-639a2d1c45a1", "tt_webid": "7011472487590888968",
                     "csrftoken": "e6b1fb5483a3d385193acf74908e8ed7",
                     "MONITOR_DEVICE_ID": "6c049f13-4a39-4dd3-a98e-f309c6c5da7c", "tt_webid": "7011472487590888968",
                     "s_v_web_id": "verify_ktz9mplp_Dw6iaiXH_HVSJ_4h2I_BMg7_rNpdntHt6Kh0",
                     "tt_scid": "YzIwI-CZ7B.FRkkqfSvnX8r91CAr2Gm4G3wZcWAiOjWTX6wA1INd.q5pLvEfyHH534d3"}
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0",
                     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                     "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                     "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1",
                     "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none",
                     "Sec-Fetch-User": "?1", "Pragma": "no-cache", "Cache-Control": "no-cache"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies).text
    er = etree.HTML(r)
    content = er.xpath("//*[@id='root']/div[2]/div[2]/div[1]/article/p/text()")
    Scont = ''
    for i in content:
        Scont += i
    print(Scont)

if __name__ == '__main__':
    #main("MS4wLjABAAAAZAVb3waD4Jb5JusEp_7vBnIHMZiHk_k4WtK8IifvnmM")
    req()
