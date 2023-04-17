import jwt

# if the user verifies the JWT show the payload. If not the correct secret, show sorry...
the_jwt = jwt.encode({"name":"Emilie", "last_name":"Fischer"}, "the secret", algorithm="HS256")

# print(the_jwt)
# jwt.decode(the_jwt, "the secret", algorithms=["HS256"])

try:
    # jwt.encode(the_jwt, "the secret", algorithms="HS256"
    print(jwt.encode(the_jwt, "the secret", algorithms="HS256"))
except Exception as ex:
    print("Sorry, we cannot verify you")


# set cookie in the browser
response.set_cookie("jwt", the_jwt)
