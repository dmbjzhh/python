from selenium import webdriver

dr = webdriver.Chrome()
dr.get('https://www.qiushibaike.com/')

main_content = dr.find_element_by_id('content-left')

contents = main_content.find_elements_by_class_name('content')  # remember is elements

i = 1
for content in contents:
	print(str(i) + '. ' + content.text + '\n')
	i += 1

dr.quit()