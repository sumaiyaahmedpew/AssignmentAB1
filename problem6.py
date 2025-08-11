# problem_06.py

books = [
    (1, "Python Basics", "John Doe", 2020),
    (2, "Advanced Python", "Jane Smith", 2021),
    (3, "Data Science 101", "John Doe", 2019)
]

def search_by_author(author):
    return [b for b in books if b[2].lower() == author.lower()]

def search_by_year_range(start, end):
    return [b for b in books if start <= b[3] <= end]

# Helper function to get book title
def get_title(book):
    return book[1]

def sort_by_title():
    return sorted(books, key=get_title)

# Example usage
print(search_by_author("John Doe"))
print(search_by_year_range(2019, 2020))
print(sort_by_title())
