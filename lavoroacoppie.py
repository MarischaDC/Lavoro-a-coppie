import 
class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            return "File non trovato."
        except IOError:
            return "Errore durante la lettura del file."

# Utilizzo della classe
file_reader = FileReader('percorso/del/tuo/file.txt')
contenuto = file_reader.read_file()
print(contenuto)
