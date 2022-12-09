from flask import Flask
import sys
from housing.logger import logging
from housing.exception import HousingExceptions

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        raise HousingExceptions(e,sys) from e
        #housing = HousingExceptions(e, sys)
        logging.info(housing.error_message)
        logging.info("we are tesing the logging module")
    return "Starting Machine Learning Project"



if __name__=="__main__":
    app.run(debug=True)