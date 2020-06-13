from enum import Enum

class PendingStatus(Enum):
    """交易状态"""
    Waiting = 1
    Success = 2
    Reject = 3
    Redraw = 4

    @classmethod
    def pending_str(cls, status, key):
        key_map = {
            cls.Waiting.value: {
                'requester': '等待对方邮寄',
                'gifter': '等待你邮寄'
            },
            cls.Reject.value: {
                'requester': '对方已拒绝',
                'gifter': '你已拒绝'
            },
            cls.Redraw.value: {
                'requester': '你已撤销',
                'gifter': '对方已撤销'
            },
            cls.Success.value: {
                'requester': '对方已邮寄',
                'gifter': '你已邮寄，交易完成'
            }
        }
        print(key_map)
        return key_map[status][key]


class GiftStatus(Enum):
    Waiting = 0
    Success = 1
    Redraw = 2
