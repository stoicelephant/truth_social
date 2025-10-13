from datetime import datetime, timezone
from api import Api

api = Api()

dt_p = api.pull_statuses(
    username='realDonaldTrump',
    replies=True,
    verbose=True,
    created_after=datetime(2025,10,13,tzinfo=timezone.utc)
)

for p in dt_p:
    print(p['created_at'])
    content_text= p['content']
    print(content_text)
