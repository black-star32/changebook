"""
 Created by 七月 on 2017/12/16.
"""
from app.libs.enums import PendingStatus

class DriftCollection:
    def __init__(self, drifts, current_user_id):
        self.data = []
        self.__parse(drifts, current_user_id)

    def __parse(self, drifts, current_user_id):
        for drift in drifts:
            temp = DriftViewModel(drift, current_user_id)
            self.data.append(temp.data)

class DriftViewModel:

    def __init__(self, drift, current_user_id):
        self.data = {}

        self.data = self.__pase(drift, current_user_id)

    @staticmethod
    def request_or_gifter(drift, currenr_user_id):
        if drift.requester_id == currenr_user_id:
            you_are = 'requester'
        else:
            you_are = 'gifter'
        return you_are


    def __pase(self, drift, currenr_user_id):
        you_are = self.request_or_gifter(drift, currenr_user_id)
        pending_status = PendingStatus.pending_str(drift.pending, you_are)
        r = {
            'you_are': you_are,
            'drift_id': drift.id,
            'book_title': drift.book_title,
            'book_author': drift.book_author,
            'book_img': drift.book_img,
            'operator': drift.requester_nickname if you_are != 'requester' \
                else drift.gifter_nickname,
            'date': drift.create_datetime.strftime('%Y-%m-%d'),
            'message': drift.message,
            'address': drift.address,
            'recipient_name': drift.recipient_name,
            'mobile': drift.mobile,
            'status': drift.pending,
            'status_str': pending_status
        }
        return r
