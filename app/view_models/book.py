class BookViewMode:
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_detail(data)]
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = len(data['books'])
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
            'image': data['images']['large'],
            'price': data['price'],
            # 'isbn': data['isbn'],
            # 'pubdate': data['pubdate'],
            'summary': data['summary'],
            'pages': data['pages']
        }
        return book
