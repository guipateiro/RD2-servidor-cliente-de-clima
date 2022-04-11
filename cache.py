from datetime import datetime, timedelta

class Cache():
    def __init__(self):
        self.cache_table = {}

    def add_data_cache(self, server, temperature):
        timeout = self.set_timeout()
        self.cache_table.update({server: {"temperature": temperature, "timeout": timeout}})

    def set_timeout(self):
        timeout = 30
        return datetime.now() + timedelta(seconds=timeout)

    def check_timeout(self, timeout):
        if timeout > datetime.now():
            return True
        else:
            return False
