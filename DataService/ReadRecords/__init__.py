import logging #a python module - logs something into either console or file

import azure.functions as func
import data_manager
from bson import json_util

def main(req: func.HttpRequest) -> func.HttpResponse: #when there is an HTTP request, the following code gets run
    logging.info('Python HTTP trigger function processed a request.') #generates in the HTTP webpage
    data_manager.initialize()
    if req.method == 'GET': #changed from 'POST'
        try:
            req_body = req.params.get("query") #return one query 
            result = data_manager.read(req_body) #result is a list
            # return func.HttpResponse(str(result), status_code=200) #only one doc is returned
            return func.HttpResponse(json_util.dumps(result), status_code = 200)
        except :
            result = data_manager.read({}) #empty curly bracket means it will return all documents in collection
            # return func.HttpResponse(str(result), status_code=200) #all docs are returned
            return func.HttpResponse(json_util.dumps(result), status_code = 200)
    else:
        return func.HttpResponse(
             "This HTTP triggered function only supports POST method.",
             status_code=400
        )
 