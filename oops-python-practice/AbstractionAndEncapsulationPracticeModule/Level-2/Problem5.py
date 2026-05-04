# problem 5 
# abstract notification system 

from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send_notification(self, msg):
        pass

class Emailnot(Notifier):
    def send_notification(self, msg):
        print("Email sent:", msg)

class SMSnot(Notifier):
    def send_notification(self, msg):
        print("SMS sent:", msg)

notifiers = [Emailnot(), SMSnot()]

for n in notifiers:
    n.send_notification("Server down!")