# from app.service.gift import GiftService
from flask import render_template, config, current_app, request, url_for
# from flask_login import login_required, current_user
from sqlalchemy import desc

from app.models.gift import Gift
from app.view_models.book import BookViewModel
from . import web

# from app.models.gift import Gift



# def __current_user_status_change():
#     r = request


@web.route('/')
# @cache.cached(timeout=100, unless=__current_user_status_change)
# @cache.cached(timeout=100)
def index():
    recent_gifts = Gift.recent()
    books = [BookViewModel(gift.book) for gift in recent_gifts]
    return render_template('index.html', recent=books)

    pass
    # """
    #     首页视图函数
    #     这里使用了缓存，注意缓存必须是贴近index函数的
    # """
    # gift_list = GiftService.recent()
    # return render_template('index.html', recent=gift_list)


@web.route('/personal')
# @login_required
def personal_center():
    pass
    # return render_template('personal.html', user=current_user.summary)


