#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2018/09/05
# 淘宝秒杀脚本，扫码登录版
import os
from selenium import webdriver
import datetime
import time
from os import path
from selenium.webdriver.common.action_chains import ActionChains

d = path.dirname(__file__)
abspath = path.abspath(d)

driver = webdriver.Firefox()
driver.maximize_window()


def login():
    # 打开淘宝登录页，并进行扫码登录
    driver.get("https://www.taobao.com")
    time.sleep(3)
    if driver.find_element_by_link_text("亲，请登录"):
        driver.find_element_by_link_text("亲，请登录").click()

    print("请在30秒内完成扫码")
    time.sleep(30)

    driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(3)
    # 点击购物车里全选按钮
    # if driver.find_element_by_id("J_CheckBox_939775250537"):
    # driver.find_element_by_id("J_CheckBox_939775250537").click()
    # if driver.find_element_by_id("J_CheckBox_939558169627"):
    # driver.find_element_by_id("J_CheckBox_939558169627").click()
    if driver.find_element_by_id("J_SelectAll1"):
        driver.find_element_by_id("J_SelectAll1").click()
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


def buy(buytime):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # 对比时间，时间到的话就点击结算
        if now > buytime:
            try:
                # 点击结算按钮
                if driver.find_element_by_id("J_Go"):
                    driver.find_element_by_id("J_Go").click()
                driver.find_element_by_link_text('提交订单').click()
            except:
                time.sleep(0.1)
                print(now)
                time.sleep(0.1)


if __name__ == "__main__":
    # times = input("请输入抢购时间：")
    # 时间格式："2018-09-06 11:20:00.000000"
    login()
    buy("2018-10-22 18:55:00.000000")


#京东抢手机脚本
from splinter.browser import Browser
import time

#登录页
def login(b):  #登录京东
    b.click_link_by_text("你好，请登录")
    time.sleep(3)
    b.fill("loginname","account*****")  #填写账户密码
    b.fill("nloginpwd","passport*****")
    b.find_by_id("loginsubmit").click()
    time.sleep(3)
    return b

#订单页
def loop(b):  #循环点击
    try:
        if b.title=="订单结算页 -京东商城":
            b.find_by_text("保存收货人信息").click()
            b.find_by_text("保存支付及配送方式").click()
            b.find_by_id("order-submit").click()
            return b
        else:  #多次抢购操作后，有可能会被转到京东首页，所以要再打开手机主页
            b.visit("http://item.jd.com/2707976.html")
            b.find_by_id("choose-btn-qiang").click()
            time.sleep(10)
            loop(b)  #递归操作
    except Exception as e: #异常情况处理，以免中断程序
        b.reload()  #重新刷新当前页面，此页面为订单提交页
        time.sleep(2)
        loop(b)  #重新调用自己


b=Browser(driver_name="chrome") #打开浏览器
b.visit("http://item.jd.com/2707976.html")
login(b)
b.find_by_id("choose-btn-qiang").click() #找到抢购按钮，点击
time.sleep(10)  #等待10sec
while True:
    loop(b)
    if b.is_element_present_by_id("tryBtn"): #订单提交后显示“再次抢购”的话
        b.find_by_id("tryBtn").click()  #点击再次抢购，进入读秒5，跳转订单页
        time.sleep(6.5)
    elif b.title=="订单结算页 -京东商城": #如果还在订单结算页
        b.find_by_id("order-submit").click()
    else:
        print('恭喜你，抢购成功')
        break