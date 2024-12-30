import json
import sys
import os

DATASETS_TO_PROCESS_FILEPATH = '/workdir/raw-images'

def detemineDatasetsToRun():
        json.dump(os.listdir('workdir'), sys.stdout)

detemineDatasetsToRun()