import argparse

# create CLI argument parser
parser = argparse.ArgumentParser(description='A translation tool betwen language pair.')


# create diectionary
parser.add_argument('--config_file', type=str, default='config.yaml', help='Configuration file with model and API settings.')
parser.add_argument('--model_name', type=str, help='Name of the Large Language Model.')
parser.add_argument('--input_file', type=str, help='PDF file to translate.')
parser.add_argument('--output_file_format', type=str, help='The file format of translated book. Now supporting PDF and Markdown')
parser.add_argument('--source_language', type=str, help='The language of the original book to be translated.')
parser.add_argument('--target_language', type=str, help='The target language for translating the original book.')

# Get arguments
args = parser.parse_args()
print(args)
print(args.config_file)

