import threading

from Data.main import main

class EmailThread(threading.Thread):
    def __int__(self,no_of_delay):
        self.no_of_delay=no_of_delay
        threading.Thread.__int__(self)

    def run(self):
        try:
            print('Thread Execution started')
            main(self.no_of_delay)
        except Exception as e:
            print(str(e))