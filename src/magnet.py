import re
import pyperclip

def extrair_codigos_magnet(links):
    codigos_magnet = []
    for link in links:
        match = re.search(r'urn:btih:(\w+)', link)
        if match:
            codigos_magnet.append(match.group(1))
    return codigos_magnet

def criar_hiperlinks(codigos_magnet):
    hiperlinks = []
    for codigo in codigos_magnet:
        hiperlink = f'<a href="magnet:?xt=urn:btih:{codigo}">{codigo}</a>'
        hiperlinks.append(hiperlink)
    return hiperlinks

def main():
    # Recebe os links magnéticos
    print("Cole os links magnéticos aqui (um por linha):")
    entrada = ""
    while True:
        try:
            linha = input()
            if not linha:
                break
            entrada += linha + "\n"
        except EOFError:
            break

    links = entrada.strip().split('\n')

    # Extrai códigos magnéticos
    codigos_magnet = extrair_codigos_magnet(links)

    # Cria hiperlinks
    hiperlinks = criar_hiperlinks(codigos_magnet)

    # Copia os hiperlinks para a área de transferência
    hiperlinks_texto = '\n'.join(hiperlinks)
    pyperclip.copy(hiperlinks_texto)

    print("Hiperlinks gerados e copiados para a área de transferência:")
    print(hiperlinks_texto)

if __name__ == "__main__":
    main()
