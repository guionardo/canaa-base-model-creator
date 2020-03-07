import argparse
# from create_models.model_creator import ModelCreator

parser = argparse.ArgumentParser(description='Canaa model creator.')
parser.add_argument('--file', '-f', dest='file_name', help='model metadata file', required=True)
parser.add_argument('--destiny', '-d', dest='destiny_folder', help='destiny folder', required=True)
args = parser.parse_args()
if not args.file_name or not args.destiny_folder:
    parser.print_help()
    exit(0)

