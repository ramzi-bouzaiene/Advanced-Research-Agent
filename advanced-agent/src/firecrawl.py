import os

from firecrawl import FirecrawlApp, ScrapeOptions
from dotenv import load_dotenv

load_dotenv()

class FirecrawlService:
    def __init__(self):
        api_key = os.getenv("FIRECRAWL_API_KEY")
        if not api_key:
            raise EnvironmentError("Environment variable FIRECRAWL_API_KEY not set")
        self.app = FirecrawlApp(api_key=api_key)

    def search_companies(self, query: str, num_result: int = 5):
        try:
            result = self.app.search(
                query=f"{query} company pricing",
                limit=num_result,
                scrape_options=ScrapeOptions(
                    formats=["markdown"]
                )
            )
            return result
        except Exception as e:
            print(e)
            return []

    def scrape_company_pages(self, url: str):
        try:
            result = self.app.scrape_url(
                url,
                formats=["markdown"]
            )
            return result
        except Exception as e:
            print(e)
            return None

# Can add more tools here