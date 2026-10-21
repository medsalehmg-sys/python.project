# creation read_json_file:
def read_json_file(file_name):
    try: 
    # we open the file :\# creation of file_name Variable :
      file=open(file_name)
      open(file.readlines())
      file.close()
    except FileNotFoundError:
       print("the doesn't exist ")
       