from telegram.ext import *
import broadcast

def help_command(update,context):
    help_text = "-- help --\n\
* /add <group id><name> untuk menambah daftar broadcast\n\
* /delete <group id> untuk menghapus group dari daftar broadcast\n\
* /info menampilkan info dari bot\n\
* /send <message> mengirim pesan ke semua group\n\
* /list mendapatkan list group id"
    update.message.reply_text(help_text)

def add_command(update,context):
    try:
        if(len(context.args)>=2):
            group_id = context.args[0]
            name = " ".join(context.args[1:])
            result = broadcast.addGroupId(group_id,name)
            update.message.reply_text(result)
        else:
            update.message.reply_text("-- Add --\nKesalahan : parameter kurang")
    except:
        update.message.reply_text("-- Add --\nKesalahan : exception")

def delete_command(update,context):
    try:
        if(len(context.args)==1):
            group_id = context.args[0]
            result = broadcast.deleteGroupId(group_id)
            update.message.reply_text(result)
        else:
            update.message.reply_text("-- Delete --\nParameter kurang atau lebih !")
    except:
        update.message.reply_text("-- Delete --\nKesalahan : exception")

def info_command(update,context):
    info_text = "-- Info --\nBot ini adalah bot untuk mengirimkan pesan broadcast\
kepada seluruh group yang sudah ada pada daftar broadcast. Ketik\
/help untuk mengetahui seluruh perintah yang dapat dijalankan"
    update.message.reply_text(info_text)

def send_command(update,context):
    try:
        if(len(context.args)>=1):
            message = " ".join(context.args[0:])
            id_list = broadcast.getChatIdList()
            for id in id_list:
                hasil = broadcast.sendBroadcast(id[0],message)
                update.message.reply_text(hasil)
        else:
            update.message.reply_text("-- Add --\nKesalahan : parameter kurang")
    except:
        update.message.reply_text("-- Add --\nKesalahan : exception")

def list_command(update,context):
    group_list = broadcast.getChatIdList()
    message = "-- List --\n"+"\n".join(["* "+i[0]+" ("+i[1]+")" for i in group_list])
    update.message.reply_text(message)
    