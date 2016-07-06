#coding=utf-8
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time, unittest, sys, os, random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
from BasicOperation import BasicOperation

class Home(unittest.TestCase,BasicOperation):
	@classmethod
	def setUpClass(cls):
		desired_caps = {}
		desired_caps['appium-version'] = '1.0'
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '5.0'
		desired_caps['deviceName'] = 'OnePlus'
		#desired_caps['app'] = os.path.abspath('/Users/eico/Downloads/Weico-weico-release.apk')
		desired_caps['appPackage'] = 'com.eico.weico'
		desired_caps['appActivity'] = 'com.eico.weico.activity.MainFragmentActivity'

		cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

	def setUp(self):
		try:
			self.driver.find_element_by_id("tab_icons_home_img").click()
			time.sleep(2)
		except:
			time.sleep(2)

	def tearDown(self):
		time.sleep(2)

	def test_01_sendWeibo(self):
		self.driver.find_element_by_id("index_title_compose").click()
		self.composeWeibo("test_01_composeWeibo")
		#加满9张图
		self.driver.find_element_by_id("buttonCam").click()
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]").click()
		time.sleep(2)
		self.driver.find_element_by_id("content").click()
		time.sleep(2)
		self.driver.find_element_by_xpath("//android.view.View[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.ImageView[2]").click()
		self.driver.find_element_by_id("btn_next").click()
		self.driver.find_element_by_id("send_ok").click()
		time.sleep(5)

	def test_02_sendWeiboFromDraft(self):
		self.driver.find_element_by_id("index_title_compose").click()
		self.composeWeibo("test_02_sendWeiboFromDraft")
		self.driver.find_element_by_id("edit_cancel").click()
		self.driver.find_element_by_id("positive_button").click()
		self.driver.find_element_by_id("index_title_compose").click()
		self.driver.find_element_by_id("buttonMore").click()
		self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[2]").click()
		self.driver.find_element_by_id("compose_view_wrap").send_keys(" I have edited the draft.")
		#删除照片
		#会闪退
		# self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.view.View[2]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.view.View[1]/android.widget.ImageView[1]").click()
		# leftFlickTime = random.randint(0,8)
		# while leftFlickTime>0:
		# 	TouchAction(self.driver).press(x=800,y=800).move_to(x=-600,y=0).wait(1000).release().perform()
		# 	leftFlickTime-=1
		# self.driver.find_element_by_id("single_image_options").click()
		# self.driver.find_element_by_id("positive_button").click()
		# time.sleep(2)
		# rightFlickTime = random.randint(0,leftFlickTime)
		# while rightFlickTime>0:
		# 	TouchAction(self.driver).press(x=300,y=800).move_to(x=800,y=0).wait(1000).release().perform()
		# 	rightFlickTime-=1
		# self.driver.find_element_by_id("single_image_options").click()
		# self.driver.find_element_by_id("positive_button").click()
		# self.driver.find_element_by_id("single_image_back").click()
		#添加照片
		self.driver.find_element_by_id("buttonCam").click()
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]").click()
		time.sleep(2)
		self.driver.find_element_by_id("content").click()
		time.sleep(2)
		self.driver.find_element_by_xpath("//android.view.View[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.ImageView[2]").click()
		self.driver.find_element_by_id("btn_next").click()
		#修改位置
		self.driver.find_element_by_id("textLocation").click()
		WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "title")))
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]").click()
		self.driver.find_element_by_id("send_ok").click()

	def test_03_switchToLongWeibo(self):
		string = "test_03_switchToLongWeibo\n\n Selenium Python bindings provides a simple API to write functional/acceptance tests using Selenium WebDriver. Through Selenium Python API you can access all functionalities of Selenium WebDriver in an intuitive way.Selenium Python bindings provide a convenient API to access Selenium WebDrivers like Firefox, Ie, Chrome, Remote etc. The current supported Python versions are 2.7, 3.2, 3.3 and 3.4.This documentation explains Selenium 2 WebDriver API. Selenium 1 / Selenium RC API is not covered here. "
		self.driver.find_element_by_id("index_title_compose").click()
		self.composeWeibo(string)
		time.sleep(3)
		self.driver.find_element_by_id("content").send_keys(string)
		try:
			self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout[4]/android.widget.ImageView[1]").click()
			self.driver.find_element_by_id("weiconote_finish").click()
		except:
			self.driver.find_element_by_id("buttonMore").click()
			self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout[4]/android.widget.ImageView[1]").click()
			self.driver.find_element_by_id("weiconote_finish").click()
		self.driver.find_element_by_id("positive_button").click()
		self.driver.find_element_by_id("send_ok").click()

	def test_04_sendToGroup(self):
		self.driver.find_element_by_id("index_title_compose").click()
		self.composeWeibo("This weibo is only can be seen by weico group.(test_04_sendToGroup)")
		self.driver.find_element_by_id("buttonMore").click()
		self.driver.find_element_by_name("group").click()
		self.driver.find_element_by_name("weico").click()
		self.driver.find_element_by_id("send_ok").click()

	def test_041_deleteFromTimeline(self):
		try:
			self.driver.find_element_by_id("index_item_delete").click()
			self.driver.find_element_by_id("negative_button").click()
			self.driver.find_element_by_id("index_item_delete").click()
			self.driver.find_element_by_id("positive_button").click()
		except:
			self.skipTest("Cannot delete this weibo.")

	def test_05_addToFavoriteFromTimeline(self):
		while True:
			try:
				self.driver.find_element_by_id("index_item_actions").click()
				break
			except:
				TouchAction(self.driver).press(x=500,y=1200).move_to(x=0,y=-200).wait(1000).release().perform()
		self.driver.find_element_by_id("index_item_fav_del").click()
		weibo_author = self.driver.find_element_by_id("index_item_screen_name").get_attribute("text")
		weibo_content = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text")
		#print weibo_author,weibo_content
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		time.sleep(2)
		self.driver.find_element_by_id("favour").click()
		WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID, "index_item_weibo_layout")))
		favorite_weibo_author = self.driver.find_element_by_id("index_item_screen_name").get_attribute("text")
		favorite_weibo_content = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text")
		#print favorite_weibo_author, favorite_weibo_content
		self.driver.find_element_by_id("back").click()
		self.assertEqual(weibo_author, favorite_weibo_author, "The weibo author is not the same one.")
		self.assertEqual(weibo_content,favorite_weibo_content,"The weibo is not marked as favorite successfully.")

	def test_06_likeFromTimeline(self):
		while True:
			try:
				self.driver.find_element_by_id("index_item_actions").click()
				break
			except:
				TouchAction(self.driver).press(x=500,y=1200).move_to(x=0,y=-200).wait(1000).release().perform()
		self.driver.find_element_by_id("index_item_praise").click()

	def test_07_repostFromTimeline(self):
		while True:
			try:
				self.driver.find_element_by_id("index_item_actions").click()
				break
			except:
				TouchAction(self.driver).press(x=500,y=1200).move_to(x=0,y=-200).wait(1000).release().perform()
		self.driver.find_element_by_id("index_item_repost").click()
		self.driver.find_element_by_id("compose_view_wrap").send_keys("test_07_repostFromTimeline")
		self.driver.find_element_by_id("send_ok").click()

	def test_08_commentFromTimeline(self):
		while True:
			try:
				self.driver.find_element_by_id("index_item_actions").click()
				break
			except:
				TouchAction(self.driver).press(x=500,y=1200).move_to(x=0,y=-200).wait(1000).release().perform()
		self.driver.find_element_by_id("index_item_comment").click()
		self.driver.find_element_by_id("compose_view_wrap").send_keys("test_08_commentFromTimeline")
		self.driver.find_element_by_id("send_ok").click()

	def test_09_addToFavoriteFromDetailPage(self):
		self.driver.find_element_by_id("index_item_weibo_content").click()
		while self.driver.find_element_by_id("detail_title_fav").is_selected():
			self.driver.find_element_by_id("back").click()
			TouchAction(self.driver).press(x=500,y=800).move_to(x=0,y=-200).wait(1000).release().perform()
			self.driver.find_element_by_id("index_item_weibo_content").click()
		weibo_author = self.driver.find_element_by_id("detail_name").get_attribute("text")
		weibo_content = self.driver.find_element_by_id("detail_status_content").get_attribute("text")
		#print weibo_author,weibo_content
		self.driver.find_element_by_id("detail_title_fav").click()
		self.driver.find_element_by_id("detail_title_goback").click()
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		time.sleep(2)
		self.driver.find_element_by_id("favour").click()
		WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID, "index_item_weibo_layout")))
		favorite_weibo_author = self.driver.find_element_by_id("index_item_screen_name").get_attribute("text")
		favorite_weibo_content = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text")
		#print favorite_weibo_author, favorite_weibo_content
		self.driver.find_element_by_id("back").click()
		self.assertEqual(weibo_author, favorite_weibo_author, "The weibo author is not the same one.")
		self.assertEqual(weibo_content,favorite_weibo_content,"The weibo is not marked as favorite successfully.")

	def test_10_commentFromDetailPage(self):
		self.driver.find_element_by_id("index_item_weibo_content").click()
		self.driver.find_element_by_id("detail_actions_comment").click()
		self.driver.find_element_by_id("send_directmessage_text").send_keys("test_10_commentFromDetailPage")
		self.driver.find_element_by_id("repost_action_option").click()
		self.driver.find_element_by_id("at_option").click()
		self.driver.find_element_by_id("search_edittext").send_keys("test")
		self.driver.find_element_by_id("item_user_checked").click()
		self.driver.find_element_by_id("done_button").click()
		self.driver.find_element_by_id("send_option_layout").click()
		self.driver.find_element_by_id("detail_title_goback").click()

	def test_11_deleteFromDetailPage(self):
		self.driver.find_element_by_id("index_item_weibo_content").click()
		try:
			self.driver.find_element_by_id("detail_title_del").click()
			self.driver.find_element_by_id("negative_button").click()
			self.driver.find_element_by_id("detail_title_del").click()
			self.driver.find_element_by_id("positive_button").click()
		except:
			self.driver.find_element_by_id("detail_title_goback").click()
			self.skipTest("Cannot delete this weibo.")
			
	def test_12_likeFromDetailPage(self):
		self.driver.find_element_by_id("index_item_weibo_content").click()
		self.driver.find_element_by_id("detail_actions_praise").click()
		self.driver.find_element_by_id("detail_title_goback").click()

	def test_13_repostFromDetailPage(self):
		self.driver.find_element_by_id("index_item_weibo_content").click()
		self.driver.find_element_by_id("detail_actions_forward").click()
		self.driver.find_element_by_id("compose_view_wrap").send_keys("test_13_repostFromDetailPage")
		self.driver.find_element_by_id("textLocation").click()
		self.driver.find_element_by_id("send_ok").click()
		self.driver.find_element_by_id("detail_title_goback").click()

	def test_14_shareFromDetailPage(self):
		self.driver.find_element_by_id("index_item_weibo_content").click()
		self.driver.find_element_by_id("detail_title_more").click()
		self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
		self.driver.find_element_by_id("searchmessage_edittext").send_keys("test")
		self.driver.find_element_by_id("friends_item_avatar_mask").click()
		self.driver.find_element_by_id("send_layout").click()
		self.driver.find_element_by_id("detail_title_goback").click()
		self.driver.find_element_by_id("dm_user_title_goback").click()
		self.driver.find_element_by_id("detail_title_goback").click()

	def test_15_addAccountFromSlidebar(self):
		self.driver.find_element_by_id("index_title_groups").click()
		self.driver.find_element_by_id("current_avatar").click()
		self.driver.find_element_by_id("slidebar_account_manage").click()
		self.driver.find_element_by_id("account_back").click()
		self.driver.find_element_by_id("current_avatar").click()
		self.driver.find_element_by_id("slidebar_account_new").click()
		self.driver.find_element_by_id("sso_button").click()
		WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.widget.EditText[1]")))
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.widget.EditText[1]").send_keys("jhwhale@163.com")
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.widget.EditText[2]").send_keys("testweico")
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[2]/android.view.View[3]").click()

	def test_16_changeAccountFromSlidebar(self):
		self.driver.find_element_by_id("index_title_groups").click()
		self.driver.find_element_by_id("current_avatar").click()
		previousUser = self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]").get_attribute("text")
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[2]").click()
		WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "index_title_group")))
		currentUser = self.driver.find_element_by_id("index_title_group").get_attribute("text")
		#print previousUser, currentUser
		self.assertNotEqual(previousUser, currentUser)

	def test_17_OriginalGroup(self):
		self.driver.find_element_by_id("index_title_groups").click()
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.SlidingPaneLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[2]").click()
		title = self.driver.find_element_by_id("index_title_group").get_attribute("text")
		self.assertIn(title, ("Original",u"原创微博"))

	def test_18_FriendGroup(self):	
		self.driver.find_element_by_id("index_title_groups").click()
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.SlidingPaneLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[3]").click()
		title1 = self.driver.find_element_by_id("index_title_group").get_attribute("text")
		self.assertIn(title1, ("Friends-All",u"好友圈-全部"))
		self.driver.find_element_by_id("home_timeline_group_orig").click()
		title2 = self.driver.find_element_by_id("index_title_group").get_attribute("text")
		self.assertIn(title2, ("Friends-Original", u"好友圈-原创"))

	def test_19_SpecialGroup(self):
		self.driver.find_element_by_id("index_title_groups").click()
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.SlidingPaneLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[4]").click()
		title = self.driver.find_element_by_id("index_title_group").get_attribute("text")
		self.assertEqual(title, u"特别关注")

	def test_20_offline(self):
		self.driver.find_element_by_id("index_title_groups").click()
		self.driver.find_element_by_id("sidebar_icon_offline_button").click()
		self.driver.find_element_by_id("positive_button").click()

	def test_21_display(self):
		self.driver.find_element_by_id("index_title_groups").click()
		self.driver.find_element_by_id("sidebar_icon_display_button").click()
		self.driver.find_element_by_id("back").click()

	def test_22_Theme(self):
		self.driver.find_element_by_id("setting_theme").click()
		if self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.GridView[1]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView[2]").is_enabled():
			self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.GridView[1]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView[2]").click()
		else:
			self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.GridView[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[2]").click()

	def test_23_Night(self):
		self.driver.find_element_by_id("index_title_groups").click()
		self.driver.find_element_by_id("night_setting_icon_bg_selector_button").click()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Home)
    unittest.TextTestRunner(verbosity=2).run(suite)			