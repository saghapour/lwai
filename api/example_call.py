import requests
import json

req = requests.post('http://localhost:8088/ner/news_fa', \
    data={'data': json.dumps([{'_id':'123','text':'حسن روحانی'},{'_id':'456', 'text':'سجاد آقاپور'}])})
result = json.loads(req.content.decode('utf8'))
print(result)