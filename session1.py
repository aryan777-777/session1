print("Single value container")
user_name = "aryankumar"
print(user_name, id(user_name), type(user_name))
print(hex(id(user_name)))
print(oct(id(user_name)))
print((bin(id(user_name))))


user= "kumar"
print(user, id(user), type(user))

another_user="Aryan"
print(another_user,id(another_user),type(another_user))

#Reference copy operation
another_user=user
print(another_user,id(another_user),type(another_user))


#update operation
user="rohan"
print(user,id(user),type(user))


#delete operation
del user
print(user,id(user),type(user))    #it will give us a error because we delete the user so we cannot print now user cntainer