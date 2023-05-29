from bottle import post, response, request
import os
import uuid


@post("/upload-picture")
def _():
   try:
      
      the_picture = request.files.get("picture")
      name, ext = os.path.splitext(the_picture.filename) #filename = happy.jpg (name = happy, ext = .jpg)
      
      # Check if the file extension is allowed
      if ext not in (".png", ".jpg", ".jpeg"): # how to check the mime type
         response.status = 400
         return "This picture is not allowed"
      
      # Generate a unique filename
      picture_name = str(uuid.uuid4().hex)
      picture_name = picture_name + ext #this will become the uuid.jpg
      
      # Save the picture to the 'images' directory
      the_picture.save(f"images/{picture_name}")

      # read the mime type
      # if it is not one that is allowed 
      # delete the picture
      # tell the user to "stop being funny and mess with the code"
      # if it is the real thing
      # repsond with "ok"

      return "picture succesfully uploaded"
   except Exception as e:
      print(e)
   finally:
      pass