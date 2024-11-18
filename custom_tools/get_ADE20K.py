import openxlab
from openxlab.dataset import get

import argparse

def get_args_parser():
    parser = argparse.ArgumentParser(add_help=False)
    
    parser.add_argument("--ak")
    parser.add_argument("--sk")
    
    return parser

def main(args):
    openxlab.login(ak=args.ak, sk=args.sk) # Log in and enter the corresponding AK/SK.
    
    get(dataset_repo='OpenDataLab/ADE20K_2016', target_path='data/ade/ADEChallengeData2016') # Dataset download

if __name__ == '__main__':
    parser = argparse.ArgumentParser(parents=[get_args_parser()])
    
    args = parser.parse_args()
    
    main(args)