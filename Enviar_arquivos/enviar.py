import os
from fun import limpar,corrente,arquivos_texto
from time import sleep
from random import randint
from telethon import TelegramClient, events, Button
import logging

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Use your own values from my.telegram.org
api_id = 22217845
api_hash = '419b473e8797968bb157b29bffa1ee45'
client = TelegramClient('upalto', api_id, api_hash)
client3 = TelegramClient('bot', api_id, api_hash)

async def main():
    cont = int(arquivos_texto.abrir_reg('cont_video')[0])
    c = 1
    async for dialog in client.iter_dialogs():
        c += 1
        if dialog.name in ("🔒Zona VIP | Xvideos RED🔒", 'Jogos_clientes', 'Xv liata', '𝕏𝕍🅡🅔🅓'):
            print(dialog.name, f'has ID numero {c}', dialog.id)
            if dialog.name in 'Jogos_clientes':
                chat = dialog.id

    async for message in client.iter_messages('🔒Zona VIP | Xvideos RED🔒',  reverse=True):
        print(message.id)


        tags = f'#{message.message}'
        legenda = f'» **Canal:**{tags} \n\n» [𝕏𝕍🅡🅔🅓⁃𝐋𝐈𝐒𝐓𝐀](https://t.me/+agKFJ3UonoFlZDE5)\n\n 𝕪𝕒𝕟𝕘☯️ ⭒🅼🅸🅳🅸🅰️🆂⭒ 〗'
        if message.photo:
            print('nao é um video')
            ids = (arquivos_texto.abrir_reg("mensagem_id_xv"))
            id1 = str(f'{message.id}')
            if id1 in ids:
                print('ja foi enviado')
            else:
                try:

                    await client.download_media(message, 'xv.jpg', progress_callback=corrente.callback(text='Baixando'))
                    await client.send_file(-1001912610506, 'xv.jpg', caption=legenda, progress_callback=corrente.callback)
                    await client.send_file(-1001959272675, 'xv.jpg', caption=legenda)
                    arquivos_texto.registro(message.id, "mensagem_id_xv", 'nao')
                    arquivos_texto.registro(tags, nome='Lista_XV_red', substituir='nao')
                except:
                    continue
        else:
            ids = (arquivos_texto.abrir_reg("mensagem_id_xv"))
            id1 = str(f'{message.id}')
            if id1 in ids:
                print('ja foi enviado')
            else:

                try:
                    sleep(randint(0, 10))
                    await client.download_media(message, 'xv.mp4', progress_callback=corrente.callback(text='Baixando'))
                    await client.send_file(-1001912610506, 'xv.mp4',supports_streaming=True, attributes=message.video.attributes,
                                           progress_callback=corrente.callback)
                    arquivos_texto.registro(message.id, "mensagem_id_xv", 'nao')
                    cont += 1
                    arquivos_texto.registro(cont, 'cont_video_xv')
                    arquivos_texto.registro(message.id, "mensagem_id_xv", 'nao')

                except:
                    continue


with client:
    client.loop.run_until_complete(main())
