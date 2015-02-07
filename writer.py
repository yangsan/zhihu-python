# -*- coding: utf8 -*-
#from zhihu import Question
#from zhihu import Answer
from zhihu import User
#from zhihu import Collection

import dbmodel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    userid = "wonderful-vczh"

    # create db engine
    engine = create_engine("sqlite:///zhihu.db", echo=False)
    dbmodel.Base.metadata.create_all(engine)

    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    url_base = "http://www.zhihu.com/people/"
    url = url_base + userid

    zhihu_user = User(url)
    username = zhihu_user.get_user_id().decode("utf8")
    #print username

    db_user = dbmodel.Dbuser(id=userid, name=username)

    # add user
    session.add(db_user)
    session.commit()

    # add answers
    for i, answer in enumerate(zhihu_user.get_answers()):
        print i
        session.add(dbmodel.Dbanswer(id=answer.answer_url,
                    upvote=answer.get_upvote(),
                    content=answer.get_content().decode("utf8"),
                    user_id=userid))
        session.commit()
