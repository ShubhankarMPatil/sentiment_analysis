from datasets import load_dataset
import os

#Set the local directory for cache of the dataset
cache_dir = os.path.join(os.getcwd(), 'datasets_cache')

# Load the IMDb dataset
dataset = load_dataset("imdb", cache_dir = cache_dir)

# Print a sample from the dataset
print(dataset['train'][0])
