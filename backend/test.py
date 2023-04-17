from firebase.sendAndGetDocxFromFirebase import upload_file, download_file
import os


try:
    # print("Текущая деректория:", os.getcwd())
    # upload_file("maket.docx")
    # print("File uploaded successfully")
    download_file("mr_smile_off.jpg")
    print("File downloaded successfully")
except Exception as e:
    print(e)
    print("Error uploading file")