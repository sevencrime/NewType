#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-14 21:30:24
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$

import os,sys,time
import random,glob
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from Commons import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class ApplyPage(BasePage.BasePage):
    # log = Logging.Logs()
    mob = glob.glob(os.path.abspath(os.path.dirname(os.getcwd()))+r'\image\*.jpg')

    def get_input(self, text, parent=False):
        if not parent:
            input_loc = (By.XPATH, "//div[contains(text(), '%s')]/following-sibling::span//input" %text)
        else:
            input_loc = (By.XPATH, "//div[contains(text(), '%s')]/parent::div/following-sibling::*//input" %text)

        return input_loc

    # def get_derivativeInput(self, text):
    #     derivativeInput_loc = (By.XPATH, "//div[contains(text(), '%s')]/parent::div/following-sibling::div//input" %text)
    #     return derivativeInput_loc

    def get_checkbox(self, text):
    	checkbox_loc = (By.XPATH, "//span[contains(text(), '%s')]/preceding-sibling::span" %text)
    	return checkbox_loc

    def get_select(self, text=False):
        if not text:
            print("getselectsssssssssssssssss")
            select_loc = (By.XPATH, "//div[contains(@style,'position: absolute;')]//li")

            selectlist = self.find_elements(*select_loc)

            randox = random.randint(0,len(selectlist)-1)
            for i in range(len(selectlist)):
                if i == randox:
                    while selectlist[i].is_displayed():
                        self.scrollinto(selectlist[i])
                        # self.script("arguments[0].click();", selectlist[i])

                        try:
                            tag_text = selectlist[i].get_attribute("textContent")
                            # print(tag_text)
                        except AttributeError:
                            continue

                    return selectlist[i].get_attribute("textContent")

        else:
            select_loc = (By.XPATH, "//span[contains(text(), '%s')]" %text) 
            select_value = self.find_element(*select_loc)
            self.scrollinto(select_value)
            return select_value

    def modify_displys(self, display=None):
        js = 'var file = document.querySelectorAll(".el-upload__input"); \
            for(var i=0;i<file.length;i++){file[i].style.display="%s";}' %display
        self.script(js)

    def get_radio(self, text):
        radio_loc = (By.XPATH, "//div[contains(text(), '%s')]/following-sibling::span//label[1]" %text)
        return radio_loc

    def get_action(self, text):
        print("action")
        parents_loc = (By.XPATH, "//div[contains(text(), '%s')]" %text)
        # time.sleep(5)
        ActionChains(self.driver).click(self.find_element(*parents_loc)).perform()

    def scrollinto(self, loc):
        self.script("arguments[0].scrollIntoView();", loc)
        self.script("arguments[0].click();", loc)

    def send_applicationFor(self, text):
        # 账户类型
        applicationFor = self.find_element(*self.get_input('账户类型'))
        self.scrollinto(applicationFor)
        tag_text = self.get_select(text=text)
        # print(applicationFor.get_attribute("value"))
        return applicationFor.get_attribute("value")
    
    def send_accountOpeningWay(self, text=False):
        # 开户方法
        accountOpeningWay = self.find_element(*self.get_input('开户方法'))
        self.scrollinto(accountOpeningWay)
        tag_text = self.get_select(text=text)

        return accountOpeningWay.get_attribute("value")

    def send_parentId(self):
        # 负责人
        parentId = self.find_element(*self.get_input('负责人'))
        self.scrollinto(parentId)
        tag_text = self.get_select(text='sales_t1')

        return parentId.get_attribute("value")

    def send_mailLanguage(self, text=False):
        # 邮件语言
        mailLanguage = self.find_element(*self.get_input('邮件语言'))
        self.scrollinto(mailLanguage)
        tag_text = self.get_select(text=text)

        return mailLanguage.get_attribute("value")

    def send_accountType(self, text):
        # 账户类别
        self.find_element(*self.get_checkbox(text)).click()

    def send_title(self):
        # 称谓
        title = self.find_element(*self.get_input('称谓'))
        self.scrollinto(title)
        tag_text = self.get_select()
        return title.get_attribute("value")

    def send_firstName(self):
        # 名字
        firstName = self.find_element(*self.get_input('名字'))
        firstName.send_keys("%sfirstname%s" %(random.randint(0,100),random.randint(0,1030)))

        return firstName.get_attribute("value")

    def send_lastName(self):
        # 姓氏
        lastName = self.find_element(*self.get_input('姓氏'))
        lastName.send_keys("%slastname%s" %(random.randint(0,100),random.randint(0,1030)))
        lastName.send_keys(Keys.ENTER)

        return lastName.get_attribute("value")

    def send_chineseName(self):
        # 中文姓名
        chineseName = self.find_element(*self.get_input('中文姓名'))
        chineseName.send_keys("郑某人")
        return chineseName.get_attribute("value")

    def send_emali(self):
        # 电邮
        email = self.find_element(*self.get_input('电邮'))
        email.send_keys("%sonedi2s%s@qq.com" %(random.randint(0,1000),random.randint(0,10300)))
        return email.get_attribute("value")

    def send_phoneAreaCode(self):
        # 电话号码区号
        phoneAreaCode = self.find_element(*self.get_input('电话号码区号'))
        self.scrollinto(phoneAreaCode)
        tag_text = self.get_select()
        return phoneAreaCode.get_attribute("value")

    def send_phone(self):
        # 电话号码
        phone = self.find_element(*self.get_input("电话号码(用于通讯)"))
        phone.send_keys("%s6253%s" %(random.randint(0,100002),random.randint(0,10502)))
        return phone.get_attribute("value")

    def send_address(self):
        # 住宅地址
        address = self.find_element(*self.get_input("住宅地址(不接受邮政信箱)"))
        address.send_keys("桑达科技大厦802")
        return address.get_attribute("value")

    def send_addressMail(self):
        # 邮寄地址
        addressMail = self.find_element(*self.get_input("邮寄地址(如与住宅地址不同)"))
        addressMail.send_keys("桑达科技大厦802")

        return addressMail.get_attribute("value")

    def send_nationality(self):
        # 国籍
        nationality = self.find_element(*self.get_input("国籍"))
        self.scrollinto(nationality)
        tag_text = self.get_select()
        return nationality.get_attribute("value")

    def send_idType(self):
        # 身份证件类型
        idType = self.find_element(*self.get_input("身份证件类型"))
        self.scrollinto(idType)
        tag_text = self.get_select()
        if tag_text == "其他":
            other_type = self.find_element(*self.get_input("其他证件类型"))
            other_type.send_keys("idType")
            idNumber = self.find_element(*self.get_input("其他证件号码"))
            idNumber.send_keys("%s423523%s" %(random.randint(0,1001),random.randint(0,10600)))
            return idType.get_attribute("value"), other_type.get_attribute("value"), idNumber.get_attribute("value")
        else:
            idNumber = self.find_element(*self.get_input("身份证或护照号码"))
            idNumber.send_keys("%s423523%s" %(random.randint(0,1001),random.randint(0,10600)))
            return idType.get_attribute("value"), idNumber.get_attribute("value")


    def send_countryIssue(self):
        # 签发国籍
        countryIssue = self.find_element(*self.get_input("签发国家"))
        self.scrollinto(countryIssue)
        tag_text = self.get_select()
        return countryIssue.get_attribute("value")

    def send_birthday(self):
        # 出生日期
        birthday = self.find_element(*self.get_input("出生日期(日/月/年)"))
        birthday.send_keys("21/01/2000")
        birthday.send_keys(Keys.ENTER)
        return birthday.get_attribute("value")

    def send_birthPlace(self):
        # 出生地点
        birthPlace = self.find_element(*self.get_input('出生地点'))
        self.scrollinto(birthPlace)
        tag_text = self.get_select()
        # print(tag_text)
        return birthPlace.get_attribute("value")

    def employment(self):
        # 就业情况
        employment = self.find_element(*self.get_input("就业情况"))
        self.scrollinto(employment)
        tag_text = self.get_select()

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

            return employment, occupation, employedPeriod, employer, businessType, businessAddress, businessPhone

        elif tag_text == "其他":
            Hidden_loc = (By.XPATH, "//div[contains(text(), '就业情况')]/parent::div/parent::span/following-sibling::span//input")
            Hidden = self.find_element(*Hidden_loc)
            Hidden.send_keys("Hidden")
            return employment, Hidden

        elif tag_text == "退休" or tag_text == "无业":
            return employment

    def uploadImage(self):
        # 上传图片
        pass



    def totalAnnualCustomerRevenueHK(self):
        # 客户全年总收入为(港元)
        self.find_element(*self.get_radio("客户全年总收入为(港元)")).click()
        self.find_element(*self.get_input("请注明资金来源", parent=True)).send_keys("资金来源")

    def customerNetAssetValueHK(self):
        # 客户资产净值(港元)
        self.find_element(*self.get_radio("客户资产净值(港元)")).click()
        self.find_element(*self.get_input("请注明资产净值", parent=True)).send_keys("请注明资产净值")

    def sourceOfWealth(self):
        # 客户交易的资金/财富来源（选择所有适用）
        self.find_element(*self.get_checkbox("就业薪金")).click()

    def securities(self):
        # 客户投资经验及曾买卖产品>证券
        securities = self.find_element(*self.get_input("证券"))
        self.scrollinto(securities)
        tag_text = self.get_select()
        return securities.get_attribute("value")

    def CBBC(self):
        # 客户投资经验及曾买卖产品>牛熊证
        CBBCcertificate = self.find_element(*self.get_input("牛熊证"))
        self.scrollinto(CBBCcertificate)
        tag_text = self.get_select()
        return CBBCcertificate.get_attribute("value")

    def warrants(self):
        # 客户投资经验及曾买卖产品>衍生权证
        derivativewarrant = self.find_element(*self.get_input("衍生权证(窝轮)"))
        self.scrollinto(derivativewarrant)
        tag_text = self.get_select()
        return derivativewarrant.get_attribute("value")

    def futures(self):
        # 客户投资经验及曾买卖产品>期货
        futures = self.find_element(*self.get_input("期货"))
        self.scrollinto(futures)
        tag_text = self.get_select()
        return futures.get_attribute("value")

    def Option(self):
        # 客户投资经验及曾买卖产品>期权
        Option = self.find_element(*self.get_input("期权"))
        self.scrollinto(Option)
        tag_text = self.get_select()
        return Option.get_attribute("value")

    def foreignExchange(self):
        # 客户投资经验及曾买卖产品>外汇
        foreignexchange = self.find_element(*self.get_input("外汇"))
        self.scrollinto(foreignexchange)
        tag_text = self.get_select()
        return foreignexchange.get_attribute("value")

    def bullion(self):
        # 贵金属
        if self.driver.page_source.find("贵金属") != -1:
            bullion = self.find_element(*self.get_input("贵金属"))
            self.scrollinto(bullion)
            tag_text = self.get_select()
            return bullion.get_attribute("value")

    def otherInvestmentText(self):
        # 客户投资经验及曾买卖产品>其他投资
        self.find_element(*self.get_input("其他投资")).send_keys("otherInvest")
        # self.get_action("其他投资")
        # time.sleep(5)
        # parent_loc = (By.XPATH, "//div[contains(text(), '其他投资')]/parent::*/parent::span/following-sibling::*//input")
        # self.find_element(parent_loc).click()
        # self.find_element(*self.get_select()).click()

    def derivativeCourse(self):
        # 客户是否曾接受有关衍生产品性质和风险的一般知识培训或修读相关课程
        derivativeCourse = self.find_element(*self.get_input("相关课程", parent=True))
        self.scrollinto(derivativeCourse)
        tag_text = self.get_select()
        return derivativeCourse.get_attribute("value")

    def derivativeJobs(self):
        # 客户是否从现时或过去拥有与衍生产品有关的工作经验?
        derivativeJobs = self.find_element(*self.get_input("工作经验", parent=True))
        self.scrollinto(derivativeJobs)
        tag_text = self.get_select()
        return derivativeJobs.get_attribute("value")

    def tradingFund(self):
        # 客户是否于过去3年曾执行 5次或以上有关衍生产品的交易
        tradingFund = self.find_element(*self.get_input("买卖基金", parent=True))
        self.scrollinto(tradingFund)
        tag_text = self.get_select()
        return tradingFund.get_attribute("value")

    def buyProduct(self):
        # 客户是否申请开通买卖衍生权证、牛熊证及结构性等产品
        buyProduct = self.find_element(*self.get_input("买卖衍生", parent=True))
        self.scrollinto(buyProduct)
        tag_text = self.get_select()
        # print(tag_text,"ssssssssssssss")
        if tag_text == "是":
            # print("是是是是是")
            riskStatement = self.find_element(*self.get_input("结构性产品相关风险声明披露", parent=True))
            self.scrollinto(riskStatement)
            tag_text = self.get_select()
            if tag_text == "否":
                messagebox = (By.XPATH, "//div[@aria-label='提示']//div[@class='el-message-box__btns']/button")
                self.find_element(*messagebox).click()

        return buyProduct.get_attribute("value")

    def bankrupt(self):
        # 客户是否曾经宣告破产或被申请破产
        bankrupt = self.find_element(*self.get_input("申请破产"))
        self.scrollinto(bankrupt)
        tag_text = self.get_select()
        if tag_text == "有":
            # 破产日期
            self.find_element(*self.get_input("破产日期")).send_keys("02/04/2019")
            self.find_element(*self.get_input("破产日期")).send_keys(Keys.ENTER)
            # 破产证明书
            self.modify_displys(display='block')
            self.find_element(*self.get_input("破产解除证明书")).send_keys(random.sample(self.mob, 1))
            self.modify_displys()
            loading_loc = (By.XPATH, "//div[contains(text(), '必需提交交易授权书')]/following-sibling::span//i[@class='el-icon-loading']")
            WebDriverWait(self.driver, 10).until_not(
                EC.presence_of_element_located(loading_loc))

        return bankrupt.get_attribute("value")

    def customerRelatives(self):
        # 客户是否艾德证券及/或艾德金业的雇员或任何其客户的亲属?
        if self.driver.page_source.find("艾德证券及/或艾德金业的雇员") != -1:
            customerRelatives = self.find_element(*self.get_input("艾德证券及/或艾德金业的雇员", parent=True))
            self.scrollinto(customerRelatives)
            tag_text = self.get_select()
            if tag_text == "是":
                self.find_element(*self.get_input("艾德金业雇员名称及关系",parent=True)).send_keys("relationship")

        else:
            customerRelatives = self.find_element(*self.get_input("艾德证券的雇员", parent=True))
            self.scrollinto(customerRelatives)
            tag_text = self.get_select()
            if tag_text == "是":
                self.find_element(*self.get_input("艾德证券雇员名称及关系",parent=True)).send_keys("relationship")

        return customerRelatives.get_attribute("value")

    def associatedcustomer(self):
        # 3.客户是否与任何艾德证券及/或艾德金业客户有关连?
        # print(self.driver.page_source.find("艾德证券及/或艾德金业客户有关连"),"find find")
        if self.driver.page_source.find("艾德证券及/或艾德金业客户有关连") != -1:
            # print("不等于-1")
            associatedcustomer = self.find_element(*self.get_input("艾德金业客户有关连", parent=True))
            self.scrollinto(associatedcustomer)
            tag_text = self.get_select()
            if tag_text == "是":
                self.find_element(*self.get_input("艾德金业客户名称", parent=True)).send_keys("ClientName")

        else:
            # print("else else")
            associatedcustomer = self.find_element(*self.get_input("艾德证券客户有关连", parent=True))
            self.scrollinto(associatedcustomer)
            tag_text = self.get_select()
            if tag_text == "是":
                self.find_element(*self.get_input("艾德证券客户名称", parent=True)).send_keys("ClientName")

        return associatedcustomer.get_attribute("value")

    def director(self):
        # 4.客户是否香港交易所之交易所参与者或证监会之持牌人或注册人之董事、雇员或认可人士?
        director = self.find_element(*self.get_input("认可人士?", parent=True))
        self.scrollinto(director)
        tag_text = self.get_select()
        if tag_text == "是":
            self.find_element(*self.get_input("认可人士(请详述)", parent=True)).send_keys("HKEX")
            # 请提供雇主同意书
            self.modify_displys(display='block')
            self.find_element(*self.get_input("请提供雇主同意书", parent=True)).send_keys(random.sample(self.mob, 1))
            self.modify_displys()
            loading_loc = (By.XPATH, "//div[contains(text(), '必需提交交易授权书')]/following-sibling::span//i[@class='el-icon-loading']")
            WebDriverWait(self.driver, 10).until_not(
                EC.presence_of_element_located(loading_loc))

    def citizenOfUSA(self):
        # 5.客户是否拥有美国公民或美国合法永久居民身份?
        citizenOfUSA = self.find_element(*self.get_input("美国公民", parent=True))
        self.scrollinto(citizenOfUSA)
        tag_text = self.get_select()
        if tag_text == "是":
            # 税务编号
            citizenOfUSA_Tax = (By.XPATH, "//div[contains(text(), '美国公民')]/parent::div/parent::div/parent::span/following-sibling::*//input")
            self.find_element(*citizenOfUSA_Tax).send_keys("citizenOfUSA_Tax")

        return citizenOfUSA.get_attribute("value")

    def americanResident(self):
        # 6.就税务而言，您是否美国居民?
        americanResident = self.find_element(*self.get_input("美国居民", parent=True))
        self.scrollinto(americanResident)
        tag_text = self.get_select()
        if tag_text == "是":
            # 税务编号
            americanResident_Tax = (By.XPATH, "//div[contains(text(), '美国居民')]/parent::div/parent::div/parent::span/following-sibling::*//input")
            self.find_element(*americanResident_Tax).send_keys("americanResident_Tax")

        return americanResident.get_attribute("value")

    def PEP_People(self):
        # 7.客户是否香港法律定义下的“政治公众人物（PEP）”或与政治公众人物有密切联系？
        PEP_People = self.find_element(*self.get_input("政治公众人物（PEP）", parent=True))
        self.scrollinto(PEP_People)
        tag_text = self.get_select()
        if tag_text == "是":
            self.find_element(*self.get_input("职位/政治公众人物名称", parent=True)).send_keys("Position/political")

        return PEP_People.get_attribute("value")

    def investmentTarget(self):
        # 8.客户的投资目标是:
        investmentTarget = self.find_element(*self.get_input("投资目标", parent=True))
        self.scrollinto(investmentTarget)
        tag_text = self.get_select()
        return investmentTarget.get_attribute("value")

    def riskTolerance(self):
        # 9.客户的风险承受能力是:
        riskTolerance = self.find_element(*self.get_input("风险承受能力", parent=True))
        self.scrollinto(riskTolerance)
        tag_text = self.get_select()
        return riskTolerance.get_attribute("value")

    def bankaccount(self):
        # 结算账户
        currency = self.find_element(*self.get_input("货币", parent=True))
        self.scrollinto(currency)
        tag_text = self.get_select()
        if not tag_text == "不适用":
            bankAccount_loc = (By.XPATH, "//span[contains(text(), '删除')]/parent::*/parent::*/preceding-sibling::div//input")
            bankAccount = self.find_elements(*bankAccount_loc)
            for bankInput in bankAccount:
                bankInput.send_keys("bankAccount")


    def marginAccount(self):
        # 1.客户的配偶是否持有艾德证券任何相关的保证金账户?
        marginAccount = self.find_element(*self.get_input("客户的配偶", parent=True))
        self.scrollinto(marginAccount)
        tag_text = self.get_select()
        if tag_text == "是":
            name_or_num = (By.XPATH, "//div[contains(text(), '客户的配偶')]/parent::div/parent::div/parent::span/following-sibling::span//input")
            el_inputs = self.find_elements(*name_or_num)
            for inputs in el_inputs: 
                inputs.send_keys("name")


    def discretion(self):
        # 2.客户及/或其配偶是否单独或共同控制艾德证券之其他保证金账户35%或以上之表决权?
        discretion = self.find_element(*self.get_input("保证金账户35%或以上之表决权", parent=True))
        self.scrollinto(discretion)
        # discretion.click()
        tag_text = self.get_select()
        if tag_text == "是":
            name_or_num = (By.XPATH, "//div[contains(text(), '保证金账户35%或以上之表决权')]/parent::div/parent::div/parent::span/following-sibling::span//input")
            el_inputs = self.find_elements(*name_or_num)
            for inputs in el_inputs: 
                inputs.send_keys("name")

        return discretion.get_attribute("value")

    def companyAccounts(self):
        # 客户是否有以客户的同一集团公司旗下之公司开立保证金账户？
        companyAccounts = self.find_element(*self.get_input("同一集团公司旗下", parent=True))
        self.scrollinto(companyAccounts)
        # companyAccounts.click()
        tag_text = self.get_select()
        if tag_text == "是":
            name_or_num = (By.XPATH, "//div[contains(text(), '同一集团公司旗下')]/parent::div/parent::div/parent::span/following-sibling::span//input")
            el_inputs = self.find_elements(*name_or_num)
            for inputs in el_inputs: 
                inputs.send_keys("name")

        return companyAccounts.get_attribute("value")

    def learnHow(self):
        # 介绍及推广>>1.您透过哪些渠道认识艾德证券及/或艾德金业?(选择所有适用)
        channel_loc = (By.XPATH, "//div[contains(text(), '您透过哪些渠道认识艾德证券')]/parent::div/following-sibling::div//label")
        channel = self.find_elements(*channel_loc)
        for i in range(len(channel)):
            if i != len(channel)-1:
                channel[i].click()



    def beneficial(self):
        # 身份声明>>1.客户是否账户的最终实益拥有人?
        beneficial = self.find_element(*self.get_input("是否账户的最终实益拥有人", parent=True))
        self.scrollinto(beneficial)
        tag_text = self.get_select()
        if tag_text == "否":
            self.find_element(*self.get_input("最终实益拥有人名称为", parent=True)).send_keys("onedi")

        return beneficial.get_attribute("value")

    def Othed_People(self):
        # 身份声明>>2.客户是否最终负责下单的人?
        othedPeople = self.find_element(*self.get_input("负责下单", parent=True))
        self.scrollinto(othedPeople)
        tag_text = self.get_select()
        if tag_text == "否":
            self.find_element(*self.get_input("最终负责下单人为", parent=True)).send_keys("onedi")
            # 必需提交交易授权书
            self.modify_displys(display='block')
            self.find_element(*self.get_input("必需提交交易授权书")).send_keys(random.sample(self.mob, 1))
            self.modify_displys()
            loading_loc = (By.XPATH, "//div[contains(text(), '必需提交交易授权书')]/following-sibling::span//i[@class='el-icon-loading']")
            WebDriverWait(self.driver, 10).until_not(
                EC.presence_of_element_located(loading_loc))

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
        return acceptStatement.get_attribute("value")


    def useStatement(self):
        # 个人资料之使用声明>>个人资料之使用声明
        useStatement = self.find_element(*self.get_input("个人资料之使用声明"))
        self.scrollinto(useStatement)
        tag_text = self.get_select()
        return useStatement.get_attribute("value")


    def click_sublime(self):
        sublime_loc = (By.CLASS_NAME, "button-1")
        sublime = self.find_element(*sublime_loc).click()






