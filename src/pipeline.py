import os
from clean import clean_data
from preprocess import preprocess

RAW = "PlantVillage"
PROCESSED = "processed"

if __name__ == "__main__":
    print("Current working dir:", os.getcwd())
    print("Check path:", os.path.exists(RAW))

    print("=== CLEAN DATA ===")
    clean_data(RAW)

    print("=== PREPROCESS ===")
    preprocess(RAW, PROCESSED)

    print("DONE!")