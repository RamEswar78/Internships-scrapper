import scrapy


class InternshalaSpider(scrapy.Spider):
    name = "internshala"
    allowed_domains = ["internshala.com"]
    start_urls = [
        "https://internshala.com/internships/ai-agent-development,artificial-intelligence-ai,backend-development,front-end-development,full-stack-development,javascript-development,python-django,software-development,web-development-internship/"
    ]

    def parse(self, response):
        jobs = response.css("div.internship_meta")
        for job in jobs:
            yield {
                "title": job.css("#job_title::text").get(),
                "company": job.css(".company-name::text").get(),
                "location": job.xpath('.//i[@class="ic-16-pin"]/following-sibling::span/text()').get(),
                "duration": job.xpath('.//i[@class="ic-16-time"]/following-sibling::span/text()').get(),
                "stipend":  job.xpath('.//i[@class="ic-16-money"]/following-sibling::span/text()').get(),
                "posted_on": job.xpath('.//i[@class="ic-16-reschedule"]/following-sibling::span/text()').get(),
                "apply_link": "https://internshala.com" + job.css(".job-title-href::attr(href)").get(),
            }

        # find next page link
        next_page = response.css("a.next_page::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
