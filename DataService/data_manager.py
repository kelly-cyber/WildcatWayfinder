import pymongo
import sys
import certifi

"""
This is a reST style.

:param param_1: this is the first parameter
:param param_2: this is the second parameter
:returns: this is a description of what is returned
:raises keyError: raises an exception

"""

# use a global variable to store your collection object
mycol = None

"""
Connect to the local MongoDB server, database, and collection.

"""
def initialize():
    # specify that we are using the global variable mycol
    global mycol
    
    # connect to your local mongoDB server
    # my_client = pymongo.MongoClient ("mongodb://localhost:27017/", serverSelectionTimeoutMS=5000)
    
    # auth_str = "kellyocean123:FLKpyPGyxpyPnWPq"
    # # URL will be something like your_username.combination_of_nums_letters.mongodb.net
    # # conn_url = "cluster0.6yf67on.mongodb.net"
    # conn_url = "cluster0.6yf67on.mongodb.net/?retryWrites=true&w=majority"
    # conn_str = f"mongodb+srv://{auth_str}@{conn_url}"
    my_client = pymongo.MongoClient("mongodb+srv://kellyocean123:FLKpyPGyxpyPnWPq@cluster0.6yf67on.mongodb.net/?retryWrites=true&w=majority", tls=True, tlsCAFile=certifi.where())

    # use the conn_str to connect to your MongoDB Atlas cluster
    # my_client = pymongo.MongoClient(conn_str)
    
    my_database = my_client["exampleCluster"]
    mycol = my_database['atlasCollection']


    # check for a successful connection
    # try:
    #     my_client.server_info()
    # except pymongo.errors.ServerSelectionTimeoutError as err:
    #     print("Connection timed out, please check if your mongod is running!")
    #     sys.exit(1)

    # # create a database named 'mydatabase'
    # my_database = my_client["mydatabase"]

    # # create a collection named 'mycollection'
    # mycol = my_database['mycollection']


"""
Drop the collection and reset global variable mycol to None.

"""
def reset():
    # specify that we are using the global variable mycol
    global mycol

    # Drop the collection
    mycol.drop()
    # Reset global variable mycol to None
    mycol = None

"""
Insert document(s) into the collection.

:param document: a Python list of the document(s) to insert
:returns: result of the operation

"""
def create(document):
    
    mycol.insert_one(document)
    print("Created document")
    return str(mycol.inserted_ids) #returns list


"""
Retrieve document(s) from the collection that match the query,
if parameter one is True, retrieve the first matched document,
else retrieve all matched documents.

:param query: a Python dictionary for the query
:param one: an indicator of how many matched documents to be retrieved, by default its value is False
:returns: all matched document(s)

"""
def read(query, one=False):
    # Retrieve document(s) from the collection that match the query
        
    if one:
        # Retrieve the first matched document
        result = mycol.find_one(query) #return a dict
    else:
        # Retrieve all matched documents
        result = mycol.find(query) #return cursor method
    return list(result)
        


"""
Update document(s) that match the query in the collection with new values.

:param query: a Python dictionary for the query
:param new_values: a Python dictionary with updated data fields / values
:returns: result of the operation

"""
def update(query, new_values):

    try:
        update_result = mycol.update_one(query, {"$set": new_values})
        print("Updated", update_result.modified_count, "documents")
        return str(True)
    except ValueError:
        print("update did not work")
        return str(False)



"""
Remove document(s) from the collection that match the query.

:param query: a Python dictionary for the query
:returns: result of the operation

"""
def delete(query):
    
    delete_result = mycol.delete_many(query)
    print("Deleted", delete_result.deleted_count, "documents")
    return str(delete_result)


if __name__ == "__main__":
    # sample tests
    initialize()

    # create({"title":"test", "message":"testing 1 2"})
    # create({"title":"test", "message":"testing 8 9"})

    create({"name":"Alice", "age":"30", "city": "New York"})
    create({"name":"Bob", "age":"25", "city": "Los Angeles"})
    create({"name":"Charlie", "age":"22", "city": "Chicago"})
    
    
    # doc = read({}, one=True)
    # print(doc)

    # update({'title':'test'}, {'message':"testing 3 4"})
    # doc = read({}, one=True)
    # print(doc)

    # delete({'title':'test'})

    # reset()