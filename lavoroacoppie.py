import numpy as np
import matplotlib.pyplot as plt
#importo la colormap
import matplotlib.cm as cm

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




#prova
with open(contenuto,'r') as mf:
    header=mf.readline()
    for line in mf:
        line=line.strip()
        columns=line.split()

        magnitude_list.append(float(columns[4]))
        color_list.append(float(columns[8]))
        age_list.append(float(columns[12]))

magnitude_list=[item*(-1) for item in magnitude_list]

magnitude=np.array(magnitude_list)
color=np.array(color_list)
age=np.array(age_list)

#definisco in quanti intervalli di età voglio suddividere la legenda
nbin=30
#creo un array i cui estremi sono l'eta della stella più giovane e l'età della stella più vecchia
#ogni "cella" di tale array contiene un intervallo di età. tali intervalli hanno tutti la stessa lunghezza temporale
bins=np.arange(np.min(age),np.max(age),((np.max(age)-np.min(age))/nbin))

#creo una tavolozza di nbin colori dalle tonalità "terrain"
#altre tonalità molto utilizzate sono "plasma", "inferno"
cmap=plt.get_cmap('terrain',nbin)

#creo un ciclo for dedicato ad ogni intervallo di età
for i in range(0,nbin-1,1):
    #np.where(condition) restituisce gli indici degli elementi dell'array age che hanno un'età compresa nell'intervallo in esame
    ind_i=np.where((bins[i]<=age) & (age<bins[i+1]))[0]
    magnitude_i=magnitude[ind_i]
    color_i=color[ind_i]

    #cm.terrain(i/nbin) seleziona dalla tavolozza il colore associato all'indice i
    plt.scatter(color_i,magnitude_i,c=cm.terrain(i/nbin),label='[{:.2f},{:.2f}]Gyr'.format(bins[i],bins[i+1]),marker='.')

plt.legend()
plt.xlabel('Color')
plt.ylabel('Magnitude')
plt.title('Modello Cosmologico')
plt.show()

