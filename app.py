from json import encoder
import requests
from parse import *
import data as info
import json 
from db import db_douguo_mongo
import concurrent.futures


header_parse=multi_to_dic(info.header)

print("header_parse",header_parse)

data_parse=query_to_dic(info.data_catalog)

r_catalog=requests.post(info.url_catalog,headers=header_parse,data=data_parse)

# print(r.text)

catalog = json.loads(r_catalog.text)

# print(catalog)

# sub_catalog: 热门/蔬菜/肉类
# sub_sub_catalog: 时令蔬菜/绿叶蔬菜
# item: 西南花/芦笋


catalog_list=[]
for sub_catalog in catalog["result"]["cs"]: 
    for sub_sub_catalog in sub_catalog["cs"]:
        for recipe in sub_sub_catalog["cs"]:
            # print(recipe)
            data_recipe_parse=query_to_dic(info.data_recipe)
            data_recipe_parse.update({'keyword':recipe['name']})
            # data_recipe_parse.update({'keyword':'豆腐'})
            catalog_list.append(data_recipe_parse)
            
# catalog_list.append(data_recipe_parse)
print("catalog_list=",catalog_list)
            
        

def recipe_scraping(p):
    i=0
    while True: 
        rs_url=str(info.url_recipe+str(i)+"/20")
        r_recipe=requests.post(rs_url,headers=header_parse,data=data_recipe_parse)
        recipe=json.loads(r_recipe.text)
        # print("recipe=",recipe)
        jump=0

        # if item==[],it will automatic not enter the loop
        for item in recipe["result"]["list"]:
            jump=1
            mongodb_store={}
            if item["type"]==13:
                mongodb_store["username"]=item["r"]["an"]
                mongodb_store["_id"]=item["r"]["id"]
                mongodb_store["recipe_title"]=item["r"]["n"]
                mongodb_store["practiced"]=item["r"]["dc"]
                mongodb_store["browsed"]=item["r"]["fc"]
                mongodb_store["cook_dif"]=item["r"]["cook_difficulty"]
                mongodb_store["cook_time"]=item["r"]["cook_time"]
                mongodb_store["rate"]=item["r"]["rate"]
                mongodb_store["ingre"]=item["r"]["major"]

                db_douguo_mongo.insert_item(mongodb_store)
            else:
                continue

        if jump==1:
            print("正在导入:",recipe["result"]["sts"],",第",int(i/20+1),"页")
            i=i+20       
            jump=0
            continue
        else:
            print(int(i/20+1),'页以后已经没有',recipe["result"]["sts"],"数据")
            return 


if __name__ == "__main__":    
    # recipe_scraping(catalog_list[0])
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        for p in catalog_list:
            print("正在执行导入：",p["keyword"])
            executor.submit(recipe_scraping, p)









