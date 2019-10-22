# インストールした discord.py を読み込む
import discord
import stage_info
from datetime import datetime

TOKEN = "ここにアクセストークンを記述" 
info = stage_info.stage_info()

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    if message.content == 'リグマ':
        info.relog()
        rule = info.league_stage()[0]
        stage = info.league_stage()[1]
        start_t = info.league_stage()[2]
        end_t = info.league_stage()[3]
        stage_count = 2
        for count in range(4):
            if count == 0:
                await message.channel.send('----------------------------\n現在のルール : %s \n マップ : %s , %s \n----------------------------' % (rule[0], stage[0], stage[1]))
            else:
                await message.channel.send('----------------------------\n%s時〜%s時のルール : %s \n マップ : %s , %s \n----------------------------' % (conv_timestamp(start_t[count] + 32400), conv_timestamp(end_t[count] + 32400), rule[count], stage[stage_count], stage[stage_count + 1]))
                stage_count += 2

def conv_timestamp(unix_time):
    time = datetime.fromtimestamp(unix_time)
    hour = time.hour
    return hour


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)

