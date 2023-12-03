from tqdm import tqdm
from telethon.tl.types import InputMessagesFilterVideo
from fun import arquivos_texto, limpar, solicitaçoes
from time import sleep
from random import randint
from telethon import TelegramClient, events
import logging

cor = solicitaçoes.cor
r = solicitaçoes.r
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

print(cor[0], f'{" " * 20}EXTRAIR MIDIAS DO TELEGRAM{" " * 20}', r[2], r[0], '\n', '-' * 65, '\n', cor[1],
      f'{" " * 23}Escolha um usuario{" " * 23}', r[2])

try:
    client2 = arquivos_texto.abrir_reg(f'continuar_client')
    if '2' in client2:
        api_id2 = 24941592
        api_hash2 = '02bcab46b7f4acc54248484d6df31811'
        sessao = 'upalto2'
        client2 = TelegramClient(sessao, api_id2, api_hash2)
    else:
        api_id = 22217845
        api_hash = '419b473e8797968bb157b29bffa1ee45'
        sessao = 'upalto'
        client2 = TelegramClient(sessao, api_id, api_hash)
    verificar = (arquivos_texto.abrir_reg(f'continuar')[0])
    mv = verificar.find(',')
    grupo_vitima = verificar[:mv]
    meu_grupo = verificar[mv + 1:]
    print(meu_grupo, grupo_vitima)
except:
    verificar = False

if verificar:
    continuar = solicitaçoes.pergunta(f'    {cor[1]}{" " * 6}DESEJA COMTINUAR O PROCESSO ANTERIOR?{" " * 6} {r[2]} '
                                      f'\n\n{" " * 6}>> Digite [ 1 ] Para sim ou [ 2 ] Para Nao{" " * 6} {r[1]}\n {"-" * 65}\n \n{" " * 1}>>')
else:
    continuar = 0

if continuar != 1:
    # Use your own values from my.telegram.org
    client_select = solicitaçoes.pergunta(f'    {cor[2]}{" " * 6}>> Usuario [ 1 ]{" " * 6} {r[2]} '
                                          f'{cor[2]}{" " * 6}>> Usuario [ 2 ]{" " * 6} {r[1]}\n {"-" * 65}\n \n{" " * 1}>>')
    if client_select == 1:
        api_id = 22217845
        api_hash = '419b473e8797968bb157b29bffa1ee45'
        sessao = 'upalto'
        client2 = TelegramClient(sessao, api_id, api_hash)
    else:
        api_id2 = 24941592
        api_hash2 = '02bcab46b7f4acc54248484d6df31811'
        sessao = 'upalto2'
        client2 = TelegramClient(sessao, api_id2, api_hash2)
    arquivos_texto.registro(sessao, nome=f'continuar_client', substituir='sim')
    grupos_nome = []
else:
    print('...')


