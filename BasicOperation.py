#coding=utf-8
from appium import webdriver
import random,time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasicOperation():
	def composeWeibo(self,content):
		#self.driver.find_element_by_id("index_title_compose").click()
		#添加tag
		self.driver.find_element_by_id("buttonTag").click()
		self.driver.find_element_by_id("editText").send_keys("weico weibo")
		#添加@
		self.driver.find_element_by_id("buttonAt").click()
		self.driver.find_element_by_id("search_edittext").send_keys("test")
		self.driver.find_element_by_id("item_user_checked").click()
		self.driver.find_element_by_id("done_button").click()
		#添加文字
		self.driver.find_element_by_id("compose_view_wrap").send_keys(content)
		#添加位置
		WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "textLocation")))
		self.driver.find_element_by_id("textLocation").click()
		WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "title")))
		self.driver.find_element_by_id("title").click()
		#拍摄照片
		self.driver.find_element_by_id("buttonCam").click()
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]").click()
		time.sleep(2)
		self.driver.find_element_by_id("content").click()
		time.sleep(2)
		self.driver.find_element_by_xpath("//android.view.View[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.ImageView[2]").click()
		photo = range(2,9)#添加7张已有图片
		for i in photo:
			self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout["+str(i)+"]/android.widget.ImageView[1]").click()
		self.driver.find_element_by_id("btn_next").click()
		#添加表情
		self.driver.find_element_by_id("buttonEmoji").click()
		self.driver.find_element_by_id("newblog_expression_expression").click()
		expression = random.randint(1,10)
		fontexpression = random.randint(1,10)
		try:
			while expression>0:
				i = random.randrange(1,22)
				self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.GridView[1]/android.widget.RelativeLayout[" +str(i)+ "]/android.widget.ImageView[1]").click()
				expression-=1
			self.driver.find_element_by_id("newblog_expression_fontexpression").click()
			while fontexpression>0:	
				i = random.randrange(1,22)
				self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.GridView[1]/android.widget.RelativeLayout[" +str(i)+ "]/android.widget.ImageView[1]").click()
				fontexpression -= 1
		except:
			time.sleep(5)
			self.driver.find_element_by_id("newblog_expression_back").click()
			

	def composeComments(self,comments):
		#添加tag
		self.driver.find_element_by_id("buttonTag").click()
		self.driver.find_element_by_id("editText").send_keys("weico comments")
		#添加@
		self.driver.find_element_by_id("buttonAt").click()
		self.driver.find_element_by_id("search_edittext").send_keys("test")
		self.driver.find_element_by_id("item_user_checked").click()
		self.driver.find_element_by_id("done_button").click()
		#添加文字
		self.driver.find_element_by_id("compose_view_wrap").send_keys(comments)
		#添加表情
		self.driver.find_element_by_id("buttonEmoji").click()
		self.driver.find_element_by_id("newblog_expression_expression").click()
		expression = random.randint(1,10)
		while expression>0:
			i = random.randrange(1,22)
			self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.GridView[1]/android.widget.RelativeLayout[" +str(i)+ "]/android.widget.ImageView[1]").click()
			expression-=1
		self.driver.find_element_by_id("newblog_expression_fontexpression").click()
		fontexpression = random.randint(1,10)
		while fontexpression>0:	
			i = random.randrange(1,22)
			self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.GridView[1]/android.widget.RelativeLayout[" +str(i)+ "]/android.widget.ImageView[1]").click()
			fontexpression -= 1
		#同时转发评论
		forwardComments = random.randint(0,1)
		if forwardComments == 1:
			self.driver.find_element_by_id("textLocation").click()

	def sendDM(self,msg):
		self.driver.find_element_by_id("buttonCam").click()
		self.driver.find_element_by_id("backImageView").click()
		self.driver.find_element_by_id("msg_text").send_keys(msg)
		self.driver.find_element_by_id("buttonTag").click()
		self.driver.find_element_by_id("newblog_expression_expression").click()
		expression = random.randint(1,10)
		while expression>0:
			i = random.randrange(1,22)
			self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.GridView[1]/android.widget.RelativeLayout[" +str(i)+ "]/android.widget.ImageView[1]").click()
			expression -=1
		self.driver.find_element_by_id("newblog_expression_fontexpression").click()
		fontexpression = random.randint(1,10)
		while fontexpression>0:
			i = random.randrange(1,22)
			self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.GridView[1]/android.widget.RelativeLayout[" +str(i)+ "]/android.widget.ImageView[1]").click()
			fontexpression -= 1
		self.driver.find_element_by_id("send_layout").click()
