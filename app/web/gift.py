# from app.libs.enums import PendingStatus
# from app.models.drift import Drift
from flask import render_template, flash, request, redirect, url_for, current_app
from flask_login import login_required, current_user
from sqlalchemy import desc, func

from app import db
from app.libs.enums import PendingStatus
from app.models.drift import Drift
from app.models.gift import Gift
from app.spider.change_book import ChangeBook
from app.view_models.gift import MyGifts
from app.view_models.trade import MyTrades
from . import web
# from app.spider.yushu_book import YuShuBook
# from app.view_models.gift import MyGifts
# from app.service.gift import GiftService

# from app.models import db
# from app.models.gift import Gift



@web.route('/my/gifts')
@login_required
def my_gifts():
    uid = current_user.id
    gifts_of_mine = Gift.get_user_gifts(uid)
    isbn_list = [gift.isbn for gift in gifts_of_mine]
    wish_count_list = Gift.get_wish_counts(isbn_list)
    view_model = MyTrades(gifts_of_mine, wish_count_list)
    return render_template('my_gifts.html', gifts=view_model.trades)
    # uid = current_user.id
    # gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(
    #     desc(Gift.create_time)).all()
    # wishes_count = GiftService.get_wish_counts(gifts)
    # view_model = MyGifts(gifts, wishes_count).package()
    # return render_template('my_gifts.html', gifts=view_model)


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
    else:
        flash('这本书已添加至你的赠送清单或已存在于你的心愿清单，请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))
    # yushu_book = YuShuBook()
    # yushu_book.search_by_isbn(isbn)
    # # gifting = Gift.query.filter_by(uid=current_user.id, isbn=isbn, status=1,
    # #                                launched=False).first()
    # # wishing = Wish.query.filter_by(uid=current_user.id, isbn=isbn, status=1,
    # #                                launched=False).first()
    # if current_user.can_save_to_list(isbn):
    #     # 既不在赠送清单，也不在心愿清单才能添加
    #     with db.auto_commit():
    #         gift = Gift()
    #         gift.uid = current_user.id
    #         gift.isbn = isbn
    #         # gift.book_id = yushu_book.data.id
    #         db.session.add(gift)
    #         current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
    # else:
    #     flash('这本书已添加至你的赠送清单或已存在于你的心愿清单，请不要重复添加')
    # return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
@login_required
def redraw_from_gifts(gid):
    gift = Gift.query.filter(Gift.id==gid, Gift.launched==False).first()
    drift = Drift.query.filter(Drift.gift_id==gid, Drift.pending==PendingStatus.Waiting).first()
    if not gift:
        flash('该书籍不存在，或已经交易，删除失败')
    elif drift:
        flash('这个礼物正处于交易状态，请先前往鱼漂完成该交易')
    else:
        with db.auto_commit():
            current_user.beans -= current_app.config['BEANS_UPLOAD_ONE_BOOK']
            gift.delete()
    return redirect(url_for('web.my_gifts'))

    # gift = Gift.query.filter_by(id=gid, launched=False).first()
    # if not gift:
    #     flash('该书籍不存在，或已经交易，删除失败')
    # drift = Drift.query.filter_by(gift_id=gid, pending=PendingStatus.waiting).first()
    # if drift:
    #     flash('这个礼物正处于交易状态，请先前往鱼漂完成该交易')
    # else:
    #     with db.auto_commit():
    #         current_user.beans -= current_app.config['BEANS_UPLOAD_ONE_BOOK']
    #         gift.delete()
    # return redirect(url_for('web.my_gifts'))
