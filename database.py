import datetime
import pymongo

class Sessions:
    
    def __init__(self, uri, database_name):
        self._client = pymongo.MongoClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users
    def new_user(self, id, token, username):
        return dict(
            id = id,
            bottoken = token,
            username = username,
            join_date = datetime.date.today().isoformat()
        )
    def add_bot(self, id, token, username):
        user = self.new_user(id, token, username)
        self.col.insert_one(user)
    def is_user_exist(self, id):
        user = self.col.find_one({'id':int(id)})
        return True if user else False
    #async def total_users_count(self):
        #count = await self.col.count_documents({})
        #return count
    def get_user(self, id):
        user = self.col.find_one({'id':int(id)})
        print (user)
        return user
    def get_bot(self, token):
        user = self.col.find_one({'bottoken':token})
        print (user)
        return user
    def delete_session(self, user_id):
        self.col.delete_one({'id': int(user_id)})
