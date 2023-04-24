import os
import yaml
import pandas as pd
import argparse

def read_params(config_path):              #opens and returns the params.yaml contents
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def get_data(config_path):
    config = read_params(config_path)
    # print(config)
    data_path = config["data_source"]["s3_source"]              #we need the data source  key which is present params.yaml 
    df = pd.read_csv(data_path, sep=",", encoding='utf-8')
    return df        #use print if you wanna view the df using command line using :  python src/get_data.py <params.yaml path>
                                                                        # its okay if we do not give params.yaml path as we gave default=params.yaml in args.add_argument(line 23)



if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")     # adds the command line argument to provide, here our argument is config file path ie. params.yaml path,but we since we gave default=prams.yaml,its not necessary to give the file path of params.yaml
                                                        
    parsed_args = args.parse_args()      #parser.parse_args() instructs parser to process and validate the command-line input
    data=get_data(config_path=parsed_args.config)