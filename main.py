from dataset import *
from network import *

import argparse


def train():
    execfile('train.py')


def sig_predict():
    execfile('single_model_prediction.py')


def combo_predict():
    execfile('combo_prediction.py')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Define subroutine.")
    parser.addArgument('--func', type=str,
                       help="""Select from 'train','sig_predict,'combo_predict' """)
    FLAGS = parser.parse_args()

    functions = {'train': lambda: train,
                 'sig_predict': lambda: sig_predict,
                 'combo_predict': lambda: combo_predict}

    functions[FLAGS.func]()
