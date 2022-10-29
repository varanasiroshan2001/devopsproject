import requests
def create_user(): 
  headers={"authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2NjY4MTk2NDkuMzYwNzE4LCJleHAiOjE2OTg0NDU2NDkuMzYwNzE4LCJ1c2VyX2lkIjoiY2RjMGFkMjMtMGUwOC00MDE2LTk2YjEtMWI5OWY3YTc1OGQwIiwiZW1haWwiOiJndWVzdC5jZGMwYWQyMy0wZTA4LTQwMTYtOTZiMS0xYjk5ZjdhNzU4ZDBAYnl0ZWxlYXJuLmFpIiwiZGlzcGxheV9uYW1lIjoidXNlciIsImZ1bGxfbmFtZSI6IkRFRkFVTFRfRlVMTF9OQU1FIiwicHJvZmlsZV9pbWFnZSI6bnVsbCwiZGVmYXVsdF9yb2xlIjoiZ3Vlc3RfdXNlciIsImltcGVyc29uYXRpbmciOmZhbHNlLCJpbXBlcnNvbmF0b3JfdXNlcl9pZCI6bnVsbCwicm9sZXMiOlsiZ3Vlc3RfdXNlciJdLCJzZXNzaW9uX2lkIjoic2Vzc2lvbl9jM2M4Y2Q5My02NzViLTQ2YWEtOTQ4My1lN2NjNGMyMWYxN2MiLCJjbGFzc19saXN0IjpbXX0.RNxrjiO535-_jO9rly9DjtDvNqjLdWdkNPA093SvHfxo_-nzuP1Uka2HWEinVlbT3jYTC2CKOfcbLIVf-5VWeoD3bWe8fWvJ5ScbiyOnP2qSYVyyFr3cXEWcEq39_zvK2ODGK0pV8Tf2wFgJ5FIoPJbClNDJ1l3FqkUxb52UEGogSLWDPtSW61QS5m_ketyrhybTFh0EGe8RlR0zyL-Gy5LraPkS03YPCLkrSxoGoJwx1OB0lgCr3y0fAhLkhKglzY6xe5tJ-QgU00ImFifH43d1SjuJKFUOtS8eHn3mjaj2qSsrwepKi7LtaK9MOa7FAyCpPR94TEQHszZbnOKyWz-N8apOHQeBJAmVJVqIrIawHe_bJ8szOvFP_QX4gDHFPtyY__mXcHyp_wklsV9wt5wYCw9Jqo32m6KFq_cuO7w72V6L2TGFD0H71-rXhFF_u2ljitvCoISvlMB3n280JDylwrttn1SxqZ_yyhnTo9Z5Lm6m7HmDi9JHqy2__89U3llXc7ujy4ohapGLQFwM1yV4x8wXdnVA76i6e1pMX2Je5KlDfEzUUYkr0Yqs9v6K8RZJ6pDvNK3Clj6A0QNFJb-CnZOF2g1F9b-kl8zqvxaym6zg1Fhpn1-qQhQqvlGjZABmVLvOlqWp0zYuSEizXkBhDAwt8hfVFSFbmomUUd4"}
  r=requests.post(url="https://preproduserapi.bytelearn.ai/api/v1/user", headers=headers, json={"password": "hello123456", "provider": "local", "school_grades": [9], "full_name": "dfvfv fvvfd","default_role": "teacher", "display_name": "dfvfv fvvfd","roles":"{0:student, 1:teacher}"})
  print(r.text)
  print(r.status_code)
  if r.status_code !=200:
    return [False,r.status_code,r.json()]
      
  return [True,r.status_code,r.json()]


create_user()

