from collections import namedtuple

from app.view_models.book import BookViewModel

# MyGift = namedtuple('MyGift', ['id', 'book', 'wishes_count'])

class MyWishes:
    def __init__(self, gifts_of_mine, wish_count_list):
        self.gifts = []

        self._gifts_of_mine = gifts_of_mine
        self._wish_count_list = wish_count_list

        self.gifts = self._parse()


    def _parse(self):
        temp_gifts = []
        for gift in self._gifts_of_mine:
            my_gift = self._matching(gift)
            temp_gifts.append(my_gift)
        return temp_gifts


    def _matching(self, gift):
        count = 0
        for wish_count in self._wish_count_list:
            if gift.isbn == wish_count['isbn']:
                count = wish_count['count']
        r = {
            'wishes_count':count,
            'book':BookViewModel(gift.book),
            'id':gift.id
        }
        return r
        # my_gift = MyGift(gift.id, BookViewModel(gift.book), count)
        # return my_gift


# class MyGift:
#     def __init__(self):
#         pass
