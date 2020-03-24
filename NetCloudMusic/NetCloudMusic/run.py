from scrapy import cmdline


name = 'getPlaylist'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())