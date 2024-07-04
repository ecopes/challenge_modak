on the application file, you have two functions
1) get_notifications_to_send():
  there you can put the examples you want to test the application, I added a first boolean parameter to test if the application is working correctly, on the other function is testing if the message was sent or not depends on this boolean

2) do_run():
  here is actually running, is creating a dict with the different user_ids (because I didn't use a database) and sending the notifications



if you want to add more notification types, do the following:
go to file constants.py , add the constant name you want
then go to file models.py , at the bottom you have dict "DEFAULT_NOTIFICATIONS" that is used instead of a database 

for example 
constants.py -> add NOTIFICATION_NAME_NEW_NOTIFICATION = "NEW_NOTIFICATION"
models.py -> on DEFAULT_NOTIFICATIONS add -> const.NOTIFICATION_NAME_NEW_NOTIFICATION: NotificationTypeManager(name=const.NOTIFICATION_NAME_NEW_NOTIFICATION, amount=2, time_limit_in_seconds=const.SECONDS_IN_HOUR)
application.py -> on get_notifications_to_send() add -> (True, const.NOTIFICATION_NAME_NEW_NOTIFICATION, "user2", "1 new_notification for user2"), or whatever you want to add
