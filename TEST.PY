
import pandas as pd


# users_df = pd.read_csv("./database/users.csv")

# username = "Irsa"
# password = "Irsa123"


# if users_df.loc[users_df["user_name"] == username]["user_password"].tolist() == [password]:
#             print('YES')
# else:
#             print('passwd')


Category = pd.read_csv("./database/Category.csv")
sub_Category = pd.read_csv("./database/sub_Category.csv")



# vertical_stack = pd.concat([Category, sub_Category], axis=0)

# vertical_stack.to_csv('database/out.csv', index=False)


df = Category.merge(sub_Category, left_on='CID', right_on='ID')