from housing.pipeline.pipeline import Pipeline
from housing.pipeline.predict_pipeline import Predictpipeline

def main():
    #pipeline=Pipeline()
    #pipeline.run_pipeline()
    predict_obj=Predictpipeline()
    predict_obj.predict()


if __name__=="__main__":
    main()