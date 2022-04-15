from datetime import datetime, timedelta

class Cache():
    def __init__(self):
        self.cache_table = {"alaska":{}, "saara":{}, "antartida":{}}

    def add_data_cache(self, chave, temperature):
        timeout = self.set_timeout()
        self.cache_table[chave].update({"temperature": temperature})#, "timeout": timeout})
        return timeout

    def set_timeout(self):
        timeout = 30
        return datetime.now() + timedelta(seconds=timeout)

    def check_timeout(self, timeout):
        if timeout < datetime.now():
            return True
        else:
            return False