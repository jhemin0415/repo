import os
from pywebpush import webpush, WebPushException


VAPID_PRIVATE_KEY = open('./vapid_private.pem', "r+").readline().strip("\n")
VAPID_PUBLIC_KEY = open('./vapid_public.pem', "r+").read().strip("\n")
def send_web_push(subscription_information, message_body):
    return webpush(
        subscription_info = subscription_information,
        data = message_body,
        vapid_private_key=VAPID_PRIVATE_KEY,
        )
subscription_information = ''
send_web_push(subscription_information,'hello_world')