async def main():
    global idd, quantia_agrup
    if verificar:
        m = []
        idd = []
        grupos = {}
        rev = arquivos_texto.abrir_reg(f'continuar_rev')
        quantia_agrup = int(arquivos_texto.abrir_reg(f'continuar_agrop'))
        resp = int(arquivos_texto.abrir_reg(f'continuar_resp'))
        verificar2 = (arquivos_texto.abrir_reg(f'continuar'))
        mv = verificar2.find(',')
        grupo_vitima = int(verificar2[mv + 1:])
        print(grupo_vitima)
        meu_grupo = int(verificar2[:mv])
        print(meu_grupo, grupo_vitima)

        async for dialog in client2.iter_dialogs():
            grupos[dialog.id] = dialog.name
            # print(cor[0], f' [ ]', r[2], cor[1], f' {dialog.name} ', r[2], cor[0], 'has ID', r[2], cor[2],
            # dialog.id, r[1])

        grupo_vitima_nome = str(grupos[grupo_vitima])
        meu_grupo_nome = str(grupos[meu_grupo])
        solicitaçoes.textos_prin(
            f'{cor[1]}{grupo_vitima_nome} {r[2]}  {cor[0]} "has ID" {r[2]} {cor[2]} {grupo_vitima}, {r[1]}',
            f'{cor[1]}{meu_grupo_nome} {r[2]}  {cor[0]} "has ID" {r[2]} {cor[2]} {meu_grupo}, {r[1]}')

    if continuar != 1:
        ctd = 0
        print(f' {"-" * 65}\n', cor[3], "  >>Carregando grupos|canais...<<", r[1], '\n')

        for ani in tqdm(range(0, 3)):
            sleep(0.5)
        m = []
        idd = []
        grupos = []
        async for dialog in client2.iter_dialogs():
            if ctd == 0:
                limpar.limpar()
                print(f'\n {"-" * 65}\n', cor[0], ' GRUPOS PRONTOS:', r[2])
            ctd += 1
            print(cor[0], f' [ {ctd} ]', r[2], cor[1], f' {dialog.name} ', r[2], cor[0], 'has ID', r[2], cor[2],
                  dialog.id,
                  r[1])
            grupos.append(dialog.id)
            grupos_nome.append(dialog.name)

        cele = solicitaçoes.pergunta(
            f'\n {"-" * 65}\n{cor[1]} Digite o numero do grupo|canal que deseja EXTRAIR as midias{r[2]}\n  >>: ')
        cele2 = solicitaçoes.pergunta(
            f'{cor[1]}  Digite o numero do grupo|canal que deseja ENVIAR as midias{r[2]}\n  >>: ')
        limpar.limpar()

        grupo_vitima = str(grupos[cele - 1])
        grupo_vitima_nome = str(grupos_nome[cele - 1])
        meu_grupo = str(grupos[cele2 - 1])
        meu_grupo_nome = str(grupos_nome[cele2 - 1])
        solicitaçoes.textos_prin(
            f'{cor[1]}{grupo_vitima_nome} {r[2]}  {cor[0]} "has ID" {r[2]} {cor[2]} {grupo_vitima}, {r[1]}',
            f'{cor[1]}{meu_grupo_nome} {r[2]}  {cor[0]} "has ID" {r[2]} {cor[2]} {meu_grupo}, {r[1]}')
        arquivos_texto.registro(f'{meu_grupo},{grupo_vitima}', nome='continuar', substituir='sim')

        reverso = solicitaçoes.pergunta(f'{cor[1]} Ordem reversa?{r[2]}\n [ 1 ]-Sim \n [ 2 ]-Nao \n >>')
        resp = solicitaçoes.pergunta(
            f'{cor[1]} ESCOLHA A LEGENDA!!{r[2]} \n [ 1 ]-Para o grupo  \n [ 2 ]-Para o canal \n [ 3 ]-VIP \n [ 4 ]- Legenda original \n >> ')
        arquivos_texto.registro(resp, nome=f'continuar_resp', substituir='sim')
        print(cor[0], f'{" " * 20}COMESANDO A EXTRAÇAO{" " * 20}', r[2], r[0], '\n', '-' * 65, '\n')
        if reverso == 1:
            rev = True
        else:
            rev = False
        arquivos_texto.registro(rev, nome=f'continuar_rev', substituir='sim')
        try:
            cont = int(arquivos_texto.abrir_reg(f'{grupo_vitima}_agrup')[0])
            quantia_agrup = int(arquivos_texto.abrir_reg(f'{grupo_vitima}_q_agrup')[0])
        except:
            quantia_agrup = solicitaçoes.pergunta(f'{cor[1]}Agrupar quantos videos [0 a 10]: {r[2]}')
            arquivos_texto.registro(quantia_agrup, nome=f'{grupo_vitima}_agrup')
            arquivos_texto.registro(quantia_agrup, nome=f'continuar_cont', substituir='sim')
            arquivos_texto.registro(quantia_agrup, nome=f'{grupo_vitima}_q_agrup')
            arquivos_texto.registro(quantia_agrup, nome=f'continuar_agrop', substituir='sim')
            cont = int(arquivos_texto.abrir_reg(f'{grupo_vitima}_agrup')[0])

        try:
            cont_agrop = int(arquivos_texto.abrir_reg(f'{grupo_vitima}_cont')[0])

        except:
            arquivos_texto.registro(1, nome=f'{grupo_vitima}_cont')
            cont_agrop = int(arquivos_texto.abrir_reg(f'{grupo_vitima}_cont')[0])
    else:
        print('ok')

    async for message in client2.iter_messages(grupo_vitima_nome, reverse=resp, filter=InputMessagesFilterVideo, ):
        duracao = str(message.document.attributes[0])
        dm = int(duracao.find('duration='))
        dm2 = int(duracao.find('.', dm))
        duracao = int(duracao[dm + 9:dm2])
        legenda4 = str(message.text)
        if duracao >= 180:
            if resp == 1:
                legenda = ('🔞꧁𝐼𝑀𝙋𝐸𝑅𝙄𝐴𝐿♾𝙋𝒪𝑅𝙉𝒪꧂🔞\n\n[💠 Canal Gratis ✅]('
                           'https://t.me/+T8MqSqaLvyw1YzEx)\n[💠 CANAL VIP 💎](https://t.me/Contratar_vip)')

            elif resp == 3:
                legenda = '🔞꧁𝐼𝑀𝙋𝐸𝑅𝙄𝐴𝐿♾𝙋𝒪𝑅𝙉𝒪꧂🔞'

            else:
                if resp == 4:
                    legenda = legenda4
                else:
                    legenda = ("🔞꧁𝐼𝑀𝙋𝐸𝑅𝙄𝐴𝐿♾𝙋𝒪𝑅𝙉𝒪꧂🔞\n\n[💠 Grupo para trocar videos 👥]("
                               "https://t.me/+uWrWJzVRpAY3OTFh)\n[💠 CANAL VIP 💎](https://t.me/Contratar_vip)")
            print(cor[0], legenda4, r[2])
            id1 = str(f'{message.id}')
            try:
                ids = (arquivos_texto.abrir_reg(f'{grupo_vitima}_ids'))
            except:
                arquivos_texto.registro(0, f'{grupo_vitima}_ids', 'nao')
                ids = (arquivos_texto.abrir_reg(f'{grupo_vitima}_ids'))
            if id1 in ids:
                if not rev:
                    print(f'{cor[0]}Videos anteriores ja forao enviados{[2]}')
                else:
                    limpar.limpar()
                    print(f'{cor[5]}ja foi enviado{r[1]}')
            else:
                idd.append(message.id)
                m.append(message)
                try:
                    print(m[quantia_agrup])
                except:
                    limpar.limpar()
                    print(f'{cor[0]}nao a {quantia_agrup} videos ainda {r[1]}')
                else:
                    limpar.limpar()
                    print(f'{cor[2]}Enviando{r[2]}')

                    try:
                        tempo = randint(0, 25)
                        for ani2 in tqdm(range(0, tempo)):
                            sleep(1)
                        await client2.send_file(meu_grupo_nome, m[-(quantia_agrup + 1):-1], file_size=100, silent=True)
                        m = []

                        # cont += quantia_agrup
                        # arquivos_texto.registro(cont, f'{grupo_vitima}_agrup')
                        # cont_agrop += 1
                        # arquivos_texto.registro(cont_agrop, f'{grupo_vitima}_cont')

                        async for message2 in client2.iter_messages(meu_grupo_nome, 1):
                            print(str(message2)[0:63])
                            await client2.edit_message(message2, legenda)

                        for nu in idd:
                            arquivos_texto.registro(nu, f'{grupo_vitima}_ids', 'nao')

                    except:
                        limpar.limpar()
                        print(f'{cor[5]}Falha ao enviar{r[1]}')


with client2:
    client2.loop.run_until_complete(main())
