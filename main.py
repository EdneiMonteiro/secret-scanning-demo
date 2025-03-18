import re
import os
import argparse

# Define padrões de segredos comuns
patterns = {
    "AWS Access Key": re.compile(r'AKIA[0-9A-Z]{16}'),
    "GitHub Token": re.compile(r'ghp_[A-Za-z0-9]{36}'),
    "Generic Password": re.compile(r'password\s*=\s*[\'"].+[\'"]', re.IGNORECASE),
    "Secret": re.compile(r'secret\s*=\s*[\'"].+[\'"]', re.IGNORECASE)
}

def scan_file(file_path):
    results = []
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for lineno, line in enumerate(f, 1):
                for name, pattern in patterns.items():
                    if pattern.search(line):
                        results.append((lineno, name, line.strip()))
    except Exception as e:
        print(f"Erro ao ler {file_path}: {e}")
    return results

def scan_directory(directory):
    report = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Pode-se filtrar por tipos de arquivo, se necessário
            file_path = os.path.join(root, file)
            matches = scan_file(file_path)
            if matches:
                report[file_path] = matches
    return report

def main():
    parser = argparse.ArgumentParser(description='Laboratório de Secret Scanning em Python')
    parser.add_argument('path', help='Caminho do arquivo ou diretório a ser escaneado')
    args = parser.parse_args()
    
    if os.path.isfile(args.path):
        results = scan_file(args.path)
        if results:
            print(f"Segredos encontrados em {args.path}:")
            for lineno, name, line in results:
                print(f"Linha {lineno}: [{name}] {line}")
        else:
            print(f"Nenhum segredo encontrado em {args.path}")
    elif os.path.isdir(args.path):
        report = scan_directory(args.path)
        if report:
            for file, matches in report.items():
                print(f"\nSegredos encontrados em {file}:")
                for lineno, name, line in matches:
                    print(f"Linha {lineno}: [{name}] {line}")
        else:
            print("Nenhum segredo encontrado no diretório.")
    else:
        print("Caminho inválido.")

if __name__ == '__main__':
    main()
