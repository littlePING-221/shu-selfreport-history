from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
URL = "https://selfreport.shu.edu.cn/ReportHistory.aspx"
d = webdriver.Chrome("chromedriver.exe")
d.get(URL)
d.find_element(By.ID, "username").send_keys(
    "********" +  # 用户名
    Keys.TAB +
    "********")  # 密码
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
    # 当天是否在上海： 在上海（不进学校）8; 不在上海 9
    d.find_element(By.ID, "fineui_8-inputEl-icon").click()  # 在上海（不进学校）
    time.sleep(0.5)
    d.find_element(By.ID, "fineui_24-inputEl-icon").click()  # 是否家庭地址
    time.sleep(0.5)
    d.find_element(By.ID, "p1_ctl01_btnSubmit").click()  # 提交
    time.sleep(0.5)
    d.find_element(By.ID, "fineui_33").click()  # 确定
    time.sleep(0.5)
    # 返回列表页
    d.get(URL)
