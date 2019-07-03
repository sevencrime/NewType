#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-14 21:30:24
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from Commons import *
import os
import sys
import time
import random
import glob
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))


class ApplyPage(BasePage.BasePage):
    # log = Logging.Logs()
    # mob = glob.glob(os.path.abspath(os.path.dirname(os.getcwd()))+r'\image\*')
    mob = glob.glob(os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd())))+r'\image\*')

    def get_input(self, text, parent=False):
        if not parent:
            input_loc = (
                By.XPATH, "//div[contains(text(), '%s')]/following-sibling::span//input" % text)
        else:
            input_loc = (
                By.XPATH, "//div[contains(text(), '%s')]/parent::div/following-sibling::*//input" % text)

        return input_loc

    def get_checkbox(self, text):
        checkbox_loc = (
            By.XPATH, "//span[contains(text(), '%s')]/preceding-sibling::span" % text)
        return checkbox_loc

    def get_select(self, text=False, randox=None):
        if not text:
            select_loc = (
                By.XPATH, "//div[contains(@style,'position: absolute;')]//li")

            selectlist = self.find_elements(*select_loc)
            if randox == None:
                randox = random.randint(0, len(selectlist)-1)

            for i in range(len(selectlist)):
                if i == randox:
                    while selectlist[i].is_displayed():
                        self.scrollinto(selectlist[i])
                        # self.script("arguments[0].click();", selectlist[i])

                        try:
                            tag_text = selectlist[i].get_attribute(
                                "textContent")
                            # print(tag_text)
                        except AttributeError:
                            continue

                    return selectlist[i].get_attribute("textContent")

        else:
            select_loc = (By.XPATH, "//span[contains(text(), '%s')]" % text)
            select_value = self.find_element(*select_loc)
            self.scrollinto(select_value)
            return select_value.get_attribute("textContent")

    def modify_displys(self, display=None):
        js = 'var file = document.querySelectorAll(".el-upload__input"); \
            for(var i=0;i<file.length;i++){file[i].style.display="%s";}' % display
        self.script(js)

    def get_radio(self, text):
        radio_loc = (
            By.XPATH, "//div[contains(text(), '%s')]/following-sibling::span//label[1]" % text)
        return radio_loc

    # def get_action(self, text):
    #     print("action")
    #     parents_loc = (By.XPATH, "//div[contains(text(), '%s')]" %text)
    #     # time.sleep(5)
    #     ActionChains(self.driver).click(self.find_element(*parents_loc)).perform()

    # def scrollinto(self, loc):
    #     self.script("arguments[0].scrollIntoView();", loc)
    #     self.script("arguments[0].click();", loc)

    def send_applicationFor(self, text):
        # 账户类型
        applicationFor = self.find_element(*self.get_input('账户类型'))
        self.scrollinto(applicationFor)
        tag_text = self.get_select(text=text)

        assert applicationFor.get_attribute("value") != ''
        return applicationFor.get_attribute("value")

    def send_accountOpeningWay(self, text=False):
        # 开户方法
        accountOpeningWay = self.find_element(*self.get_input('开户方法'))
        self.scrollinto(accountOpeningWay)
        tag_text = self.get_select(text=text)

        assert accountOpeningWay.get_attribute("value") != ''

        if text == False and (accountOpeningWay.get_attribute("value") == '手机应用程式身份验证' or accountOpeningWay.get_attribute("value") == '电子签名认证'):
            # bankname = self.find_element(
            #     *self.get_input("银行名称")).send_keys("中国农业银行")
            # bankAccountNumber = self.find_element(
            #     *self.get_input("银行账户号码")).send_keys("6228481412637493782")
            # certificateNb = self.find_element(
            #     *self.get_input("电子签名证书号码")).send_keys("certificate Number")
            self.send_appBankName()
            self.send_appBankAccount()
            self.send_appcertificateNb()

        return accountOpeningWay.get_attribute("value")

    def send_appBankName(self):
        bankname = self.find_element(
            *self.get_input("银行名称")).send_keys("中国农业银行")  

    def send_appBankAccount(self):
        bankAccountNumber = self.find_element(
            *self.get_input("银行账户号码")).send_keys("6228481412637493782")

    def send_appcertificateNb(self):
        certificateNb = self.find_element(
            *self.get_input("电子签名证书号码")).send_keys("certificate Number")


    def send_parentId(self):
        # 负责人
        parentId = self.find_element(*self.get_input('负责人'))
        self.scrollinto(parentId)
        tag_text = self.get_select(text='sales_t1')

        assert parentId.get_attribute("value") != ''
        return parentId.get_attribute("value")

    def send_mailLanguage(self, text=False):
        # 邮件语言
        mailLanguage = self.find_element(*self.get_input('邮件语言'))
        self.scrollinto(mailLanguage)
        tag_text = self.get_select(text=text)

        assert mailLanguage.get_attribute("value") != ''
        return mailLanguage.get_attribute("value")

    def send_accountType(self, text):
        # 账户类别
        self.find_element(*self.get_checkbox(text)).click()

    def send_title(self, text=False):
        # 称谓
        title = self.find_element(*self.get_input('称谓'))
        self.scrollinto(title)
        tag_text = self.get_select()
        assert title.get_attribute("value") != ''
        return title.get_attribute("value")

    def send_firstName(self):
        # 名字
        firstName = self.find_element(*self.get_input('名字'))
        firstName.send_keys("%sfirstname%s" %
                            (random.randint(0, 100), random.randint(0, 1030)))

        assert firstName.get_attribute("value") != ''
        return firstName.get_attribute("value")

    def send_lastName(self):
        # 姓氏
        lastName = self.find_element(*self.get_input('姓氏'))
        lastName.send_keys("%slastname%s" %
                           (random.randint(0, 100), random.randint(0, 1030)))
        lastName.send_keys(Keys.ENTER)

        assert lastName.get_attribute("value") != ''
        return lastName.get_attribute("value")

    def send_chineseName(self):
        # 中文姓名
        chineseName = self.find_element(*self.get_input('中文姓名'))
        chineseName.send_keys("郑某人")
        assert chineseName.get_attribute("value") != ''
        return chineseName.get_attribute("value")

    def send_emali(self):
        # 电邮
        email = self.find_element(*self.get_input('电邮'))
        email.send_keys("%sonedi2s%s@qq.com" %
                        (random.randint(0, 1000), random.randint(0, 10300)))
        assert email.get_attribute("value") != ''
        return email.get_attribute("value")

    def send_phoneAreaCode(self):
        # 电话号码区号
        phoneAreaCode = self.find_element(*self.get_input('电话号码区号'))
        self.scrollinto(phoneAreaCode)
        tag_text = self.get_select()
        assert phoneAreaCode.get_attribute("value") != ''
        return phoneAreaCode.get_attribute("value")

    def send_phone(self):
        # 电话号码
        phone = self.find_element(*self.get_input("电话号码(用于通讯)"))
        phone.send_keys("%s6253%s" %
                        (random.randint(0, 100002), random.randint(0, 10502)))
        assert phone.get_attribute("value") != ''
        return phone.get_attribute("value")

    def send_address(self):
        # 住宅地址
        address = self.find_element(*self.get_input("住宅地址(不接受邮政信箱)"))
        address.send_keys("桑达科技大厦802")
        assert address.get_attribute("value") != ''
        return address.get_attribute("value")

    def send_addressMail(self):
        # 邮寄地址
        addressMail = self.find_element(*self.get_input("邮寄地址(如与住宅地址不同)"))
        addressMail.send_keys("桑达科技大厦802")

        assert addressMail.get_attribute("value") != ''
        return addressMail.get_attribute("value")

    def send_nationality(self):
        # 国籍
        nationality = self.find_element(*self.get_input("国籍"))
        self.scrollinto(nationality)
        tag_text = self.get_select()
        assert nationality.get_attribute("value") != ''
        return nationality.get_attribute("value")

    def send_idType(self, num=None):
        # 身份证件类型
        idType = self.find_element(*self.get_input("身份证件类型"))
        self.scrollinto(idType)
        tag_text = self.get_select(randox=num)
        if tag_text == "其他":
            other_type = self.find_element(*self.get_input("其他证件类型"))
            other_type.send_keys("idType")
            idNumber = self.find_element(*self.get_input("其他证件号码"))
            idNumber.send_keys("%s423523%s" % (
                random.randint(0, 1001), random.randint(0, 10600)))
            assert idType.get_attribute("value") != ''
            assert other_type.get_attribute("value") != ''
            assert idNumber.get_attribute("value") != ''
            return idType.get_attribute("value"), other_type.get_attribute("value"), idNumber.get_attribute("value")
        else:
            idNumber = self.find_element(*self.get_input("身份证或护照号码"))
            idNumber.send_keys("%s423523%s" % (
                random.randint(0, 1001), random.randint(0, 10600)))
            assert idType.get_attribute("value") != ''
            assert idNumber.get_attribute("value") != ''
            return idType.get_attribute("value"), idNumber.get_attribute("value")

    def send_countryIssue(self):
        # 签发国籍
        countryIssue = self.find_element(*self.get_input("签发国家"))
        self.scrollinto(countryIssue)
        tag_text = self.get_select()
        assert countryIssue.get_attribute("value") != ''
        return countryIssue.get_attribute("value")

    def send_birthday(self):
        # 出生日期
        birthday = self.find_element(*self.get_input("出生日期(日/月/年)"))
        birthday.send_keys("21/01/2000")
        birthday.send_keys(Keys.ENTER)
        assert birthday.get_attribute("value") != ''
        return birthday.get_attribute("value")

    def send_birthPlace(self):
        # 出生地点
        birthPlace = self.find_element(*self.get_input('出生地点'))
        self.scrollinto(birthPlace)
        tag_text = self.get_select()
        assert birthPlace.get_attribute("value") != ''
        return birthPlace.get_attribute("value")

    def employment(self, num=None):
        # 就业情况
        employment = self.find_element(*self.get_input("就业情况"))
        self.scrollinto(employment)
        tag_text = self.get_select(randox=num)

        if tag_text == "就业" or tag_text == "自雇":
            occupation = self.find_element(*self.get_input("职位"))
            occupation.send_keys("销售")
            employedPeriod = self.find_element(*self.get_input("受雇年期"))
            employedPeriod.send_keys("十年以上")
            employer = self.find_element(*self.get_input("目前雇主名称"))
            employer.send_keys("newtype")
            businessType = self.find_element(*self.get_input("业务性质"))
            businessType.send_keys("互联网")
            businessAddress = self.find_element(*self.get_input("办公室地址"))
            businessAddress.send_keys("广东省深圳市南山区桑达科技大厦802")
            businessPhone = self.find_element(*self.get_input("办公室电话"))
            businessPhone.send_keys("15089500015")

            assert employment.get_attribute("value") != ''
            assert occupation.get_attribute("value") != ''
            assert employedPeriod.get_attribute("value") != ''
            assert employer.get_attribute("value") != ''
            assert businessType.get_attribute("value") != ''
            assert businessAddress.get_attribute("value") != ''
            assert businessPhone.get_attribute("value") != ''
            return employment, occupation, employedPeriod, employer, businessType, businessAddress, businessPhone

        elif tag_text == "其他":
            Hidden_loc = (
                By.XPATH, "//div[contains(text(), '就业情况')]/parent::div/parent::span/following-sibling::span//input")
            Hidden = self.find_element(*Hidden_loc)
            Hidden.send_keys("Hidden")
            assert employment.get_attribute("value") != ''
            assert Hidden.get_attribute("value") != ''
            return employment, Hidden

        elif tag_text == "退休" or tag_text == "无业":
            assert employment.get_attribute("value") != ''
            return employment

    def uploadImage(self):
        # 上传图片
        # self.modify_displys(display='block')
        pass

    def totalAnnualCustomerRevenueHK(self):
        # 客户全年总收入为(港元)
        self.find_element(*self.get_radio("客户全年总收入为(港元)")).click()
        totalAnnual = self.find_element(
            *self.get_input("请注明资金来源", parent=True))
        totalAnnual.send_keys("资金来源")
        assert totalAnnual.get_attribute("value") != ''
        return totalAnnual

    def customerNetAssetValueHK(self):
        # 客户资产净值(港元)
        self.find_element(*self.get_radio("客户资产净值(港元)")).click()
        netEstate = self.find_element(*self.get_input("请注明资产净值", parent=True))
        netEstate.send_keys("请注明资产净值")
        assert netEstate.get_attribute("value") != ''
        return netEstate

    def sourceOfWealth(self, text=False):
        # 客户交易的资金/财富来源（选择所有适用）
        if not text:
            self.find_element(*self.get_checkbox("就业薪金")).click()
        else:
            self.find_element(*self.get_checkbox(text)).click()
            if text == "其他":
                otherOfWealth_loc = (
                    By.XPATH, "//span[contains(text(), '就业薪金')]/ancestor::span[@class='checkbox']/following-sibling::span//input")
                therOfWealth = self.find_element(*otherOfWealth_loc)
                therOfWealth.send_keys("Other of Wealth")
                assert therOfWealth.get_attribute("value") != ''
                # return therOfWealth

    def securities(self):
        # 客户投资经验及曾买卖产品>证券
        securities = self.find_element(*self.get_input("证券"))
        self.scrollinto(securities)
        tag_text = self.get_select()
        assert securities.get_attribute("value") != ''
        return securities.get_attribute("value")

    def CBBC(self):
        # 客户投资经验及曾买卖产品>牛熊证
        CBBCcertificate = self.find_element(*self.get_input("牛熊证"))
        self.scrollinto(CBBCcertificate)
        tag_text = self.get_select()
        assert CBBCcertificate.get_attribute("value") != ''
        return CBBCcertificate.get_attribute("value")

    def warrants(self):
        # 客户投资经验及曾买卖产品>衍生权证
        derivativewarrant = self.find_element(*self.get_input("衍生权证(窝轮)"))
        self.scrollinto(derivativewarrant)
        tag_text = self.get_select()
        assert derivativewarrant.get_attribute("value") != ''
        return derivativewarrant.get_attribute("value")

    def futures(self):
        # 客户投资经验及曾买卖产品>期货
        futures = self.find_element(*self.get_input("期货"))
        self.scrollinto(futures)
        tag_text = self.get_select()
        assert futures.get_attribute("value") != ''
        return futures.get_attribute("value")

    def Option(self):
        # 客户投资经验及曾买卖产品>期权
        Option = self.find_element(*self.get_input("期权"))
        self.scrollinto(Option)
        tag_text = self.get_select()
        assert Option.get_attribute("value") != ''
        return Option.get_attribute("value")

    def foreignExchange(self):
        # 客户投资经验及曾买卖产品>外汇
        foreignexchange = self.find_element(*self.get_input("外汇"))
        self.scrollinto(foreignexchange)
        tag_text = self.get_select()
        assert foreignexchange.get_attribute("value") != ''
        return foreignexchange.get_attribute("value")

    def bullion(self):
        # 贵金属
        if self.driver.page_source.find("贵金属") != -1:
            bullion = self.find_element(*self.get_input("贵金属"))
            self.scrollinto(bullion)
            tag_text = self.get_select()
            assert bullion.get_attribute("value") != ''
            return bullion.get_attribute("value")

    def automatic(self):
        # 自动程式交易
        if self.driver.page_source.find("自动程式交易") != -1:
            automatic = self.find_element(*self.get_input("自动程式交易"))
            self.scrollinto(automatic)
            tag_text = self.get_select()
            assert automatic.get_attribute("value") != ''
            return automatic.get_attribute("value")

    def otherInvestmentText(self):
        # 客户投资经验及曾买卖产品>其他投资
        self.find_element(*self.get_input("其他投资")).send_keys("otherInvest")
        # self.get_action("其他投资")
        # time.sleep(5)
        # parent_loc = (By.XPATH, "//div[contains(text(), '其他投资')]/parent::*/parent::span/following-sibling::*//input")
        # self.find_element(parent_loc).click()
        # self.find_element(*self.get_select()).click()

    def derivativeCourse(self, num=None):
        # 客户是否曾接受有关衍生产品性质和风险的一般知识培训或修读相关课程
        derivativeCourse = self.find_element(
            *self.get_input("相关课程", parent=True))
        self.scrollinto(derivativeCourse)
        tag_text = self.get_select(randox=num)
        assert derivativeCourse.get_attribute("value") != ''
        return derivativeCourse.get_attribute("value")

    def derivativeJobs(self, num=None):
        # 客户是否从现时或过去拥有与衍生产品有关的工作经验?
        derivativeJobs = self.find_element(
            *self.get_input("工作经验", parent=True))
        self.scrollinto(derivativeJobs)
        tag_text = self.get_select(randox=num)
        assert derivativeJobs.get_attribute("value") != ''
        return derivativeJobs.get_attribute("value")

    def tradingFund(self, num=None):
        # 客户是否于过去3年曾执行 5次或以上有关衍生产品的交易
        tradingFund = self.find_element(*self.get_input("买卖基金", parent=True))
        self.scrollinto(tradingFund)
        tag_text = self.get_select(randox=num)
        assert tradingFund.get_attribute("value") != ''
        return tradingFund.get_attribute("value")

    def buyProduct(self, num=None, linkTag=True, linknum=None):
        # 客户是否申请开通买卖衍生权证、牛熊证及结构性等产品
        if self.driver.page_source.find("买卖衍生") != -1:
            buyProduct = self.find_element(*self.get_input("买卖衍生", parent=True))
            self.scrollinto(buyProduct)
            tag_text = self.get_select(randox=num)
            if tag_text == "是" and linkTag == True:
                self.riskStatement(linknum)

            assert buyProduct.get_attribute("value") != ''
            return buyProduct.get_attribute("value")

    def riskStatement(self, num=None):
        # 客户是否已明白买卖衍生权证，牛熊证及结构性产品的风险。并已详细阅读「结构性产品相关风险声明披露」
        riskStatement = self.find_element(*self.get_input("结构性产品相关风险声明披露", parent=True))
        self.scrollinto(riskStatement)
        tag_text = self.get_select(num)
        if tag_text == "否":
            messagebox = (
                By.XPATH, "//div[@aria-label='提示']//div[@class='el-message-box__btns']/button")
            self.find_element(*messagebox).click()


    def bankrupt(self, num=None):
        # 客户是否曾经宣告破产或被申请破产
        bankrupt = self.find_element(*self.get_input("申请破产"))
        self.scrollinto(bankrupt)
        tag_text = self.get_select(randox=num)
        if tag_text == "有":
            # 破产日期
            self.find_element(*self.get_input("破产日期")).send_keys("02/04/2019")
            self.find_element(*self.get_input("破产日期")).send_keys(Keys.ENTER)

            # 破产证明书
            imgli_loc = (
                By.XPATH, "//div[contains(text(), '破产解除证明书')]/following-sibling::span//li")

            self.modify_displys(display='block')
            # import pdb; pdb.set_trace()
            self.find_element(*self.get_input("破产解除证明书")).send_keys(random.sample(self.mob, 1))
            self.modify_displys()

            loading_loc = (
                By.XPATH, "//div[contains(text(), '请提供破产解除证明书')]/following-sibling::span//i[@class='el-icon-loading']")
            WebDriverWait(self.driver, 20).until_not(
                EC.presence_of_element_located(loading_loc))

        assert bankrupt.get_attribute("value") != ''
        return bankrupt.get_attribute("value")

    def customerRelatives(self, num=None):
        # 客户是否艾德证券及/或艾德金业的雇员或任何其客户的亲属?
        if self.driver.page_source.find("艾德证券及/或艾德金业的雇员") != -1:
            customerRelatives = self.find_element(
                *self.get_input("艾德证券及/或艾德金业的雇员", parent=True))
            self.scrollinto(customerRelatives)
            tag_text = self.get_select(randox=num)
            if tag_text == "是":
                self.find_element(
                    *self.get_input("艾德金业雇员名称及关系", parent=True)).send_keys("relationship")

        else:
            customerRelatives = self.find_element(
                *self.get_input("艾德证券的雇员", parent=True))
            self.scrollinto(customerRelatives)
            tag_text = self.get_select(randox=num)
            if tag_text == "是":
                self.find_element(
                    *self.get_input("艾德证券雇员名称及关系", parent=True)).send_keys("relationship")

        assert customerRelatives.get_attribute("value") != ''
        return customerRelatives.get_attribute("value")

    def associatedcustomer(self, num=None):
        # 3.客户是否与任何艾德证券及/或艾德金业客户有关连?
        if self.driver.page_source.find("艾德证券及/或艾德金业客户有关连") != -1:
            # print("不等于-1")
            associatedcustomer = self.find_element(
                *self.get_input("艾德金业客户有关连", parent=True))
            self.scrollinto(associatedcustomer)
            tag_text = self.get_select(randox=num)
            if tag_text == "是":
                self.find_element(*self.get_input("艾德金业客户名称",
                                                  parent=True)).send_keys("ClientName")

        else:
            # print("else else")
            associatedcustomer = self.find_element(
                *self.get_input("艾德证券客户有关连", parent=True))
            self.scrollinto(associatedcustomer)
            tag_text = self.get_select(randox=num)
            if tag_text == "是":
                self.find_element(*self.get_input("艾德证券客户名称",
                                                  parent=True)).send_keys("ClientName")

        assert associatedcustomer.get_attribute("value") != ''
        return associatedcustomer.get_attribute("value")

    def director(self, num=None):
        # 4.客户是否香港交易所之交易所参与者或证监会之持牌人或注册人之董事、雇员或认可人士?
        director = self.find_element(*self.get_input("认可人士?", parent=True))
        self.scrollinto(director)
        tag_text = self.get_select(randox=num)
        if tag_text == "是":
            self.find_element(*self.get_input("认可人士(请详述)",
                                              parent=True)).send_keys("HKEX")

            # 请提供雇主同意书
            imgli_loc = (
                By.XPATH, "//div[contains(text(), '请提供雇主同意书')]/parent::div/following-sibling::*//li")

            self.modify_displys(display='block')
            self.find_element(*self.get_input("请提供雇主同意书", parent=True)
                              ).send_keys(random.sample(self.mob, 1))
            self.modify_displys()

            loading_loc = (
                By.XPATH, "//div[contains(text(), '请提供雇主同意书')]/parent::div/following-sibling::div/span//i[@class='el-icon-loading']")
            WebDriverWait(self.driver, 20).until_not(
                EC.presence_of_element_located(loading_loc))

    def citizenOfUSA(self, num=None):
        # 5.客户是否拥有美国公民或美国合法永久居民身份?
        citizenOfUSA = self.find_element(*self.get_input("美国公民", parent=True))
        self.scrollinto(citizenOfUSA)
        tag_text = self.get_select(randox=num)
        if tag_text == "是":
            # 税务编号
            citizenOfUSA_Tax = (
                By.XPATH, "//div[contains(text(), '美国公民')]/parent::div/parent::div/parent::span/following-sibling::*//input")
            self.find_element(*citizenOfUSA_Tax).send_keys("citizenOfUSA_Tax")

        assert citizenOfUSA.get_attribute("value") != ''
        return citizenOfUSA.get_attribute("value")

    def americanResident(self, num=None):
        # 6.就税务而言，您是否美国居民?
        americanResident = self.find_element(
            *self.get_input("美国居民", parent=True))
        self.scrollinto(americanResident)
        tag_text = self.get_select(randox=num)
        if tag_text == "是":
            # 税务编号
            americanResident_Tax = (
                By.XPATH, "//div[contains(text(), '美国居民')]/parent::div/parent::div/parent::span/following-sibling::*//input")
            self.find_element(
                *americanResident_Tax).send_keys("americanResident_Tax")

        assert americanResident.get_attribute("value") != ''
        return americanResident.get_attribute("value")

    def PEP_People(self, num=None):
        # 7.客户是否香港法律定义下的“政治公众人物（PEP）”或与政治公众人物有密切联系？
        PEP_People = self.find_element(
            *self.get_input("政治公众人物（PEP）", parent=True))
        self.scrollinto(PEP_People)
        tag_text = self.get_select(randox=num)
        if tag_text == "是":
            self.find_element(*self.get_input("职位/政治公众人物名称",
                                              parent=True)).send_keys("Position/political")

        assert PEP_People.get_attribute("value") != ''
        return PEP_People.get_attribute("value")

    def investmentTarget(self, text=None):
        # 8.客户的投资目标是:
        # investmentTarget = self.find_element(*self.get_input("投资目标", parent=True))
        # self.scrollinto(investmentTarget)
        # tag_text = self.get_select()
        # assert investmentTarget.get_attribute("value") != ''
        # return investmentTarget.get_attribute("value")
        if text == None:
            self.find_element(*self.get_checkbox('对冲')).click()
        else:
            self.find_element(*self.get_checkbox(text)).click()


    def riskTolerance(self, num=None):
        # 9.客户的风险承受能力是:
        riskTolerance = self.find_element(*self.get_input("客户的风险承受能力是", parent=True))
        self.scrollinto(riskTolerance)
        tag_text = self.get_select(randox=num)
        if tag_text != "高":
            # import pdb; pdb.set_trace()
            # 弹出框:若阁下选择低或中风险，将不能买卖槓杆式外汇、黄金、结构性产品及衍生产品
            # 定位弹窗的确定按钮
            warnbox_loc = (By.XPATH, '//div[@class="el-message-box"]//button[span]')
            while True:
                # 利用死循环,保证弹框消失
                warnbox = self.find_element(*warnbox_loc)
                if warnbox == False:
                    # 校验风险填低或高时,不是否能填内容
                    assert riskTolerance.get_attribute("value") == ''
                    return True

                warnbox.click()


        return riskTolerance.get_attribute("value")

    def jointRiskTolerance(self):
        # 9.本人确认并同意主要账户持有人之风险承受能力选择:
        jointRiskTolerance = self.find_element(
            *self.get_input("本人确认并同意主要账户持有人之风险承受能力选择", parent=True))
        self.scrollinto(jointRiskTolerance)
        tag_text = self.get_select()
        assert jointRiskTolerance.get_attribute("value") != ''
        return jointRiskTolerance.get_attribute("value")

    def bankaccount(self, num=None):
        # 结算账户
        currency = self.find_element(*self.get_input("货币", parent=True))
        self.scrollinto(currency)
        tag_text = self.get_select(randox=num)
        if not tag_text == "不适用":
            bankAccount_loc = (
                By.XPATH, "//span[contains(text(), '删除')]/parent::*/parent::*/preceding-sibling::div//input")
            bankAccount = self.find_elements(*bankAccount_loc)
            for bankInput in bankAccount:
                bankInput.send_keys("bankAccount")

    def marginAccount(self, num=None):
        # 1.客户的配偶是否持有艾德证券任何相关的保证金账户?
        marginAccount = self.find_element(
            *self.get_input("客户的配偶", parent=True))
        self.scrollinto(marginAccount)
        tag_text = self.get_select(randox=num)
        if tag_text == "是":
            name_or_num = (
                By.XPATH, "//div[contains(text(), '客户的配偶')]/parent::div/parent::div/parent::span/following-sibling::span//input")
            el_inputs = self.find_elements(*name_or_num)
            for inputs in el_inputs:
                inputs.send_keys("name")

    def discretion(self, num=None):
        # 2.客户及/或其配偶是否单独或共同控制艾德证券之其他保证金账户35%或以上之表决权?
        discretion = self.find_element(
            *self.get_input("保证金账户35%或以上之表决权", parent=True))
        self.scrollinto(discretion)
        # discretion.click()
        tag_text = self.get_select(randox=num)
        if tag_text == "是":
            name_or_num = (
                By.XPATH, "//div[contains(text(), '保证金账户35%或以上之表决权')]/parent::div/parent::div/parent::span/following-sibling::span//input")
            el_inputs = self.find_elements(*name_or_num)
            for inputs in el_inputs:
                inputs.send_keys("name")

        assert discretion.get_attribute("value") != ''
        return discretion.get_attribute("value")

    def companyAccounts(self, num=None):
        # 客户是否有以客户的同一集团公司旗下之公司开立保证金账户？
        companyAccounts = self.find_element(
            *self.get_input("同一集团公司旗下", parent=True))
        self.scrollinto(companyAccounts)
        # companyAccounts.click()
        tag_text = self.get_select(randox=num)
        if tag_text == "是":
            name_or_num = (
                By.XPATH, "//div[contains(text(), '同一集团公司旗下')]/parent::div/parent::div/parent::span/following-sibling::span//input")
            el_inputs = self.find_elements(*name_or_num)
            for inputs in el_inputs:
                inputs.send_keys("name")

        assert companyAccounts.get_attribute("value") != ''
        return companyAccounts.get_attribute("value")

    def learnHow(self):
        # 介绍及推广>>1.您透过哪些渠道认识艾德证券及/或艾德金业?(选择所有适用)
        channel_loc = (
            By.XPATH, "//div[contains(text(), '您透过哪些渠道认识艾德证券')]/parent::div/following-sibling::div//label")
        channel = self.find_elements(*channel_loc)
        for i in range(len(channel)):
            if i != len(channel)-1:
                channel[i].click()

    def beneficial(self, num=None):
        # 身份声明>>1.客户是否账户的最终实益拥有人?
        beneficial = self.find_element(
            *self.get_input("是否账户的最终实益拥有人", parent=True))
        self.scrollinto(beneficial)
        tag_text = self.get_select(randox=num)
        if tag_text == "否":
            self.find_element(*self.get_input("最终实益拥有人名称为",
                                              parent=True)).send_keys("onedi")

        assert beneficial.get_attribute("value") != ''
        return beneficial.get_attribute("value")

    def Othed_People(self, num=None):
        # 身份声明>>2.客户是否最终负责下单的人?
        othedPeople = self.find_element(*self.get_input("负责下单", parent=True))
        self.scrollinto(othedPeople)
        tag_text = self.get_select(randox=num)
        if tag_text == "否":
            self.find_element(*self.get_input("最终负责下单人为",
                                              parent=True)).send_keys("onedi")
            # 必需提交交易授权书
            self.modify_displys(display='block')
            self.find_element(*self.get_input("必需提交交易授权书")
                              ).send_keys(random.sample(self.mob, 1))
            self.modify_displys()
            loading_loc = (
                By.XPATH, "//div[contains(text(), '必需提交交易授权书')]/following-sibling::span//i[@class='el-icon-loading']")
            WebDriverWait(self.driver, 20).until_not(
                EC.presence_of_element_located(loading_loc))

        assert othedPeople.get_attribute("value") != ''
        return othedPeople.get_attribute("value")

    def jurisdiction(self):
        # 居留司法管辖区及税务编号或具有等同功能的识辨编号>>请选择您就税务用途的居留司法管辖区(您可选多一项)

        self.find_element(*self.get_checkbox("香港身份证号码")).click()
        # self.find_element(*self.get_checkbox("请填写下表")).click()
        # self.find_element(*(By.XPATH, "//div[contains(text(), '居留司法局')]/following-sibling::div[@class='el-input")).send_keys("China")
        # self.find_element(*(By.XPATH, "//div[contains(text(), '识辨编号')]/following-sibling::div[@class='el-input")).send_keys("Tax number")

    def acceptStatement(self):
        # 本人声明>>本人接受上述声明
        acceptStatement = self.find_element(*self.get_input("本人接受上述声明"))
        self.scrollinto(acceptStatement)
        tag_text = self.get_select()
        assert acceptStatement.get_attribute("value") != ''
        return acceptStatement.get_attribute("value")

    def useStatement(self):
        # 个人资料之使用声明>>个人资料之使用声明
        useStatement = self.find_element(*self.get_input("个人资料之使用声明"))
        self.scrollinto(useStatement)
        tag_text = self.get_select()
        assert useStatement.get_attribute("value") != ''
        return useStatement.get_attribute("value")

    def click_sublimeApply(self, text):
        # 点击按钮
        sublimeApply_loc = (
            By.XPATH, '//div[contains(@class, "button-1")]/button[span[contains(text(), "{btntext}")]]'.format(btntext=text))
        # sublime = self.find_element(*sublime_loc).click()
        sublimeApply = self.find_element(*sublimeApply_loc)
        # self.scrollinto(sublimeApply)

        # 滑动操作. 在这里先用js滑动到控件位置,然后再点击控件
        # 直接使用self.scrollinto,会出现没有点击的错误
        self.script("arguments[0].scrollIntoView();", sublimeApply)
        sublimeApply.click()

    def primaryRelations(self, num=None):
        # 联名账户- 与主要账户持有人关系
        primaryRelations = self.find_element(*self.get_input("与主要账户持有人的关系"))
        self.scrollinto(primaryRelations)
        tag_text = self.get_select(randox=num)
        if tag_text == "直系亲属":
            self.find_element(*self.get_input("直系亲属，请注明")).send_keys("直系亲属")
        elif tag_text == "其他":
            self.find_element(*self.get_input("其他，请注明")).send_keys("其他亲属")
        else:
            pass

        assert primaryRelations.get_attribute("value") != ''
        return primaryRelations.get_attribute("value")

    # 已废弃, 老的ops审核输入编号(没有自动创建生成)
    def send_accountNumber(self, randox=None):
        # ops审核菜单
        self.find_element(*self.get_input("客户编号", parent=True)
                          ).send_keys(random.randint(0, 999999))

        if self.driver.page_source.find("证券账户号") != -1:
        # 存在证券账户号码
            self.find_element(*self.get_input("证券账户号", parent=True)).send_keys(random.randint(0, 9999999999))

        if self.driver.page_source.find("期货账户号") != -1:
            # 存在证券账户号码
            self.find_element(*self.get_input("期货账户号", parent=True)
                              ).send_keys(random.randint(0, 9999999999))

        if self.driver.page_source.find("外汇账户号(MT5)") != -1:
            # 存在证券账户号码
            self.find_element(*self.get_input("外汇账户号(MT5)", parent=True)
                              ).send_keys(random.randint(0, 9999999999))

        if self.driver.page_source.find("现货黄金账户号") != -1:
            # 存在证券账户号码
            self.find_element(*self.get_input("现货黄金账户号", parent=True)
                              ).send_keys(random.randint(0, 9999999999))

        promoCode_loc = (
            By.XPATH, '//span[contains(text(), " 优惠码 ")]/following-sibling::div//input')
        promoCode_select_loc = (
            By.XPATH, "//div[contains(@style,'position: fixed;')]//li[@class='el-select-dropdown__item']")
        promoCode = self.find_element(*promoCode_loc)
        promoCode.click()

        promoCodeValueList = self.find_elements(*promoCode_select_loc)
        if randox == None:
            randox = random.randint(0, len(promoCodeValueList)-1)

        for i in range(len(promoCodeValueList)):
            if i == randox:
                while promoCodeValueList[i].is_displayed():
                    self.scrollinto(promoCodeValueList[i])
                    # self.script("arguments[0].click();", promoCodeValueList[i])

                    try:
                        tag_text = promoCodeValueList[i].get_attribute(
                            "textContent")
                        # print(tag_text)
                    except AttributeError:
                        continue

                # return promoCodeValueList[i].get_attribute("textContent")

        sublime_popwindow_loc = (
            By.XPATH, "//span[text()='确定']//parent::button")
        self.find_element(*sublime_popwindow_loc).click()


    def rejectReason(self, btntext):
        reasontext = ["开户资料", "主要账户持有人资料", "主要账户持有人就业资料", "主要账户持有人证明资料",
                      "客戶财务资料", "客户投资经验及曾买卖产品", "客户对衍生产品的认识", "客戶其他資料", "结算账户资料",
                      "相关保证金融资账户(只适用于证券账户(保证金))", "身份声明", "居留司法管辖区及税务编号或具有等同功能的识辨编号",
                      "介绍及推广", "其他"]

        pickReasonTitle_loc = (By.XPATH, '//div[contains(text(), "请选择可多选")]')
        reasonRemark_loc = (
            By.XPATH, '//span[@class="align" and contains(text(), "备注")]/parent::div/following-sibling::div//textarea')
        reasonBtn_loc = (
            By.XPATH, '//div[@class="button-1 text-center"]//button[span[contains(text(), "{btn}")]]'.format(btn=btntext))

        self.find_element(*pickReasonTitle_loc).click()
        for n in reasontext:
            reason_loc = (
                By.XPATH, '//span[text()="{}"]/preceding-sibling::label//span[@class="el-checkbox__inner"]'.format(n))
            reason = self.find_element(*reason_loc)
            self.scrollinto(reason)

        reasonRemark = self.find_element(*reasonRemark_loc)
        reasonRemark.send_keys("这是拒绝原因123qaz,./")
        assert reasonRemark.get_attribute("value") != ''

        self.find_element(*reasonBtn_loc).click()


    def click_popWindow(self, text):
        popWindow_loc = (By.XPATH, '//div[@class="el-message-box"]//div[@class="el-message-box__btns"]/button[span[contains(text(), "{btntext}")]]'.format(btntext=text))
        return self.find_element(*popWindow_loc).click()


    def apply_error(self):
        # import pdb; pdb.set_trace()
        errormsg_loc = (By.XPATH, '//div[@class="el-form-item__error"]/ancestor::span/preceding-sibling::div')
        errormsg2_loc = (By.XPATH, '//div[@class="el-form-item__error"]/ancestor::span/parent::div/preceding-sibling::div/div')
        try:
            errormsg = self.find_elements(*errormsg_loc)
            errormsg2 = self.find_elements(*errormsg2_loc)
            if errormsg != False:
                print("errormsg 不为空")
                for err in errormsg:
                    print(err.text, "栏 字段不能为空! ")

            if errormsg2 != False:
                print("errormsg2 不为空")
                for err2 in errormsg2:
                    print(err2.text, "栏 字段不能为空! ")

        except Exception as e:
            print("表单必填项已全部填写")
            print("错误原因可能是接口报错")


    """
        ops审核, 下拉列表选择账户类型, 点击生成按钮
    """
    def autoCreateAccountNO(self, randox=None):

        # 生成按钮
        generate_btn_loc = (By.XPATH, '//span[contains(text(), "生成")]/parent::button')
        # 客户编号下拉框
        accountNOSel_loc = (By.XPATH, '//span[contains(text(), "生成")]/parent::button/preceding-sibling::div[@class="el-select"]')

        # 下拉框
        accountwaySel_loc = (By.XPATH, '//div[@x-placement="bottom-start"]//li')

        # 下拉列表选择客户编号
        self.find_element(*accountNOSel_loc).click()
        accountwaylist = self.find_elements(*accountwaySel_loc)

        if randox == None:
            randox = random.randint(0, len(accountwaylist)-1)

        for i in range(len(accountwaylist)):
            if i == randox:
                while accountwaylist[i].is_displayed():
                    self.scrollinto(accountwaylist[i])
                    # self.script("arguments[0].click();", selectlist[i])

                    try:
                        tag_text = accountwaylist[i].get_attribute("textContent")
                        # print(tag_text)
                    except AttributeError:
                        continue

                # 点击生成按钮
                self.find_element(*generate_btn_loc).click()

                return accountwaylist[i].get_attribute("textContent")

    # 点击确定,创建账号
    def createTradeAccount(self):
        # 客户编号确认按钮
        accountNobtn_loc = (By.XPATH, '//span[contains(text(), "生成")]/parent::button/following-sibling::button[span[contains(text(), "确认")]]')
        self.find_element(*accountNobtn_loc).click()

    # 手动输入客户编号
    def manualSendAccountNo(self):
        # 客户编号输入框
        accountNoInput_loc = (By.XPATH, '//span[contains(text(), "生成")]/parent::button/preceding-sibling::div[@class="el-input"]')
        self.find_element(*accountNoInput_loc).send_keys(random.randint(0, 999999))

    # 输入优惠码
    def send_promoCode(self, randox=None):

        promoCode_loc = (
            By.XPATH, '//span[contains(text(), "优惠码")]/following-sibling::div//input')
        promoCode_select_loc = (
            By.XPATH, "//div[contains(@style,'position: fixed;')]//li[@class='el-select-dropdown__item']")

        promoCode = self.find_element(*promoCode_loc)
        promoCode.click()

        promoCodeValueList = self.find_elements(*promoCode_select_loc)
        if randox == None:
            randox = random.randint(0, len(promoCodeValueList)-1)

        for i in range(len(promoCodeValueList)):
            if i == randox:
                while promoCodeValueList[i].is_displayed():
                    self.scrollinto(promoCodeValueList[i])
                    # self.script("arguments[0].click();", promoCodeValueList[i])

                    try:
                        tag_text = promoCodeValueList[i].get_attribute("textContent")
                        # print(tag_text)
                    except AttributeError:
                        continue

                # return promoCodeValueList[i].get_attribute("textContent")

    # OPS创建账号框,点击确定
    def ops_createNO(self):
        sublime_popwindow_loc = (
            By.XPATH, "//span[text()='确定']//parent::button")
        self.find_element(*sublime_popwindow_loc).click()