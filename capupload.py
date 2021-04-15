import cv2
import dropbox
import random 
import time

start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)
    print(number)
    videoCaptureObject=cv2.VideoCapture(0)

    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        ing_name="img" + str(number) + ".png"
        cv2.imwrite(ing_name,frame)
        start_time=time.time()
        result = False
    return ing_name 
    print("snapshot taken")    
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(ing_name) :
    access_token = 'sl.AuhiljqbQJptjgjOas2Ux7FjUM3P9RNzuOMclTJDe-8X6IAwas-FrpH-hXnkof7Ny3GParmdBhPs-iJYV_6abD5Yy51a3DfP9iQc1plG9Xvm8FETRSo__mP8aIio1ODrd_YLNkE'
    file=ing_counter 
    file_from=file
    file_to="/newfolder1/" +(ing_name)
    dbx=dropbox.Dropbox(self.access_token)

    with open(file_from , 'rb')as f :
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)



def main ():
    while(True):
        if((time.time()-start_time)>=100):
            name=take_snapshot()
            upload_file(name)



main()            


