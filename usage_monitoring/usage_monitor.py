import smtplib
import sys
import json
import threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

try:
    from usage_monitoring.usage_monitor_credentials import UsageMonitorCredentials as Credentials
except ImportError:
    Credentials = None


class UsageMonitor:
    @classmethod
    def send_msg(cls, subject, msg_dict):
        try:
            if Credentials is not None:

                with smtplib.SMTP(Credentials.get("server"), Credentials.get("port")) as server:

                    server.starttls()
                    server.login(Credentials.get("mail"),
                                 Credentials.get("token"))

                    msg = MIMEMultipart()
                    msg['From'] = Credentials.get("mail")
                    msg['To'] = Credentials.get("mail")
                    msg['Subject'] = subject

                    msg.attach(MIMEText(json.dumps(msg_dict, indent=4), 'plain'))
                    server.send_message(msg)

        except Exception as err:
            pass

    @classmethod
    def new_log_msg_thread(cls, open_times, user_id):
        msg_dict = {"user_id": user_id,
                    "opening_times": open_times}

        cls.send_msg("GuitarTuner-LOG", msg_dict)

    @classmethod
    def new_log_msg(cls, open_times, user_id):
        try:
            new_thread = threading.Thread(daemon=True, target=cls.new_log_msg_thread, args=(open_times, user_id))
            new_thread.start()
        except Exception as err:
            pass