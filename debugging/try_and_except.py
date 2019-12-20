# try:
#     foobar
# except :
#     print("Error")

# print("After Error handling")

d = {"name" :"Kush"}
# d["Kush"]

def get(d, key):
    try:
        print(d[key])
    except KeyError:
        print("The given value is not found in the dictionary.")

get(d, "hello")
get(d, "name")