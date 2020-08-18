class RouteTrie:
    def __init__(self, handler = None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, path, handler = None):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root

        path_list = path.split('/')

        if len(path_list) <= 1:
            return

        for p in path_list:
            if p in node.children:
                node = node.children[p]
            else:
                new_node = node.insert(p)
                node = new_node

        node.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if path[-1] == '/':
            path = path[:-1]

        path_list = path.split('/')

        node = self.root

        if len(path) <= 1:
            return node.handler

        for p in path_list:
            if p in node.children:
                node = node.children[p]
            else:
                return None

        return node.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, sub_path, handler = None):
        # Insert the node as before
        new_node = RouteTrieNode(handler)
        self.children[sub_path] = new_node
        return new_node


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root = RouteTrie(handler)
        self.not_found_handler = not_found_handler 

    def add_handler(self, path, handler):
        # Add a handler for a path
        self.root.insert(path, handler)


    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        handler = self.root.find(path)

        if handler:
            return handler
        else:
            return self.not_found_handler




# create the router and add a route
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler'
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler'
print(router.lookup("/home/about/me")) # should print 'not found handler'