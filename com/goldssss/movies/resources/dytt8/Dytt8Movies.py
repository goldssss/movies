import re
import urllib3
from bs4 import BeautifulSoup
from com.goldssss.movies.config import MoviesConfig
from com.goldssss.movies.resources.SelectMovies import SelectMovies

class Dytt8(SelectMovies):
    url = "http://s.ygdy8.com/plus/so.php?typeid=1&"
    # 电影天堂搜索逻辑
    def selectMovies(self,name):
        print('ddty select movie >>> ' + name)
        url = MoviesConfig.dytt8Url + urllib3.util.url.quote(name.encode(MoviesConfig.dytt8UrlEncoding))
        print('ddty select open url >>>' + url)
        urllib3.disable_warnings()
        dyttResponse = urllib3.PoolManager().request(MoviesConfig.httpRequestGet,url,headers={})
        soup = BeautifulSoup(dyttResponse.data)
        hrefs = soup.find_all('a')
        for a in hrefs:
            print(a)

ddty = Dytt8()
ddty.selectMovies(name='复仇者')