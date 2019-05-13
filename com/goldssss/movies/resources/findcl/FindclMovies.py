import urllib

from com.goldssss.movies.config import MoviesConfig
from com.goldssss.movies.resources.SelectMovies import SelectMovies


class Dytt8(SelectMovies):
    # 傻逼吧  https://www.findcl.co/
    def selectMovies(self,name):
        print("findcl select movie >>> " + name)
        print(MoviesConfig.dytt8Url + urllib.quote(name))
        response1 = urllib.urlopen(MoviesConfig.dytt8Url + urllib.quote(name))

