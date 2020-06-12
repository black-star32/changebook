from app.view_models.book import BookViewModel


class TradeInfo:
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self._parse(goods)

    def _parse(self, goods):
        self.total = len(goods)
        self.trades = [self._map_to_trade(gift) for gift in goods]

    def _map_to_trade(self, single):
        if single.create_datetime:
            time = single.create_datetime.strftime('%Y-%m-%d')
        else:
            time = '未知'
        return dict(
            user_name=single.user.nickname,
            time=time,
            id=single.id
        )

class MyTrades:
    def __init__(self, trades_of_mine, trade_count_list):
        self.trades = []

        self._trades_of_mine = trades_of_mine
        self._trade_count_list = trade_count_list

        self.trades = self._parse()


    def _parse(self):
        temp_trades = []
        for trade in self._trades_of_mine:
            my_trade = self._matching(trade)
            temp_trades.append(my_trade)
        return temp_trades


    def _matching(self, trade):
        count = 0
        for wish_count in self._trade_count_list:
            if trade.isbn == wish_count['isbn']:
                count = wish_count['count']
        r = {
            'wishes_count':count,
            'book':BookViewModel(trade.book),
            'id':trade.id
        }
        return r
        # my_gift = MyGift(gift.id, BookViewModel(gift.book), count)
        # return my_gift
