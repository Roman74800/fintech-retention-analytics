import numpy as np
import pandas as pd
from pathlib import Path
rng = np.random.default_rng(42)
out = Path(__file__).resolve().parent / 'data'
out.mkdir(exist_ok=True)
users = pd.DataFrame({'user_id': np.arange(1, 5001), 'signup_month': rng.choice(pd.date_range('2025-01-01', periods=6, freq='MS'), 5000), 'channel': rng.choice(['organic','paid','referral'],5000,p=[.5,.3,.2])})
rows=[]
for u in users.itertuples(index=False):
    for m in pd.date_range(u.signup_month, '2025-12-01', freq='MS'):
        age=(m.year-u.signup_month.year)*12+m.month-u.signup_month.month
        prob=np.clip(.83*np.exp(-.115*age)+(.06 if u.channel=='referral' else 0),.1,.96)
        if rng.random()<prob:
            rows.append((u.user_id,m.date().isoformat(),int(rng.poisson(4)+1),round(float(rng.gamma(2,1200)),2)))
activity=pd.DataFrame(rows,columns=['user_id','activity_month','transactions','volume_rub'])
users.to_csv(out/'users.csv',index=False)
activity.to_csv(out/'monthly_activity.csv',index=False)
print('Saved',len(users),'users and',len(activity),'activity rows')
