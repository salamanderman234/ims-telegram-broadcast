import requests
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
db_host = str(os.environ.get("MYSQL_HOST"))
db_user = str(os.environ.get("MYSQL_USER"))
db_name = str(os.environ.get("MYSQL_DATABASE"))
bot_token = str(os.environ.get("BOT_TOKEN"))


def updateStatusAccount(chat_id):
    db = mysql.connector.connect(
        host=db_host,
        user=db_user,
        passwd="",
        database=db_name
    )
    query = "UPDATE tb_telegram_account SET sent={} WHERE chat_id={}".format(1,chat_id)
    cursor = db.cursor()
    cursor.execute(query)
    db.commit()

def getChatIdList():
    db = mysql.connector.connect(
        host=db_host,
        user=db_user,
        passwd="",
        database=db_name
    )
    query = "SELECT chat_id,name FROM tb_telegram WHERE sent = 0"
    cursor = db.cursor()
    cursor.execute(query)
    hasil = cursor.fetchall()
    return tuple(hasil)


def sendBroadcast(id,message):
    api_link = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&parse_mode=Markdown&text={}".format(bot_token,id,message)
    hasil = requests.get(api_link)
    if hasil.status_code==200:
        return "-- Send --\n*Berhasil Mengirim Pesan ke- "+id
    else:
        return "-- Send --\n*Gagal Mengirim Pesan ke- "+id

def addGroupId(id,username):
    try :
        hasil = getChatIdList()
        for i in hasil:
            if(id==i[0]):
                return "-- Add --\nGroup Id sudah pernah ditambahkan"
        db = mysql.connector.connect(
            host=db_host,
            user=db_user,
            passwd="",
            database=db_name
        )
        query = "INSERT INTO tb_telegram(chat_id, name, sent) VALUES (%s,%s,%s)"
        value = (id,username,"0")
        cursor = db.cursor()
        cursor.execute(query,value)
        db.commit()
        return "-- Input --\nInput id-"+id+" Berhasil !"
    except:
        return "-- Input --\nKesalahan : proses input error"

def deleteGroupId(id):
    try :
        db = mysql.connector.connect(
            host=db_host,
            user=db_user,
            passwd="",
            database=db_name
        )
        query = "DELETE FROM tb_telegram WHERE chat_id=%s"
        value = (id,)
        cursor = db.cursor()
        cursor.execute(query,value)
        db.commit()
        return "-- Delete --\nDelete id-"+id+" Berhasil !"
    except:
        return "-- Delete --\nKesalahan : proses delete error"

