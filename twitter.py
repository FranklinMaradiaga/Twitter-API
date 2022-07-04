from pytwitter import Api
from cryptography.x509 import load_pem_x509_certificate
import pandas as pd
import sqlalchemy as db

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAGBLeQEAAAAAaHebLkgV5Z9RTfB9uh1u%2FZp3iKo%3DVVj15lNsi2yfas" \
               "lS0l6CffwelmWPUCvNN4efJOfiRTxc7h9AeZ"

my_api = Api(bearer_token=BEARER_TOKEN)

# This should return a dictionary of the follow
# The parameters should all be of type list([])
def get_dict(ids, names, usernames):

    dict = {
        'ids': ids,
        'names': names,
        'usernames': usernames
    }

    return dict

# This should return a dictionary by calling the get_dict
# The id must be a of type string and max_users should be of type int 
def get_following_users(id, max_users):
    response = my_api.get_following(user_id=id, max_results=max_users)
    ids = []
    names = []
    usernames = []

    for data in response.data:
        ids.append(data.id)
        names.append(data.name)
        usernames.append(data.username)

    return get_dict(ids, names, usernames)

# The info must be a dictionary to add to the database, d
# b_name, and table_name should be of type string
def create_database(info, db_name, table_name):

    data = pd.DataFrame.from_dict(followers)
    engine = db.create_engine('sqlite:///' + db_name + '.db')

    data.to_sql(table_name, con=engine, if_exists='replace', index=False)
    query_result = engine.execute("SELECT * FROM " + table_name + ";").fetchall()
    print(pd.DataFrame(query_result), "\n")


followers = get_following_users("44196397", 5)
create_database(followers, "Twitter", "followers")
