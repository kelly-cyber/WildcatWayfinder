import logging

import azure.functions as func
import data_manager as DataManager

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    DataManager.initialize()
    if req.method == 'POST':
        try:
            req_body = req.get_json()
            result = DataManager.create(req_body)
            return func.HttpResponse(str(result), status_code=200) #request processed
        except ValueError:
            return func.HttpResponse("Invalid input.", status_code=400) #error
    else:
        return func.HttpResponse(
             "This HTTP triggered function only supports POST method.",
             status_code=400
        )
    