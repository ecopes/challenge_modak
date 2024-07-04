import constants as const
from models import UserNotification


def get_notifications_to_send():
    # response a tuple of tuples, the tuple has to have 4 elements
    # 1: bool -> True if it should be sent or False otherwise
    # 2: str -> Notification name, you should use the constants
    # 3: str -> user_id
    # 4: str -> the notification text that is going to be sent
    return (
        (True, const.NOTIFICATION_NAME_STATUS, "user1", "1 status for user1"),
        (True, const.NOTIFICATION_NAME_STATUS, "user1", "2 status for user1"),
        (False, const.NOTIFICATION_NAME_STATUS, "user1", "3 status for user1"),
        (False, const.NOTIFICATION_NAME_STATUS, "user1", "4 status for user1"),
        (True, const.NOTIFICATION_NAME_NEWS, "user1", "1 news for user1"),
        (False, const.NOTIFICATION_NAME_NEWS, "user1", "2 news for user1"),
        (True, const.NOTIFICATION_NAME_MARKETING, "user1", "1 marketing for user1"),
        (True, const.NOTIFICATION_NAME_MARKETING, "user1", "2 marketing for user1"),
        (False, const.NOTIFICATION_NAME_MARKETING, "user1", "3 marketing for user1"),
        (True, const.NOTIFICATION_NAME_STATUS, "user2", "1 status for user1"),
        (True, const.NOTIFICATION_NAME_STATUS, "user2", "2 status for user1"),
        (False, const.NOTIFICATION_NAME_STATUS, "user2", "3 status for user1"),
        (False, const.NOTIFICATION_NAME_STATUS, "user2", "4 status for user1"),
        (True, const.NOTIFICATION_NAME_NEWS, "user2", "1 news for user1"),
        (False, const.NOTIFICATION_NAME_NEWS, "user2", "2 news for user1"),
        (True, const.NOTIFICATION_NAME_MARKETING, "user2", "1 marketing for user1"),
        (True, const.NOTIFICATION_NAME_MARKETING, "user2", "2 marketing for user1"),
        (False, const.NOTIFICATION_NAME_MARKETING, "user2", "3 marketing for user1"),
    )


def do_run():
    users = {}
    for should_be_send, notification_name, user_id, notification_text in get_notifications_to_send():
        users[user_id] = users.get(user_id, UserNotification(user_id=user_id))
        was_sent = users[user_id].send_notification(notification_name=notification_name,
                                                    notification_text=notification_text)
        assert (should_be_send == was_sent)


do_run()
