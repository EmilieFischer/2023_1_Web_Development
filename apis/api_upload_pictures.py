# from bottle import post, response, request
# import os
# import uuid


# @post("/upload-picture")
# def _():
#    try:
      
#       the_picture = request.files.get("picture")
#       name, ext = os.path.splitext(the_picture.filename) #filename = happy.jpg (name = happy, ext = .jpg)
      
#       # Check if the file extension is allowed
#       if ext not in (".png", ".jpg", ".jpeg"): # how to check the mime type
#          response.status = 400
#          return "This picture is not allowed"
      
#       # Generate a unique filename
#       picture_name = str(uuid.uuid4().hex) + ext.lower()
      
#       the_picture.save(f"pictures/{picture_name}")

#       return "picture succesfully uploaded"
#    except Exception as e:
#       print(e)
#    finally:
#       pass