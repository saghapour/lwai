class BaseNER:
    def __init__(self, platform: str):
        self._test = 10

    def get(self, data: list) -> list:
        result = []
        for d in data:
            result.append({'_id': d['_id'], 'pos': ['sala', 'tala']})
        return result