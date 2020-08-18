# The solution to this problem is in Trie.ipynb file. Jupyter Notebook file.
# I copied the solution here because for some reason it was not graded by submission.



## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = dict()
    
    def insert(self, char):
        ## Add a child node in this Trie
        new_node = TrieNode()
        self.children[char] = new_node
        return new_node
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root
        
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = node.insert(char)
                node = new_node
        
        node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root
        
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return None
            
        return node

class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = dict()
    
    def insert(self, char):
        ## Add a child node in this Trie
        new_node = TrieNode()
        self.children[char] = new_node
        return new_node
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        suffixes = list()
        
        def find_suffix(node, string = ''):
            if node.is_word:
                suffixes.append(string)
                
            for char in node.children:
                find_suffix(node.children[char], string + char)
                
        find_suffix(self)
        
        return suffixes


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');