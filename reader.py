# -*- coding: utf8 -*-
import dbmodel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    engine = create_engine("sqlite:///zhidu.db", echo=True)
    dbmodel.Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    #fuwocheng = session.query(dbmodel.Dbuser).filter(dbmodel.Dbuser.id=='fuwocheng').all()[0]
    answers = session.query(dbmodel.Dbanswer).filter(dbmodel.Dbanswer.user_id=='wonderful-vczh')
    upvotes = []
    for an in answers:
        upvotes.append(an.upvote)

    data = np.asarray(upvotes)
    plt.hist(data, bins=100, alpha=0.5)
    plt.show()
