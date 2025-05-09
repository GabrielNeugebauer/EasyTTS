import edge_tts
import asyncio
import os

async def main():
    try:
        print('Bem vindo ao EasyTTS!\nDeveloped by @gabrielneugebauer\n\nDigite o caminho do arquivo de texto que deseja converter em áudio:')
        path = input().replace("\\", "/").replace("'", "").replace('"', "")
        texto = loadFile(path)
        texto = texto = ', '.join(texto).replace(".,",".")
        if not texto:
            print("[!] O arquivo está vazio ou não foi encontrado.")
            return
        print('Digite o nome do arquivo de áudio que deseja salvar (sem extensão):')
        nome_arquivo = input()
        print (f"{path}")
        # print (texto) # Para debug
        comunicador = edge_tts.Communicate(
            text=texto,
            voice="pt-BR-AntonioNeural",  # Ou "pt-BR-FranciscaNeural"
            rate="+5%",  # velocidade: -100% a +100%
        )
        await comunicador.save(f"Resultados\\{nome_arquivo}.mp3")
        print(f"Arquivo de áudio gerado com sucesso em {os.getcwd()}\\Resultados\\{nome_arquivo}.mp3!")
    except Exception as error:
        print(f"[!] Ocorreu um erro: {error}")
        return


def loadFile(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]
    except Exception as error:
        print(f"[!] Failed to load wordlist: {error}")
        return []
asyncio.run(main())
print("Programa encerrado!")