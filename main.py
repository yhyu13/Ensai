if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Define subroutine.")
    parser.add_argument('--func', type=str, required=True,
                       help="""Select from 'train','sig_predict,'combo_predict' """)
    FLAGS = parser.parse_args()

    from dataset import *
    from network import *

    def train():
        execfile('train.py')

    def sig_predict():
        execfile('single_model_prediction.py')

    def combo_predict():
        execfile('combo_prediction.py')


    functions = {'train': lambda: train(),
                 'sig_predict': lambda: sig_predict(),
                 'combo_predict': lambda: combo_predict()}
                 
    functions[FLAGS.func]()
