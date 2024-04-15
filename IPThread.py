from tradingview_scraper import Ideas

obj = Ideas().scraper(symbol: str = None,
                      startPage: int = 1,
                      endPage: int = 2,
                      to_csv: bool = False,
                      return_json: bool = False)
print(obj)