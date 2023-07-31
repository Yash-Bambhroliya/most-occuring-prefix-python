# most-occuring-prefix-python
# Word Prefix Counter

This Python script counts the prefixes of every word in a given paragraph, excluding special characters and single characters, and finds the top three longest prefixes with the highest occurrence.

## How It Works

1. The script takes a paragraph as input (hardcoded in the `main` function for demonstration purposes).
2. It tokenizes the paragraph into individual words and removes any special characters (punctuation marks) from each word.
3. For each word, it calculates all possible prefixes (excluding the word itself) and stores them in a dictionary along with their occurrence count.
4. The dictionary is then sorted first by the length of prefixes (in descending order) and then by their occurrence count (in descending order).
5. The top three longest prefixes with the highest occurrence are stored in a separate dictionary.
6. The script prints the top three most occurring prefixes by count regardless of their length and the top three longest prefixes with their highest occurrence.

## How to Use

1. Clone the repository or copy the Python code from the provided snippet into a Python (.py) file.
2. Run the Python script using a Python interpreter (e.g., `python word_prefix_counter.py`).
3. The script will display the top three most occurring prefixes and the top three longest prefixes in the provided paragraph.

## Note

- The paragraph can be modified in the `main` function to test with different input.

Feel free to use and modify the code according to your needs. If you have any questions or suggestions, please feel free to reach out.
