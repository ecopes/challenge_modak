import copy
import datetime

import constants as const


class NotificationTypeManager:
    name: str
    call_amount: int
    time_limit_in_seconds: int
    first_call: datetime.datetime
    remain_calls: int

    def __init__(self, name: str, amount: int, time_limit_in_seconds: int):
        self.name = name
        self.call_amount = amount
        self.time_limit_in_seconds = time_limit_in_seconds
        self.first_call = datetime.datetime.now()
        self.remain_calls = amount

    def do_call(self, user_id: str, notification_text: str) -> bool:
        # return True if the call can be done, otherwise False
        if not self._call_can_be_done():
            return False
        # here you have to put the code of the real call, depends on the notification type,
        # so you should user user_id and notification_text
        return True

    def _call_can_be_done(self) -> bool:
        now = datetime.datetime.now()
        if (self.first_call + datetime.timedelta(
                seconds=self.time_limit_in_seconds)) < now:
            self.remain_calls = self.call_amount
            self.first_call = now
        if self.remain_calls > 0:
            self.remain_calls -= 1
            return True
        return False


class UserNotification:
    user_id: str
    notifications: {}

    def __init__(self, user_id: str):
        self.user_id = user_id
        self.notifications = copy.deepcopy(DEFAULT_NOTIFICATIONS)

    def send_notification(self, notification_name: str, notification_text: str) -> bool:
        sent = self.notifications.get(notification_name).do_call(user_id=self.user_id,
                                                                 notification_text=notification_text)
        print("--------------------")
        print("CORRECT SENT") if sent else print("INCORRECT SENT")
        print(f"user_id: {self.user_id}")
        print(f"notification_name: {notification_name}")
        print(f"notification_text: {notification_text}")
        print("--------------------")
        return sent


# this should be saved on the database instead of a dict
DEFAULT_NOTIFICATIONS = {
    const.NOTIFICATION_NAME_STATUS: NotificationTypeManager(name=const.NOTIFICATION_NAME_STATUS, amount=2,
                                                            time_limit_in_seconds=const.SECONDS_IN_MINUTE),
    const.NOTIFICATION_NAME_NEWS: NotificationTypeManager(name=const.NOTIFICATION_NAME_NEWS, amount=1,
                                                          time_limit_in_seconds=const.SECONDS_IN_DAY),
    const.NOTIFICATION_NAME_MARKETING: NotificationTypeManager(name=const.NOTIFICATION_NAME_MARKETING, amount=2,
                                                               time_limit_in_seconds=const.SECONDS_IN_HOUR)
}
