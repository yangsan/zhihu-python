# -*- coding: utf8 -*-
import pyCookieCheat
import requests
from zhihu import Question
from zhihu import Answer
from zhihu import User
from zhihu import Collection

if __name__ == "__main__":
    #s = requests.Session()
    #dict_cookie = pyCookieCheat.chrome_cookies("http://zhihu.com")
    #requests.utils.add_dict_to_cookiejar(s.cookies, dict_cookie)

    #r = s.get("http://www.zhihu.com", cookies = dict_cookie)
    ##print s.cookies

    ##print s.cookies

    ###r = s.get("http://www.weibo.com", cookies = dict_cookie)
    ##r = s.get("http://i.baidu.com", cookies=dict_cookie)
    ##print r.text.encode("utf8")
    #r1 = s.get("http://www.zhihu.com/people/liuniandate", cookies = dict_cookie)
    #print r1.text.encode("utf8")


    #url = "http://www.zhihu.com/people/liuniandate"
    url = "http://www.zhihu.com/people/WxzxzW"
    user = User(url)
    #print user.get_user_id()
    for an in user.get_answers():
        print an.get_upvote()
