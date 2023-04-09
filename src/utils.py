import os
import sys
import pandas as pd
import numpy as np
import dill
from src.exception import CustomException

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok= True)
        with open(file=file_path, mode= "wb") as fileobj:
            dill.dump(obj,fileobj)

    except Exception as e:
        raise CustomException(e,sys)