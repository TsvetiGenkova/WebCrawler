import matplotlib.pyplot as plt
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from create_db import CrawlerData

engine = create_engine("sqlite:///crawler_data.db")
Session = sessionmaker(bind=engine)
session = Session()

result_dict = {}
tmp = session.query(CrawlerData.server).group_by(CrawlerData.server).all()
for i in tmp:
    if i[0] != None:
        q = session.query(CrawlerData).filter(CrawlerData.server == i[0]).count()
        result_dict.update({i[0]: q})


keys = list(result_dict.keys())
values = list(result_dict.values())

X = list(range(len(keys)))

plt.bar(X, list(result_dict.values()), align="center")
plt.xticks(X, keys)

plt.title(".bg servers")
plt.xlabel("Server")
plt.ylabel("Count")

plt.savefig("histogram.png")