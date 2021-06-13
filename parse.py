import re

def query_to_dic(i):
    key=re.findall(r"([\d\w\-\_]+)=[\d\w\-\_]+",i)
    value=re.findall(r"[\d\w\-\_]+=([\d\w\-\_]+)",i)
    # print(key,value)
    d=zip(key,value)
    #print(dict(d))
    return dict(d)
  
  


def multi_to_dic(m):
    #remove all 
    m_r=re.sub(": ",":",m)
    key=re.findall(r'(.*):.*\n',m_r)
    value=re.findall(r'.*:(.*)\n',m_r)
    d=zip(key,value)
    # print(dict(d))
    return dict(d)


def url_split(u):
    url=re.split(r'\?',u)[0]
    params=query_to_dic(re.split(r'\?',u)[1])
    print(url,params)
   # return {}

########################TEST  multi_to_dic########################
string=r"""User-Agent: Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G955N Build/NRD90M.G955NKSU1AQDC)
device_identifier: 6c72b4a3677e5b8f
app_version: 9.4.11
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6WyJ3cml0ZSJdLCJleHAiOjE2MjM0ODk3ODMsImF1dGhvcml0aWVzIjpbIlJPTEVfQURNSU4iXSwianRpIjoiMjkwZGQ0MDEtZjNjZS00MTdiLThjMWEtMGU0MWNjZDMzYTQxIiwiY2xpZW50X2lkIjoiNWI4NWMwM2MxNmJiYjg1ZDk2ZTIzMmIxMTJlZTg1ZGMifQ.nrNwDhqNZ5kuvet5C7J6ARRMHaKodQz-E7kje0Y8D0U
Signature: bf368aa2e416f7d6bb2c82fd9f279bdb8b997174274bdf207d76cea9a0f0ceed
seed: fd4cdd24-0f59-487b-b41c-b6d5868b0993
Content-Type: application/x-www-form-urlencoded
Content-Length: 179
Host: secure.idealista.com
Connection: Keep-Alive
Accept-Encoding: gzip
"""
 
# multi_to_dic(string) 


########################TEST query_to_dic##########################


i=r'client=4&_session=1623500405970354730244971762&v=1623489514&_vs=0&sign_ran=cceb74f6e7192095cc4a8df3a5b083a6&code=e9459c6ed50cd705'
# query_to_dic(i)


########################TEST url_split###############################

url=r"/api/3.5/es/search?t=6c72b4a3677e5b8f&k=5b85c03c16bbb85d96e232b112ee85dc&user=j_demx%40yahoo.com&token=01b520d73184c2ce3fa8c1142c1592bc&timestamp=1623482026471"

# url_split(url)

