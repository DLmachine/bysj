from scrapy import cmdline


name = 'songsSpider'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())