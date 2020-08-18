# Time
Time complexity is O(n). Most logic are in RouteTrie insert and find methods both of which use for loop.

# Space
Space complexity is O(n * m). n is the number of URLS (depth of RouteTrie). m is the average length of unique path which is stored in each Node. 