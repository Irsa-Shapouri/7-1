import pandas as pd 



# ############################# USER DB #############################

# templist = []

# user_name = ["Irsa", "Reyhane", "Aida", "Mobin", "Mohammad", "Amirali"]
# user_last_name = ['Shapouri', 'Mohammadi','Bayati','Ahmadpour','Babai', 'Najafi']
# user_password = ['Irsa123','Reyhane123','Aida123','Mobin123','Mohammad123', 'Amirali123']
# user_phone_number = ["09129174792","09934709809", "09367609871", "09931917832", "09109869079", "09217975724"]

# for i in range(len(user_name)):

#     Table_dict = {
#         "user_id" : i,
#         "user_name" : user_name[i],
#         "user_last_name": user_last_name[i], 
#         "user_password":  user_password[i], 
#         "user_phone_number": user_phone_number[i]
#         }

#     templist.append(Table_dict) 
#     df = pd.DataFrame(templist)

# df.to_csv('./database/users.csv',index=False)



# ############################# BRAND BD #############################

# templist = []

# brand_name = ["Apple", "Samsung", "Nikon", "Xiaomi", "Canon", "Asus", "Acer", "Hp", "Sony", "Huawei"]

# for i in range(len(brand_name)):
    
#     Table_dict = {
#         "brand_id" : i,
#         "brand_name" : brand_name[i],
#     }

#     templist.append(Table_dict) 
#     df = pd.DataFrame(templist)

# df.to_csv('./database/brands.csv',index=False)




# ############################# PRODUCT #############################


templist = []

Products = ["Laptop", "Smart Phone and Tablet", "Case", "Monitor", "Camera", "Accessories", "About Us"]

for i in range(len(Products)):
    
    Table_dict = {
        "Products_id" : i,
        "Products_name" : Products[i],
    }

    templist.append(Table_dict) 
    df = pd.DataFrame(templist)

df.to_csv('./database/Products.csv',index=False)




