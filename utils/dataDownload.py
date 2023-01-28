import os
import requests

# Define the name and path of tiny shakespeare dataset
data_file_name = 'tiny_shakespeare.txt'
data_file_path = os.path.dirname(__file__)

# Download the tiny shakespeare dataset if not exist
defined_file_path = os.path.join(data_file_path, data_file_name)
if not os.path.exists(defined_file_path):
    data_url = 'https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt'
    
    with open(defined_file_path, 'w') as f:
        f.write(requests.get(data_url).text)

