class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.author = book['author']
        self.publisher = book['publisher']
        self.image = book['image']
        self.price = book['price']
        self.summary = book['summary']
        self.pages = book['pages']

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False,
                        [self.author, self.publisher, self.price])
        return '/'.join(intros)

class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, book, keyword):
        self.total = book.total
        self.keyword = keyword
        self.books = [BookViewModel(bk['data']) for bk in book.books]



class _BookViewModel:
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_detail(data['data'])]
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls.__cut_book_detail(book) for book in data['books']]
        return returned

    @classmethod
    def __cut_book_detail(cls, data):
        book = {
            'title': data['title'],
            'author': data['author'],
            # 'author': '、'.join(data['author']),
            # 'binding': data['binding'],
            'publisher': data['publisher'],
            'image': data['image'],
            'price': data['price'],
            # 'isbn': data['isbn'],
            # 'pubdate': data['pubdate'],
            'summary': data['summary'] or '',
            'pages': data['pages'] or ''
        }
        return book
