from flask import Flask
from src.logger import logging
from src.exception import CustomException
import os,sys 

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    try:
        raise Exception('We are testing our custom exception file')
    
    except Exception as e:
        custom = CustomException(e,sys)
        logging.info(custom.error_message)
        logging.info("We are testing logging module")

        return "hello world"
    

try:
    pass
except Exception as e:
    raise CustomException(e,sys)


if __name__ == "__main__":
    app.run(debug=True)