from datetime import datetime, timedelta

#N = 8000000
N = 80000

date_N_days_ago = datetime.now() - timedelta(days=N)

print datetime.now()
print date_N_days_ago