# !/bin/usr/python

import requests
from bs4 import BeautifulSoup
import sys
# import webbrowser


def test_crawler(max_page):
	start = 0
	page = 1
	while page <= int(max_page):
		keywords = sys.argv[1:-1]
		search_term = '+'.join(keywords)
		url = 'http://in.linkedin.com/jobs/search?keywords=' + str(search_term) + '&locationId=in:0&start=' + str(start) + '&count=25&trk=jobs_jserp_pagination_' + str(page)
		source = requests.get(url)
		text = source.text
		to_crawl = BeautifulSoup(text)
		print page
		print start
		
		job_title = to_crawl.findAll('a', {'class': 'job-title-link'})
		company_name = to_crawl.findAll('span', {'class': 'company-name-text'})
		location = to_crawl.findAll('span', {'itemprop': 'addressLocality'})
		for link1, link2, link3 in zip(job_title, company_name, location):
			href = link1.get('href')
			print link1.text
			print href
			print link2.text
			print link3.text
			print '\n'

		page += 1
		start += 25

if __name__ == "__main__":
	test_crawler(sys.argv[-1])
