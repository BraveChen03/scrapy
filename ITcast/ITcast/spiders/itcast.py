import scrapy
from ITcast.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    name='itcast'
    allowed_domains=['itcast.cn']
    start_urls=["http://www.itcast.cn/channel/teacher.shtml"]
    print '------------------'
    def parse(self, response):
    	print '--*-*---------///'
    	node_list=response.xpath("//div[@class='li_txt']")
    	print '--*-*---------'
    	for node in node_list:
			print '-*-*-*-*-*-*-*-*-*'
			item=ItcastItem()
			item['name']=node.xpath("./h3/text()").extract()
			item['title']=node.xpath("./h4/text()").extract()
			item['info']=node.xpath("./p/text()").extract()

			yield item
