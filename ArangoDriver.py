from arango import ArangoClient

#Singelton Class
class ArangoDriver:
    __instance = None
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if ArangoDriver.__instance == None:
            ArangoDriver()
        return ArangoDriver.__instance
    
    def __init__(self):
        """ Virtually private constructor. """
        if ArangoDriver.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            ArangoDriver.__instance = self

        self.client = ArangoClient(hosts="http://localhost:8555")

        self.db = self.client.db("gaming-manager", username="root", password="1234")

        collection_names = ["players", "teams", "tournaments"]

        for collection in collection_names:
            if not self.db.has_collection(collection):
                self.db.create_collection(collection)

        if not self.db.has_collection("matches"):
            self.db.create_collection("matches", edge=True)    
        
    def addDocument(self, document, collection_name):
        collection = self.db.collection(collection_name)
        collection.insert(document)

    def deleteDocument(self, document, collection_name):
        collection = self.db.collection(collection_name)
        collection.delete(document)

    def updateDocument(self, document, collection_name):
        collection = self.db.collection(collection_name)
        collection.update(document)       
