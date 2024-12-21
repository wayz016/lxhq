from wxauto import WeChat
import wxauto
import time
import datetime
import sys


def send_message(wx, who, msg):
    wx.SendMsg(msg, who)
    print(f"已向 {who} 发送消息：{msg}")


def main():
    wx = WeChat()
    who = '榔盛槟榔¥萧剑徽'

    while True:
        now = datetime.datetime.now()
        current_time = now.time()
        current_hour = current_time.hour
        current_minute = current_time.minute

        if current_minute == 0 or current_minute == 30:
            if 0 <= current_hour < 5:
                msg = '萧老板凌晨好[玫瑰]'
                send_message(wx, who, msg)
            elif 5 <= current_hour < 11:
                msg = '萧老板早上好[玫瑰]'
                send_message(wx, who, msg)
            elif 11 <= current_hour < 13:
                msg = '萧老板中午好[玫瑰]'
                send_message(wx, who, msg)
            elif 13 <= current_hour < 17:
                msg = '萧老板下午好[玫瑰]'
                send_message(wx, who, msg)
            elif 17 <= current_hour < 24:
                msg = '萧老板晚上好[玫瑰]'
                send_message(wx, who, msg)

        time.sleep(45)


if __name__ == "__main__":
    main()
