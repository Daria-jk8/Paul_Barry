# --> py.test --pep8 vsearch.py
# --> pycodestyle vsearch.py

def search4vowels(phrase: str) -> set:
    """Prints the vowels found in the specified word"""
    """Returns any vowels found in a supplied phrase.""" 
    vowels = set('aeiou')
     # word = input("Provide a word to search for vowels: ")
    return vowels.intersection(set(phrase))
      

def search4letters(phrase: str, letters: str='aeiou') -> set: # add two arguments with an annotation
    """Returns a set of the 'letters' found in 'phrase'. """
    return set(letters).intersection(set(phrase))
