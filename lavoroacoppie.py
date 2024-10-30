class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                content = file.readlines() 
            return content
        except FileNotFoundError:
            return ["File non trovato."]
        except IOError:
            return ["Errore durante la lettura del file."]

file_reader = FileReader('data.txt')
contenuto = file_reader.read_file()

for riga in contenuto:
    print(riga.strip())  

