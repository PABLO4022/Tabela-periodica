from colorama import Fore, Style
from colorama.initialise import reset_all

while True:
    tabela_periodica = {
        'H': {
            'nome': 'Hidrogênio',
            'numero': 1,
            'peso': 1.008
        },
        'He': {
            'nome': 'Hélio',
            'numero': 2,
            'peso': 4.0026
        },
        'Li': {
            'nome': 'Lítio',
            'numero': 3,
            'peso': 6.94
        },
        'Be': {
            'nome': 'Berílio',
            'numero': 4,
            'peso': 9.0122
        },
        'B': {
            'nome': 'Boro',
            'numero': 5,
            'peso': 10.81
        },
        'C': {
            'nome': 'Carbono',
            'numero': 6,
            'peso': 12.01
        },
        'N': {
            'nome': 'Nitrogênio',
            'numero': 7,
            'peso': 14.01
        },
        'O': {
            'nome': 'Oxigênio',
            'numero': 8,
            'peso': 16.00
        },
        'F': {
            'nome': 'Flúor',
            'numero': 9,
            'peso': 19.00
        },
        'Ne': {
            'nome': 'Neônio',
            'numero': 10,
            'peso': 20.18
        },
        'Na': {
            'nome': 'Sódio',
            'numero': 11,
            'peso': 22.99
        },
        'Mg': {
            'nome': 'Magnésio',
            'numero': 12,
            'peso': 24.305
        },
        'Al': {
            'nome': 'Alumínio',
            'numero': 13,
            'peso': 26.982
        },
        'Si': {
            'nome': 'Silício',
            'numero': 14,
            'peso': 28.085
        },
        'P': {
            'nome': 'Fósforo',
            'numero': 15,
            'peso': 30.974
        },
        'S': {
            'nome': 'Enxofre',
            'numero': 16,
            'peso': 32.06
        },
        'Cl': {
            'nome': 'Cloro',
            'numero': 17,
            'peso': 35.45
        },
        'Ar': {
            'nome': 'Argônio',
            'numero': 18,
            'peso': 39.948
        },
        'K': {
            'nome': 'Potássio',
            'numero': 19,
            'peso': 39.098
        },
        'Ca': {
            'nome': 'Cálcio',
            'numero': 20,
            'peso': 40.078
        },
        'Sc': {
            'nome': 'Escândio',
            'numero': 21,
            'peso': 44.956
        },
        'Ti': {
            'nome': 'Titânio',
            'numero': 22,
            'peso': 47.867
        },
        'V': {
            'nome': 'Vanádio',
            'numero': 23,
            'peso': 50.942
        },
        'Cr': {
            'nome': 'Cromo',
            'numero': 24,
            'peso': 51.996
        },
        'Mn': {
            'nome': 'Manganês',
            'numero': 25,
            'peso': 54.938
        },
        'Fe': {
            'nome': 'Ferro',
            'numero': 26,
            'peso': 55.845
        },
        'Co': {
            'nome': 'Cobalto',
            'numero': 27,
            'peso': 58.933
        },
        'Ni': {
            'nome': 'Níquel',
            'numero': 28,
            'peso': 58.933
        },
        'Cu': {
            'nome': 'Cobre',
            'numero': 29,
            'peso': 63.546
        },
        'Zn': {
            'nome': 'Zinco',
            'numero': 30,
            'peso': 65.38
        },
        'Ga': {
            'nome': 'Gálio',
            'numero': 31,
            'peso': 69.723
        },
        'Ge': {
            'nome': 'Germânio',
            'numero': 32,
            'peso': 72.630
        },
        'As': {
            'nome': 'Arsênio',
            'numero': 33,
            'peso': 74.922
        },
        'Se': {
            'nome': 'Selênio',
            'numero': 34,
            'peso': 78.971
        },
        'Br': {
            'nome': 'Bromo',
            'numero': 35,
            'peso': 79.904
        },
        'Kr': {
            'nome': 'Kripton',
            'numero': 36,
            'peso': 83.798
        },
        'Rb': {
            'nome': 'Rubídio',
            'numero': 37,
            'peso': 84.468
        },
        'Sr': {
            'nome': 'Estrôncio',
            'numero': 38,
            'peso': 87.62
        },
        'Y': {
            'nome': 'Ítrio',
            'numero': 39,
            'peso': 88.906
        },
        'Zr': {
            'nome': 'Zircônio',
            'numero': 40,
            'peso': 91.224
        },
        'Nb': {
            'nome': 'Nióbio',
            'numero': 41,
            'peso': 92.906
        },
        'Mo': {
            'nome': 'Molibdênio',
            'numero': 42,
            'peso': 95.95
        },
        'Tc': {
            'nome': 'Tecnécio',
            'numero': 43,
            'peso': 98.00
        },
        'Ru': {
            'nome': 'Rutênio',
            'numero': 44,
            'peso': 101.07
        },
        'Rh': {
            'nome': 'Ródio',
            'numero': 45,
            'peso': 102.91
        },
        'Pd': {
            'nome': 'Paládio',
            'numero': 46,
            'peso': 106.42
        },
        'Ag': {
            'nome': 'Prata',
            'numero': 47,
            'peso': 107.87
        },
        'Cd': {
            'nome': 'Cádmio',
            'numero': 48,
            'peso': 112.41
        },
        'In': {
            'nome': 'Índio',
            'numero': 49,
            'peso': 114.82
        },
        'Sn': {
            'nome': 'Estanho',
            'numero': 50,
            'peso': 118.71
        },
        'Sb': {
            'nome': 'Antimônio',
            'numero': 51,
            'peso': 121.76
        },
        'Te': {
            'nome': 'Telúrio',
            'numero': 52,
            'peso': 127.60
        },
        'I': {
            'nome': 'Iodo',
            'numero': 53,
            'peso': 126.90
        },
        'Xe': {
            'nome': 'Xenônio',
            'numero': 54,
            'peso': 131.29
        },
        'Cs': {
            'nome': 'Césio',
            'numero': 55,
            'peso': 132.91
        },
        'Ba': {
            'nome': 'Bário',
            'numero': 56,
            'peso': 137.33
        },
        'La': {
            'nome': 'Lantânio',
            'numero': 57,
            'peso': 138.91
        },
        'Ce': {
            'nome': 'Cério',
            'numero': 58,
            'peso': 140.12
        },
        'Pr': {
            'nome': 'Praseodímio',
            'numero': 59,
            'peso': 140.91
        },
        'Nd': {
            'nome': 'Neodímio',
            'numero': 60,
            'peso': 144.24
        },
        'Pm': {
            'nome': 'Promécio',
            'numero': 61,
            'peso': 145.00
        },
        'Sm': {
            'nome': 'Samário',
            'numero': 62,
            'peso': 150.36
        },
        'Eu': {
            'nome': 'Európio',
            'numero': 63,
            'peso': 151.96
        },
        'Gd': {
            'nome': 'Gadolínio',
            'numero': 64,
            'peso': 157.25
        },
        'Tb': {
            'nome': 'Térbio',
            'numero': 65,
            'peso': 158.93
        },
        'Dy': {
            'nome': 'Disprósio',
            'numero': 66,
            'peso': 162.50
        },
        'Ho': {
            'nome': 'Hólmio',
            'numero': 67,
            'peso': 164.93
        },
        'Er': {
            'nome': 'Érbio',
            'numero': 68,
            'peso': 167.26
        },
        'Tm': {
            'nome': 'Túlio',
            'numero': 69,
            'peso': 168.93
        },
        'Yb': {
            'nome': 'Itérbio',
            'numero': 70,
            'peso': 173.04
        },
        'Lu': {
            'nome': 'Lutécio',
            'numero': 71,
            'peso': 174.97
        },
        'Hf': {
            'nome': 'Háfnio',
            'numero': 72,
            'peso': 178.49
        },
        'Ta': {
            'nome': 'Tântalo',
            'numero': 73,
            'peso': 180.95
        },
        'W': {
            'nome': 'Tungstênio',
            'numero': 74,
            'peso': 183.84
        },
        'Re': {
            'nome': 'Rênio',
            'numero': 75,
            'peso': 186.21
        },
        'Os': {
            'nome': 'Ósmio',
            'numero': 76,
            'peso': 190.23
        },
        'Ir': {
            'nome': 'Irídio',
            'numero': 77,
            'peso': 192.22
        },
        'pt': {
            'nome': 'Platina',
            'numero': 78,
            'peso': 195.08
        },
        'Au': {
            'nome': 'Ouro',
            'numero': 79,
            'peso': 197.00
        },
        'Hg': {
            'nome': 'Mercúrio',
            'numero': 80,
            'peso': 200.59
        },
        'Tl': {
            'nome': 'Tálio',
            'numero': 81,
            'peso': 204.38
        },
        'Pb': {
            'nome': 'Chumbo',
            'numero': 82,
            'peso': 207.20
        },
        'Bi': {
            'nome': 'Bismuto',
            'numero': 83,
            'peso': 208.98
        },
        'Po': {
            'nome': 'Polônio',
            'numero': 84,
            'peso': 209.00
        },
        'At': {
            'nome': 'Astato',
            'numero': 85,
            'peso': 210.00
        },
        'Rn': {
            'nome': 'Radônio',
            'numero': 86,
            'peso': 222.00
        },
        'Fr': {
            'nome': 'Frâncio',
            'numero': 87,
            'peso': 223.00
        },
        'Ra': {
            'nome': 'Radiênio',
            'numero': 88,
            'peso': 226.00
        },
        'Ac': {
            'nome': 'Actínio',
            'numero': 89,
            'peso': 227.00
        },
        'Th': {
            'nome': 'Tório',
            'numero': 90,
            'peso': 232.04
        },
        'Pa': {
            'nome': 'Protactínio',
            'numero': 91,
            'peso': 231.04
        },
        'U': {
            'nome': 'Urânio',
            'numero': 92,
            'peso': 238.03
        },
        'Np': {
            'nome': 'Neptúnio',
            'numero': 93,
            'peso': 237.05
        },
        'Pu': {
            'nome': 'Plutônio',
            'numero': 94,
            'peso': 244.06
        },
        'Am': {
            'nome': 'Amerício',
            'numero': 95,
            'peso': 243.06
        },
        'Cm': {
            'nome': 'Cúrio',
            'numero': 96,
            'peso': 247.07
        },
        'Bk': {
            'nome': 'Berquélio',
            'numero': 97,
            'peso': 247.07
        },
        'Cf': {
            'nome': 'Califórnio',
            'numero': 98,
            'peso': 251.08
        },
        'Es': {
            'nome': 'Einstênio',
            'numero': 99,
            'peso': 252.08
        },
        'Fm': {
            'nome': 'Férmio',
            'numero': 100,
            'peso': 257.10
        },
        'Md': {
            'nome': 'Mendelévio',
            'numero': 101,
            'peso': 258.10
        },
        'No': {
            'nome': 'Nobélio',
            'numero': 102,
            'peso': 259.10
        },
        'Lr': {
            'nome': 'Laurêncio',
            'numero': 103,
            'peso': 262.11
        },
        'Rf': {
            'nome': 'Rutherfórdio',
            'numero': 104,
            'peso': 267.12
        },
        'Db': {
            'nome': 'Dúbnio',
            'numero': 105,
            'peso': 270.13
        },
        'Sg': {
            'nome': 'Seabórgio',
            'numero': 106,
            'peso': 271.13
        },
        'Bh': {
            'nome': 'Bóhrio',
            'numero': 107,
            'peso': 270.13
        },
        'Hs': {
            'nome': 'Hássio',
            'numero': 108,
            'peso': 277.15
        },
        'Mt': {
            'nome': 'Meitnério',
            'numero': 109,
            'peso': 276.15
        },
        'Ds': {
            'nome': 'Darmstádio',
            'numero': 110,
            'peso': 281.16
        },
        'Rg': {
            'nome': 'Roentgênio',
            'numero': 111,
            'peso': 282.17
        },
        'Cn': {
            'nome': 'Copernício',
            'numero': 112,
            'peso': 285.18
        },
        'Nh': {
            'nome': 'Nihônio',
            'numero': 113,
            'peso': 286.18
        },
        'Fl': {
            'nome': 'Fleróvio',
            'numero': 114,
            'peso': 289.19
        },
        'Mc': {
            'nome': 'Moscóvio',
            'numero': 115,
            'peso': 290.19
        },
        'Lv': {
            'nome': 'Livermório',
            'numero': 116,
            'peso': 293.20
        },
        'Ts': {
            'nome': 'Tenessino',
            'numero': 117,
            'peso': 294.20
        },
        'Og': {
            'nome': 'Oganessônio',
            'numero': 118,
            'peso': 294.21
        },
    }

    sigla = str(input(Fore.BLACK + 'Digite a sigla: ')).capitalize()

    if sigla in tabela_periodica:
        info = tabela_periodica[sigla]
        print(Fore.YELLOW + f'Nome: {info["nome"]}')
        print(Fore.BLUE + f'numero: {info["numero"]}')
        print(Fore.CYAN + f'peso: {info["peso"]}')

    else:
        print(Fore.LIGHTRED_EX + 'Sigla inválida.')

    resposta = input(Fore.BLACK + "Deseja continuar? (s/n): ").strip().lower()
    if resposta != 's':
        print(Fore.RED + "Fechando codigo...")
        break
