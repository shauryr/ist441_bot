# ist441_bot


Contains the code for crawling a whole domain and getting all the links in that domain

Once you have the links - you can fetch the contents quickly

Runs with latest version of scrapy - `pip install scrapy`

For example here we demonstrate ACL crawling


1. ist441_bot/spiders/follow_spider.py

Edit the domain and start url if needed.

All links are saved in the file - `links.txt`

to run this code type - `scrapy crawl geturl`


2. Once you have the links - Crawl/wget them using your own code or use : `ist441_bot/spiders/get_json.py`

run - `scrapy crawl urlgetjson`

This will store the raw contents of the links in a `data.jl` file

If you want to fetch pdfs or other files - just change the parse_obj callback to save the file as pdf whenever encountered with a pdf link.
