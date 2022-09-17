from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
URL = "https://selfreport.shu.edu.cn/ReportHistory.aspx"
### Edge浏览器 ###
d = webdriver.Edge("msedgedriver.exe")
d.get(URL)
d.find_element(By.ID, "username").send_keys(
    " " +  # 用户名
    Keys.TAB +
    " ")  # 密码
d.find_element(By.ID, "submit-button").click()

while True:
    time.sleep(1)
    days = d.find_elements(By.TAG_NAME, "li")
    for i in days[::-1]:
        if "未填报，请点击此处补报" in i.text:
            i.click()
            break
    time.sleep(0.5)
    d.find_element(By.ID, "p1_ChengNuo-inputEl-icon").click()  # 勾选承诺
    time.sleep(0.5)
    # 近7日是否曾赴外省市，是0否1 
    d.find_element(By.ID, "fineui_1-inputEl-icon").click()  # 否
    time.sleep(0.5)
    #当天是否在上海：在上海（进学校）9；在上海（不进学校）10；不在上海11
    d.find_element(By.ID, "fineui_10-inputEl-icon").click()  # 不进学校
    time.sleep(0.5)
    #是否家庭地址，是26否27
    d.find_element(By.ID, "fineui_26-inputEl-icon").click()  # 是
    time.sleep(0.5)
    # 近7日是否有高中低风险地区旅居史，无 高 中 低 依次为 28 29 30 31
    d.find_element(By.ID, "fineui_28-inputEl-icon").click()  # 无
    time.sleep(0.5)
    # 是否被认定为密接：是 32，否33
    d.find_element(By.ID, "fineui_33-inputEl-icon").click()  # 否
    time.sleep(0.5)
    d.find_element(By.ID, "p1_ctl01_btnSubmit").click() # 提交
    time.sleep(0.5)
    d.find_element(By.ID, "fineui_41").click()  # 确定
    time.sleep(0.5)
    # 返回列表页
    d.get(URL)
