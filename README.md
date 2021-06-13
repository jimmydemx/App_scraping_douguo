# 1. Introduction
[Douguo](www.douguo.com) is a very popular food recipe sharing App/forum in China. It compacts the socialziation, iteration among different users,picture sharing,comment and online shop. It is Instagram alike, however specializing only at food.
![豆果](https://i1.douguo.com/upload/banner/1/c/0/1c723b7852d66dc25fa4907a417ef2b0.jpg)


This Project scrapes all the data from the Android [App](https://cp1.douguo.com//static/nweb/images/qrcode.png?2001) of Douguo.
 
Other things notable:
- use `Fiddler` for Web package monitoring
- use `nox` Android Simulator for App download and testing
- Use 10 Processes to speed up the scraping process with cocurrence future with Python.
- set the menus_id as the major key of MongoDB to avoid the duplication of data.
- `Echarts` is used for the visualization of data 


The Purpose of Scraping:

- [x] Analysis the preference of tastes of people in China.
- [x] Analysis the preference of combination of food.
- [x] what types of cake do people love most in China? 



# 2. Setup 



- setup Mongodb on the computer, modify the host and port in `db.py` accordingly for the creatation of database for `dougou` 

- Run App.py



Note:
- Python: 3.3+ Cocurrent pool is used. to maximized the scraping speed.
- requests package shall be installed

# To-Do List

- data Wash
  