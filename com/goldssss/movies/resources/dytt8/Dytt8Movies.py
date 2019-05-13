import urllib3
import requests
from idna import unicode

from com.goldssss.movies.config import MoviesConfig
from com.goldssss.movies.resources.SelectMovies import SelectMovies


class Dytt8(SelectMovies):
    url = "http://s.ygdy8.com/plus/so.php?typeid=1&"
    # 电影天堂搜索逻辑
    def selectMovies(self,name):
        print("ddty select movie >>> " + name)
        url = MoviesConfig.dytt8Url + urllib3.util.url.quote(name.encode(MoviesConfig.dytt8UrlEncoding))
        urllib3.disable_warnings()
        dyttResponse = urllib3.PoolManager().request(MoviesConfig.httpRequestGet,url)
        print(dyttResponse.data)




#
ddty = Dytt8()
ddty.selectMovies(name='中文')
#
# s = '\xc5\xb7\xc3\xc0\xb5\xe7\xca\xd3'
# ss = s.encode('raw_unicode_escape')
#
# print(ss.decode())