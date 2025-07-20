from os.path import curdir
from random import *
import tkinter
from tkinter import *

import customtkinter as ctk
import pygame
from PIL import Image, ImageTk
from PIL.ImageOps import expand
from customtkinter import CTkLabel
from tkinter import messagebox
import copy
from pygame import *


pygame.init()
mixer.init()

tela = Tk()
tela.title("Quem quer ser Médico? (Versão Beta)")
tela.config(background="#0068b7")
tela.geometry("1440x900")
tela.minsize(800, 600)
tela.iconbitmap("Assets/Images/Simbolo_da_medicina.ico")

dificuldade = ""
range_ratio = 0

def shuffle_dict_with_return(dicionário):

    global Questions

    keys = []
    new_dict = {}

    for k in dicionário.keys():
        keys.append(k)

    shuffle(keys)
    for k in keys:
        new_dict[k] = ""

    for k, v in dicionário.items():
        for k2 in new_dict.keys():
            if k == k2:
                new_dict[k2] = v

    return new_dict


def load_60_question(dicion, dificulty):
    # Bring the dictionaries keys


    dicion = shuffle_dict_with_return(dicion)
    keys = list(dicion.keys())

    # Delete Questions

    if dificulty == "Fácil":

        x = len(dicion)
        break_point = 25
        y = 0

        for i in range(x):
            y += 1
            if y == break_point:
                break

        range_ratio = x - y

        for i in range(range_ratio):
            del dicion[keys[i]]

    elif dificulty == "Normal":

        x = len(dicion)
        break_point = 60
        y = 0

        for i in range(x):
            y += 1
            if y == break_point:
                break

        range_ratio = x - y

        for i in range(range_ratio):
            del dicion[keys[i]]
    else:

        x = len(dicion)
        break_point = 200
        y = 0

        for i in range(x):
            y += 1
            if y == break_point:
                break

        range_ratio = x - y

        for i in range(range_ratio):
            del dicion[keys[i]]


    return dicion

# Questions Variables Section

Questions_General_Questions = {

    #General Questions

    "Qual é o maior osso do corpo humano?": ['Rádio', 'Estribo', 'Etmoide', '*Fêmur'],
    "onde se realiza a gluconeogêneses?": ['*Fígado', 'Baço', 'Cérebro', 'Músculo liso'],
    "qual é o maior orgão do corpo humano?": ['Paratiroides', '*Pele', 'Pulmão', 'Fêmur'],
    "onde se localiza a veia basilar?": ['*Antebraço', 'Pelvis', 'Perna', 'Braço'],
    "qual é a função do miocardio?": ['*Contração', 'Homeostasia', 'Leucotitopoieses', 'Hematose'],
    "quais são as moleculas de baixo peso molecular que participam na #formação de Marcomoleculas que ajudam na transmissão# e conservação do material genético?": ['Monossacarídeos', 'Lipoproteínas', '*Ácidos nucleicos', 'Aminoácidos'],
    "as enzimas aceleram a velocidade das reações#químicas dimnuindo?...": ['A energia de aceleração',
                                                                                          '*A energia de activação',
                                                                                          'A energia Potencial Química',
                                                                                          'A energia de absorção'],
    "a tradução é um processo que ocorre#principalmente a nível de que organelo?": ['*Núcleo', 'Mitocôndrias', 'Reticulo endoplasmático Rugoso', 'Ribossoma'],
    "as junturas fibrosas classificam-se em:": ['*Suturais, Sindesmose, Gonfose', 'Suturais, Escamosa, Sínfise', 'Sindesmose, Sincondrose, Gonfose', 'Sidesmose, Suturais, Escamosas'],
    "qual dos seguintes processos corresponde a processos de#destruição hística, uma vez morto o organismo ou a#separar dele?": ['Inclusão',
                                                                                           'Corte',
                                                                                           '*Fixação',
                                                                                           'Coloração'],
    "tecido avascularizado que contem células capazes#de gerar Potenciais de ação?": ['Conjuntivo', 'Muscular', 'Esquelético',
                                                                                '*Nervoso'],
    "tem função de absorção e proteção e suas células#descansam sobre uma membrana basal?": ['*Tecido Epitelial',
                                                                                               'Tecido Muscular',
                                                                                               'Tecido cartilaginoso',
                                                                                               'Tecido Nervoso'],
    "tecido em que suas células estão dispostas em#forma de rede unidas entre si através de estruturas denominadas#discos intercalares e citoplasma abundante em#glucogénio?": ['Tecido muscalar liso',
                                                                                                      '*Tecido Muscular cardíaco',
                                                                                                      'Tecido Reticuloendotelial',
                                                                                                      'Tecido tiroideo'],
    "um dos músculos responsáveis pela retração da#mandíbula?": ['*Músculo Pterigoide Medial',
                                                                                           'Esternocleidomastoideo',
                                                                                           'Platisma',
                                                                                           'Auricular Anterior'],
    "qual delas pode ser classificada como uma articulação do#tipo sutura?": [
                      'Articulação Temporo-Mandibular', 'Radio-Ulnal', 'Talocural',
                      '*Lambda'],

    "um dos músculos responsável pela abdução e rotação#medial do braço?": ['Deltoides', 'Tríceps Braquial', 'Braquial', '*Peitoral Maior'],

    "os núcleos Somáticos Motores se localizam em que#parte da Medula Espinhal": ['*Anterior',
                                                                                               'Posterior',
                                                                                               'Superior',
                                                                                               'Medial'],
    "selecione a opção que contém os certos elementos#da camada fibrosa do olho.": ['*Esclera, córnea',
                                                                                                      'Glándula lacrimal, Tecido adiposo, osso nasal',
                                                                                                      'Coriodes, coprpo ciliar e cilios',
                                                                                                      'Retina, Pálpebra, Órbita'],

    "qual é o componente do ciclo de krebs que recebe#regulação alosterica pela presensa de ATP": ['*Desidrogenasa Isocítrica',
                                                                                               'Citrato Sintetasa',
                                                                                               'Ácido alfa-cetoglutarato',
                                                                                               'Énzima Málica'],
    "um tipo de aferência que o sistema espinotalámico#apresenta é: ": ['Toques Discrimitivos', 'Vibrações', '*Dor',
                                                                                'Propiocepção'],

    "hormona responsável pela mielinização das fibras#nervosas?": [
                         'Prolactina', '*Triodotironina', 'Testosterona', 'GH Growth Hormone'],

    "uma das susbstâncias que se conjuga com a heparina e contribui#como um fator anticoagulante do sangue é?": ['*Anti-Trombina III',
                                                                                                      'Proteína C',
                                                                                                      'Proteína Kinasa R',
                                                                                                      'Trombina'],

    "qual é o organelo resposnsável pela respiração#celular?": ['*Mitocôndrias', 'Membrana Celular', 'RER', 'Peroxissomas'], "dentre as opções qual é o osso que se comunica#com o esfenoides": ['Ulna', '*Occipital', 'Hiodes', 'Mandibular'], "anatomicamente o corpo humano possui aproximadamente#quantos ossos?": ['208', '*206', '197', '252'], "qual é o maior glândula mista do corpo humano": ['*Pâncreas', 'Fígado', 'Timo', 'Hipófises'], "em que glândulas ocrre a síntese e excreção de#catecolaminas": ['Rins', 'Pâncreas', 'Parotida', '*Adrenais'],
    "qual das seguintes opções é um aminoácido essencial?": ['Arginina', 'Histidina', '*Fenilalanina', 'Alanina'],
    "que tipo de células se encontram na camada#molecular do cerebelo?": ['Células de Kupffer', 'Megacariocítos', 'Neuroglias', '*Células Estreladas e células em Cesta'], "a Triodotironina e Tiroxina é segregada a nível donde?": ['Parótida', 'Timo', 'Paratiroides', '*Tiroides'], "qual das seguintes opções segrega gastrina que estimula#a prododução de ácido cloridritco no estomago?": ['*Pâncreas', 'Fígado', 'Vesícula Biliar', 'Hipotálamo'], "qual das seguintes é um dos componentes da#barreira hematotesticular?": ['*Células de Sertoli', 'Células de Leyding', 'Testosterona', 'Plexo Pampiriforme'], "na etapa folicular do ciclo ovariano é induzida#a secrecção de qual hormona?": ['*Estrogênio', 'Progesterona', 'Lactogéno Placentário', 'Oxcitoxina'],
    'a classificação da articulação Temporo-Mandibular#(ATM) é do tipo:': ["*Juntura sinovial condilar biaxial", "Juntura cartilaginosa do tipo sincondrose", "Juntura fibrosa do tipo gonfose", "Juntura sinovial plana monoaxial"],
    "funções biológicas dos ossos são:" : ['*Metabolismo mineral, Hematopoiesis', 'Sínteses de Cálcio', 'Armazenamento de Na e Fe', 'Diferenciação de células Epiteliais'],
    "detalhes anatômicos do osso esfenoides são:" : ['*Seia turca, Sulco quiasmático, Canal óptico', 'Foramen oval, Dorso da seia turca, Lámina Perpendicular', 'Fossita Hipofisária, Processo Clinoide Posterior, Processo Corioideo', 'Lámina Perpendicular, Dorso da Seia Turca, Canal óptico'],
    "a abertura piriforme é uma estrutura que#se encontra na:" :  ['*Cavidade Nasal', 'Cavidade Orbital', 'Cavidade Oral', 'Cavidade Auricular'],
    "a maioria das vertebras possui essencialmente#quais das seguintes caracteristicas?" :  ['*Corpo vertebral, Arco vertebral e Processos ou Apófises', 'Arco Vertebral, Foramen Vertebral e Processos Espinhosos', 'Foramen Vertebral, Arco Vertebral e Foramen Magno', 'Processos Espinhosos, Espinha Bífida e Fossa Vertebral'],
    "as costelas apresentam 2 porções, uma posterior mais# longa e a outra anterior mais curta, quais das#opções coincide com a prévia afirmação?" :  ['*Osso costal e Cartilagem Costal', 'Sulco costal e Tubérculo', 'Ângulo costal e Sulco costal', 'Cabeça e Colo'],
    "um dos ossos do membro superior que tem como um de#seus detalhes anatômicos o “Olecrânio”?" : ['*Ulna', 'Rádio', 'Úmero', 'Pisiforme'],
    "a articulcão coxo-femoral é formada pela união#do osso ilíaco e fêmur, porém, por meio de#quais estruturas isso acontece?" : ['*Cabeça do fêmur e Cara simlunar do acetábulo', 'Cabeça do fêmur e foramen obturador', 'Trocanter do fêmur e foramen obturador', 'Foramen Obturador e Colo do fêmur'],
    "um músculo anterior do pescoço suprahiodeo é:" : ['*Digástrico', 'Esternohioideo', 'Tirohioideo', 'Omohioideo'],
    "um dos músculos superficiais do pescoço que é#auxiliar da respiração é o:" : ['*Esternocleidomastoideo', 'Platisma', 'Escaleno Anterior', 'Longo de Pescoço'],
    "qual é o músculo mais forte do corpo humano?" : ['*Masseter', 'Quadriceps Femoral', 'Bíceps Braquial', 'Pectorallis Majoris'],
    "o músculo diafragma grande músculo da respiração,#é principalmente inervado por qual nervo?" : ['*Nervo Frénico', 'Nervo Vago', 'Nervos Intercostais', 'Nervo Pudendo'],
    "qual dos músculos do tórax abaixo aproximam a escápula#à linha medeia e a mantêm em posição#junto ao serrato anterior?" : ['*Romboides maior e menor', 'Elevador da Escápula', 'Trapézio', 'Dorsal longo'],
    "um músculo da cara superficial Anterior do#antebraço é:" : ['*Pronador Redondo', 'Pronador Quadrado', 'Braquiorradial', 'Supinador'],
    "os aminoácidos são ácidos orgânicos que apresentam#ao menos um grupo carboxilo e um#amino unidos a seu: " : ['*Carbono alfa', 'Carbono beta', 'Carbono gama', 'Carbono sigma'],
    "segundo a posição do grupo carbonilo os#monossacarídeos se classificam em:" : ['*Aldosas e Cetosas', 'Triosas e maltosas', 'Tetrosas e Pentosas', 'Hexosas e manosas'],
    "as Caracteristicas gerais das macromolecas são:Alto peso#molecular, carácter polimérico, caráter uniforme, caráter#linear, caráter tridimensional, caráter informacional… :" : ['*Relação estrutura função e Tendência à agregação', 'Ativação molecular e Conformação específica', 'Seletividade de acção e agregação macromolecular', 'Neutralização e Migração molecular'],
    "os principais tipos de interações debeis são:#uniões salinas ou ionicas, pontes de#hidrogénio, forças de van der waals e:" : ['*Uniões hidrofóbicas', 'Pontes disulfuro', 'Ligação Polar', 'Ligação apolar'],
    "segundo o modelo secundário de DNA de Watson e#Crick o DNA consiste em duas cadeias de desoxirribonucleótideos#enroladas ao longo de um eixo comun, em forma de#dupla hélice com giro à direita..." : ['*Antiparalelas', 'Paralelas', 'Perpendiculares', 'Isométricas'],
    "os lípidos caracterizam-se por terem escassa#solubilidade em água e alta solubilidade em: " : ['*Componentes apolares', 'Componentes polares', 'Glicongênio', 'Permanganato de Potássio'],
    'quais são os lipídios mais abundantes#na natureza e que constituem o#principal lipídio da dieta humana?': ["*Triacilglicérideos", "Ácidos gordos", "Colesterol", "Fosfoglicéridos"],
    'os lípidos que em um meio polar formam complexos nos que#as regiões polares estão em contato com a água e as#regiões hidrofóbicas ou apolares se dispõem para#o interior chamam-se?' : ["*Anfípaticos", "Apolares", "Micelas", "Esfingolípidos"],
    'qual o tipo de tranposte que se caracteriza#por ser contra o gradiente e requerer o#uso de prteínas?' : ["*Transporte activo", "Transporte passivo", "Difusão simples", "Difusão por canais"],
    'a estrutura do centro activo de uma enzima é#formada por esqueleto peptídico, grupos de#ambientação, grupos de fixação e: ' : ["*Grupos catalíticos", "Grupo Proteíco", "Centro enzimático", "Grupo catabólico"],
    'uma vitamina hidrosolúvel é: ' : ["*Vitamina C", "Vitamina A", "Vitamina D", "Vitamina K"],
    'se uma enzima tiver um pequeno valor de Km#alcança a  máxima eficiência catalítica à...' : ["*Baixas Concentrações", "Altas Concentrações", "Normais Concentrações", "Nenhuma Concentração"],
    'qual o parametro cinético que representa#uma medida da afinidade da enzima pelo#substrato? ' : ["*Constante de Michaelis", "Velocidade Máxima", "Concentração de Substrato", "Eficiência Catalítica"],
    'sobre os mecanismos de regulação enzimática,#os mecanismos que modificam a atividade#enzimática são: Modificação alostérica e:' :  ["*Modificação Covalente", "Repressão", "Indução Enzimática", "Modifcação Conformacional"],
    'o enlace covalente responsavél pela polimerização# de ácidos nucleicos denomina-se: ' :  ["*3’ 5’ fosfodiéster", "5’ 3’ fosfodiéster", "5’ 3’ fosfoéster", "3’ 5´ fosfoéster"],
    'qual o nome da enzima que converte o ácido#oxalacético em ácido cítrico?' : ["*Sintetasa Cítrica", "Desidrogenasa Isocítrica", "Desidrogenasa málica", "Piruvato Carboxilasa"],
    'diga o processo mediante o qual os equivalentes de redução,#quer dizer, os hidrogénios ou electrões dos cofactores reduzidos#, provenientes do ciclo do Krebs e outras vias metabólicas,#reagem com o oxigénio de forma gradual, formando água e#liberando energia.' : ["*Cadeia Transportadora de Electrões", "Ciclo de Krebs", "Fosoforilação Oxidativa", "Respiração Celular"],
    'qual das teorias abaixo afirma o seguinte:#o potencial electroquímico deste gradiente é#aproveitado para sintetizar  ATP' : ["*Teoria Quimioosmótica", "Teoria Celular", "Teoria Electroquímica", "Teoria da Relatividade"],
    "qual término se refere à capacidade de certas células#de transformar-se em uma grande variedade de#tipos celulares?" : ['*Potencialidade celular', 'Diferenciação celular', 'Especialização celular', 'Compartimentação celular'],
    "quais são os organelos essencialmente caracteristicos de#todas as células?" : ['*Membrana celular, citoplasma e material genético', 'Núcleo, Reticulo endoplasmático e Lisossomas', 'Citoplasma, Complexo de golgi e Núcleo', 'Mitocôndrias, citoplasmas e Núcleo'],
    "qual é o organelo caracteristico das células que condiciona#a compartimentação destas: " : ['*Membrana celular', 'Núcleo', 'Citoesqueleto', 'Parede Celular'],
    "principais componentes das membranas biológicas são: " : ['*Proteínas, lipidos e glícidos',  'Colesterol, Fosfolípidos e Glicolípidos',  'Glicopreteínas, Proteínas Periféricas e Proteínas Integrais' ,  'Miscelas, Glicogénio e Colesterol'],
    "fluidez que permite que os lipídios e as proteínas possam#efetuar movimentos dentro da bicapa, corresponde à: " : ['*Modelo do Mosaico Fluido', 'Modelo da bicapa Glícida', 'Modelo da Bicamada Proteica', 'Modelo de Thomson'],
    "que célula conhece-se classicamente por apresentar seu material#genético envolvido pela carioteca?" : ['*Célula Eucariota', 'Célula Procariota', 'Célula Protozoária', 'Célula Vegetal'],
    "que célula conhece-se classicamente por não apresentar seu#material genético envolvido pela carioteca?" : ['Célula Eucariota', '*Célula Procariota', 'Célula Protozoária', 'Célula Vegetal'],
    "dois organelos não membranosos são: " : ['*Ribossomos e centriolos', 'Lisossomos e peroxissomos', 'Membrana plasmática e Retículo Rugoso', 'Núcleo e Microtúbulos'],

}

Questions_Histologia_I = {
#Histologia I
                       "qual é a origem embrionária correta do tecido epitelial?": [
                           "*Endodermo, Ectodermo e Mesodermo",
                           "Mesodermo",
                           "Ectodermo",
                           "Endodermo"
                       ],
                       "componentes comuns aos tecidos básicos são: células, matriz#extracelular e:": [
                           "*Líquido Tisular",
                           "Proteínas extracelulares",
                           "Glicosaminoglicanos",
                           "Lipoproteínas"
                       ],
                       "a substância fundamental amorfa está formada por essencialmente#por qual das seguintes substâncias?": [
                           "*Fibras",
                           "Glicoproteínas",
                           "Glicosaminoglicanos",
                           "Proteoglicanos"
                       ],
                       "qual o componente mais desenvolvido no modelo da célula secretora#de glicoproteína ou mucoproteína?": [
                           "*Aparelho de Golgi",
                           "Mitocôndria",
                           "Reticuloendoplasmático Rugoso",
                           "Granulos de Secreção"
                       ],
                       "que tipo de fibras caracterizam-se por serem ramificadas e formam#um trançado firme que liga o tecido conjuntivo aos#tecidos vizinhos.": [
                           "*Fibras reticulares",
                           "Fibras elasticas",
                           "Fibras colagénas",
                           "Fibras Cardíacas"
                       ],

    "o tecido conjuntivo denso modelado também pode ser conhecido#como:": ["*Tendinoso", "Fibroso", "Cartilaginoso", "Ósseo"],
    "uma das características importante do tecido conjuntivo é:": ["*Conectar os tecidos", "Carece de vasos snaguíneos", "Presença de estriações", "Grande coesão celular"],
    "suas células descançam sobre uma lámina basal:": ["*Tecido epitelial", "Tecido Conjuntivo", "Tecido Muscular", "Tecido Nervoso"],
    "quando a célula destroe-se junto com o produto#da secreção, pode ser classificada como:": ["*Holócrina", "Merócrina", "Apócrina", "Serosa"],
    "que tipo de variedade de tecido muscular se caracteriza#por ter células multinucleadas (até 35 núcleos em 1mm#de longitude) com forma ovalada e situados até à#periferia.": ["Tecido Muscular Liso", "Tecido Muscular Cardíaco", "*Tecido Muscular Estriado Esquelético", "Tecido Muscular Estriado Liso"],
}

Questions_Histologia_II = {
#Histologia II
    "qual é a função das células da glia#no tecido nervoso?": ["*Suporte e proteção aos neurônios", "Condução dos impulsos nervosos", "Produção de neurotransmissores", "Transmissão de sinais elétricos"],
    "o que são as células de Schwann?": ["*Células que formam a mielina no sistema nervoso periférico", "Células que conduzem impulsos nervosos", "Células do sistema nervoso central que protegem os neurônios", "Células que produzem neurotransmissores"],
    "qual é a função das células da microglia?": ["*Realizar a defesa imunológica no sistema nervoso central", "Conduzir impulsos elétricos", "Produzir mielina", "Suporte estrutural para os neurônios"],
    "qual é a principal função dos astrócitos#no cérebro?": ["*Suporte estrutural e manutenção da barreira hematoencefálica", "Condução do impulso nervoso", "Produção de mielina e de anticorpos para defesa", "Defesas imunológicas e fagocitose de microorganismos"],
    "qual estrutura do cérebro é composta por matéria#cinza e tem a função de processar e integrar informações#sensoriais e motoras?": ["*Córtex cerebral", "Corpo caloso", "Substância branca", "Cerebelo"],
    "a substância branca no cérebro é composta#principalmente por...": ["*Axônios mielinizados", "Corpos celulares de neurônios", "Sinapses", "Dendritos"],
    "o que caracteriza a camada de células de#Purkinje no cerebelo?": ["*São células grandes e com extensos dendritos", "Que secretam neurotransmissores", "Que conduzem impulsos nervosos", "Que formam a substância branca do cerebelo"],
    "o que compõe a substância cinza do cerebelo?": ["*Células de Purkinje e células granulares", "Axônios mielinizados", "Somente axônios", "Somente dendritos"],
    "qual a principal característica das#células granulares do cerebelo?": ["*São pequenas e formam sinapses com as células de Purkinje", "São grandes e responsáveis pela produção de mielina", "São células da glia que formam a barreira hematoencefálica", "São células responsáveis pela defesa imunológica"],
    "qual é a função das fibras paralelas no#cerebelo?": ["*Transmitir sinais das células granulares para as células de Purkinje", "Produzir mielina para facilitar a condução do impulso nervoso", "Conduzir impulsos nervosos aos músculos", "Processar informações sensoriais"],
    "o que caracteriza a camada molecular do#cerebelo?": ["*Fibras nervosas e células de estrelas", "Células de Purkinje e axônios", "Corpos celulares de células granulares", "Axônios mielinizados e altamente excitavéis"],
    "a medula espinhal é composta#principalmente por...": ["*Substância cinza e substância branca", "Células de Purkinje e astrócitos", "Células da microglia e oligodendrócitos", "Axônios mielinizados e células epiteliais"],
    "a substância cinza na medula espinhal é#composta por...": ["*Corpos celulares de neurônios e dendritos", "Axônios mielinizados e altamente excitaveis", "Fibras nervosas muito extensas e rápidas", "Células gliais"],
    "onde ocorrem as sinapses nas fibras#nervosas da medula espinhal?": ["*Na substância cinza", "Na substância branca", "Nos nervos periféricos", "Nos músculos esqueléticos"],
    "qual célula da glia é responsável pela#produção de mielina na medula espinhal?": ["*Oligodendrócitos", "Astrócitos", "Células de Schwann", "Microglia"],
    "a medula espinhal é protegida por três#camadas de tecidos conhecidos como...": ["*Meninges", "Músculos esqueléticos", "Epitélio", "Cartilagem"],
    "a principal função da medula espinhal é...": ["*Transmitir impulsos nervosos entre o cérebro e o corpo", "Produzir hormônios que ajudam na neurotransmissão", "Regular a produção de mielina", "Controlar a respiração mediante impulsos nervosos"],
    "qual é a principal função da substância#branca na medula espinhal?": ["*Condução dos impulsos nervosos", "Processamento de informações sensoriais", "Produção de neurotransmissores", "Defesa imunológica"],
    "qual camada das meninges é a mais#externa e resistente?": ["*Dura-máter", "Pia-máter", "Aracnoide", "Substância branca"],
    "qual é a principal função da aracnoide#nas meninges?": ["*Amortecer impactos e permitir a circulação do líquido cefalorraquidiano", "Proteger o cérebro contra infecções", "Produzir mielina que aumenta a atividade do sistema nervoso", "Conectar os hemisférios cerebrais"],
    "a pia-máter, que é a camada mais interna#das meninges, tem como principal função...": ["*Apoiar e nutrir o sistema nervoso central", "Produzir mielina", "Conectar os nervos periféricos ao sistema nervoso central", "Proteger o cérebro contra infecções"],
                       "o líquido cefalorraquidiano circula entre quais camadas das meninges?": [
                           "*Entre a aracnoide e a pia-máter", "Entre a dura-máter e a aracnoide",
                           "Dentro da dura-máter", "Dentro do cérebro"],
                       "qual das meninges é responsável por envolver#diretamente o cérebro e a medula espinhal?": [
                           "*Pia-máter", "Dura-máter", "Aracnoide", "Epêndima"],
                       "o sistema nervoso periférico é composto por...": ["*Nervos e gânglios",
                                                                          "Células de Purkinje e axônios",
                                                                          "Fibras mielinizadas do cérebro",
                                                                          "Córtex cerebral e medula espinhal"],
                       "o que são os gânglios no sistema nervoso#periférico?": [
                           "*Conjuntos de corpos celulares de neurônios", "Axônios mielinizados altamente excitaveis", "Células gliais",
                           "Fibras nervosas que conduzem impulsos"],
                       "qual é a função dos nervos no sistema nervoso#periférico?": [
                           "*Conduzir impulsos nervosos entre o sistema nervoso central e o corpo", "Produzir mielina que ajuda na actividade nervosa",
                           "Regular os batimentos cardíacos", "Armazenar neurotransmissores"],
                       "qual tipo de nervo no sistema nervoso periférico#transporta informações sensoriais para o sistema nervoso#central?": [
                           "*Nervos aferentes", "Nervos eferentes", "Nervos motores", "Nervos mistos"],
                       "o que são os corpúsculos de Pacini e onde estão#localizados?": [
                           "*Receptores sensoriais que detectam pressão e vibração",
                           "Receptores sensoriais de luz localizados na retina",
                           "Receptores responsáveis pela percepção de som localizados na cóclea",
                           "Receptores de dor localizados nas articulações"],
                       "o que são os mecanorreceptores e qual é sua função?": [
                           "*Receptores sensoriais que detectam estímulos como pressão e vibração",
                           "Receptores que detectam luz e se localizam na retina", "Receptores responsáveis pela percepção de calor",
                           "Receptores que percebem o sabor"],
                       "os receptores auditivos são encontrados#em qual parte do ouvido?": ["*Côclea",
                                                                                            "Pavilhão auricular",
                                                                                            "Canal auditivo externo",
                                                                                            "Trompa de Eustáquio"],
                       "qual é a principal função dos receptores do#equilíbrio no ouvido interno?": [
                           "*Manter a estabilidade e o equilíbrio do corpo", "Detectar sons de alta frequência",
                           "Captar odores do ambiente", "Perceber as vibrações do som e adaptá-las"],

                       "onde estão localizadas as células alfa e beta no#pâncreas, que produzem hormônios como insulina#e glucagon?": [
                           "*Nos ilhotas de Langerhans", "Na cápsula adrenal", "No córtex da glândula tireoide",
                           "No fígado"],
                       "qual parte da glândula tireoide é composta por#células que produzem os hormônios tiroxina (T4) e#triiodotironina (T3)?": [
                           "*Os folículos tireoidianos", "As células alfa das ilhotas pancreáticas",
                           "As células cromafins da medula adrenal", "Os ductos das glândulas salivárias"],
                       "o que caracteriza as células da hipófise#anterior (adenohipófise)?": [
                           "*Elas produzem hormônios que regulam outras glândulas endócrinas",
                           "Elas secretam adrenalina que regula a pressão arterial", "Elas produzem hormônios relacionados ao sistema nervoso",
                           "Elas produzem insulina e glucagon que ajudam no metabolismo"],
                       "a glândula pineal é responsável pela secreção#de qual hormônio?": ["*Melatonina", "Adrenalina",
                                                                                           "Cortisol", "Insulina"],
                       "quais células da glândula adrenal estão localizadas#na região externa (córtex) e são responsáveis pela secreção de corticosteroides?": [
                           "*Células do córtex adrenal", "Células da medula adrenal", "Células da hipófise anterior",
                           "Células do pâncreas"],
                       "as glândulas endócrinas liberam seus produtos diretamente#para...": ["*A corrente sanguínea",
                                                                                             "Os ductos de excreção",
                                                                                             "O ambiente externo",
                                                                                             "Os nervos periféricos"],
                       "qual tipo de epitélio está presente nos túbulos#seminíferos, onde ocorre a espermatogênese?": [
                           "*Epitélio germinativo", "Epitélio simples cúbico",
                           "Epitélio pseudoestratificado cilíndrico", "Epitélio estratificado pavimentoso"],
                       "o epitélio presente no epidídimo é do tipo...": [
                           "*Epitélio pseudoestratificado cilíndrico com células ciliadas e células basais",
                           "Epitélio simples cuboide", "Epitélio estratificado pavimentoso", "Epitélio simples colunar pseudostratificado revestido com queratina"],
                       "qual é o tipo de epitélio que reveste a parede do#ducto deferente?": [
                           "*Epitélio pseudoestratificado cilíndrico", "Epitélio estratificado cuboide",
                           "Epitélio simples cilíndrico", "Epitélio estratificado pavimentoso"],
                       "o que caracteriza o tecido muscular encontrado nas#paredes dos ductos deferentes?": [
                           "*Músculo liso", "Músculo esquelético", "Músculo estriado cardíaco", "Tecido conjuntivo"],
                       "qual é o tipo de epitélio que reveste a#glândula prostática?": [
                           "*Epitélio glandular cuboide ou cilíndrico", "Epitélio simples cúbico",
                           "Epitélio estratificado pavimentoso", "Epitélio pseudocolunar"],
                       "as células de Sertoli, presentes nos túbulos#seminíferos, são sustentadas por que tipo de tecido?": [
                           "*Tecido conjuntivo frouxo", "Tecido epitelial", "Tecido muscular liso", "Tecido nervoso"],
                       "qual é a principal característica das células#de Leyding localizadas no interstício testicular?": [
                           "*Elas possuem muitas mitocôndrias e produzem testosterona",
                           "Elas são grandes e secretam espermatozoides", "Elas secretam líquido seminal",
                           "Elas são células germinativas"],
                       "o epitélio que reveste a mucosa do útero#(endométrio) é do tipo...": [
                           "*Epitélio cilíndrico simples", "Epitélio pavimentoso estratificado",
                           "Epitélio cuboide simples", "Epitélio pseudoestratificado"],
                       "qual tipo de epitélio reveste a vagina?": [
                           "*Epitélio estratificado pavimentoso não queratinizado", "Epitélio simples cúbico queratinizado",
                           "Epitélio cilíndrico simples", "Epitélio pseudoestratificado não queratinizado"],
                       "o epitélio que reveste as trompas#de Falópio é...": [
                           "*Epitélio cilíndrico simples com células ciliadas", "Epitélio pavimentoso estratificado",
                           "Epitélio cuboide simples", "Epitélio estratificado pavimentoso"],
                       "o epitélio presente nos folículos ovarianos#(em torno dos oócitos) é do tipo...": [
                           "*Epitélio cúbico ou plano simples", "Epitélio estratificado pavimentoso",
                           "Epitélio cilíndrico simples", "Epitélio pseudoestratificado"],
                       "o tipo de tecido presente no corpo do útero,#que envolve o endométrio, é...": [
                           "*Tecido muscular liso (miométrio)", "Tecido conjuntivo denso",
                           "Tecido epitelial estratificado", "Tecido nervoso"],
                       "a camada interna do colo do útero#(canal cervical)é revestida por...": [
                           "*Epitélio cilíndrico simples", "Epitélio estratificado pavimentoso",
                           "Epitélio simples cuboide", "Epitélio pseudoestratificado"],
"qual tipo de epitélio reveste a superfície externa#do ovário?": ['*epitélio simples cúbico (ou mesotelial)', 'epitélio simples cilíndrico queratinizado', 'epitélio estratificado pavimentoso', 'epitélio pseudoestratificado'],
    "o tecido que forma as glândulas mamárias,#responsáveis pela secreção de leite, é...": ['*tecido glandular (epitelial)', 'tecido muscular liso', 'tecido adiposo especial', 'tecido conjuntivo frouxo'],
    "o epitélio presente no interior da#glândula mamária é...": ['*epitélio cuboide ou cilíndrico', 'epitélio estratificado pavimentoso', 'epitélio simples cúbico', 'epitélio pseudoestratificado cilíndrico'],
    "qual é o tipo de tecido encontrado na#camada externa do útero (serosa ou peritônio)?": ['*tecido epitelial simples pavimentoso (mesotélio)', 'tecido muscular liso', 'tecido conjuntivo denso modular', 'tecido epitelial simples cúbico (queratinzado)'],
"que caracteriza os glóbulos vermelhos (hemácias)?": ['possuem núcleo e são de forma bicôncova', '*são anucleados e possuem forma bicôncava', 'são esféricos e possuem núcleo', 'contêm várias mitocôndrias'],
    "onde as células sanguíneas são originadas#durante o desenvolvimento fetal?": ['nos pulmões', '*no fígado e baço', 'nos ossos e medula óssea', 'nos rins'],
    "o que caracteriza a medula óssea hematopoética?": ['é rica em tecido adiposo e pro-eritroblastos', '*é rica em células precursoras das linhagens sanguíneas', 'contém fibras colágenas', 'não possui células especializadas'],
    "o que é a eritropoese?": ['produção de leucócitos (Células brancas)', '*produção de glóbulos vermelhos', 'produção de plaquetas', 'produção de linfócitos'],
    "quais são os componentes principais do#plasma sanguíneo?": ['glóbulos vermelhos e plaquetas', '*água, proteínas, glicose, hormônios e resíduos', 'leucócitos, plaquetas, água e sais minerais(Na+, Ca+, Fe++...)', 'células-tronco hematopoéticas'],
    "qual tipo de tecido compõe o miocárdio?": ['tecido epitelial', '*muscular estriado cardíaco', 'muscular estriado esquelético', 'tecido muscular liso'],
    "o que caracteriza as células do miocárdio?": ['elas são multinucleadas e possuem estriações', '*elas possuem estriações e um único núcleo', 'elas são semelhantes às células musculares esqueléticas', 'elas são anucleadas'],
    "onde estão localizados os discos intercalares nas#células do miocárdio?": ['no núcleo celular', '*nas junções entre as células musculares cardíacas', 'no sarcoplasma', 'na região do retículo sarcoplasmático'],
    "qual é a principal função das células#musculares cardíacas?": ['produzir sangue', '*contrair para bombear o sangue', 'secretar hormônios como o péptideo natriuretico atrial', 'absorver nutrientes'],
    "qual tipo de tecido compõe as#válvulas cardíacas?": ['tecido muscular cardíaco', '*tecido conjuntivo denso', 'tecido epitelial', 'tecido conjuntivo elástico'],
    "quais são as características das fibras musculares#cardíacas em comparação com as musculares esqueléticas?": ['elas possuem mais mitocôndrias e mais gordura que ajuda na contracção', '*elas são menores, ramificadas e possuem discos intercalares', 'elas são mais longas e multinucleadas', 'elas são anucleadas'],
    "qual é o tipo de tecido predominante nas camadas#mais internas das artérias?": ['epitélio simples cuboide queratinizado', '*endotélio (epitélio simples pavimentoso)', 'tecido muscular estriado', 'tecido conjuntivo denso'],
    "qual é a principal característica das paredes#das veias em comparação com as artérias?": ['mais espessas e com menos fibras musculares', '*mais finas e com menos fibras musculares', 'mais elásticas', 'mais grossas e rígidas'],
    "o que caracteriza as células do endotélio#nos vasos sanguíneos?": ['elas são musculares', '*elas são planas e formam uma camada contínua', 'elas possuem estriações', 'elas são muito grandes e multinucleadas'],
"o que é a camada média (túnica média) dos#vasos sanguíneos composta?": ["epitélio", "*músculo liso e fibras elásticas", "tecido conjuntivo denso modular", "células endoteliais"],
    "onde os vasos linfáticos se originam?": ["nos órgãos", "*nos capilares linfáticos", "nas veias", "no coração"],
    "qual é o tipo de tecido predominante nas#cápsulas dos linfonodos?": ["tecido epitelial", "*tecido conjuntivo denso", "tecido muscular liso", "tecido adiposo"],
    "qual é a principal função do baço no#sistema imunológico?": ["produzir células sanguíneas", "*filtrar o sangue e remover células velhas ou danificadas", "produzir linfa que ajuda na esplenomegalia", "regular a temperatura corporal"],
    "onde os linfócitos b amadurecem?": ["nos linfonodos", "*na medula óssea", "no timo", "no baço e no fígado"],
    "o que são as zonas corticais nos linfonodos?": ["áreas onde os linfócitos t se acumulam", "*áreas ricas em linfócitos b e células dendríticas", "áreas de circulação sanguínea", "áreas de medula óssea"],
    "qual célula do tecido linfóide é responsável#pela fagocitose?": ["células t", "*células dendríticas", "células b", "macrófagos"],
    "qual é a função dos linfonodos no#sistema imunológico?": ["produzir glóbulos vermelhos", "*filtrar a linfa e ativar as células imunes", "produzir hormônios e anticorpos", "regular a temperatura do corpo"],
    "qual é a característica do tecido#linfóide no baço?": ["ele produz linfa", "*ele filtra o sangue e elimina células sanguíneas velhas", "ele regula a produção de anticorpos e activa o sistem imune", "ele armazena proteínas plasmáticas como globulinas"],
    "quais estruturas são encontradas no#tecido linfóide secundário?": ["macrófagos, mastócitos e células assassinas naturais", "*linfócitos, macrófagos, células dendríticas", "células assassinas naturais e mastócitos", "placas de gordura"],
    "qual tipo de epitélio reveste a#cavidade nasal?": ["epitélio escamoso estratificado", "*epitélio pseudoestratificado ciliado colunar", "epitélio simples cuboide", "epitélio simples pavimentoso pseudoestratificado"],
"qual é a função das células ciliadas nas#vias respiratórias?": ["produzir muco que netraliza patogênos", "*mover partículas e muco para fora das vias respiratórias", "secretar enzimas que combatem microorganismos áereos", "absorver oxigênio"],
    "o que caracteriza o epitélio alveolar?": ["é formado por células epiteliais colunares pseudoestratificadas", "*é formado principalmente por células simples pavimentosas", "possui cílios especilizados na filtração", "tem células mucosas especializadas"],
    "o que caracteriza os brônquios em termos#de histologia?": ["possuem apenas epitélio pavimentoso", "*possuem epitélio ciliado e cartilagem hialina", "são formados apenas por músculo liso", "são revestidos por tecido conjuntivo"],
    "qual célula é responsável pela produção de#surfactante nos pulmões?": ["células endoteliais", "células de clara", "*células alveolares tipo ii", "células t"],
    "o que caracteriza o epitélio do túbulo#contornado distal?": ["é simples e pavimentoso", "*é simples cúbico e sem microvilosidades", "é estratificado", "é pseudoestratificado"],
    "qual é a função do sistema mesangial#no glomérulo?": ["reabsorver água", "*manter a estrutura do glomérulo e filtrar resíduos", "produzir urina", "controlar o fluxo sanguíneo renal"],
    "qual é o tipo de epitélio presente#no túbulo coletor?": ["epitélio simples pavimentoso", "*epitélio cúbico ou colunar, dependendo da região", "epitélio estratificado", "epitélio de transição"],
    "quais células são responsáveis pela#troca de íons no túbulo proximal?": ["células mesangiais", "*células epiteliais com microvilosidades", "células endoteliais", "células musculares lisas"],
    "qual é o tipo de epitélio que reveste#a mucosa da boca?": ["epitélio colunar simples", "*epitélio estratificado escamoso", "epitélio pseudoestratificado", "epitélio cuboide"],
    "o que caracteriza o epitélio do estômago?": ["é estratificado e escamoso", "*é simples colunar com células mucosas", "é cilíndrico com microvilosidades", "é simples cúbico"],
    "qual tipo de glândulas são encontradas#na submucosa do esôfago?": ["glândulas salivares", "*glândulas mucosas", "glândulas sebáceas", "glândulas exócrinas"],
    "qual é a função principal das células#principais no estômago?": ["produzir muco", "*produzir pepsinogênio", "secretar ácido clorídrico", "absorver nutrientes"],
    "qual célula na mucosa gástrica é responsável#pela secreção de ácido clorídrico?": ["células de paneth", "*células parietais", "células enterocromafins", "células do estroma"],
    "qual é o tipo de tecido que compõe as#vilosidades intestinais?": ["teclado muscular estriado", "*tecido conjuntivo frouxo com epitélio columnar", "tecido epitelial cúbico", "tecido elástico"],
    "qual é a principal função das células#de paneth no intestino delgado?": ["produzir muco", "*produzir enzimas antimicrobianas", "fagocitar patógenos", "produzir hormônios digestivos"],
    "qual é a principal função das células musculares#lisas na camada muscular do trato digestivo?": ["produzir enzimas digestivas", "*conduzir movimentos peristálticos", "regular a secreção de muco", "secretar hormônios intestinais"],
    "qual tipo de epitélio reveste o esôfago?": ["epitélio colunar", "*epitélio estratificado escamoso não queratinizado", "epitélio cilíndrico", "epitélio pavimentoso queratinizado"],
    "qual é a função das células enteroendócrinas#no intestino?": ["produzir suco gástrico", "*liberar hormônios que controlam a motilidade e secreção digestiva", "absorver nutrientes", "fagocitar micro-organismos"],
    "qual é o tipo de epitélio que compõe#a epiderme?": ["epitélio colunar", "*epitélio estratificado escamoso queratinizado", "epitélio cuboide", "epitélio simples pavimentoso"],
"qual célula na epiderme é responsável pela#produção de queratina?": ["melanócitos", "*queratinócitos", "células de langerhans", "células de merkel"],
    "qual é a principal função dos#melanócitos na epiderme?": ["produzir queratina", "*produzir melanina", "secretar suor", "formar a barreira lipídica"],
    "qual é a camada da epiderme onde os queratinócitos#começam a morrer e formar a camada córnea?": ["camada basal", "*camada espinhosa", "camada granulosa", "camada córnea"],
    "qual é a função das células de#langerhans na epiderme?": ["produzir queratina", "*atuar na resposta imunológica", "secretar melanina", "regular a produção de sebo"],
    "onde estão localizadas as glândulas#sebáceas?": ["na derme profunda", "*na derme, próximas aos folículos pilosos", "na epiderme", "na camada hipodérmica"],
    "qual é a principal função das glândulas#sudoríparas ecrinas?": ["produzir sebo", "*produzir suor para controle térmico", "secretar hormônios", "lubrificar a pele"],
    "qual é o tipo de tecido que compõe a#hipoderme?": ["tecido epitelial", "*tecido adiposo e conjuntivo frouxo", "tecido muscular liso", "tecido cartilaginoso"],
    "qual camada da pele é responsável pela troca de#nutrientes e oxigênio entre a epiderme e a derme?": ["camada espinhosa", "*membrana basal", "camada córnea", "camada papilar"],
    "onde as fibras de colágeno são predominantes#na pele?": ["na epiderme", "*na derme reticulada", "na hipoderme", "na camada córnea"],
    "qual estrutura da pele é responsável pela#formação dos pelos?": ["glândulas sebáceas", "*folículo piloso", "glândula sudorípara", "camada basal"],
}

Questions_Anatomia_II = {

#Anatomia II
"do ponto de vista ontogenético o sistema nervoso#central pose ser classificado como:": ["*Somático e visceral", "Central e periférico", "Segmentar e suprasegmentar", "Vida de relação e vegetativo"],
    "porções do tronco encefálico são:": ["*Medula Oblonga, ponte e mesencéfalo", "Cinthila óptica, Sulco Protuberancial inferior e Decusação piramidal", "Medula Oblonga, cinthila óptica e Ponte", "Formação reticular, ponte e bulbotálamo"],
    "funções do cerebelo são: equilíbrio corporal,#cordenação dos movimentos e:": ["*Regulação do tonus muscular", "Mecanismos de sono e vigilância", "Mecanismos de atenção e orientação", "Controle da entrada aferente"],
    "os núcelos do cerebelo são: núcleo denteado,#núcleo do teto, núcleo globoso e:": ["*Núcleo emboliforme", "Núcleo do globo pálido", "Núcleo putamen", "Núcleo Lenticular"],
    "porções do diencéfalo são:": ["*Talamoencéfalo e hipotálamo", "Tálamo e epitálamo", "Metalámo e quiásma óptico", "Infundibulo e hipófise"],
    "o telencéfalo possui 5 lóbulos que são: frontal,#parietal, occipital, temporal e:": ["*Lóbulo da ínsula", "Lóbulo Caudado", "Lóbulo amigdalino", "Lóbulo cortical"],
    "os núcleos da base do telencéfalo são:": ["*Corpo estriado, claustro e amigdalino", "Caudado, putamen e globo pálido", "Lenticular, caudado e globo pálido", "Denteado, teto e globoso"],
    "a saída do crânio do nervo vago se dá#através de qual foramen?": ["*Foramen jugular", "Foramen Magno", "Foramen Oval", "Foramen estilomastoideo"],
"o nervo mediano é ramo importante de#qual plexo?": ["*Plexo braquial", "Plexo Cervical", "Plexo Sacral", "Plexo Lombar"],
    "o nervo femoral é um ramo importante de#qual plexo?": ["*Plexo lombar", "Plexo Sacral", "Plexo Braquial", "Plexo Sacral"],
    "qual é o maior de todos os plexos?": ["*Plexo sacral", "Plexo lombar", "Plexo Braquial", "Plexo cervical"],
    "qual é a principal função do funículo#espermático?": ["*Suspenção dos testiculos", "Maturação dos espermatozoides", "Comunicação com o epidídimo", "Conducção dos espermatozoides"],
    "em qual das seguintes estruturas ocorre a#fecundação?": ["*Trompas de Falópio", "Útero", "Vagina", "Ovários"],
}

Questions_Anatomia_III = {
    # Anatomia III

    "qual estrutura no coração é responsável#pela iniciação do impulso elétrico que desencadeia a#contração?": [
        '*nódulo sinoatrial (nodo sa)', 'nódulo atrioventricular (nodo av)', 'feixe de his', 'fibras de purkinje'],
    "qual é o principal vaso sanguíneo que#transporta sangue do coração para o resto do#corpo?": ['*aorta',
                                                                                                  'artéria pulmonar',
                                                                                                  'vena cava inferior',
                                                                                                  'veia jugular'],
    "o sistema de condução do coração é#responsável por...": [
        '*controlar os batimentos cardíacos e a contração do coração', 'aumentar o volume sanguíneo e a atividade eléctrica',
        'regular a pressão arterial aumentando a volemia', 'garantir a oxigenação do sangue graças a contração'],
    "qual é o nome da válvula que separa#o átrio esquerdo do ventrículo esquerdo?": ['*válvula mitral',
                                                                                     'válvula tricúspide',
                                                                                     'válvula pulmonar',
                                                                                     'válvula aórtica'],
    "qual é a função principal do sistema#cardiovascular?": [
        '*transportar oxigênio, nutrientes, hormônios e resíduos através do corpo', 'produzir sangue para transporte de electrolitos',
        'regular a temperatura corporal porque o sangue é quente', 'controlar a distribuição de produtos residuais'],
    "o coração é composto por quantos#átrios e ventrículos?": ['*dois átrios e dois ventrículos',
                                                               'um átrio e um ventrículo',
                                                               'três átrios e dois ventrículos',
                                                               'dois átrios e um ventrículo'],
    "a artéria aorta se divide em três partes principais. qual#delas está localizada entre o ventrículo esquerdo e a curva#da aorta?": [
        '*aorta ascendente', 'aorta torácica', 'aorta abdominal', 'aorta subclávia'],
    "qual é a função da válvula aórtica, localizada na#base da artéria aorta?": [
        '*evitar o retorno do sangue para o ventrículo esquerdo após a sístole',
        'impedir o fluxo de sangue desoxigenado para os pulmões', 'regular a pressão arterial prevenindo hipertensão',
        'controlar a quantidade de oxigênio no sangue'],
    "a aorta torácica, que é uma parte da artéria aorta,#passa por qual região do corpo?": [
        '*pelo tórax, abaixo da clavícula', 'pela cavidade abdominal', 'ao redor do pescoço', 'pela cabeça e pescoço'],
    "a artéria aorta se ramifica para fornecer#sangue para quais regiões do corpo?": [
        '*para todos os órgãos e tecidos do corpo', 'apenas para o cérebro e pulmões',
        'somente para os membros inferiores', 'para os músculos cardíacos e pulmões'],

    "a aorta abdominal é responsável por irrigar#quais partes do corpo?": ['*os órgãos abdominais e membros inferiores',
                                                                           'o cérebro e a cabeça',
                                                                           'o coração, pulmões e vários órgãos mediastinais',
                                                                           'o fígado e os rins'],
    "qual é o nome da estrutura que conecta a#artéria aorta à artéria pulmonar?": ['*o tronco pulmonar',
                                                                                   'o ducto arterioso',
                                                                                   'a válvula aórtica',
                                                                                   'a veia cava inferior'],
    "em que parte da artéria aorta ocorrem os#maiores picos de pressão sanguínea?": ['*na aorta ascendente',
                                                                                     'na aorta abdominal',
                                                                                     'na aorta torácica',
                                                                                     'na bifurcação da aorta'],


    "qual é a principal característica da parede#da artéria aorta?": [
        '*ela é composta por fibras elásticas que permitem sua distensão e contração',
        'ela é formada por tecido muscular liso que não permite distensão e elasticidade',
        'ela possui poucas fibras de colágeno, tornando-se rígida',
        'ela é composta por tecido ósseo para dar maior resistência'],

    "em casos de hipertensão, a artéria#aorta pode sofrer...": ['*aumento da rigidez e dilatação',
                                                                'aumento da elasticidade e complacencia', 'diminuição do diâmetro',
                                                                'diminuição do fluxo sanguíneo'],
    "as artérias carótidas são responsáveis#por fornecer sangue para...": ['*o cérebro', 'a parte inferior do corpo',
                                                                           'o sistema linfático',
                                                                           'os músculos esqueléticos'],
    "as artérias ilíacas comuns se originam#de qual artéria principal?": ['*a aorta abdominal', 'a artéria femoral',
                                                                          'a artéria carótida comum',
                                                                          'a veia cava inferior'],
    "as artérias ilíacas internas são responsáveis#por fornecer sangue para...": [
        '*a pelve e os órgãos reprodutores internos', 'o cérebro e medula espinhal', 'a parte inferior das pernas',
        'o sistema digestivo'],
    "a artéria ilíaca externa se divide em duas#principais ramificações. quais são elas?": [
        '*a artéria femoral e a artéria profunda da coxa', 'a artéria carótida interna e a artéria braquial',
        'a artéria poplítea e a artéria tibial', 'a artéria renal e a artéria mesentérica'],

    "a veia cava superior se forma pela#junção de quais vasos sanguíneos?": [
        '*veias braquiocefálicas direita e esquerda', 'artérias carótidas comuns direita e esquerda',
        'veias femorais direita e esquerda', 'veias ilíacas comuns direita e esquerda'],

    "a veia cava inferior é mais visível#em casos de...": ['*aumento da pressão venosa central',
                                                           'aumento da pressão arterial sistêmica',
                                                           'diminuição do retorno venoso', 'hipotensão arterial'],

    "o que conecta a faringe à laringe?": ['*a traqueia', 'o esôfago', 'o palato mole', 'a epiglote'],

    "o pulmão direito é dividido em#quantos lobos?": ['*três', 'dois', 'quatro', 'cinco'],

    "qual estrutura da laringe é responsável por#proteger a entrada das vias respiratórias durante a#deglutição?": [
        '*a epiglote', 'a glote', 'a traqueia', 'as cordas vocais'],

    "onde ocorre a troca gasosa entre o oxigênio e#o dióxido de carbono nos pulmões?": ['*nos alvéolos', 'na traqueia',
                                                                                        'nos brônquios', 'na laringe'],

    "qual é a principal função dos brônquios?": ['*conduzir o ar para os pulmões', 'realizar a troca gasosa',
                                                 'filtrar o ar purificando-o', 'produzir muco'],

    "a traqueia é formada por quantos#anéis cartilaginosos?": ['*de 16 a 20', '12 a 14', '22 a 24', '10 a 12'],

    "o que caracteriza as células alveolares#tipo I nos alvéolos pulmonares?": [
        '*elas são responsáveis pela troca gasosa', 'elas produzem surfactante', 'elas secretam muco',
        'elas ajudam na defesa imunológica'],

    "qual é o nome da estrutura que conecta#a traqueia aos pulmões?": ['*brônquios', 'alvéolos', 'laringes', 'faringe'],

    "em qual parte do aparelho respiratório se#encontram as cordas vocais?": ['*na laringe', 'na traqueia',
                                                                              'nos brônquios', 'nos alvéolos'],

    "qual estrutura forma a separação entre a#cavidade nasal e a nasofaringe?": ['*o palato mole', 'o septo nasal',
                                                                                 'a epiglote', 'o óstio nasal'],

    "a pleura parietal é responsável por#revestir qual parte do corpo?": ['*a parede torácica e o diafragma',
                                                                          'o pulmão e os brônquios',
                                                                          'a cavidade abdominal',
                                                                          'a cavidade nasal e a faringe'],

    "o que é a principal função do intestino#delgado?": ['*absorver nutrientes dos alimentos', 'produzir bile que ajuda na digestão dos lípidos',
                                                         'armazenar fezes', 'secretar enzimas digestivas'],

    "o intestino delgado é composto por três#partes. quais são essas partes?": ['*duodeno, jejuno e íleo',
                                                                                'cólon ascendente, cólon transverso e cólon descendente',
                                                                                'cólon sigmoide, reto e ânus',
                                                                                'esôfago, estômago e duodeno'],
    "o que caracteriza as vilosidades intestinais#do intestino delgado?": [
        '*aumentar a superfície de absorção de nutrientes', 'ajudam a secretar suco gástrico', 'ajudam a produzir bile',
        'auxiliar na digestão de proteínas'],

    "onde ocorre a maior parte da absorção dos nutrientes no sistema digestivo?": [
        '*no intestino delgado', 'no intestino grosso', 'no estômago', 'no cólon descendente'],

    "qual é a função do intestino grosso no#processo digestivo?": ['*absorver água e formar fezes',
                                                                   'secretar enzimas digestivas',
                                                                   'produzir bile e soluções hipoláticas',
                                                                   'absorver nutrientes'],

    "o que é o apêndice vermiforme?": ['*uma estrutura vestigial localizada no ceco',
                                       'uma parte do intestino grosso responsável pela absorção de água',
                                       'uma estrutura do intestino delgado',
                                       'uma glândula associada ao sistema digestivo'],

    "quais são as principais funções do#peritônio?": [
        '*revestir a cavidade abdominal e apoiar os órgãos abdominais', 'produzir suco gástrico',
        'absorver nutrientes', 'proteger a cavidade abdominal contra traumas intensos'],

    "o que é o mesentério?": [
        '*uma dobra do peritônio que sustenta e conecta o intestino delgado à parede abdominal',
        'um tipo de músculo do intestino grosso que ajuda na motilidade grastrointestinal', 'uma região do estômago',
        'uma estrutura que conecta o fígado ao intestino grosso'],

    "o que caracteriza o intestino grosso em#comparação ao intestino delgado?": [
        '*ele é mais largo, tem uma camada muscular mais espessa e não tem vilosidades intestinais',
        'ele é mais longo e mais estreito que o intestino delgado e tem vilosidades intestinais',
        'ele tem uma função predominantemente digestiva e não absorvente',
        'ele possui glândulas para secreção de sucos gástricos e ajuda na absorção de àgua'],

    "o que ocorre no ceco do intestino grosso?": [
        '*é a primeira parte do intestino grosso onde o alimento não digerido chega',
        'é a região onde a absorção de nutrientes ocorre bem como a de minerais e água',
        'é a parte onde ocorre a digestão dos alimentos', 'é a parte final do processo digestivo onde se formam as fezes'],

}

Questions_Bioquímica_II = {
#Bioquímica II
    "a digestão dos glicidos começa na boca#por acção de qual enzima?": ["*Alfa-amilasa-salivar", "Maltasa", "Alfa-dextrinas-limite", "Sacarasa"],
    "o transportador glut-5 pode ser transportador de#qual dos glicídos?": ["*Fructose", "Glicose", "Galactose", "Maltose"],
    "uma vez que a glucose penetra na célula qual é#seu principal destino?": ["*Fosforilação", "Glicolisis", "Glucnoneogêneses", "Oxidação"],
    "qual a enzima que fosoforila a glicose e a converte#em glucosa-6-fosfato e se encontra somente#no fígado?": ["*Glucoquinasa", "Hexoquinasa", "Glucosa-6-fosfatasa", "Glucosa-6-fosfato desidrogenasa"],
    "qual processo metabólico é responsável pela manutenção#dos níveis sanguíneos de glicose?": ["*Glicogenolisis hepática", "Glicolisis", "Glucogêneses", "Gluconeogêneses"],
    "quando a fructose-2,6-bisfosfatose encontra em#altas concentrações activa qual processo?": ["*Glicolise", "Gluconeogêneses", "Gligogêneses", "Glicogenolisis"],
    "qual via é conhecida como via de oxidação#direita da glicose?": ["*Via das pentosas", "Glicolise", "Ciclo de Krebs", "Glicogenolise"],
    "qual dos seguintes representa a principal forma#de energia armazenada no organismo:": ["*Lípidos", "Glicídos", "Proteínas", "Corpos cetônicos"],
    "para facilitar o metabolismo dos lípidos os sais#biliares funcionam como:": ["*Detergentes", "Redutores", "Biocatalizadores", "Reguladores"],

"qual é a enzima principal da digestão dos#triacilglicéridos no duodeno?": ["*Lipasa Pancreática", "Lipasa duodenal", "Lipasa Estomacal", "Lipasa Intestinal"],
    "percursos imediatos da lipogêneses são:": ["*Acil-CoA e Glicerol-3-Fosfato", "Ácidos gordos e Glicerol", "Acetil-CoA e Dihidroxiacetona Fosfato", "Ácidos gordos e glícidos"],
    "para sintetizar o ácido palmítico requer-se 14 moléculas de#nadph, as mesmas provêm de duas fontes fundamentais,#que são:": ["*Ciclo das pentosas e reação da enzima málica", "Ciclo de Krebs e Lipolise", "Ciclo da ureia e Glicolise", "Bicicleta de Krebs e Reação da Enzima Piruvato Kinasa"],
    "qual é a enzima reguladora da lipolise?": ["*Lipasa Hormona Sensível", "Carnitina acil transferasa I", "Carnitina Palmitil Transferasa II", "Lipasa Lingual"],
    "qual é o nome da principal enzima da#cetogêneses?": ["*HMG-CoA Sintetasa", "HMG-CoA Reductasa", "Tiolasa", "HMG-CoA Liasa"],
    "qual é o nome da enzima reguladora da#coleisteroidogêneses?": ["HMG-CoA Sintetasa", "*HMG-CoA Reductasa", "Tiolasa", "HMG-CoA Liasa"],
    "qual das seguintes lipoproteínas carrega a#maior quantidade de triacilglicéridos?": ["*Quilomicrones", "LDL (Low density lipoprotein)", "HDL (High density lipoprotein)", "IDL (Intermediate density lipoprotein)"],
    "uma das formas de ingestão de nitrogênio metabolicamente#útil ao organismo é através de:": ["*Aminoácidos", "Monossacarídeos", "Ácidos gordos", "Fructose-6-fosfato"],
    "qual é a enzima proteolítica primária do#estômago?": ["*Pepsina", "Elastasa", "Tripsina", "Quimiotripsina"],
    "a descarboxilação de aminoácidos é um processo#importante porque possibilita a formação de:": ["*Aminas biogênicas", "Cetoácidos", "Nitrogênio livre", "Outros aminoácidos"],
    "a fenilcetonúria é uma enfermidade metabólica#causada pela deficiência de:": ["*Enzima Fenilalanina Hidroxilasa", "Aminoácido fenilalanina", "Proteínas", "Aminoácido Tirosina"],
    "qual o nome da enzima que a partir de dióxido de#carbono e amoníaco sintetiza carbamil fosfato?": ["*Carbamil fosfato sintetasa II", "Carbamil fosfato sintetasa I", "Arginina Succinato Sintetasa", "Glutaminase"],
    "a síndrome de lesh nyhan é uma enfermidade relacionada#com o metabolismo dos nucleotídeos causada pela deficiência#de qual enzima?": ["*Hipoxantina Guanina Fosforibosil Transferasa", "Desoxirribonucleases", "Carbamil Fosfato Sintetasa II", "Adenina Fosforibosil Transferasa"],
    "os principais precursores do metabolismo das#porfirinas são:": ["*Succinil-CoA e Glicina", "Arginina e Ferro", "Succinato e Glicerol", "Acetil-CoA e Glucose"],
    "um exemplo de metabólito de encruzilhada é:": ["*Glucose-6-fosfato", "Gliceraldeído-3-fosfato", "Fructose-6-fosfato", "NADH"],
    "o amp cíclico atua alostericamente em qual enzima#desencadeando uma resposta de fosforilação?": ["*Proteínas Kinasas", "Adenil Ciclase", "Piruvato Carboxilase", "Glucogênio fosforilase"],
    "a maior parte de ATP no músculo é armazenada#em forma de quê?": ["*Fosfocreatina", "Creatina", "Glucogênio", "Trialcilglicéridos"],
    "muito lactato produzido pelo músculo esquelético é transportado#pelo sangue ao fígado, onde é usado para sintetizar#glucose. fala-se de qual processo?": ["*Ciclo de Cori", "Ciclo de Krebs", "Ciclo de Cahill", "Glicólise Anaeróbica"],
    "que tipo de diabetes se caracteriza por mutações que#provocam vários tipos de alterações em relação aos#receptores de insulina?": ["*Diabetes Mellitus tipo II", "Diabetes Mellitus tipo I", "Diabetes MODY", "Diabetes Gestacional"],
}

Questions_Médicina_Comunitária_I = {
    #Informática Médica
    "componentes da medicina familiar na APS são:#integralidade, continuidade e permanência,#acessibilidade, dispensarização, trabalho em equipe,#setorização…": ["*Participação Social e Comunitária", "Grupo Básico de Trabalho (GBT)", "Comunidade Saudável", "Atenção Primária de Saúde"],
    "a classificação da lavagem de mãos pode ser:#lavagem social das mãos, lavagem higiênico#ou médico das mãos e:": ["*Lavagem Cirúrgico das Mãos", "Lavagem Asséptica das mãos", "Lavagem Profissional das mãos", "Lavagem esterilizante das mãos"],
    "quais das opções é certa para as etapas do#metodo cientifico?": ["*Observaço, Hipótese e Verificação da hipótese", "Testes, Hipótese e Conclusão", "Experiência, Avaliação e Formulação", "Conjectura, Experiência e Formulação da tese"],
}

Questions_Médicina_Comunitária_II = {
    #Medicina Comunitária II
    "quais são as principais doenças tratadas#durante a dispensarização?": ["doenças infecciosas", "*doenças crônicas não transmissíveis", "doenças de transmissão sexual", "doenças relacionadas à nutrição"],
    "quem realiza a dispensarização na comunidade?": ["profissionais de farmácia e médicos de familia bastante especializados", "*equipes de saúde da família e profissionais de saúde comunitária", "médicos especialistas", "voluntários de saúde"],
    "quais informações são coletadas durante o#processo de dispensarização?": ["histórico de cirurgias", "*histórico de doenças crônicas", "histórico de gravidez", "histórico de doenças infecciosas"],
    "a dispensarização é principalmente realizada#em quais ambientes?": ["em hospitais e em bairros com baixo saneamento básico", "*em unidades de saúde comunitária e ambulatórios", "em clínicas privadas", "em escolas que necessitam de atendimento sanitário"],
    "quando ocorre a mudança mais significativa#para uma família durante a etapa de extensão?": ["quando os pais decidem se separar", "*quando nasce o primeiro filho", "quando o casal compra uma casa nova", "quando todos os filhos atingem a maioridade"],
    "quais fatores influenciam a transição da etapa#de formação para a extensão de uma família?": ["o planejamento de aposentadoria", "*o nascimento de filhos ou a adoção", "a mudança de residência para uma nova cidade", "a decisão de vender a casa"],

"o que caracteriza uma família nuclear?": ["é uma família com vários avós", "*é composta por pai, mãe e filhos", "é composta por irmãos e irmãs", "é composta por um único adulto com filhos"],
    "qual é a principal função da família#no contexto social?": ["controlar as finanças de seus membros", "*proteger e educar seus membros", "fornecer alimentação apenas", "organizar eventos sociais para a comunidade"],
    "na teoria sociológica, qual é o papel#da família nuclear?": ["fornecer apoio jurídico aos filhos", "*ser a unidade básica de socialização", "resolver conflitos entre a comunidade", "controlar a moralidade pública"],
    "qual é a principal função dos carboidratos#na alimentação?": ["servir como fonte de proteínas", "*fornecer energia para o corpo", "regenerar células musculares", "regular o equilíbrio hormonal"],

    "qual nutriente é responsável pela construção#e reparação dos tecidos?": ["vitaminas", "*proteínas", "carboidratos", "águas"],
    "qual é o papel das fibras alimentares#na saúde?": ["fornecer calorias e água para o corpo", "*auxiliar no funcionamento do sistema digestivo", "fornecer energia rápida", "regular os níveis de glicose no sangue"],
    "quais alimentos são ricos em vitamina c?": ["carnes vermelhas, leite e seus derivados", "*frutas cítricas como laranja, abacaxi e limão", "peixes e frutos do mar", "grãos, cereais e pão"],
    "qual é a principal função das vitaminas#na alimentação?": ["fornecer energia e ajudar a armazenar em forma de gordura", "*regular as funções metabólicas e proteger o organismo", "construir músculos ativando a creatina quinasa", "melhorar a digestão em especial a absorção"],
    "qual é a principal fonte de cálcio#na alimentação?": ["grãos e cereais", "*leite e derivados", "carne vermelha", "frutas e legumes"],
    "qual é a função principal da água#na alimentação?": ["fornecer energia e ajudar no funcionamento dos rins", "*manter o equilíbrio hídrico e auxiliar em reações químicas do corpo", "fornecer nutrientes essenciais em especial sais minerais", "ajudar na absorção de vitaminas"],
    "a atenção primária à saúde foca em#qual tipo de cuidados?": ["atendimento especializado", "*prevenção de doenças e promoção do bem-estar", "cuidados intensivos", "cirurgias de emergência"],
    "qual dos seguintes serviços faz parte#da atenção primária à saúde?": ["tratamento de câncer e doenças crônicas", "*consultas com médicos de família", "cirurgias ortopédicas", "atendimentos hospitalares de urgência"],
    "qual é o principal objetivo da prevenção#primária de enfermidades?": ["tratar doenças já instaladas", "*prevenir o aparecimento de doenças", "fornecer medicamentos para tratamento imediato", "diagnosticar doenças em estágios iniciais"],
    "o que caracteriza a prevenção secundária?": ["prevenção de doenças em indivíduos saudáveis", "*detecção precoce de doenças para tratamento imediato", "focar em cuidados paliativos", "evitar a progressão de doenças crônicas"],
    "qual é o tipo de vacina que utiliza#vírus ou bactérias enfraquecidos?": ["vacinas inativadas", "vacinas de rna mensageiro", "*vacinas de microrganismos vivos atenuados", "vacinas recombinantes"],
"qual vacina é indicada para prevenir#o tétano?": ["vacina bcg", "*vacina antitetânica", "vacina contra hepatite b", "vacina tríplice viral"],
    "qual é a função dos adjuvantes#em vacinas?": ["neutralizar os efeitos da vacina", "*aumentar a resposta imunológica à vacina", "diminuir a eficácia do antígeno", "reduzir os efeitos colaterais"],
    "o que caracteriza a vacina bcg?": ["é usada para prevenir hepatite", "*é usada para prevenir a tuberculose", "é usada para prevenir a difteria", "é usada para prevenir a poliomielite"],
    "qual é a primeira etapa do método#epidemiológico?": ["*identificação do problema de saúde", "coleta de dados secundários", "realização de intervenção", "avaliação do impacto da intervenção"],
    "qual é a etapa final do método#epidemiológico?": ["formação de novas hipóteses mediante testes e exprimentos", "*avaliação e implementação de intervenções baseadas nos achados", "recoleta de dados", "publicação de artigos científicos"]
}

Questions_Embriologia_I = {
#Embriologia I
"como se chama a série de divisões celulares mitóticas#do zigoto que resultam na formação das primeiras células#embrionárias – os blastômeros?": ["*Clivagem", "Diferenciação", "Implantação", "Gastrulação"],
    "em qual dos processos forma-se um disco embrionário#trilaminar (terceira semana)?": ["*Gastrulação", "Segmentação", "Morulação", "Blastulação"],
    "em qual das seguintes etapas ocorre a#determinação do sexo cromossômico?": ["*Fecundação", "Segmentação", "Blastulação", "Implantação"],
    "qual das seguintes estruturas é uma membrana#bastante vascularizada que envolve tanto o embrião quanto todos os#demais anexos embrionários, fornecendo proteção e#nutrição?": ["*Saco coriônico", "Pedículo embrionário", "Saco vitelino", "Cavidade amniótica"],
    "quais células produzem gonadotrofina coriônica humana#(HGC), que é responsável pela manutenção do corpo lúteo#durante os primeiros meses de gestação?": ["*Trofoblastos", "Citotrofoblasto", "Sinciciotrofoblastos", "Blastocistos"],
    "em que semana do desenvolvimento embrionário as#células dos alvéolos pulmonares iniciam a produção de#surfactante, uma substância que permitirá a respiração?": ["*24ª", "21ª", "22ª", "23ª"],
"qual é o nome do processo pelo qual o blastocisto se#fixa à parede do útero?": ["*Nidação", "Ovulação", "Clivagem", "Gastrulação"],
    "durante o desenvolvimento embrionário, qual é o#nome da estrutura que se forma antes da#gástrula?": ["*Blástula", "Zigoto", "Mórula", "Neurula"],
    "qual é o termo usado para a camada uterina que#forma a parte materna da placenta?": ["*Decídua", "Endométrio", "Miométrio", "Amniótico"],
    "qual é a principal função da placenta durante#a gestação?": ["*Trocas gasosas e nutricionais", "Produção de hormônios apenas", "Sustentação mecânica do feto", "Proteção imunológica completa"],
    "qual exame é usado para identificar precocemente#defeitos congênitos durante a gestação?": ["*Ultrassonografia", "Radiografia", "Tomografia computadorizada", "Hemograma completo"],
    "qual é a principal causa dos defeitos congênitos?": ["*Fatores genéticos e ambientais", "Exposição a antibióticos", "Exclusivamente herança genética", "Má nutrição apenas"],
    "qual é a síndrome causada pela exposição do#embrião ao álcool durante a gravidez?": ["*Síndrome alcoólica fetal", "Síndrome de Edwards", "Síndrome de Turner", "Síndrome de Patau"],

}

Questions_Embriologia_II = {
#Embriologia II
                       "durante o desenvolvimento embrionário, o tubo neural#se forma a partir de qual camada germinativa?": [
                           '*ectoderma', 'mesoderma', 'endoderma', 'epiderma'],
                       "o fechamento do tubo neural forma a base de#quais estruturas?": [
                           '*o cérebro e a medula espinhal', 'os ossos, músculos e tecido conjuntivo', 'o fígado e os rins',
                           'o sistema cardiovascular'],
                       "o que é a crista neural e qual é a sua#principal função no desenvolvimento?": [
                           '*formar células do sistema nervoso periférico', 'desenvolver a pele e os cabelos',
                           'criar o esqueleto axial e apendicular', 'produzir somente células glias e neurónios'],
                       "o que forma o sistema cardiovascular primitivo#durante o desenvolvimento embrionário?": [
                           '*o tubo cardíaco', 'o intestino primitivo', 'a medula óssea', 'o fígado'],
                       "qual é a função do ducto venoso no embrião?": [
                           '*desviar o sangue da veia umbilical diretamente para a veia cava inferior',
                           'transportar o oxigênio para os pulmões e dai acontecer a hematose pulmonar', 'absorver nutrientes da placenta',
                           'estabelecer a circulação pulmonar'],
                       "durante o desenvolvimento, o forame oval se#fecha após o nascimento, transformando-se em qual#estrutura?": [
                           '*fossa oval', 'veia cava superior', 'artéria pulmonar', 'aorta'],
                       "o intestino primitivo é formado a partir de#qual camada germinativa?": ['*endoderma',
                                                                                                'ectoderma',
                                                                                                'mesoderma',
                                                                                                'epiderma'],
                       "a formação do pâncreas embrionário ocorre#a partir de qual parte do intestino primitivo?": [
                           '*o duodeno', 'o jejuno', 'o ceco', 'o reto'],
                       "a formação da boca e do ânus durante o#desenvolvimento embrionário ocorre a partir#de que processo?": [
                           '*a formação de duas aberturas no intestino primitivo',
                           'a separação do tubo digestivo em partes distintas', 'o fechamento do tubo neural',
                           'o desenvolvimento das glândulas salivares'],
                       "o que origina os pulmões durante o#desenvolvimento embrionário?": [
                           '*a brotação do intestino anterior', 'a divisão do tubo neural',
                           'a diferenciação da mesoderma lateral', 'o crescimento do esôfago'],
                       "o que é o divertículo respiratório, e qual#é sua função no desenvolvimento do sistema#respiratório?": [
                           '*é a estrutura que dará origem aos pulmões', 'é a parte inicial do esôfago',
                           'a primeira parte do intestino grosso', 'a estrutura que forma o diafragma'],
                       "o sistema musculoesquelético deriva de#qual camada germinativa?": ['*mesoderma', 'ectoderma',
                                                                                           'endoderma', 'epiderma'],
                       "o que são os somitos e qual sua função#no desenvolvimento embrionário?": [
                           '*eles são blocos de mesoderma que formam os músculos e ossos',
                           'são responsáveis pela formação dos órgãos internos', 'são as células que formam a pele',
                           'são responsáveis pela formação do sistema nervoso'],
                       "o que forma a cartilagem durante o#desenvolvimento embrionário?": ['*o mesênquima',
                                                                                           'a ectoderme', 'o endoderma',
                                                                                           'o epitélio'],
                       "o sistema reprodutor masculino origina-se#a partir de qual parte do embrião?": [
                           '*gônadas indiferenciadas', 'mesênquima', 'endoderma', 'mesoderma lateral'],
                       "durante o desenvolvimento embrionário, qual#é a primeira estrutura que se diferencia para formar o#sistema reprodutor feminino?": [
                           '*as gônadas indiferenciadas', 'o ducto de Müller', 'o ducto de Wolff', 'o reto'],
                       "a diferenciação sexual no embrião ocorre#principalmente devido à ação de quais hormônios?": [
                           '*hormônios gonadotróficos', 'estrogênio e testosterona', 'insulina e cortisol',
                           'hormônios da tireoide'],
                       "o sistema urinário deriva de qual#camada germinativa?": ['*mesoderma', 'ectoderma', 'endoderma',
                                                                                 'epiderma'],
                       "o que é o sistema excretor embrionário primitivo#que se desenvolve antes dos rins?": [
                           '*os túbulos mesonéfricos', 'os túbulos renais', 'os ductos biliares',
                           'o sistema linfático'],
                       "durante o desenvolvimento embrionário,#onde se formam os rins?": ['*nas regiões lombares',
                                                                                          'na região pélvica',
                                                                                          'na região torácica',
                                                                                          'nas extremidades'],
                       "durante o desenvolvimento embrionário,#a musculatura esquelética é formada a#partir de qual estrutura?": [
                           '*somitos', 'mesênquima', 'dermátomo', 'notocorda'],
                       "o que são os miotomos e qual é sua função#no desenvolvimento do sistema muscular?": [
                           '*são blocos de mesoderma que dão origem aos músculos esqueléticos',
                           'são estruturas que formam a pele e glânduas sebáceas', 'são responsáveis pela formação dos ossos',
                           'são células do sistema nervoso periférico'],
                       "qual é o tipo de músculo que se origina#do mesênquima e não dos miotomos?": ['*músculo liso',
                                                                                                     'músculo esquelético',
                                                                                                     'músculo cardíaco',
                                                                                                     'músculo estriado'],

                       "a musculatura cardíaca é derivada#de qual parte do embrião?": ['*mesoderma', 'ectoderma',
                                                                                       'endoderma', 'epiderma'],

"a diferenciação da musculatura cardíaca começa#a partir de quais células durante o desenvolvimento?": ['*células do mesoderma', 'células da notocorda', 'células do ectoderma', 'células do endoderma'],
    "a musculatura lisa é originada de qual#camada germinativa?": ['*mesoderma', 'ectoderma', 'endoderma', 'epiderma'],
    "durante o desenvolvimento embrionário, o que é#responsável pela formação das cavidades do corpo?": ['*o mesoderma', 'o ectoderma', 'o endoderma', 'o epiderma'],
    "qual estrutura embrionária origina as cavidades corporais#primárias, como a cavidade torácica e a cavidade abdominal?": ['*o celoma', 'o tubo neural', 'o intestino primitivo', 'a notocorda'],
    "a cavidade pericárdica, onde o coração se desenvolverá,#origina-se de qual parte do embrião?": ['*o celoma', 'o tubo neural', 'o mesênquima', 'a camada ectodérmica'],
    "a cavidade abdominal e pélvica se desenvolvem a#partir de qual estrutura?": ['*o celoma intraembrionário', 'o tubo neural', 'o intestino primitivo', 'a camada ectodérmica'],
    "durante o desenvolvimento embrionário, a cavidade#pleural se forma ao redor de qual estrutura?": ['*os pulmões', 'o coração', 'o esôfago', 'o fígado'],
    "qual das seguintes cavidades se forma primeiro#durante o desenvolvimento do embrião?": ['*a cavidade pericárdica', 'a cavidade pleural', 'a cavidade abdominal', 'a cavidade pélvica'],
    "o que é a membrana serosa que reveste as cavidades#corporais durante o desenvolvimento embrionário?": ['*o peritônio', 'a pleura', 'o pericárdio', 'o mesotélio'],
    "qual é a função do celoma durante o#desenvolvimento embrionário?": ['*formar as cavidades corporais e dar origem a várias membranas serosas', 'proteger o embrião e nutri-lo durante todo seu desenvolvimento', 'regular a temperatura do embrião para melhor desenvolvimento', 'formar os ossos, músculos e tendões'],

}

Questions_Fisiologia_I = {
#Fisiologia I
"qual tipo de fibra nervosa é responsável por#conduzir sinais de dor rápida e aguda?": ["*Fibras A-delta", "Fibras C", "Fibras B", "Fibras A-beta"],
    "qual área do cérebro processa as informações#provenientes das sensações somáticas?": ["*Córtex somatossensorial", "Cerebelo", "Hipotálamo", "Corpo caloso"],
    "qual receptor está associado à percepção de#temperatura?": ["*Terminações nervosas livres", "Corpúsculo de Ruffini", "Fuso muscular", "Corpúsculo de Meissner"],
    "qual receptor somático é responsável por detectar#o estiramento muscular?": ["*Fuso muscular", "Órgão tendinoso de Golgi", "Disco de Merkel", "Corpúsculo de Pacini"],
    "o que ocorre quando há a ativação de nociceptores?": ["*Geração de sensações de dor", "Percepção de pressão profunda", "Sensação de calor", "Detecção de vibrações"],
    "qual é o nome do fenômeno em que uma dor visceral#é percebida como dor em uma região superficial#do corpo?": ["*Dor referida", "Dor fantasma", "Dor neuropática", "Dor crônica"],
    "qual estrutura do olho é responsável pela#maior parte da refração da luz?": ["*Córnea", "Cristalino", "Retina", "Íris"],
    "qual célula da retina é responsável pela#percepção de cores?": ["*Cones", "Bastonetes", "Células ganglionares", "Células bipolares"],
    "qual parte do cérebro processa informações#visuais recebidas da retina?": ["*Córtex occipital", "Tálamo", "Hipotálamo", "Córtex frontal"],
    "qual pigmento visual está presente nos#bastonetes?": ["*Rodopsina", "Iodopsina", "Melanopsina", "Retinol"],
    "qual é o nome da região da retina onde#a acuidade visual é mais alta?": ["*Fóvea central", "Disco óptico", "Periferia da retina", "Coroide"],
    "qual nervo transmite informações visuais#da retina para o cérebro?": ["*Nervo óptico", "Nervo oculomotor", "Nervo abducente", "Nervo troclear"],
    "qual condição ocorre quando o ponto focal#da luz não coincide corretamente com a retina?": ["*Erro refrativo", "Glaucoma", "Catarata", "Daltonismo"],
    "o que é responsável pela adaptação do#olho à luz e ao escuro?": ["*Mudança no tamanho da pupila e regeneração de pigmentos visuais", "Movimento dos bastonetes para a fóvea", "Alteração na forma da córnea", "Mudança na posição do cristalino"],
"qual é o nome da fase em que um novo#potencial de ação não pode ser gerado?": ["*Período refratário absoluto", "Período refratário relativo", "Período de latência", "Fase limiar"],
    "durante qual fase do potencial de ação#ocorre a saída de íons potássio (K⁺) da#célula?": ["*Repolarização", "Despolarização", "Hiperpolarização", "Potencial de repouso"],
    "qual fator aumenta a velocidade de propagação#do potencial de ação ao longo de um axônio?": ["*Presença de mielina", "Menor diâmetro do axônio", "Alta concentração de cloreto", "Ausência de canais de sódio"],
    "no músculo liso, qual proteína é ativada#pelo cálcio para iniciar a contração?": ["*Calmodulina", "Troponina C", "Tropomiosina", "Actina"],
    "qual das seguintes opções descreve melhor#o músculo liso?": ["*Contração lenta e sustentada", "Contração rápida e voluntária", "Estriado e multinucleado", "Depende exclusivamente de glicogênio para energia"],
    "qual proteína regula a ligação entre a#actina e a miosina no músculo esquelético?": ["*Tropomiosina", "Troponina", "Calmodulina", "Titina"],
    "qual é o principal tipo de receptor responsável#pela sensação de toque leve?": ["*Corpúsculo de Meissner", "Corpúsculo de Pacini", "Terminações nervosas livres", "Disco de Merkel"],
    "qual receptor sensorial detecta alterações#na pressão e vibrações profundas?": ["*Corpúsculo de Pacini", "Corpúsculo de Meissner", "Disco de Merkel", "Fuso muscular"],
    "qual papila gustativa é mais numerosa,#mas não possui botões gustativos?": ["*Filiforme", "Fungiforme", "Circunvalada", "Foliada"],
    "qual é o tipo de receptor responsável#pela percepção do sabor doce?": ["*Receptores acoplados à proteína G", "Canais iônicos de sódio", "Canais iônicos de cálcio", "Terminações nervosas livres"],
    "qual nervo craniano transmite informações#gustativas do terço posterior da língua?": ["*Nervo glossofaríngeo (IX)", "Nervo facial (VII)", "Nervo vago (X)", "Nervo trigêmeo (V)"],
"qual célula é responsável por captar#estímulos químicos no epitélio olfatório?": ["*Células receptoras olfatórias", "Células basais", "Células de sustentação", "Células mitrais"],
    "qual estrutura no cérebro é responsável#por processar informações olfativas?": ["*Bulbo olfatório", "Tálamo", "Hipotálamo", "Córtex somatossensorial"],
    "o que ocorre no epitélio olfatório para#gerar o sinal nervoso?": ["*Ligação de moléculas odorantes aos receptores acoplados à proteína G", "Abertura direta de canais de sódio por estímulo mecânico", "Conversão química de odores em luz", "Contração das células de sustentação"],
    "qual estrutura do ouvido transforma vibrações#mecânicas em sinais nervosos?": ["*Células ciliadas da cóclea", "Membrana timpânica", "Osso martelo", "Tuba auditiva"],
    "qual parte do ouvido é responsável por amplificar#as vibrações sonoras antes de chegarem à cóclea?": ["*Ossículos", "Tuba auditiva", "Membrana basilar", "Canal semicircular"],
    "qual é a função da membrana basilar na#audição?": ["*Separar frequências sonoras para ativar diferentes regiões da cóclea", "Proteger o ouvido interno e a cóclea de sons altos ou graves", "Impedir refluxo de fluidos na cóclea", "Transportar som diretamente ao nervo auditivo"],
    "qual região do cérebro é responsável pelo#planejamento e controle de movimentos#voluntários?": ["*Córtex motor primário", "Córtex pré-frontal", "Hipocampo", "Tálamo"],
    "qual é o nome do trato motor que controla#os movimentos voluntários dos músculos#esqueléticos?": ["*Trato corticoespinhal", "Trato espinocerebelar", "Trato vestibuloespinhal", "Trato rubroespinhal"],
    "qual estrutura no sistema nervoso é essencial#para a coordenação motora e equilíbrio?": ["*Cerebelo", "Hipotálamo", "Gânglios da base", "Medula espinhal"],
    "qual neurotransmissor é liberado na junção#neuromuscular para ativar o músculo#esquelético?": ["*Acetilcolina", "Dopamina", "Glutamato", "Noradrenalina"],
    "o que ocorre durante o reflexo miotático#(reflexo de estiramento)?": ["*O músculo se contrai em resposta ao seu alongamento", "O músculo relaxa para evitar lesões", "A medula espinhal inibe a resposta reflexa", "O cérebro controla diretamente a contração"],
    "qual estrutura é responsável pela inibição de#movimentos indesejados e regulação da tonicidade#muscular?": ["*Gânglios da base", "Tálamo", "Cerebelo", "Córtex motor suplementar"],
    "o que caracteriza um neurônio motor#inferior danificado?": ["*Paralisia flácida", "Paralisia espástica", "Hiperreflexia", "Tremor intencional"],
    "qual é o papel do córtex pré-motor?": ["*Planejar e preparar movimentos", "Executar movimentos reflexos", "Processar informações sensoriais", "Regular a frequência cardíaca durante o esforço físico"],
    "qual é a função principal dos motoneurônios#gama?": ["*Ajustar a sensibilidade dos fusos musculares", "Gerar força muscular", "Inibir reflexos musculares", "Estimular o relaxamento muscular"],
    "qual estrutura conecta o cerebelo ao tronco#encefálico?": ["*Pedúnculos cerebelares", "Corpo caloso", "Tálamo", "Nervos cranianos"],
    "o que acontece quando o cerebelo sofre danos?": ["*Perda de coordenação e equilíbrio", "Dificuldade em processar emoções", "Diminuição da capacidade de visão", "Dificuldade na memória verbal"],
    "qual parte do cerebelo é mais envolvida no#controle motor fino e na coordenação?": ["*Cerebelo anterior", "Lobo floculonodular", "Lobo posterior", "Vermis"],
    "o que é a ataxia cerebelar?": ["*Perda de coordenação muscular devido a danos no cerebelo", "Deficiência visual associada a danos no cerebelo", "Dificuldade respiratória causada por lesão cerebelar", "Perda de consciência devido à falha do cerebelo"],
    "qual parte do córtex cerebral é responsável pelo#processamento de informações sensoriais, como#tato e dor?": ["*Córtex somatossensorial", "Córtex visual", "Córtex auditivo", "Córtex motor primário"],
"qual área do córtex é responsável pela#produção da fala?": ["*Área de Broca", "Área de Wernicke", "Córtex auditivo", "Córtex somatossensorial"],
    "onde está localizada a área de Wernicke,#e qual é sua função?": ["*No lobo temporal, associada à compreensão da linguagem", "No lobo frontal, associada à produção da fala", "No lobo occipital, associada à visão", "No lobo parietal, associada ao processamento espacial"],
    "o que caracteriza o córtex motor primário?": ["*Controla movimentos voluntários", "Processa estímulos táteis", "Regula funções visuais", "Recebe informações sobre temperatura"],
    "qual função está associada ao lobo frontal do#córtex cerebral?": ["*Planejamento e execução de movimentos", "Processamento de informações auditivas", "Percepção sensorial de dor", "Controle dos reflexos involuntários"],
    "qual das seguintes opções descreve a função#do sistema nervoso parassimpático?": ["*Promover o descanso e a digestão", "Preparar o corpo para o estresse", "Aumentar a frequência cardíaca", "Estimular a contração muscular esquelética"],
    "o que é a resposta 'luta ou fuga'?": ["*Ativação do sistema nervoso simpático em situações de estresse", "Ativação do sistema nervoso parassimpático para repouso", "Resposta reflexa à dor", "Resposta ao calor para controlar a temperatura corporal"],
    "qual órgão é um exemplo de alvo do#sistema nervoso autônomo?": ["*Coração", "Fígado", "Pulmão", "Estômago"],
    "em relação ao sistema nervoso autônomo, o#que significa 'dualidade' das ações do simpático#e parassimpático?": ["*Eles têm efeitos opostos sobre os órgãos-alvo", "Eles atuam no mesmo órgão para reforçar a resposta", "Eles apenas regulam funções sensoriais", "Eles não têm interações diretas"],
    "o que acontece quando há um bloqueio da atividade parassimpática?": ["*O corpo entra em um estado de excitação prolongada", "Diminui a frequência cardíaca e a pressão arterial", "O corpo entra em um estado de repouso", "A digestão é intensificada"],
    "qual neurotransmissor é liberado pelo sistema#nervoso parassimpático?": ["*Acetilcolina", "Noradrenalina", "Serotonina", "Glutamato"],
    "qual estrutura no cérebro controla o#sistema nervoso autônomo?": ["*Hipotálamo", "Córtex cerebral", "Cerebelo", "Tronco encefálico"],
    "qual glândula é responsável pela produção#do hormônio de crescimento (GH)?": ["*Glândula pituitária anterior", "Glândula tireoide", "Pâncreas", "Glândula adrenal"],
    "o que o hormônio de crescimento (GH)#estimula principalmente no corpo?": ["*Crescimento ósseo e muscular", "Produção de leite", "Metabolismo de carboidratos", "Função imunológica"],
    "qual é o principal efeito do GH nos#ossos?": ["*Estímulo do alongamento ósseo", "Redução da mineralização óssea", "Aumento da densidade óssea", "Inibição da formação de cartilagem"],
    "qual é a condição associada à produção#excessiva de hormônio de crescimento na infância?": ["*Gigantismo", "Acromegalia", "Nanismo", "Hipotireoidismo"],
    "qual é a principal função do GH no#metabolismo de lipídios?": ["*Aumento da lipólise", "Estimulo à síntese de gordura", "Redução do consumo de lipídios", "Inibição da utilização de gorduras como fonte de energia"],
    "qual é a função principal dos hormônios#tireoidianos (T3 e T4)?": ["*Regulação do metabolismo corporal", "Aumento da produção de leite", "Estimulo à secreção de GH", "Regulação da função hepática"],
    "o que ocorre em caso de hipotireoidismo?": ["*Diminuição da taxa metabólica e ganho de peso", "Aumento da frequência cardíaca e perda de peso", "Aumento da temperatura corporal e insônia", "Produção excessiva de energia"],
    "qual é o papel do iodo na síntese#dos hormônios tireoidianos?": ["*Ele é necessário para a formação de T3 e T4", "Ele inibe a produção de hormônios tireoidianos", "Ele ativa a conversão de T4 em T3", "Ele é um precursor de calcitonina"],
"qual é a condição associada à produção excessiva#de hormônios tireoidianos?": ["*Hipertireoidismo", "Hipotireoidismo", "Tireoidite", "Bócio"],
    "que acontece quando há uma deficiência#de insulina no organismo?": ["*Hiperglicemia", "Hipoglicemia", "Aumento da função renal", "Hipotensão"],
    "qual é a função do glucagon no corpo?": ["*Estimular a liberação de glicose no sangue", "Reduzir a quantidade de glicose no sangue", "Estimular a produção de insulina", "Diminuir a lipólise"],
    "qual é o principal efeito da adrenalina#no corpo?": ["*Aumento da frequência cardíaca e dilatação das vias aéreas", "Diminuição da pressão arterial e aumento da digestão", "Redução da taxa de glicose no sangue", "Aumento da secreção de saliva"],
    "o que acontece quando o corpo libera#catecolaminas em resposta ao estresse?": ["*Preparação para a 'luta ou fuga'", "Redução do gasto de energia", "Aumento da atividade digestiva", "Diminuição da frequência cardíaca"],
    "qual é o efeito da noradrenalina no#sistema cardiovascular?": ["*Aumento da pressão arterial e da frequência cardíaca", "Diminuição da pressão arterial e atividade respiratória", "Aumento da produção de bile", "Estímulo da secreção de insulina"],
    "qual glândula é responsável pela#produção de cortisol?": ["*Glândula adrenal", "Glândula pituitária", "Glândula tireoide", "Pâncreas"],
    "qual é a principal função do cortisol#no corpo?": ["*Aumentar a resposta ao estresse e regular o metabolismo", "Estimular a síntese de proteínas, carbohidratos e lípidos", "Aumentar a produção de hormônios sexuais e androgenios", "Diminuir a produção de glicose"],
    "que acontece quando há uma produção#excessiva de cortisol?": ["*Síndrome de Cushing", "Doença de Addison", "Hipotireoidismo", "Hipoglicemia"],
    "qual é o efeito do cortisol sobre o#sistema imunológico?": ["*Supressão da resposta imune", "Estimulação da inflamação", "Aumento da produção de anticorpos", "Aumento da produção de leucócitos"],
    "qual é a principal função do paratormônio#(PTH) no corpo?": ["*Aumentar os níveis de cálcio no sangue", "Diminuir os níveis de cálcio no sangue", "Estimular a produção de vitamina D", "Aumentar os níveis de fosfato no sangue"],
    "como o PTH aumenta os níveis de cálcio#no sangue?": ["*Estimulando a liberação de cálcio dos ossos", "Aumentando a excreção de cálcio pelos rins", "Inibindo a absorção de cálcio no intestino", "Estimulando a secreção de calcitonina"],
    "o que ocorre quando há produção excessiva#de PTH?": ["*Hiperparatireoidismo", "Hipoparatireoidismo", "Hipotireoidismo", "Hipercalcemia"],
    "o paratormônio exerce efeitos diretos#em qual órgão para aumentar os níveis de#cálcio?": ["*Rins", "Fígado", "Pâncreas", "Pulmões"],
    "qual é a principal função da calcitonina?": ["*Reduzir os níveis de cálcio no sangue", "Aumentar os níveis de cálcio no sangue", "Estimular a produção de vitamina D", "Aumentar a excreção de cálcio pelos rins"],
    "qual glândula é responsável pela produção#de calcitonina?": ["*Glândula tireoide", "Glândula paratireoide", "Glândula adrenal", "Glândula pituitária"],
    "como a calcitonina age para reduzir os#níveis de cálcio no sangue?": ["*Inibindo a liberação de cálcio dos ossos", "Estimulando a absorção de cálcio no intestino", "Aumentando a excreção de cálcio pelos rins", "Estimulando a produção de PTH"],
    "o que ocorre quando há produção excessiva#de calcitonina?": ["*Hipocalcemia", "Hipercalcemia", "Hipotireoidismo", "Hipoparatireoidismo"],
    "a calcitonina e o paratormônio têm efeitos opostos#em relação aos níveis de cálcio no sangue. qual hormônio#aumenta os níveis de cálcio e qual diminui?": ["*Paratormônio aumenta e calcitonina diminui", "Paratormônio diminui e calcitonina aumenta", "Ambos aumentam", "Ambos diminuem"],
    "onde ocorre a produção dos espermatozoides?": ["*Nos túbulos seminíferos", "No epidídimo", "Na próstata", "Nas glândulas bulbouretrais"],
    "qual é a função da próstata?": ["*Produzir parte do líquido seminal", "Produzir esperma", "Regular a produção de testosterona", "Produzir hormônios femininos"],
    "qual estrutura conduz os espermatozoides do#epidídimo até a uretra?": ["*Ducto deferente", "Uretra", "Pênis", "Vesícula seminal"],
    "o que é a função da glândula#bulbouretral (glândula de Cowper)?": ["*Produzir um fluido lubrificante que neutraliza a acidez da uretra", "Produzir esperma que nutre os espermatozoides", "Produzir testosterona", "Regular a produção de sêmen e espermatzoides"],
    "qual é a função das trompas de falópio?": ["*Transportar os óvulos dos ovários para o útero", "Produzir óvulos durante a fase menstrual", "Produzir hormônios femininos como estrogênio", "Regular a menstruação e produção de óvulos"],
    "qual é o principal hormônio produzido#pelos ovários?": ["*Estrogênio", "Testosterona", "Progesterona", "Prolactina"],
    "qual é a função da progesterona no sistema#reprodutor feminino?": ["*Preparar o útero para a implantação do embrião", "Estimular a produção de óvulos", "Controlar o ciclo menstrual", "Estimular a produção de leite"],
    "o que é a função do colo do útero (cérvix)?": ["*Permitir a passagem de espermatozoides para o útero", "Produzir hormônios como progesterona", "Controlar o ciclo menstrual", "Manter o útero em posição"],
    "qual célula do sistema nervoso central#é responsável pela produção de mielina?": ["*Oligodendrócito", "Célula de Schwann", "Astrócito", "Microglia"],
}

Questions_Fisiologia_II = {
#Fisiologia II
    "o plasma sanguíneo é composto principalmente#por qual substância?": ['*água', 'glóbulos vermelhos', 'plaquetas', 'hemoglobina'],
    "qual é o principal componente responsável#pela cor vermelha do sangue?": ['*hemoglobina', 'albumina', 'glóbulos brancos', 'plaquetas'],
    "qual é a função das plaquetas#(trombócitos) no sangue?": ['*auxiliar na coagulação sanguínea', 'transportar oxigênio', 'combater infecções', 'regular o pH do sangue'],
    "a eritropoiese, a formação dos glóbulos vermelhos,#ocorre em qual órgão principal do corpo?": ['*medula óssea', 'fígado', 'baço', 'rim'],
    "a quantidade de oxigênio transportada no sangue#é principalmente dependente de qual proteína?": ['*hemoglobina', 'albumina', 'fibrinogênio', 'transferrina'],
    "o pH do sangue é mantido em qual intervalo#ideal para a função normal do corpo?": ['*7,35-7,45', '6,8-7,0', '7,5-7,8', '6,5-7,3'],
    "qual é o processo pelo qual o sangue é coagulado após#uma lesão vascular?": ['*hemostasia', 'filtração', 'osmose', 'difusão'],
    "durante a coagulação sanguínea, qual proteína#é convertida em fibrina para formar o coágulo?": ['*fibrinogênio', 'albumina', 'globulina', 'hemoglobina'],
    "quais células do sistema imunológico são#responsáveis pela resposta imune adaptativa?": ['*linfócitos T e B', 'macrófagos', 'células dendríticas', 'neutrófilos'],
    "qual é o principal órgão onde os#linfócitos T amadurecem?": ['*timo', 'baço', 'medula óssea', 'fígado'],
    "a produção de anticorpos pelos linfócitos#B é chamada de resposta imune:": ['*humoral', 'celular', 'inata', 'inflamatória'],
    "qual é a principal função das citocinas#no sistema imunológico?": ['*regular e coordenar as respostas imunes', 'transportar oxigênio para os demais tecidos', 'proteger os órgãos contra lesões', 'estimular a produção de anticorpos'],
"qual é a função do sistema complemento#na imunidade?": ['*ajudar na destruição de patógenos e ativar outras respostas imunológicas', 'regular a produção de anticorpos e resposta fagocitária', 'promover a inflamação crônica facilitando a eliminação de patogenos', 'acelerar a coagulação sanguínea'],
    "qual dos seguintes antígenos está presente#nas hemácias do grupo sanguíneo A?": ['*antígeno A', 'antígeno B', 'antígeno Rh', 'nenhum antígeno'],
    "qual grupo sanguíneo é conhecido como#receptor universal?": ['*grupo AB positivo', 'grupo O negativo', 'grupo A negativo', 'grupo B positivo'],
    "qual grupo sanguíneo é conhecido como#doador universal?": ['*grupo O negativo', 'grupo AB positivo', 'grupo A positivo', 'grupo B negativo'],
    "qual seria o risco de uma transfusão#incompatível entre dois grupos sanguíneos?": ['*hemólise', 'aumento na pressão sanguínea', 'formação de coágulos', 'nenhum risco significativo'],
    "qual é o grupo sanguíneo do receptor#ideal para receber sangue do grupo O negativo?": ['*qualquer grupo sanguíneo', 'apenas O negativo', 'apenas AB positivo', 'apenas A positivo'],
    "qual é a primeira fase da hemostasia?": ['*vasoconstrição', 'formação de coágulo', 'fase inflamatória', 'fase fibrinolítica'],
    "qual é o papel da trombina na#coagulação sanguínea?": ['*converter fibrinogênio em fibrina', 'impedir a adesão das plaquetas', 'estimular a vasoconstrição', 'aumentar a circulação sanguínea'],
    "o que é o fator Xa na cascata#de coagulação?": ['*é o fator chave que ativa a trombina', 'quebra a fibrina para impedir a coagulação', 'inibe a função plaquetária', 'impede a agregação plaquetária'],
    "quais são os principais fatores da#coagulação que agem para formar o coágulo?": ['*fibrinogênio, trombina, plaquetas e fibrina', 'hemoglobina, leucócitos e plaquetas', 'glóbulos vermelhos, trombina e linfócitos', 'ácido fólico e cálcio'],
    "como o cálcio (Ca²⁺) participa no#processo de coagulação?": ['*ele é essencial para a ativação de vários fatores da coagulação', 'ele impede a formação de coágulos prevenindo tromboses', 'ele facilita a remoção das plaquetas', 'ele mantém a pressão sanguínea constante'],
    "o que o eletrocardiograma (ECG) mede?": ['*a atividade elétrica do coração', 'a pressão arterial', 'a produção de hormônios', 'a circulação sanguínea'],
    "qual é a função da onda P no ECG?": ['*representa a despolarização dos átrios', 'representa a despolarização dos ventrículos', 'representa a repolarização dos átrios', 'representa a repolarização dos ventrículos'],
    "o que é a onda QRS no ECG?": ['*representa a despolarização dos ventrículos', 'representa a despolarização dos átrios', 'representa a repolarização dos átrios', 'representa a repolarização dos ventrículos'],
    "o que indica a onda T no ECG?": ['*a repolarização dos ventrículos', 'a despolarização dos átrios', 'a repolarização dos átrios', 'a despolarização dos ventrículos'],
    "o que pode indicar uma distensão do#intervalo QT no ECG?": ['*um risco aumentado de arritmias cardíacas', 'um aumento da pressão arterial', 'uma diminuição da frequência cardíaca', 'uma redução do débito cardíaco'],
    "o que é a linha de base em um ECG?": ['*é a linha de referência na qual as ondas do ECG são registradas', 'é a linha que indica a frequência cardíaca', 'é a linha de repolarização dos ventrículos', 'é a linha de despolarização dos átrios'],
    "qual é a frequência normal de um#complexo QRS?": ['*0,06 a 0,10 segundos', '0,12 a 0,20 segundos', '0,15 a 0,30 segundos', '0,02 a 0,05 segundos'],
    "o que um intervalo PR longo pode#indicar?": ['*um bloqueio cardíaco de primeiro grau', 'um aumento da frequência cardíaca', 'uma diminuição na contratilidade do coração', 'uma insuficiência cardíaca congestiva'],
    "o que caracteriza um ritmo sinusal#normal no ECG?": ['*ondas P precedem cada complexo QRS', 'ondas T são mais altas que as ondas P', 'não há ondas P visíveis', 'o intervalo QT é prolongado'],
    "o que pode um intervalo QT encurtado#no ECG indicar?": ['*síndrome de Wolff-Parkinson-White', 'síndrome de Brugada', 'taquicardia ventricular', 'hipocalemia'],
    "o que caracteriza um infarto do#miocárdio no ECG?": ['*elevação ou depressão do segmento ST', 'prolongamento ou alongamento do intervalo PR', 'ausência de onda T', 'aumento do intervalo QT'],
    "o que é o fluxo sanguíneo laminar?": ['*é o fluxo sanguíneo ordenado e sem turbulência', 'é o fluxo sanguíneo que ocorre apenas nas artérias', 'é o fluxo sanguíneo rápido e irregular', 'é o fluxo sanguíneo nas veias durante a respiração'],
    "qual é o principal fator que determina a velocidade#do fluxo sanguíneo nos vasos sanguíneos?": ['*o raio dos vasos sanguíneos', 'a quantidade de oxigênio no sangue', 'o volume de plaquetas no sangue', 'a pressão nos capilares'],
    "qual é o impacto da vasodilatação na microcirculação?": ['*aumenta o fluxo sanguíneo nos capilares', 'diminui o fluxo sanguíneo nos capilares', 'aumenta a pressão venosa', 'diminui a troca de gases nos pulmões'],
    "qual é a principal função do sistema#linfático na microcirculação?": ['*recolher o excesso de fluido intersticial e devolvê-lo à circulação sanguínea', 'aumentar a pressão arterial nos capilares facilitando a respiração interna', 'produzir glóbulos vermelhos no sangue', 'armazenar oxigênio nas células'],
    "como o sistema nervoso simpático contribui para#o aumento da pressão arterial?": ['*estimula a vasoconstrição e aumenta a frequência cardíaca', 'reduz a frequência cardíaca e promove a vasodilatação', 'estimula a produção de renina nos rins', 'aumenta a excreção de sódio nos rins'],
    "qual é o principal sistema responsável pela#regulação de longo prazo da pressão arterial?": ['*o sistema renal', 'o sistema nervoso autônomo', 'o sistema endócrino', 'o sistema linfático'],
    "como o fluxo sanguíneo é regulado durante#o exercício físico?": ['*redireciona o fluxo sanguíneo para os músculos esqueléticos', 'aumenta o fluxo sanguíneo para os pulmões', 'o fluxo sanguíneo é constante em todos os órgãos', 'aumenta o fluxo sanguíneo apenas nos pulmões'],
"qual é a principal variável que afeta#o débito cardíaco?": ['volume sistólico', '*frequência cardíaca', 'pressão venosa central', 'resistência vascular periférica'],
    "que é a pressão venosa central (pvc)?": ['é a pressão no ventrículo esquerdo após o sangue ter saído', '*é a pressão no final da veia cava, antes de entrar no coração', 'a pressão nas artérias pulmonares e nos coração direito', 'a pressão nos capilares'],
    "o que ocorre quando o retorno venoso#diminui?": ['o coração aumenta a frequência cardíaca para compensar', '*o débito cardíaco diminui', 'a pressão arterial aumenta', 'a resistência periférica aumenta'],
    "qual fator pode aumentar o retorno venoso?": ['hidratação excessiva', '*contração muscular', 'aumento da pressão arterial', 'aumento da frequência respiratória'],
    "como o aumento do volume sanguíneo#afeta o retorno venoso?": ['não tem efeito', '*aumenta o retorno venoso', 'diminui a resistência vascular', 'diminui o volume de sangue no coração'],
    "qual é a principal função da bomba#muscular no retorno venoso?": ['aumentar a pressão arterial nas veias cavas superiores e inferiores', '*ajudar a impulsionar o sangue de volta ao coração', 'dilatar as artérias principais', 'regular a troca de gases nos capilares'],
    "como o aumento da pressão intratorácica#afeta o retorno venoso?": ['reduz o retorno venoso', '*facilita o retorno venoso ao coração', 'não afeta o retorno venoso', 'aumenta a resistência nos capilares pulmonares'],
    "como é regulada a circulação coronária?": ['por necessidade metabólica do miocárdio', '*através da pressão sistêmica nas artérias coronárias', 'pela ação direta do sistema nervoso simpático', 'pelos barorreceptores localizados nas veias pulmonares'],
    "o que ocorre com a circulação pulmonar#quando há aumento da pressão arterial?": ['a pressão nos capilares pulmonares diminui', '*a pressão nos capilares pulmonares aumenta', 'não há alteração significativa', 'o fluxo sanguíneo é interrompido'],
    "qual é o efeito da hipoxia (baixa concentração#de oxigênio) na circulação pulmonar?": ['reduz o fluxo sanguíneo causando vasoconstrição local', '*provoca vasoconstrição nas arteríolas pulmonares', 'aumenta a troca de gases nos pulmões', 'aumenta a pressão venosa central'],
    "quais fatores podem influenciar a regulação#da circulação pulmonar?": ['somente a pressão arterial sistêmica', '*fatores como oxigenação do sangue e ph', 'o sistema nervoso simpático', 'a quantidade de sangue nos pulmões'],
    "qual é a resposta da circulação cerebral#em casos de aumento do co2 no sangue?": ['reduz o fluxo sanguíneo cerebral para ajudar na difusão de gases', '*aumenta o fluxo sanguíneo cerebral para ajudar na remoção do co2', 'não altera o fluxo sanguíneo', 'causa vasoconstrição nas artérias cerebrais'],
    "como a pressão intracraniana elevada#afeta a circulação cerebral?": ['não afeta', '*pode reduzir o fluxo sanguíneo cerebral devido à compressão dos vasos', 'aumenta o fluxo sanguíneo cerebral gerando diversos problemas', 'aumenta a pressão nas artérias pulmonares'],
    "como o sistema nervoso autônomo afeta#a circulação coronária durante o exercício?": ['não tem efeito', '*aumenta o fluxo sanguíneo coronário através da vasodilatação', 'diminui o fluxo sanguíneo coronário', 'causa vasoconstrição nas artérias coronárias desencadeando um sindrome coronário'],
    "qual é a principal função da inspiração?": ['retirar dióxido de carbono do sangue', '*permitir a entrada de oxigênio nos pulmões', 'aumentar a pressão pulmonar', 'aumentar o volume de ar exalado'],
    "o que ocorre com os músculos respiratórios#durante a inspiração?": ['eles relaxam', '*eles se contraem', 'não há movimento muscular', 'eles ficam em repouso'],
    "como a pressão no interior dos pulmões#se comporta durante a inspiração?": ['ela aumenta', '*ela diminui', 'não muda', 'ela se mantém constante'],
    "qual é a relação entre a capacidade pulmonar#e a resistência das vias aéreas?": ['capacidade pulmonar aumenta com a resistência', '*a resistência das vias aéreas diminui a capacidade pulmonar', 'não há relação', 'capacidade pulmonar e resistência são inversamente proporcionais'],
    "como a pressão pleural se comporta#durante a inspiração?": ['ela se mantém constante', '*ela se torna mais negativa', 'ela se torna mais positiva', 'ela aumenta drasticamente'],
    "qual é o efeito da expiração forçada#sobre os músculos respiratórios?": ['eles se contraem ativamente', '*eles relaxam', 'a pressão intrapulmonar diminui', 'não há movimento muscular'],
    "como a elasticidade pulmonar afeta#a ventilação?": ['ela diminui a ventilação', '*ela facilita a expiração', 'não tem efeito sobre a ventilação', 'ela aumenta a resistência nas vias aéreas'],
    "como as vias aéreas superiores afetam#a ventilação?": ['elas não afetam a ventilação', '*elas aquecem, umedecem e filtram o ar', 'aumentam a resistência nas vias aéreas', 'elas aumentam o volume corrente'],
    "o que ocorre com a pressão alveolar#durante a expiração?": ['ela diminui', '*ela aumenta', 'não há variação', 'ela se mantém constante'],
    "como a compliância pulmonar afeta a#ventilação?": ['ela aumenta a resistência das vias aéreas', '*ela facilita a expansão dos pulmões durante a inspiração', 'não tem efeito', 'ela reduz a troca de gases nos alvéolos'],
    "qual é o papel da membrana alveolocapilar#na difusão dos gases?": ['ela impede a troca de gases nos alveolos pulmonares', '*ela facilita a troca de gases entre os alvéolos e o sangue', 'ela restringe o movimento de oxigênio', 'ela bloqueia a entrada de dióxido de carbono nos alvéolos'],
    "como a espessura da membrana alveolocapilar#afeta a difusão dos gases?": ['ela não tem efeito sobre a difusão dos gases alveolares', '*aumentos na espessura da membrana reduzem a taxa de difusão', 'ela facilita a troca gasosa', 'ela aumenta a eficiência da difusão'],
    "como a área de superfície afeta a difusão#dos gases?": ['ela não tem efeito na difusão', '*quanto maior a área de superfície, maior será a taxa de difusão', 'aumenta a resistência nas vias aéreas', 'ela diminui a capacidade de troca gasosa'],
"qual fator reduz a difusão de gases#nos pulmões?": ["*aumento da espessura da membrana alveolocapilar", "Maior pressão parcial de oxigênio nos pulmões e no sangue", "Maior área de superfície", "Diminuição do volume de ar nos pulmões"],
    "como a temperatura afeta a difusão#dos gases?": ["*a temperatura mais alta aumenta a taxa de difusão dos gases", "A temperatura baixa aumenta a taxa de difusão dos gases", "A temperatura altera a pressão nos pulmões", "Não tem efeito"],
    "o que ocorre com a difusão do oxigênio em condições#de doença pulmonar obstrutiva crônica (dpoc)?": ["*ela é prejudicada devido à diminuição da área de troca gasosa", "Ela é aumentada devido ao aumento da área de troca gasosa nos pulmões", "Ela não é afetada", "Ela é melhorada pela vasodilatação pulmonar"],
    "como o oxigênio é transportado no sangue?": ["*é ligado à hemoglobina nas células vermelhas do sangue", "É dissolvido no plasma", "Ele é transportado como bicarbonato", "Ele se combina com o dióxido de carbono formando um composto solúvel"],
    "qual é o principal meio de transporte#do dióxido de carbono no sangue?": ["*é transportado como bicarbonato (hco3-)", "É transportado como oxigênio dissolvido", "Ele se liga diretamente à hemoglobina", "Ele é armazenado nas células vermelhas do sangue"],
    "o que acontece com o oxigênio quando#ele chega aos tecidos?": ["*ele se dissocia da hemoglobina e difunde-se para as células", "Ele é convertido em dióxido de carbono", "Ele é mantido no sangue", "Ele é liberado como gás e se difunde para os tecidos periféricos"],
    "qual fator aumenta a capacidade da#hemoglobina de ligar oxigênio?": ["*aumento da pressão parcial de oxigênio", "O aumento da pressão parcial dióxido de carbono", "Aumento da concentração de dióxido de carbono no sangue", "A redução da pressão arterial"],
    "o que acontece quando o oxigênio se dissocia#da hemoglobina nos tecidos?": ["*ele se difunde para as células dos tecidos", "Ele é transportado para o fígado", "Ele é absorvido pelos alvéolos", "Ele é convertido em dióxido de carbono e liberado pelos pulmões"],
    "qual é o papel da mioglobina no#transporte de oxigênio?": ["*ela armazena oxigênio nos músculos", "Ela transporta oxigênio no sangue", "Ela facilita a troca de oxigênio nos pulmões", "Ela transporta dióxido de carbono para os pulmões"],
    "onde ocorre o controle central da ventilação?": ["*no bulbo e na ponte do cérebro", "No coração pelos quimiorrecptores periféricos", "Nos pulmões", "No tronco encefálico"],
    "quais são os principais sensores responsáveis#por monitorar a ventilação?": ["*os quimiorreceptores e os mecanorreceptores", "O fígado e os músculos", "O pâncreas e os nervos", "As células da pele como os corpúsculos de Pacini"],
    "qual fator influencia diretamente a respiração,#detectado pelos quimiorreceptores?": ["*concentração de dióxido de carbono no sangue", "Temperatura corporal e aumento do metabolismo basal", "Quantidade de oxigênio no ar", "Pressão arterial"],
    "o que ocorre quando a concentração de#dióxido de carbono no sangue aumenta?": ["*a ventilação aumenta para eliminar o excesso de co2", "Os quimiorreceptores não têm efeito", "A ventilação diminui para ajudar na compensação renal", "O oxigênio é liberado nos tecidos"],
    "qual é o principal efeito da hipoxia#(baixo nível de oxigênio) na ventilação?": ["*aumenta a frequência respiratória", "Reduz a frequência respiratória", "Não afeta a ventilação", "Diminui a troca gasosa especialmente de CO2"],
    "qual é a principal função dos quimiorreceptores#periféricos?": ["*detectar as mudanças nos níveis de oxigênio e dióxido de carbono", "Monitorar a pressão arterial à expensas do sistema Renina Angiotensia Aldosterona", "Regular a temperatura e o metabolismo basal", "Controlar os batimentos cardíacos"],
    "onde estão localizados os quimiorreceptores#centrais?": ["*na medula oblonga", "No coração", "Nas artérias carótidas", "No cérebro"],
    "como a regulação do ph no sangue afeta a#ventilação?": ["*a ventilação aumenta para expelir dióxido de carbono e restaurar o ph normal", "Ela diminui a troca de gases para convervar o Oxigênio remanescente", "Não afeta a ventilação", "Ela reduz a eficiência da troca de gases"],
    "o que acontece durante a hiperventilação?": ["*o CO2 é expelido em excesso", "O dióxido de carbono é retido", "O oxigênio é retido para prevenir anóxia", "Não há alteração na ventilação"],
    "qual é o papel do centro respiratório no#tronco encefálico?": ["*controla a frequência e a profundidade da respiração", "Regula a circulação sanguínea bem como a pressão arterial", "Controla a digestão", "Regula os batimentos cardíacos"],
    "o que ocorre quando os quimiorreceptores#detectam um aumento de dióxido de carbono no sangue?": ["*eles aumentam a taxa de ventilação", "Eles diminuem a taxa de ventilação", "Não há alteração na ventilação", "Eles param de enviar sinais ao cérebro"],
    "como a ventilação é afetada por um aumento#da pressão arterial?": ["*não há alteração significativa", "Ela diminui", "Ela aumenta para compensar", "Aumento da troca de oxigênio"],
    "qual é o efeito da hipoventilação (ventilação#inadequada) sobre o ph sanguíneo?": ["*aumento da concentração de CO2", "Não há efeito", "Resulta em aumento de oxigênio", "Reduz a pressão sanguínea"],
    "onde ocorre o principal controle do equilíbrio#ácido-base no corpo?": ["*nos rins", "Nos pulmões", "No fígado", "No intestino"],
    "qual é o papel do sistema respiratório na#regulação do ph sanguíneo?": ["*ele elimina CO2, que reduz a acidez", "Ele retém oxigênio para prevenir anóxia", "Ele retém íons hidrogênio", "Ele aumenta a acidez"],
    "qual é o principal tampão utilizado pelo#sangue para manter o equilíbrio ácido-base?": ["*o tampão de bicarbonato-ácido carbônico", "O tampão de bicarbonato", "O tampão de fosfato", "O tampão de proteína"],
    "como os rins ajudam a regular o equilíbrio#ácido-base?": ["*excretando íons hidrogênio e reabsorvendo bicarbonato", "Eliminando oxigênio e reabsorvendo dióxido de carbono", "Retendo dióxido de carbono", "Filtrando glicose"],
    "o que ocorre quando o ph sanguíneo diminui#(acidemia)?": ["*a ventilação aumenta para eliminar mais dióxido de carbono", "Os rins aumentam a excreção de bicarbonato e a reabsorção de O2", "O corpo retém mais oxigênio", "A troca de gases diminui"],
    "o que é alcalose?": ["*um aumento no ph sanguíneo (menos ácido)", "Um aumento na concentração de dióxido de carbono", "Uma diminuição da concentração de bicarbonato", "Aumento da excreção de dióxido de carbono"],
"o que é a compensação respiratória no equilíbrio#ácido-base?": ['eliminação de bicarbonato pelos rins bem como dióxido de carbono', '*alteração na taxa respiratória para remover ou reter CO2', 'retenção de oxigênio pelos pulmões', 'excreção de íons hidrogênio'],
    "como os íons hidrogênio (h+) afetam o ph#sanguíneo?": ['não têm efeito sobre o ph', '*aumentam a acidez (diminuem o ph)', 'reduzem a acidez (aumentam o ph)', 'estabilizam o ph'],
    "qual é o efeito de uma dieta rica em proteínas#sobre o equilíbrio ácido-base?": ['ela aumenta a excreção de bicarbonato', '*ela pode aumentar a acidez sanguínea', 'ela diminui a concentração de ácido no sangue', 'ela reduz a excreção de dióxido de carbono'],
    "onde ocorre a principal regulação da#osmolaridade no corpo?": ['no fígado', '*nos rins', 'nos pulmões', 'no coração'],
    "qual hormônio é responsável pela regulação da#osmolaridade, ajudando na retenção de água pelos rins?": ['adrenalina', '*vasopressina (adh)', 'insulina', 'cortisol(hormona do estresse)'],
    "o que acontece quando a osmolaridade#do sangue aumenta?": ['o volume de urina aumenta bem como a proteinuria e excreção de electrolitos', '*a liberação de vasopressina aumenta, fazendo os rins reterem mais água', 'o corpo excreta mais sódio', 'o volume de urina diminui sem alterações no adh'],
    "como os rins ajudam a regular a#osmolaridade do sangue?": ['eliminando oxigênio e monóxido de carbono', '*filtrando e reabsorvendo água e íons', 'excretando dióxido de carbono', 'retendo glicose'],
    "o que ocorre com a osmolaridade do sangue#durante a desidratação?": ['ela diminui, o que ativa a liberaçãode aldosterona', '*ela aumenta, o que ativa a liberação de vasopressina', 'ela se mantém estável', 'ela diminui por conta da perda de sódio'],
    "qual é o papel da vasopressina na regulação#da osmolaridade?": ['ela aumenta a excreção de sódio', '*ela aumenta a reabsorção de água pelos rins', 'ela diminui a produção de urina pelos rins', 'ela aumenta a produção de urina pelos rins'],
    "como o consumo excessivo de água afeta a#osmolaridade do sangue?": ['ela aumenta a osmolaridade, fazendo o corpo rter mais água', '*ela diminui a osmolaridade, fazendo o corpo excretar mais água', 'não afeta a osmolaridade', 'ela causa desidratação'],
    "o que é a osmolaridade do sangue?": ['é a quantidade de proteínas no sangue como albumina, globulinas e fibrinogênio', '*é a concentração de solutos, como sódio, potássio e glicose', 'é a pressão arterial', 'é a quantidade de oxigênio no sangue'],
    "o que é a resposta do corpo à osmolaridade#elevada no sangue?": ['o aumento da secreção de aldosterona', '*a liberação de vasopressina para reter água', 'aumento da excreção de sódio nos rins', 'aumento da produção de urina'],
    "como a osmolaridade do sangue é regulada#após a ingestão de alimentos salgados?": ['ela diminui, estimulando a liberação de aldosterona para rter água', '*ela aumenta, estimulando a liberação de vasopressina para reter água', 'ela se mantém inalterada', 'ela faz o corpo excretar mais potássio'],
    "onde ocorre a filtração glomerular#nos rins?": ['no túbulo contorcido proximal', '*no glomérulo', 'no túbulo distal', 'nos dutos coletores'],
    "qual é o principal componente filtrado no#início da filtração glomerular?": ['proteínas', '*plasma', 'glicose', 'células sanguíneas'],
    "o que ocorre durante o processo de#reabsorção tubular?": ['o sangue excreta toxinas como amônia, amoníaco, mnóxido de carbono...', '*substâncias úteis como água, sódio e glicose são reabsorvidas', 'a urina é diluída', 'o sangue perde oxigênio'],
    "qual é a função dos túbulos renais no#processo de filtração?": ['produzir urina fracamente concentrada', '*reabsorber água e solutos do filtrado', 'produzir hormônios', 'regular o fluxo sanguíneo'],
    "o que é a depuração renal?": ['o processo de excreção de urina pelos rins', '*a taxa com que os rins removem substâncias do sangue', 'o processo de reabsorção de glicose', 'a produção de proteínas pelos rins'],
    "qual substância é frequentemente usada#para medir a taxa de filtração glomerular?": ['ácido úrico', '*creatinina', 'glicose', 'amônia'],
    "onde ocorre a maior parte da reabsorção#de água nos rins?": ['no túbulo distal', '*no túbulo contorcido proximal', 'no glomérulo', 'nos dutos coletores renais'],
    "o que é reabsorvido ativamente no#túbulo contorcido proximal?": ['ácido úrico', '*sódio e glicose', 'potássio', 'creatinina'],
    "qual é a principal função do túbulo#distal no processo de filtração?": ['produzir urina altamente concentrada em sódio', '*regular o equilíbrio de sódio, potássio e ph', 'reabsorver a maior parte da água', 'excretar toxinas'],
    "qual é o principal movimento responsável#pela propulsão dos alimentos no esôfago?": ['vasoespasmo muscular', '*peristaltismo', 'segmentação', 'defecação'],
    "onde ocorre o movimento de segmentação,#que ajuda na mistura do quimo?": ['no esôfago', '*no intestino delgado', 'no estômago', 'no reto'],
    "como os movimentos peristálticos no#intestino delgado ajudam na digestão?": ['absorvem nutrientes ao alongo do tracto digestivo', '*empurram os alimentos ao longo do trato digestivo', 'separam os nutrientes ao longo do tracto digestivo', 'aumentam a produção de sucos gástricos'],
    "o que acontece durante a motilidade do#intestino grosso?": ['absorção de nutrientes', '*reabsorção de água e formação de fezes', 'produção de bile', 'secreção de enzimas digestivas'],
    "quais são os efeitos da motilidade alterada#no sistema digestivo?": ['aumento da secreção gástrica', '*diarreia ou constipação', 'aumento da absorção de nutrientes', 'perda de controle da deglutição'],
    "como a segmentação no intestino delgado#contribui para a digestão?": ['aciona a defecação', '*mistura os alimentos com enzimas digestivas', 'movimenta os alimentos ao longo do intestino grosso', 'separa os nutrientes'],
"quais fatores podem alterar a motilidade#intestinal?": ['temperatura do corpo e aumento do metabolismo basal', '*hormônios, dieta e sistema nervoso', 'frequência cardíaca e estimulação simpática', 'peso corporal'],
    "onde são secretados os sucos gástricos#que ajudam na digestão?": ['no fígado', '*no estômago', 'no pâncreas', 'nos intestinos'],
    "qual célula é responsável pela produção#de ácido clorídrico no estômago?": ['enterócitos', '*células parietais', 'células principais', 'células alfa'],
    "qual é a principal função da bile#produzida pelo fígado?": ['digestão de proteínas', '*emulsificação de gorduras', 'quebra de carboidratos', 'produção de suco gástrico'],
    "o que é secretado pelas células#principais do estômago?": ['ácido clorídrico', '*pepsinogênio', 'bile', 'insulina'],
    "qual é a função das glândulas salivares?": ['produzir enzimas digestivas como alfa-amido-salivar', '*produzir saliva que contém amilase', 'produzir ácido clorídrico', 'produzir bile'],
    "onde a secreção de suco pancreático ocorre?": ['no fígado', '*no pâncreas', 'no estômago', 'nos intestinos'],
    "qual substância é secretada pelo pâncreas#para ajudar na neutralização do quimo ácido?": ['amilase', '*bicarbonato', 'lipase', 'pepsinogênio'],
    "o que é a função da amilase salivar?": ['quebra de proteínas', '*quebra de carboidratos', 'emulsificação de gorduras', 'neutralização do ácido gástrico'],
    "onde o suco pancreático se mistura com o#quimo para continuar a digestão?": ['no estômago', '*no duodeno', 'no jejuno', 'no cólon'],
    "qual é a principal função das células do#fígado na digestão?": ['produzir sucos gástricos, intestinas e enzimas que ajudam na digestão', '*produzir bile para emulsificação de gorduras', 'produzir insulina', 'produzir amilase'],
    "o que o pâncreas secreta para ajudar na#digestão das proteínas?": ['pepsina', '*tripsina', 'amilase', 'lipase'],
    "qual é o efeito da secreção de insulina#no sistema digestivo?": ['estimula a secreção de bile', '*ajuda na absorção de glicose pelas células', 'facilita a digestão e absorção de proteínas no tracto digestivo', 'aumenta a secreção de sucos gástricos'],
    "o que ocorre quando o pâncreas não secreta#enzimas digestivas adequadas?": ['ocorre constipação', '*há má digestão de alimentos', 'a bile não é produzida corretamente', 'o ácido gástrico é insuficiente'],
    "qual é a principal função do suco#gástrico no estômago?": ['neutralizar o quimo criando um ambiente alcalino', '*quebrar proteínas e criar um ambiente ácido', 'emulsificar gorduras', 'quebrar carboidratos'],
    "como a bile é transportada para o#intestino delgado?": ['por meio do ducto pancreático', '*por meio do ducto colédoco', 'por meio da veia cava', 'por meio da artéria hepática'],
    "onde ocorre a maior parte da absorção#de nutrientes no sistema digestivo?": ['no estômago', 'no cólon', '*no intestino delgado', 'nos dutos biliares'],
    "qual é a principal função dos vilosidades#intestinais no intestino delgado?": ['produzir bile que aumenta a superficie de absorção', '*absorver nutrientes para a corrente sanguínea', 'segregar sucos digestivos', 'emulsificar gorduras'],
    "qual tipo de nutrientes é principalmente#absorvido no jejuno?": ['água e sódio', '*carboidratos, proteínas e lipídios', 'vitaminas e cofacotres enzimaticos', 'sais minerais e diversos nutrientes inorgânicos'],
    "o que é a função dos microvilosidades nas#células epiteliais do intestino delgado?": ['proteger o intestino contra patógenos', '*aumentar a área de superfície para absorção', 'produzir enzimas digestivas para complementar a digestão', 'regular a secreção de bile'],
    "como os nutrientes como glicose e aminoácidos#entram nas células intestinais?": ['por difusão simples', '*por transporte ativo', 'por endocitose', 'por difusão facilitada'],
"onde ocorre a absorção de água e eletrólitos#no sistema digestivo?": ['no estômago', '*no intestino grosso', 'no pâncreas', 'nos ductos biliares'],
    "qual é a função das células do epitélio#intestinal na absorção de lipídios?": ['produzir sucos gástricos para desnaturalizar proteínas e lípidos', '*formar quilomícrons para transportar lipídios', 'neutralizar o quimo', 'produzir bile'],
    "qual estrutura facilita a absorção de#lipídios no intestino delgado?": ['microvilosidades', '*quilomícrons', 'vilosidades', 'pâncreas'],
    "como os ácidos graxos e glicerol são#absorvidos pelas células intestinais?": ['por transporte ativo', '*por difusão simples', 'por endocitose', 'por transporte facilitado'],
    "quais vitaminas são absorvidas no#intestino delgado?": ['vitaminas a, b1 e c e maior parte das vitaminas hidrossolúveis', '*vitaminas lipossolúveis (a, d, e, k) e algumas vitaminas hidrossolúveis', 'vitaminas b12 e k', 'vitaminas c e b9'],
    "qual é o papel do sistema linfático na#absorção dos lipídios?": ['transportar água absorvida pelo intestino delgado e grosso', '*transportar quilomícrons formados a partir dos lipídios', 'absorver glicose', 'regular a secreção de bile'],
    "como os minerais como cálcio e ferro são#absorvidos no intestino delgado?": ['por transporte ativo', '*por transporte facilitado ou ativo', 'por difusão simples', 'por endocitose'],
    "qual parte do intestino é responsável pela#absorção de a maioria dos nutrientes?": ['no cólon', '*no jejuno e íleo', 'no cólon descendente e reto', 'no duodeno'],
    "como o corpo humano responde ao aumento#da temperatura durante o exercício?": ['reduzindo a frequência cardíaca e estimulando o sistema parassimpático', '*aumentando a sudorese para dissipar o calor', 'reduzindo a respiração', 'aumentando a pressão arterial'],
    "qual é a principal forma de perda de calor#durante o exercício intenso?": ['evaporação', '*evaporação do suor', 'radiação', 'condução'],
    "o que acontece com a temperatura corporal#durante o exercício em ambientes quentes?": ['a temperatura corporal diminui', '*a temperatura corporal aumenta', 'não há alteração', 'a temperatura corporal se estabiliza'],
    "qual mecanismo o corpo usa para regular a#temperatura durante o exercício?": ['contração muscular', '*transpiração e vasodilatação', 'aumento da frequência cardíaca', 'contração do esfíncter anal'],
    "o que pode ocorrer se a temperatura do corpo#aumentar excessivamente durante o exercício?": ['hipotensão', '*hipertermia', 'hipoglicemia', 'hipotermia'],
    "durante o exercício em clima frio, qual é a#resposta do corpo para preservar o calor?": ['sudorese excessiva', '*vasoconstrição periférica e tremores musculares', 'aumento da circulação sanguínea nas extremidades', 'relaxamento muscular'],
    "quais são os efeitos do exercício físico em#ambientes frios sobre o corpo?": ['desidratação', '*aumento da produção de calor corporal', 'aumento da pressão arterial periférica', 'diminuição da produção de suor'],
    "qual é a função da sudorese durante o#exercício em climas quentes?": ['reduzir a frequência respiratória', '*dissipar o calor do corpo e regular a temperatura', 'vasconstrição periférica que aumenta a pressão arterial', 'ajudar na digestão'],
    "o que pode ocorrer se o corpo não conseguir se#resfriar adequadamente durante o exercício em ambientes#quentes?": ['desidratação', '*golpe de calor', 'hipotermia', 'hipoglicemia'],
    "qual é a temperatura corporal considerada#perigosa durante o exercício em ambientes quentes?": ['37°C', '38°C', '*acima de 40°C', 'abaixo de 36°C'],
    "quais fatores podem influenciar a resposta da#temperatura do corpo ao exercício?": ['idade', '*ambiente', 'intensidade do exercício e vestimenta', 'peso corporal'],
}

Questions_Informática_Médica_II = {
    "que representa o valor de p em uma#análise estatística?": ["o intervalo de confiança e desconfiança e variavéis mutáveis", "*a probabilidade de que os resultados obtidos são devido ao acaso", "a média da amostra bem como a mediana", "a variabilidade ou aleatoriedade dos dados"],
    "qual é o principal indicador utilizado para#avaliar a saúde de uma população em termos de expectativa#de vida?": ["taxa de natalidade", "*expectativa de vida ao nascer", "taxa de mortalidade infantil", "taxa de fecundidade"],
    "que é um erro tipo I na inferência estatística?": ["errar ao não rejeitar a hipótese nula", "*rejeitar a hipótese nula verdadeira", "não detectar uma relação significativa", "aceitar uma hipótese alternativa falsa"],
    "o que caracteriza um problema científico?": ['*é uma questão específica e testável que orienta a pesquisa', 'é uma suposição não verificável que ajuda na investigação', 'é uma conjectura baseada em dados não testados', 'é um dado empírico que não necessita de explicação'],
    "qual é a primeira etapa ao desenvolver#um projeto de investigação científica?": ['*definir claramente o problema de pesquisa', 'coletar dados de campo para a pesquisa', 'analisar a literatura científica', 'elaborar a hipótese de pesquisa'],
}

Questions_Genética_Médica = {
# Genética
    "quem é considerado o pai da#genética moderna?": ["charles darwin", "alfred wallace", "*gregor mendel", "watson e crick"],
    "qual foi o organismo modelo utilizado#por gregor mendel em seus experimentos?": ["mosca-das-frutas", "milho", "*ervilhas (pisum sativum)", "bactérias"],
    "qual foi a descoberta mais importante de#watson e crick em 1953?": ["mutação genética", "lei da hereditariedade", "*estrutura em dupla hélice do dna", "código genético"],
    "qual o nome da técnica usada para identificar#as bases do dna e confirmar sua estrutura?": ["eletroforese", "*difração de raios x", "PCR", "sequenciamento de rna"],
    "qual cientista descobriu que o dna é o#material hereditário em 1944?": ["Gregor mendel", "Charles darwin", "*Oswald avery", "Rosalind franklin"],
    "quem descobriu os elementos genéticos#móveis (transposons)?": ["James watson", "Gregor mendel", "*Barbara mcclintock", "Alfred wallace"],
    "o que são cromossomos?": ["unidades funcionais de proteínas responsáveis pela transcripção de proteínas", "*estruturas compostas por dna e proteínas que carregam material genético", "sequências de rna mensageiro para posterior tradução de proteínas", "células especializadas no núcleo"],
    "qual é a técnica usada para visualizar#cromossomos em uma célula?": ["western blotting", "*cariótipo", "pcr (reação em cadeia da polimerase)", "eletroforese em gel"],
    "qual é o nome da região do cromossomo onde#as cromátides-irmãs estão unidas?": ["*centrômero", "telômero", "exão", "intrão"],
    "o que caracteriza uma aneuploidia?": ["*alteração no número normal de cromossomos", "mutação genética em um único gene", "quebra de cromossomos em duas partes simetricamente iguais", "alteração nas sequências intrônicas"],
    "qual é o tipo de cromossomo encontrado#nas células sexuais humanas?": ["cromossomos somáticos", "*cromossomos sexuais (x e y)", "cromossomos poliploides", "cromossomos homólogos (x e y)"],
    "qual condição é causada pela presença de#um cromossomo 21 adicional?": ["síndrome de turner", "*síndrome de down (trissomia 21)", "síndrome de klinefelter", "síndrome de patau"],
    "qual é a alteração presente na síndrome#de turner?": ["*monossomia do cromossomo x (45,x)", "trissomia do cromossomo 13", "duplicação do cromossomo y", "perda de parte do cromossomo 5"],
    "qual é uma característica das alterações#cromossômicas estruturais?": ["*Alteração na estrutura de um ou mais cromossomos", "Alteração no número de cromossomos", "Troca de material genético entre cromossomos homólogos", "Mutações genéticas pontuais"],
    "qual é uma das principais causas das#alterações cromossômicas numéricas?": ["*Erro na segregação cromossômica durante a mitose ou meiose", "Alterações no DNA nuclear mediante à exposição de factores mutgênicos", "Mutações nos cromossomos sexuais", "Exposição a radiações"],
    "o que caracteriza a síndrome de Down?": ["*Trissomia do cromossomo 21", "Monossomia do cromossomo 18", "Trissomia do cromossomo 13", "Deleção do cromossomo 21"],
    "qual é a alteração cromossômica associada#à síndrome de Turner?": ["*Monossomia do cromossomo X", "Trissomia do cromossomo X", "Deleção do cromossomo Y", "Trissomia do cromossomo 21"],
    "o que é uma translocação cromossômica?": ["*Troca de material genético entre cromossomos não homólogos", "Troca de material genético entre cromossomos homólogos", "Duplicação de um segmento cromossômico", "Perda de um segmento de cromossomo"],
    "quais alterações cromossômicas estão associadas#à síndrome de Klinefelter?": ["*Presença de cromossomos sexuais XXY", "Presença de cromossomos sexuais XXXY", "Monossomia do cromossomo X", "Trissomia do cromossomo 21"],
    "o que é uma deleção cromossômica?": ["*Perda de um segmento de cromossomo", "Aumento do número de cromossomos", "Troca de material genético entre cromossomos homólogos", "Duplicação de uma região cromossômica"],
    "qual é o padrão de herança em que um único#gene afeta várias características fenotípicas?": ["*Pleiotropia", "Epistasia", "Herança ligada ao sexo", "Herança dominante"],
    "o que caracteriza a herança dominante?": ["*Apenas uma cópia do gene alterado é necessária para expressar o fenótipo", "Ambas as cópias do gene alterado são necessárias para expressar o fenótipo", "O gene afetado está no cromossomo Y", "O gene afetado não se manifesta em heterozigotos"],
    "qual padrão de herança envolve a manifestação#do fenótipo somente quando o indivíduo é homozigoto#para o alelo alterado?": ["*Herança recessiva", "Herança dominante", "Herança ligada ao sexo", "Pleiotropia"],
    "qual é o padrão de herança em que a manifestação#do fenótipo depende da presença de dois alelos diferentes#em dois loci diferentes?": ["*Epistasia", "Herança dominante", "Herança incompleta", "Herança codominante"],
    "o que caracteriza a herança ligada ao sexo?": ["*O gene afetado está localizado no cromossomo X", "O gene afetado está localizado no cromossomo Y", "O gene afetado está no cromossomo 21", "A manifestação depende da interação entre cromossomos autossômicos e sexuais"],
    "qual é o padrão de herança em que ambos os#alelos se manifestam parcialmente no fenótipo?": ["*Herança codominante", "Herança recessiva", "Herança incompleta", "Herança dominante"],
    "o que caracteriza a herança incompleta?": ["*O fenótipo do heterozigoto é uma mistura dos fenótipos dos homozigotos", "Apenas um alelo se manifesta no heterozigoto", "O fenótipo do heterozigoto é igual ao fenótipo do homozigoto dominante", "Ambos os alelos dominam sobre o outro"],
    "o que caracteriza a herança poligênica?": ["*A interação de múltiplos genes para influenciar uma característica fenotípica", "A expressão de um único gene em para influenciar múltiplas características fenótipo", "A herança de características ligadas ao sexo", "A interação entre genes e ambiente"],
    "quais características são típicas de#uma herança poligênica?": ["*Caráter quantitativo com variação contínua", "Caráter qualitativo com variação discreta", "Herança ligada ao cromossomo Y", "Expressão dominante e recessiva"],
    "o que caracteriza a herança multifatorial?": ["*A influência de múltiplos genes e fatores ambientais sobre o fenótipo", "A interação entre genes de diferentes cromossomos", "A presença de apenas um gene dominante que influencia varios fenótipos", "A herança de características ligadas ao sexo"],
    "exemplo clássico de herança poligênica é?": ["*Altura humana", "Tipo sanguíneo", "Padrões de cores em flores", "Doenças genéticas recessivas"],
    "qual é o principal fator que contribui para#o padrão multifatorial na ocorrência de doenças como#a diabetes tipo 2?": ["*Genes e fatores ambientais", "Apenas genes", "Apenas fatores ambientais", "Alterações cromossômicas"],
    "em um padrão multifatorial, qual é a relação#entre genes e ambiente?": ["*Ambos interagem para influenciar o fenótipo", "Os genes determinam completamente o fenótipo", "O ambiente determina o fenótipo", "A herança é exclusivamente genética"],
    "o que é esperado em uma característica#poligênica?": ["*Uma distribuição contínua de fenótipos", "Fenótipos discretos e bem definidos", "Expressão uniforme em todos os indivíduos", "Ausência de variação entre os indivíduos"],
"qual é o conceito principal da genética#matemática?": ["*Estudo das frequências alélicas e genotípicas em populações", "Estudo da herança de características mendelianas em populações", "Análise das mutações genéticas em indivíduos nas populações", "Estudo da evolução de uma única espécie nas populações"],
    "o que é o equilíbrio de Hardy-Weinberg?": ["*Frequências alélicas e genotípicas permanecem constantes em uma população ideal", "É a condição onde ocorre mutação genética constante em uma população ideal", "É a condição onde há seleção natural contínua em uma população ideal", "É a condição onde a variabilidade genética é eliminada"],
    "qual fator não afeta o equilíbrio de#Hardy-Weinberg?": ["*Ausência de mutação", "Seleção natural", "Migração de indivíduos", "Endogamia"],
    "o que é uma população em termos de genética#de populações?": ["*Indivíduos da mesma espécie que interagem e podem se reproduzir entre si", "Um grupo de indivíduos com características idênticas", "Um grupo de indivíduos com variação genética não significativa em uma população", "Uma população de indivíduos de diferentes espécies"],
    "quais são os pressupostos para o equilíbrio#de Hardy-Weinberg?": ["*Ausência de mutações, seleção natural, migração, deriva genética e endogamia", "Mutação constante, seleções naturais frequentes, deriva genética e endogamia", "Falta de variabilidade genética e isolamento geográfico", "Reprodução sexuada e nenhuma migração"],
    "qual é a fórmula do equilíbrio de Hardy-Weinberg#para a frequência alélica?": ["*p² + 2pq + q² = 1", "p + q = 1", "p = 1 - q", "p² = 2pq"],
    "o que a deriva genética causa em#uma população?": ["*Mudança aleatória nas frequências alélicas devido ao acaso", "Mudança nas frequências alélicas devido à seleção natural", "Alteração nas frequências alélicas devido a migração", "Estabilidade nas frequências genéticas de uma população"],
    "qual é o impacto da migração em uma população,#de acordo com a genética de populações?": ["*Pode alterar as frequências alélicas, introduzindo novos genes", "Não tem impacto, pois os genes são preservados", "Aumenta a variabilidade genética de uma população", "Reduz a diversidade genética na população ideal"],
"qual é a causa da síndrome de Down?": ["*Trissomia do cromossomo 21", "Monossomia do cromossomo 18", "Trissomia do cromossomo 13", "Mutações no gene CFTR"],
    "qual gene está relacionado à fibrose#cística?": ["*CFTR", "BRCA1", "APC", "TP53"],
    "o que causa a hemofilia?": ["*Mutação no gene do fator de coagulação", "Deficiência de hemoglobina", "Defeito no gene da insulina", "Mutação no gene que causa excesso de plaquetas"],
    "qual é a herança da síndrome de Turner?": ["*Monossomia do cromossomo X", "Trissomia do cromossomo 18", "Mutações no gene CFTR", "Herança dominante autossômica"],
    "qual é a característica genética da doença#de Huntington?": ["*Mutação repetitiva de CAG no gene HTT", "Mutação no gene BRCA1 e no gene BRCA2", "Mutação no gene TP53", "Alteração cromossômica do cromossomo 5"],
    "o que causa a distrofia muscular de#Duchenne?": ["*Mutação no gene da distrofina", "Deficiência no gene BRCA2", "Excesso de mutações no gene TP53", "Mutação no gene CFTR"],
    "qual a base genética da anemia falciforme?": ["*Mutação no gene da hemoglobina, resultando em hemoglobina S", "Alteração no gene do fator de coagulação", "Deficiência do gene que ajuda no metabolismo do ferro", "Mutações no gene da Espectrina que-o faz ter forma de S"],
    "qual é a herança da fenilcetonúria?": ["*Herança autossômica recessiva", "Herança autossômica dominante", "Herança ligada ao X", "Herança mitocondrial"],
    "qual é a principal característica genética#da síndrome de Marfan?": ["*Mutação no gene FBN1", "Mutação no gene BRCA2", "Defeito no gene CFTR", "Alteração no gene do fator de coagulação"],
    "qual é a mutação associada ao câncer de#mama hereditário?": ["*Mutação nos genes BRCA1 e BRCA2", "Mutação no gene TP53", "Mutação no gene APC", "Mutação no gene EGFR"],
    "o que é a consulta genética?": ["*Avaliação do risco genético e aconselhamento para doenças hereditárias", "Análise do cariótipo dos pacientes para detetar alterações genéticas", "Exame físico e clínico para detectar doenças genéticas", "Análise de mutações em tecidos somáticos"],
    "quem pode se beneficiar de uma consulta#genética?": ["*Pessoas com histórico familiar de doenças genéticas", "Pessoas com histórico doenças infecciosas crônicas", "Pessoas com problemas circulatórios genéticos", "Somente pessoas com doenças raras diagnosticadas"],
    "qual é o principal objetivo da consulta#genética?": ["*Aconselhar sobre o risco genético e orientar decisões", "Exclusivamente para diagnosticar doenças genéticas raras", "Identificar mutações para prescrição de tratamentos imediatos", "Realizar exames laboratoriais de rotina"],
    "quais são as ferramentas usadas na#consulta genética?": ["*Histórico familiar, exame físico e testes laboratoriais", "Testes rápidos para doenças infecciosas e exame do cariótipo", "Exames radiológicos de tecidos musculares para detetar alterações genétcias", "Análises psicométricas para avaliação do comportamento"],
    "qual é a importância do aconselhamento#genético?": ["*Ajudar na compreensão dos riscos genéticos e opções reprodutivas", "Fornecer diagnósticos médicos definitivos frente a doenças genéticas raras", "Aplicar tratamentos para doenças hereditárias", "Diagnosticar doenças genéticas com base em testes clínicos"],
}
#Stoppage Point!
Questions_Introdução_à_Clínica = {
#Introdução a la clínica!!
"o que é clínica médica?": ["*Ramo da medicina que se dedica ao diagnóstico e tratamento de doenças", "Estudo de terapias alternativas para  tratamento de doenças", "Análise de exames laboratoriais em pacientes para diagnóstico de doenças", "Cirurgia para remoção de tumores cancerígenos"],
    "qual é a principal função do médico#clínico geral?": ["*Avaliar, diagnosticar e tratar condições clínicas gerais", "Realizar cirurgias para doenças complexas", "Especializar-se em tratamentos intensivos para tratar casos complexos gerais", "Prescrever medicamentos para doenças infecciosas"],
    "o que caracteriza a consulta clínica?": ["*Entrevista médica, exame físico e análise dos sintomas", "Exame de imagem e prescrição de tratamentos específicos", "Somente a análise de exames laboratoriais", "Consultas de urgência para doenças graves, crônicas e infecciosas"],
    "qual a importância do exame físico#na clínica geral?": ["*Permite ao médico avaliar sinais e sintomas para diagnóstico", "É usado apenas para monitoramento de doenças crônicas", "Serve para realizar tratamentos terapêuticos", "Não é relevante, pois os exames laboratoriais são suficientes"],
    "quais são os principais sistemas avaliados durante#uma consulta clínica?": ["*Sistema cardiovascular, respiratório, digestivo, nervoso e urinário", "Sistema musculoesquelético, endócrino-metabólico, hemolinfopoietico e urogenital", "Sistema linfático e reprodutivo", "Somente sistema respiratório e cardiovascular"],
    "o que é diagnóstico diferencial?": ["*Processo de exclusão de várias condições até chegar à doença correta", "É o tratamento baseado no histórico do paciente", "Análise de exames laboratoriais sem considerar sintomas", "Avaliação clínica com base apenas em um único sintoma preliminar"],
    "qual a relação entre a clínica geral e#especialidades médicas?": ["*A clínica geral é a base para encaminhamento a especialidades quando necessário", "A clínica geral substitui as especialidades médicas pois em si já é suficiente", "As especialidades não têm relação com a clínica geral", "A clínica geral trata somente doenças infecciosas e não agudas"],
    "qual é o objetivo da anamnese na#consulta clínica?": ["*Coletar informações sobre histórico de saúde para ajudar no diagnóstico", "Realizar uma avaliação psicológica, fornecendo uma biografia do paciente", "Determinar o melhor tratamento cirúrgico e geral com base no histórico", "Fornecer conselhos sobre dieta e estilo de vida"],
    "como os exames laboratoriais auxiliam#na consulta clínica?": ["*Confirmam ou descartam suspeitas diagnósticas feitas durante a anamnese", "Substituem completamente o exame físico seguindo já os exames complementares", "São usados apenas para diagnósticos de doenças raras", "Não são necessários em uma consulta clínica nromal"],

"qual é a técnica básica utilizada para avaliar os#sinais vitais de um paciente?": ["*Aferição da pressão arterial, frequência cardíaca, temperatura e respiração", "Exame de imagem, frequência cardíaca, temperatura e respiração", "Ultrassonografia, Ragiografia, Tomografia Axial Computadorizada e Temperatura", "Ressonância magnética nuclear, Tomografia Axial Computadorizada e Electrocardiograma"],
    "qual é o objetivo da palpação na avaliação clínica?": ["*Avaliar textura, temperatura, consistência e dor", "Observar a cor da pele, motilidade e sensibilidade", "Apenas medir a pressão arterial", "Realizar exames de função pulmonar como manobra 33"],
    "o que a inspeção física permite ao médico?": ["*Observar a aparência, postura, mobilidade e sinais de doenças visíveis", "Realizar exames laboratoriais funcionais e provas imagineológicas", "Avaliar exclusivamente os reflexos musculares", "Determinar a causa do sintoma através de exame de imagem"],
    "qual a função da percussão na avaliação clínica?": ["*Identificar alterações nos sons produzidos pelo corpo", "Aferir a temperatura corporal e Timpanismo tóracico", "Analisar o ritmo cardíaco", "Detectar anomalias nas articulações como dor"],
    "o que caracteriza a auscultação em um exame físico?": ["*Escutar sons corporais", "Avaliar a cor da pele", "Medir a pressão arterial", "Examinar os reflexos de profundidade"],
    "qual é a principal técnica utilizada para#avaliar a função cardíaca?": ["*Auscultar os batimentos cardíacos e verificar os sons cardíacos", "Analisar exames de sangue e electrocardiograma", "Realizar a tomografia axial computadorizada para anomalias", "Medir a pressão arterial apenas"],
    "como a palpação pode ser útil na avaliação#abdominal?": ["*Permite identificar áreas de dor, massa ou distensão abdominal", "É usada apenas para determinar o timpanismo abdominal", "Avalia os níveis de glicose no sangue", "Serve para verificar apenas visceromegalia"],
    "qual técnica básica é usada para avaliar#a função pulmonar?": ["*Auscultação para detectar sons respiratórios anormais", "Exame para detetar dor tóracica como osteocondritis", "Análise da frequência respiratória apenas", "Realização de ultrassonografia torácica"],
#Sttopage Point
    "como a inspeção pode ser utilizada na#avaliação de problemas neurológicos?": ["*Identificar sinais de paralisia, tremores e movimentos anormais", "Determinar a função hepática", "Verificar a pressão arterial", "Avaliar a densidade óssea"],
    "o que pode ser identificado durante a#palpação do pescoço?": ["*Linfadenopatias, presença de nódulos ou alterações na tireoide", "Alterações nos batimentos cardíacos", "Mudanças no ritmo respiratório", "Apenas sinais de infecção de pele"],
"qual é o objetivo principal do exame#físico geral?": ["*Avaliar o estado geral de saúde do paciente", "Diagnosticar doenças específicas", "Apenas verificar os sinais vitais", "Obter exames laboratoriais"],
    "qual é a primeira etapa do exame físico#geral?": ["*Inspeção visual do paciente", "Realizar a palpação", "Medir a pressão arterial", "Fazer uma ressonância magnética"],
    "o que se observa durante a inspeção no#exame físico?": ["*Postura, movimentos e sinais visíveis de doenças", "Temperatura corporal", "Apenas a pressão arterial", "Sinais de infecção de pele"],
    "qual técnica é usada para avaliar a densidade#muscular e os reflexos?": ["*Palpação e testes neurológicos", "Auscultação e análise de som respiratório", "Exames laboratoriais", "Ressonância magnética"],
    "como a auscultação é usada no exame#físico geral?": ["*Para ouvir os sons do coração, pulmões e outros órgãos", "Apenas para verificar a pressão arterial", "Analisar os reflexos do paciente", "Medir a temperatura corporal"],
    "qual é a importância da palpação#no exame físico?": ["*Verificar a presença de dor, nódulos e outras anomalias", "Verificar a saturação de oxigênio", "Apenas medir a temperatura", "Observar os movimentos do paciente"],
    "qual é a técnica usada para avaliar o#funcionamento do sistema cardiovascular?": ["*Auscultar os batimentos cardíacos e murmúrios", "Medir a pressão arterial", "Analisar os reflexos musculares", "Realizar tomografia computadorizada"],
    "como o exame físico geral pode auxiliar#no diagnóstico de doenças respiratórias?": ["*Auscultando sons pulmonares e observando a respiração", "Medindo a pressão arterial", "Analisando exames laboratoriais", "Realizando exames de imagem"],
    "quais sinais podem ser observados durante o#exame físico de uma pessoa com insuficiência cardíaca?": ["*Edema, cianose e dificuldade respiratória", "Febre alta", "Palidez nas extremidades", "Perda de apetite"],
    "qual a importância da inspeção da pele durante#o exame físico geral?": ["*Identificar sinais de doenças dermatológicas, infecções e desidratação", "Medir a temperatura corporal", "Avaliar os reflexos do paciente", "Apenas verificar a pressão arterial"],
                       "qual é o objetivo do exame físico regional?": [
                           "*Avaliar de forma detalhada cada parte do corpo",
                           "Realizar um diagnóstico final de doenças específicas", "Apenas medir a pressão arterial",
                           "Obter exames laboratoriais"],
                       "qual técnica é utilizada para examinar as articulações#durante o exame físico regional?": [
                           "*Palpação e movimentação das articulações", "Auscultação dos sons articulares",
                           "Realizar exames de imagem", "Analisar os reflexos musculares"],
                       "o que se observa durante a inspeção da cabeça e pescoço#no exame físico regional?": [
                           "*Sinais de infecção, deformidades e simetria", "Apenas dor de garganta",
                           "Temperatura corporal", "Pressão arterial"],
                       "qual é o principal objetivo da palpação durante o exame#físico regional dos membros?": [
                           "*Identificar anomalias nos músculos, ossos e articulações", "Observar o fluxo sanguíneo",
                           "Medir a temperatura da pele", "Verificar a pressão sanguínea"],
                       "quais sinais são verificados durante o exame físico#regional da região torácica?": [
                           "*Palpação do tórax, auscultação pulmonar e cardíaca", "Medir a pressão arterial",
                           "Avaliar os reflexos nos braços", "Apenas checar a temperatura corporal"],
                       "qual técnica é utilizada para examinar a coluna vertebral#no exame físico regional?": [
                           "*Palpação das vértebras e movimentação da coluna", "Auscultar o coração",
                           "Medir a pressão intracraniana", "Realizar tomografia de coluna"],
                       "como é realizada a inspeção abdominal durante o exame#físico regional?": [
                           "*Observar a forma, simetria e distensão do abdômen", "Medir a pressão arterial",
                           "Analisar os reflexos gastrointestinais", "Apenas realizar exames laboratoriais"],
                       "o que a palpação abdominal pode revelar no exame#físico regional?": [
                           "*Sinais de dor, massas ou aumento de órgãos", "Alterações no ritmo respiratório",
                           "Sinais de hipertensão", "Movimentos musculares involuntários"],
                       "qual é o foco do exame físico regional dos sistemas#urinário e genital?": [
                           "*Palpação e inspeção da região pélvica, avaliação de edema e simetria",
                           "Medir a pressão arterial", "Realizar exames de sangue", "Avaliar os reflexos do joelho"],
                       "como a inspeção das extremidades pode ajudar no diagnóstico#durante o exame físico regional?": [
                           "*Verificar sinais de inchaço, deformidades e circulação sanguínea",
                           "Observar a dor nas articulações", "Analisar o fluxo respiratório",
                           "Realizar um exame de imagem das articulações"],
"qual é a primeira etapa no exame físico do#sistema respiratório?": ["*Inspeção visual do padrão respiratório", "Medir a pressão arterial", "Realizar exames laboratoriais", "Palpação das extremidades"],
    "o que é observado durante a inspeção do#sistema respiratório?": ["*Simetria torácica, movimentos respiratórios e sinais de esforço", "A pressão sanguínea", "Reflexos no pescoço", "A frequência cardíaca"],
    "qual técnica é utilizada para auscultar os pulmões#no exame físico respiratório?": ["*Auscultação com estetoscópio", "Palpação das costelas", "Tensão arterial", "Verificação da temperatura corporal"],
    "o que pode indicar a presença de estertores ou roncos#ao auscultar os pulmões?": ["*Obstruções ou secreções nas vias respiratórias", "Desidratação", "Problemas cardíacos", "Alterações musculares"],
    "qual é o objetivo da palpação durante o exame físico#do sistema respiratório?": ["*Identificar movimentos anormais da parede torácica e alterações de temperatura", "Observar sinais de infecção", "Medir a pressão arterial", "Verificar a função renal"],
    "o que é verificado ao realizar a percussão torácica#no exame físico respiratório?": ["*Diferenças nos sons que podem indicar presença de líquido ou ar nos pulmões", "Alterações nos reflexos motores", "Níveis de colesterol", "Diferenças na respiração abdominal"],
    "quais sinais podem ser observados ao avaliar o padrão#respiratório de um paciente?": ["*Frequência, profundidade e ritmo da respiração", "Níveis de glicose no sangue", "Reflexos de tosse", "Pressão arterial"],
    "como a inspeção da caixa torácica pode ajudar no#diagnóstico respiratório?": ["*Detectar deformidades, como a escoliose ou o tórax em barril", "Medir a pressão arterial", "Analisar os reflexos dos membros", "Verificar os níveis de oxigênio"],
    "o que a palpação do tórax pode revelar no exame#físico respiratório?": ["*Alterações de movimento ou dor localizadas", "Diferenças de temperatura no abdômen", "Sinais de infecção urinária", "Perda de mobilidade nas articulações"],
    "quais sinais indicam que o paciente pode estar com#dificuldades respiratórias ao realizar o exame físico?": ["*Uso de musculatura acessória, respiração superficial ou rápida", "Aumento da pressão arterial", "Respiração profunda sem esforço", "Palidez nas extremidades"],
                       "qual é a primeira etapa no exame físico#do abdômen?": [
                           "*Inspeção do abdômen para observar simetria e sinais de distensão",
                           "Auscultação para ouvir sons intestinais", "Palpação suave do abdômen",
                           "Percussão das costas"],
                       "o que deve ser observado na inspeção do abdômen?": [
                           "*Simetria, movimentos respiratórios, presença de cicatrizes ou distensão", "A cor da pele",
                           "Sinais de cianose nas extremidades", "A pressão arterial"],
                       "qual é o objetivo da auscultação abdominal?": [
                           "*Avaliar os sons intestinais para identificar possíveis anormalidades",
                           "Verificar os níveis de glicose no sangue", "Medir a pressão arterial",
                           "Detectar alterações na função respiratória"],
                       "o que pode indicar a ausência de sons intestinais#durante a auscultação?": [
                           "*Obstrução intestinal ou paralisação do intestino", "Infecção respiratória", "Hipotensão",
                           "Dificuldades circulatórias"],
                       "o que deve ser avaliado durante a palpação#do abdômen?": [
                           "*Presença de dor, massa, tensão muscular ou órgãos aumentados", "Diferenças na cor da pele",
                           "Reflexos de tosse", "Alterações nas articulações"],
                       "como a percussão abdominal é utilizada#no exame físico?": [
                           "*Identificar áreas de timpanismo ou macicez, o que pode indicar líquido ou massas",
                           "Avaliar a respiração", "Medir os níveis de pressão arterial",
                           "Observar sinais de infecção nas extremidades"],
                       "quais são os sinais de peritonite durante o exame#físico do abdômen?": [
                           "*Dor intensa à palpação, rigidez muscular e sinais de defesa involuntária",
                           "Aumento da pressão arterial", "Alterações respiratórias", "Palidez nas extremidades"],
                       "o que a palpação profunda pode revelar durante#o exame abdominal?": [
                           "*Massa ou órgãos aumentados, como fígado ou baço", "Alterações na frequência cardíaca",
                           "Diferenças nos reflexos de tosse", "Sinais de desidratação"],
                       "qual é a importância de verificar a área do fígado#durante a palpação abdominal?": [
                           "*Identificar hepatomegalia ou sinais de doenças hepáticas",
                           "Verificar a presença de doenças respiratórias",
                           "Identificar alterações na pressão arterial", "Observar sinais de problemas circulatórios"],
                       "o que é indicado se o paciente apresentar dor abdominal#localizada com sinais de peritonite?": [
                           "*Encaminhamento urgente para avaliação cirúrgica",
                           "Análise laboratorial para hemograma completo", "Exame de radiografia torácica",
                           "Tratamento com antibióticos orais"],
"qual é o objetivo principal do exame físico#das mamas?": ["*Detectar alterações ou sinais de doenças, como nódulos ou secreções anormais", "Avaliar a pressão arterial", "Observar sinais de infecção na pele", "Medir a temperatura corporal"],
    "qual é a primeira etapa do exame físico#das mamas?": ["*Inspeção visual das mamas e região ao redor", "Auscultação cardíaca", "Palpação das articulações", "Exame da cavidade oral"],
    "o que o médico observa durante a inspeção#das mamas?": ["*Mudanças no tamanho, forma, simetria, ou sinais de irritação ou secreção", "Alterações na cor da pele", "Sinais de cianose nas extremidades", "Diferenças na frequência cardíaca"],
    "qual técnica é utilizada na palpação das mamas?": ["*Palpação suave com os dedos em movimentos circulares, cobrindo toda a mama", "Auscultação com estetoscópio", "Percussão nas axilas", "Observação da postura do paciente"],
    "como deve ser a palpação das mamas no exame#físico?": ["*Começar do centro da mama e ir em direção às bordas, cobrindo toda a área", "Verificar a pressão arterial", "Palpação profunda na cavidade abdominal", "Palpação das articulações do ombro"],
    "o que deve ser observado ao realizar a#palpação das mamas?": ["*Presença de nódulos, alterações de textura, dor ou secreção anormal", "Alterações no ritmo respiratório", "Mudanças na cor da pele", "Sinais de hipotensão"],
    "o que pode indicar a presença de secreção#anormal nos mamilos?": ["*Possível infecção, distúrbios hormonais ou câncer de mama", "Problemas digestivos", "Alterações nos níveis de glicose", "Doenças respiratórias"],
    "qual é o exame complementar frequentemente solicitado#após o exame físico das mamas?": ["*Mamografia ou ultrassonografia", "Exame de sangue para hemograma", "Tomografia computadorizada torácica", "Radiografia de ossos e articulações"],
    "qual é a importância da palpação das axilas durante#o exame físico das mamas?": ["*Verificar a presença de linfonodos aumentados ou massas", "Avaliar os níveis de glicose", "Detectar sinais de infecção nos pulmões", "Observar a presença de edema nas pernas"],
    "o que é indicado caso seja encontrado um nódulo#suspeito nas mamas?": ["*Encaminhamento para biópsia e exames complementares", "Recomendar repouso e medicação", "Ajuste na alimentação", "Exames de radiografia torácica"],
"qual é o primeiro passo no exame físico#cardiovascular?": ["*Inspeção geral do paciente e avaliação do ritmo cardíaco", "Auscultar os pulmões", "Avaliar os reflexos", "Medir a pressão arterial nas extremidades"],
    "qual deve ser a posição do paciente durante a#ausculta do coração?": ["*Paciente deitado ou semi-sentado, com o tronco elevado", "Deitado em posição supina, com as pernas esticadas", "Sentado com os braços elevados", "Deitado de lado, com as pernas flexionadas"],
    "o que o médico avalia ao auscultar o coração?": ["*Sons cardíacos normais e anormais, como sopros ou murmúrios", "A frequência respiratória", "A pressão nos vasos sanguíneos", "A presença de turgor cutâneo"],
    "o que pode indicar a presença de um#sopro cardíaco?": ["*Anomalias nas válvulas cardíacas ou defeitos no septo", "Alterações no ritmo respiratório", "Problemas nos linfonodos", "Comprometimento das articulações"],
    "quais são as manobras utilizadas para#identificar sopros cardíacos?": ["*Manobra de Valsalva e inclinação do paciente", "Compressão das artérias", "Exame de fundo de olho", "Teste de pressão muscular"],
    "o que é avaliado durante a palpação#do coração?": ["*Pulsação apical, presença de frêmitos ou descontinuidade no batimento", "Temperatura da pele", "Reflexos tendinosos", "Alterações no ritmo respiratório"],
    "qual é a localização comum para a#palpação do impulso apical?": ["*No 5º espaço intercostal, linha médio-clavicular esquerda", "No 2º espaço intercostal, linha axilar", "Na região esternal", "No lado direito do peito, acima da clavícula"],
    "qual exame complementar pode ser solicitado#após o exame físico cardiovascular?": ["*Eletrocardiograma (ECG) e ecocardiograma", "Radiografia torácica", "Tomografia computadorizada do cérebro", "Exames de sangue para hemograma"],
    "o que pode ser identificado durante a#percussão cardíaca?": ["*Alterações no tamanho do coração e na área de matidez", "Sinais de infecção pulmonar", "Alterações nas articulações do peito", "Aumento de glândulas salivares"],
    "qual é o objetivo da palpação das artérias durante#o exame cardiovascular?": ["*Avaliar a força e a regularidade do pulso", "Observar a movimentação do diafragma", "Detectar alterações na pressão arterial", "Verificar os reflexos nas extremidades"],
"o que significa a sigla SOMA no exame físico?": ["*Sinais, Observação, Medição e Avaliação", "Sinais, Observação, Monitoramento e Avaliação", "Sistema, Observação, Medição e Avaliação", "Sinais, Organização, Medição e Avaliação"],
    "qual é o primeiro passo no exame físico SOMA?": ["*Observação geral do paciente e coleta de dados", "Medir pressão arterial e temperatura", "Auscultar os pulmões", "Inspecionar a cavidade oral"],
    "o que é avaliado durante a fase de sinais no#exame SOMA?": ["*Avaliação de sinais vitais, como pressão arterial, frequência cardíaca e temperatura", "Verificação da mobilidade do paciente", "Observação da postura", "Verificação dos reflexos nervosos"],
    "qual é a importância da observação no exame#SOMA?": ["*Permite identificar sinais clínicos, como coloração da pele, padrão respiratório e postura", "Apenas avaliar a frequência cardíaca", "Avaliar a resposta a estímulos externos", "Determinar o nível de consciência do paciente"],
    "qual é a fase do exame SOMA que envolve a#medição de parâmetros clínicos?": ["*Fase de medição, que inclui aferição de pressão arterial, temperatura, peso e altura", "Fase de avaliação do histórico médico", "Fase de observação de sinais neurológicos", "Fase de verificação do nível de dor"],
    "o que é avaliado na fase de avaliação#do exame SOMA?": ["*Análise do histórico clínico, diagnósticos prévios e exames complementares", "Apenas os sinais vitais", "A mobilidade do paciente", "O nível de consciência do paciente"],
    "como a fase de medição contribui para#o exame SOMA?": ["*Fornece dados objetivos que podem indicar alterações no estado clínico do paciente", "Determina o prognóstico da doença", "Ajuda a identificar doenças genéticas", "Substitui exames laboratoriais"],
    "qual é o objetivo da fase de sinais#no exame SOMA?": ["*Avaliar os sinais vitais do paciente, como pressão arterial e frequência respiratória", "Verificar os reflexos", "Avaliar a temperatura do corpo", "Observar a postura do paciente"],
    "qual das fases do exame SOMA envolve a análise#de resultados de exames laboratoriais?": ["*Fase de avaliação, que usa resultados de exames e histórico médico para determinar o diagnóstico", "Fase de observação", "Fase de medição", "Fase de sinais vitais"],
    "qual é a fase do exame SOMA em que o paciente#é fisicamente examinado?": ["*A fase de sinais, com ênfase na avaliação de sinais vitais", "Fase de medição", "Fase de avaliação", "Fase de observação"],
"qual é o primeiro passo no exame físico do#sistema nervoso?": ["*Avaliação do nível de consciência do paciente", "Testar os reflexos profundos", "Exame da coordenação motora", "Inspeção da postura do paciente"],
    "o que é avaliado ao examinar o nível de#consciência do paciente?": ["*Orientação no tempo, espaço e pessoa", "A mobilidade do paciente", "A resposta a estímulos", "A frequência cardíaca"],
    "qual é o teste utilizado para avaliar a força#muscular durante o exame físico do sistema nervoso?": ["*Teste de força contra resistência", "Teste de reflexos", "Teste de movimento ocular", "Teste de resposta verbal"],
    "o que é observado ao examinar a marcha do#paciente?": ["*A simetria, coordenação e equilíbrio ao caminhar", "A postura da cabeça", "A flexibilidade das articulações", "O nível de dor do paciente"],
    "quais são os reflexos mais comumente avaliados#durante o exame físico do sistema nervoso?": ["*Reflexos patelares e do tendão de Aquiles", "Reflexos de Babinski", "Reflexos de flexão", "Reflexos de extensão"],
    "como a coordenação motora é testada no exame#físico do sistema nervoso?": ["*Pedindo ao paciente para tocar o nariz com os dedos alternados", "Avaliação da força nas mãos", "Inspeção da marcha do paciente", "Observação da expressão facial"],
    "qual é o objetivo de examinar a sensibilidade#do paciente?": ["*Avaliar a resposta do paciente a estímulos táteis, dolorosos e térmicos", "Avaliar a força dos músculos", "Verificar a coordenação motora", "Observar a postura do paciente"],
    "qual é a principal função do exame dos#nervos cranianos?": ["*Verificar a integridade da função sensorial e motora do cérebro", "Avaliar o movimento das extremidades", "Verificar a resposta do paciente a estímulos", "Examinar a frequência respiratória"],
    "o que é testado ao avaliar os reflexos do#paciente?": ["*A resposta involuntária do sistema nervoso a estímulos", "A coordenação dos músculos", "A flexibilidade das articulações", "A mobilidade do paciente"],
    "qual teste é utilizado para avaliar o nervo#facial durante o exame físico do sistema nervoso?": ["*Pedir ao paciente para fazer caretas ou sorrir", "Pedir ao paciente para mover os dedos das mãos", "Avaliar o movimento ocular", "Testar a resposta do paciente a dor"],
"qual é o primeiro par craniano a ser examinado#durante o exame físico?": ["*Nervo olfatório (I)", "Nervo óptico (II)", "Nervo trigêmeo (V)", "Nervo facial (VII)"],
    "como é testado o nervo olfatório (I)?": ["*Pedir ao paciente para fechar os olhos e identificar cheiros", "Pedir ao paciente para abrir os olhos e ver objetos próximos", "Testar o movimento ocular", "Avaliar a sensibilidade da pele"],
    "qual é a função do nervo óptico (II)?": ["*Responsável pela visão", "Responsável pela movimentação ocular", "Responsável pela sensação tátil", "Responsável pelo paladar"],
    "como o nervo óptico (II) é examinado durante#o exame físico?": ["*Verificação da acuidade visual e do campo visual", "Avaliação da resposta à luz", "Verificação da coordenação motora", "Teste de força muscular"],
    "o que é testado ao avaliar o nervo#oculomotor (III)?": ["*Movimentos dos olhos e resposta à luz", "Sensibilidade da face", "Força muscular das extremidades", "Controle da respiração"],
    "qual função o nervo troclear (IV) exerce?": ["*Movimento do olho para baixo e para dentro", "Movimento do olho para cima e para fora", "Sensibilidade do rosto", "Controle da mastigação"],
    "como o nervo trigêmeo (V) é testado no#exame físico?": ["*Avaliar a sensibilidade da face e os reflexos da mordida", "Avaliar a coordenação dos membros superiores", "Testar o movimento ocular", "Verificar a resposta à luz"],
    "o que é examinado ao testar o nervo abducente (VI)?": ["*Movimento dos olhos para os lados", "Sensibilidade do rosto", "Reflexos pupilares", "Coordenação motora das pernas"],
    "qual função o nervo facial (VII) desempenha?": ["*Controle dos músculos faciais e sensação gustativa", "Movimento ocular", "Sensibilidade da pele", "Movimento das extremidades"],
    "como o nervo vestibulococlear (VIII) é examinado?": ["*Avaliar a audição e o equilíbrio", "Testar os reflexos da mandíbula", "Verificar a resposta do paciente à dor", "Testar a acuidade visual"],
    "qual a primeira etapa do exame físico abdominal?": ["*Inspeção", "Palpação", "Percussão", "Auscultação"],
    "como é feita a inspeção abdominal durante o#exame físico?": ["*Observando a simetria, presença de distensão, cicatrizes e movimentos", "Palpando a região abdominal", "Verificando a dor do paciente", "Escutando os sons intestinais"],
    "o que a palpação abdominal pode revelar?": ["*Sensibilidade, resistência muscular e massas abdominais", "Som de percussão", "Distensão gástrica", "Presença de hematomas"],
    "qual é o objetivo da percussão no exame abdominal?": ["*Avaliar a densidade dos órgãos e identificar a presença de líquidos ou gases", "Medir o tamanho do fígado", "Verificar a acuidade visual", "Avaliar os reflexos de dor"],
    "como se realiza a ausculatação no exame físico#abdominal?": ["*Ouvir os sons intestinais para avaliar o funcionamento do sistema digestivo", "Verificar a presença de sons cardíacos", "Escutar a respiração", "Avaliar a pressão arterial"],
    "o que a presença de sons intestinais hiperativos#pode indicar?": ["*Possível diarreia ou aumento da motilidade intestinal", "Deficiência de enzimas digestivas", "Presença de cálculos biliares", "Problemas hepáticos"],
    "como é realizado o exame de Murphy?": ["*Pressionando o quadrante superior direito do abdômen e pedindo para o paciente inspirar profundamente", "Percorrendo a parte inferior do abdômen", "Palpando a região do fígado e baço", "Observando a simetria do abdômen"],
    "o que indica a presença de defesa muscular no#exame abdominal?": ["*Possível inflamação peritoneal", "Distensão abdominal", "Movimentos peristálticos acelerados", "Presença de hérnia"],
    "qual a importância do exame de bónus durante#o exame físico digestivo?": ["*Detectar a presença de líquido livre ou distensão abdominal", "Medir os reflexos", "Verificar a função renal", "Avaliar o estado nutricional do paciente"],
    "o que a palpação do fígado pode revelar?": ["*Hepatomegalia ou aumento do fígado", "Problemas nos pulmões", "Presença de cálculos renais", "Alterações nas vias respiratórias"],
    "qual é o primeiro passo no exame físico do#sistema urogenital?": ["*Inspeção da área genital", "Palpação do abdômen", "Auscultação dos rins", "Percussão do fígado"],
    "o que se deve observar durante a inspeção#da região genital no exame físico?": ["*Anormalidades como lesões, secreções ou assimetrias", "Dor ao toque", "Alterações no tônus muscular", "Ressonância abdominal"],
    "como é realizado o exame de palpação renal?": ["*Palpando os flancos, com o paciente em decúbito dorsal ou sentado", "Percorrendo a região abdominal", "Inspecionando os membros inferiores", "Verificando a distensão abdominal"],
    "o que indica a dor à palpação nos flancos#durante o exame físico urogenital?": ["*Possível presença de cálculos renais ou infecção urinária", "Problemas musculares", "Inflamação no sistema digestivo", "Distensão gástrica"],
    "o que se deve verificar durante o exame#físico das mamas no contexto urogenital?": ["*Alterações visíveis ou palpáveis, como nódulos ou secreção", "Alterações nos reflexos", "Presença de infecção respiratória", "Dor muscular na região"],
    "qual o objetivo da percussão no exame físico#do sistema urogenital?": ["*Detectar áreas de dor referida ou aumento dos órgãos genitais", "Avaliar a distensão abdominal", "Palpação de massas", "Verificar os sons intestinais"],
    "qual é o exame físico realizado para avaliar a#presença de retenção urinária?": ["*Palpação do suprapúbico para detectar distensão da bexiga", "Inspeção da cavidade oral", "Auscultação dos pulmões", "Percussão do fígado"],
    "o que se avalia durante a inspeção da uretra#no exame físico?": ["*Presença de secreção ou anormalidades", "Alterações na pressão arterial", "Pulsos periféricos", "Reflexos musculares"],
    "o que pode indicar a dor ao realizar a#palpação da próstata?": ["*Possível prostatite ou hipertrofia prostática benigna", "Problemas no trato respiratório", "Distúrbios metabólicos", "Alterações no sistema nervoso"],
    "quais sinais podem indicar infecção urinária#durante o exame físico?": ["*Sensibilidade abdominal inferior, febre e disúria", "Hipotensão", "Dificuldade respiratória", "Dor torácica"],
                       "qual é o primeiro passo no exame físico do#sistema linfático?": [
                           "*Inspeção e palpação dos linfonodos", "Auscultação cardíaca", "Palpação abdominal",
                           "Inspeção das extremidades"],
                       "onde os linfonodos podem ser palpados durante o#exame físico?": [
                           "*Pescoço, axilas, virilha e área supraclavicular", "No abdômen inferior",
                           "Nos membros inferiores", "Nos ossos longos"],
                       "qual é a principal característica a ser observada ao#examinar os linfonodos?": [
                           "*Tamanho, consistência, dor e mobilidade", "Forma", "Temperatura", "Cor da pele"],
                       "qual é o que pode indicar a presença de linfonodos#aumentados durante o exame físico?": [
                           "*Infecções, câncer ou doenças autoimunes", "Deficiência de vitaminas",
                           "Problemas respiratórios", "Alterações neurológicas"],
                       "o que pode indicar linfonodos duros e fixos#à palpação?": ["*Possível malignidade",
                                                                                   "Inflamação leve", "Edema linfático",
                                                                                   "Distúrbios digestivos"],
                       "como deve ser realizada a palpação dos#linfonodos inguinais?": [
                           "*Com os dedos curvados, pressionando suavemente a região inguinal",
                           "Com pressão forte na região abdominal", "Usando a palma das mãos para compressão",
                           "Percorrendo a região torácica"],
                       "qual é o que a palpação dos linfonodos cervicais#pode indicar?": [
                           "*Infecções respiratórias, mononucleose ou linfoma", "Problemas cardíacos",
                           "Distúrbios alimentares", "Alterações respiratórias"],
                       "quais linfonodos são mais frequentemente palpados#durante o exame físico?": [
                           "*Cervicais, axilares e inguinais", "Subclávios e epigástricos", "Pélvicos e femorais",
                           "Torácicos e carótidas"],
                       "o que a ausência de linfonodos palpáveis pode#indicar?": [
                           "*Normalidade, sem sinais de infecção ou doenças", "Infecção generalizada",
                           "Necessidade de exames de imagem", "Distúrbios metabólicos"],
                       "qual é o significado de linfonodos dolorosos#à palpação?": [
                           "*Indica inflamação, geralmente por infecção", "Indica distúrbios hormonais",
                           "É sinal de resistência a tratamento", "Está relacionado a problemas articulares"],
}

Questions_Microbiologia = {
#Microbiologia
"qual é o principal objetivo da microbiologia?": ["*Estudar microrganismos e seus efeitos sobre os seres vivos", "Estudar a anatomia dos microrganismos", "Estudar os microrganismos por sua cor e tamanho", "Estudar o metabolismo celular dos microrganismos"],
    "quais são os tipos principais de microrganismos#estudados na microbiologia?": ["*Bactérias, vírus, fungos e protozoários", "Somente bactérias e vírus", "Somente fungos e protozoários", "Somente bactérias e parasitas"],
    "qual é o papel dos microrganismos no ambiente?": ["*Decomposição de matéria orgânica e reciclagem de nutrientes", "Produção de alimentos para plantas", "Resistência a agentes externos", "Crescimento de células humanas"],
    "o que caracteriza as bactérias gram-positivas?": ["*Parede celular espessa e corante retido na coloração de Gram", "Ausência de parede celular e baixa afinidade com corante de Gram", "Parede celular fina e corante não retido", "Presença de cápsula gelatinosa"],
#Sttopage Point
    "quais são as principais formas de transmissão#de microrganismos?": ["*Aérea, contato direto e via sanguínea", "Somente via aérea", "Somente via digestiva", "Somente via sanguínea"],
    "o que é um agente patogênico?": ["*Um microrganismo que pode causar doenças", "Uma célula saudável", "Uma célula do sistema imunológico", "Um produto químico usado em vacinas"],
    "qual é a principal função das enzimas#microbianas?": ["*Degradar substâncias no ambiente ou hospedeiro", "Produzir substâncias tóxicas", "Gerar energia para os microrganismos", "Proteger contra radiação ultravioleta"],
    "qual é a principal diferença entre vírus#e bactérias?": ["*Vírus não possuem estrutura celular, enquanto bactérias possuem", "Vírus têm uma parede celular, bactérias não", "Bactérias são maiores que vírus", "Vírus têm DNA, enquanto bactérias têm RNA"],
    "o que são antibióticos?": ["*Substâncias que combatem infecções bacterianas", "Substâncias que combatem infecções virais", "Medicamentos usados para tratar alergias", "Substâncias que aumentam a imunidade"],
    "o que é resistência antimicrobiana?": ["*Quando microrganismos se tornam insensíveis a medicamentos", "Quando os antibióticos aumentam de efeito", "Quando os microrganismos se multiplicam rapidamente", "Quando o sistema imunológico combate as infecções"],
"o que é um ecossistema?": ["*Uma comunidade de organismos interagindo com seu ambiente físico", "Uma população de uma única espécie", "Uma área de alta biodiversidade", "Uma zona de proteção ambiental"],
"o que é uma relação interespecífica?": ["*Relação entre indivíduos de espécies diferentes", "Relação entre indivíduos da mesma espécie", "Relação entre um organismo e seu ambiente", "Relação entre predadores e presas"],
    "o que caracteriza a simbiose?": ["*Uma relação de interação entre seres vivos de espécies diferentes, em que ambos se beneficiam", "Uma relação entre indivíduos da mesma espécie", "Uma relação em que uma espécie se beneficia enquanto a outra é prejudicada", "Uma relação em que um organismo é comido por outro"],
    "o que é uma relação de parasitismo?": ["*Quando uma espécie se beneficia às custas de outra, prejudicando-a", "Quando duas espécies se beneficiam mutuamente", "Quando duas espécies competem por recursos", "Quando uma espécie ajuda a outra a sobreviver"],
    "o que é uma relação de competição?": ["*Quando duas espécies competem pelos mesmos recursos em um ambiente", "Quando uma espécie se alimenta de outra", "Quando duas espécies se ajudam mutuamente", "Quando uma espécie se beneficia sem prejudicar a outra"],
    "o que caracteriza uma relação de mutualismo?": ["*Quando duas espécies se beneficiam mutuamente", "Quando uma espécie se alimenta de outra", "Quando uma espécie é beneficiada e a outra prejudicada", "Quando duas espécies competem pelos mesmos recursos"],
    "o que é a predação?": ["*Quando um organismo caça e se alimenta de outro organismo", "Quando duas espécies competem pelos mesmos recursos", "Quando duas espécies vivem juntas em uma relação mutuamente benéfica", "Quando uma espécie ajuda outra sem esperar nada em troca"],
    "o que é uma relação de comensalismo?": ["*Quando uma espécie se beneficia e a outra não é nem beneficiada nem prejudicada", "Quando uma espécie caça e se alimenta de outra", "Quando duas espécies competem pelos mesmos recursos", "Quando uma espécie prejudica outra para se beneficiar"],
    "o que caracteriza a protocooperação?": ["*Uma relação em que duas espécies se beneficiam, mas não é obrigatória para sua sobrevivência", "Uma relação onde uma espécie se beneficia às custas da outra", "Uma relação em que duas espécies competem pelos mesmos recursos", "Uma relação em que uma espécie se adapta ao ambiente e a outra não"],
    "o que é uma relação amensalismo?": ["*Quando uma espécie é prejudicada sem que a outra seja beneficiada", "Quando duas espécies competem pelos mesmos recursos", "Quando duas espécies se beneficiam mutuamente", "Quando uma espécie se alimenta de outra"],
    "qual é a principal característica de uma relação#de antibiose?": ["*Quando um organismo secreta substâncias que matam ou inibem o crescimento de outro organismo", "Quando duas espécies se beneficiam mutuamente", "Quando uma espécie se adapta ao ambiente de outra", "Quando duas espécies competem por recursos limitados"],
"o que é epidemiologia?": ["*É o estudo da distribuição e determinantes das doenças na população", "É o estudo das causas genéticas das doenças", "É o estudo do tratamento das doenças infecciosas", "É o estudo das características psicológicas dos pacientes"],
    "qual é o objetivo principal da epidemiologia?": ["*Estudar a distribuição e os determinantes das doenças e agravos à saúde", "Estudar as causas psicológicas das doenças", "Desenvolver novos medicamentos para doenças infecciosas", "Monitorar o comportamento de doenças genéticas"],
    "o que caracteriza uma doença infecciosa?": ["*É causada por agentes patogênicos como bactérias, vírus ou fungos", "É uma doença mental que afeta o comportamento", "É causada por fatores ambientais como poluição", "É uma doença genética que afeta as células"],
    "o que é um surto epidemiológico?": ["*É o aumento de casos de uma doença em uma área geográfica limitada", "É a propagação de uma doença globalmente", "É a redução de casos de uma doença em uma área geográfica", "É a erradicação de uma doença em uma população"],
    "qual é a principal forma de transmissão das#doenças infecciosas?": ["*Por contato direto ou indireto com o agente patogênico", "Por contato com alimentos contaminados", "Por ingestão de medicamentos", "Por exposição a radiações"],
    "o que é uma doença endêmica?": ["*É uma doença que ocorre de forma constante em uma determinada região", "É uma doença que ocorre de forma esporádica", "É uma doença que afeta o sistema nervoso central", "É uma doença genética presente na população"],
    "o que é uma doença pandêmica?": ["*É uma doença que afeta grandes áreas geográficas e populações globais", "É uma doença que ocorre apenas em áreas rurais", "É uma doença que afeta apenas uma parte do corpo", "É uma doença transmitida por vetores como mosquitos"],
    "qual é a diferença entre doença transmissível#e não transmissível?": ["*Doenças transmissíveis são causadas por patógenos e podem ser transmitidas de pessoa para pessoa", "Doenças não transmissíveis são causadas por patógenos", "Doenças não transmissíveis podem ser transmitidas por alimentos", "Doenças transmissíveis não afetam o sistema respiratório"],
    "o que é uma zoonose?": ["*É uma doença infecciosa transmitida de animais para seres humanos", "É uma doença transmitida exclusivamente por contato sexual", "É uma doença respiratória transmitida por gotículas", "É uma doença genética que afeta a pele"],
    "qual é o papel da vigilância epidemiológica?": ["*Monitorar e investigar a distribuição de doenças, visando prevenir e controlar surtos", "Estudar os sintomas das doenças para diagnóstico", "Desenvolver vacinas para doenças infecciosas", "Fornecer tratamento médico às populações infectadas"],
    "o que caracteriza uma célula procariota?": ["*Ela não possui núcleo definido", "Ela possui núcleo delimitado por membrana", "Ela possui mitocôndrias", "Ela tem um sistema endomembranar desenvolvido"],
    "qual é o material genético presente nas#células procarioticas?": ["*O material genético está na região chamada nucleoide", "O material genético está dentro de um núcleo envolvido por uma carioteca", "O material genético é organizado em cromossomos lineares", "O material genético é envolvido por uma membrana nuclear"],
    "qual estrutura das células procarioticas é#responsável pela síntese de proteínas?": ["*Ribossomos", "Mitocôndrias", "Complexo de Golgi", "Retículo endoplasmático"],
    "qual é a função da parede celular nas células#procarioticas?": ["*Proteger a célula e dar forma", "Controlar a entrada e saída de substâncias", "Armazenar nutrientes", "Realizar a síntese de proteínas"],
    "qual estrutura é encontrada em algumas células#procarioticas e permite a mobilidade?": ["*Flagelos", "Lisossomos", "Retículo endoplasmático", "Peroxissomos"],
    "o que é a cápsula de algumas células procarioticas?": ["*É uma camada externa de polissacarídeos que protege a célula", "É uma camada de lipídios que forma a membrana plasmática", "É uma estrutura de flagelos que auxilia no movimento", "É uma estrutura de proteínas que ajuda na respiração celular"],
    "o que são plasmídeos nas células procarioticas?": ["*São pequenos fragmentos de DNA que podem ser transferidos entre células", "São estruturas de proteínas que realizam a digestão intracelular", "São organelas responsáveis pela produção de energia", "São cromossomos presentes no núcleo celular"],
    "qual é a função da membrana plasmática nas#células procarioticas?": ["*Controlar a entrada e saída de substâncias", "Sintetizar proteínas", "Produzir ATP", "Armazenar informações genéticas"],
    "qual é o tipo de divisão celular em células#procarioticas?": ["*Fissão binária", "Mitose", "Meiose", "Endocitose"],
    "como ocorre a respiração celular nas células#procarioticas?": ["*Ela ocorre na membrana plasmática ou em invaginações da membrana", "Ela ocorre no citoplasma", "Ela ocorre nas mitocôndrias", "Ela ocorre no núcleo"],
"qual é a principal função da técnica de#coloração de Gram?": ["*Classificar as bactérias em gram-positivas e gram-negativas", "Identificar a presença de vírus", "Detectar fungos", "Colorir as células eucarióticas"],
    "qual cor as bactérias gram-positivas ficam após#a coloração de Gram?": ["*Roxa", "Verde", "Vermelha", "Amarela"],
    "qual cor as bactérias gram-negativas ficam após#a coloração de Gram?": ["*Vermelha", "Roxa", "Verde", "Amarela"],
    "qual cor a metilenina azul utiliza para coloração#de estruturas celulares?": ["*Azul", "Vermelho", "Amarelo", "Verde"],
    "para que serve a coloração de Ziehl-Neelsen?": ["*Para detectar micobactérias, como o Mycobacterium tuberculosis", "Para colorir células eucarióticas", "Para diferenciar tipos de fungos", "Para identificar bactérias gram-negativas"],
    "qual é a característica da coloração de Gram#que a torna útil em microbiologia?": ["*Ela permite a distinção entre bactérias com base na estrutura da parede celular", "Ela cora todas as células de forma igual", "Ela detecta a presença de ribossomos", "Ela serve para identificar vírus e fungos"],
    "qual é o uso da coloração de Giemsa?": ["*Para detectar parasitas e células sanguíneas", "Para corar bactérias Gram-negativas", "Para observar células cancerígenas", "Para identificar vírus no sangue"],
    "qual é a técnica de coloração utilizada para#estudar estruturas nucleares das células?": ["*Coloração de Hematoxilina e Eosina", "Coloração de Gram", "Coloração de Saffranina", "Coloração de Ziehl-Neelsen"],
    "qual a técnica de coloração é mais usada para a#visualização de células com grandes quantidades de RNA?": ["*Coloração de azul de metileno", "Coloração de Gram", "Coloração de Giemsa", "Coloração de Hematoxilina e Eosina"],
    "qual técnica de coloração é usada para detectar#organismos intracelulares, como Chlamydia e Rickettsia?": ["*Coloração de Giemsa", "Coloração de Gram", "Coloração de Wright", "Coloração de Wright-Giemsa"],
    "qual é o nome da técnica de coloração utilizada#para visualizar a presença de fungos, como o Candida?": ["*Coloração de PAS (Ácido Periódico de Schiff)", "Coloração de Gram", "Coloração de Hematoxilina e Eosina", "Coloração de Giemsa"],
"qual é a principal diferença entre o metabolismo#aeróbico e anaeróbico?": ["*O metabolismo aeróbico utiliza oxigênio, enquanto o anaeróbico não", "O metabolismo anaeróbico usa oxigênio, enquanto o aeróbico não", "Ambos os metabolismos utilizam oxigênio da mesma forma", "Ambos não utilizam oxigênio de maneira significativa"],
    "o que é a glicólise?": ["*É o processo de quebra da glicose para produção de energia", "É a síntese de proteínas", "É o processo de divisão celular", "É o transporte de elétrons na cadeia respiratória"],
    "qual produto final é gerado durante a fermentação#láctica?": ["*Ácido láctico", "Ácido acético", "Álcool etílico", "Ácido pirúvico"],
    "qual é a função da cadeia de transporte de elétrons#no metabolismo aeróbico?": ["*Gerar ATP a partir da transferência de elétrons e prótons", "Produzir glicose a partir de oxigênio", "Transportar os ácidos graxos para a célula", "Fermentar a glicose em ausência de oxigênio"],
    "qual é o produto final da respiração aeróbica?": ["*Água e dióxido de carbono", "Álcool e oxigênio", "Ácido lático e oxigênio", "Ácido acético e oxigênio"],
    "qual processo metabólico ocorre no citoplasma#das células bacterianas?": ["*Glicólise", "Cadeia de transporte de elétrons", "Ciclo de Krebs", "Fosforilação oxidativa"],
    "qual é a principal função do ciclo de Krebs no#metabolismo celular?": ["*Gerar moléculas de alta energia como NADH e FADH2", "Produzir glicose", "Sintetizar proteínas", "Gerar oxigênio para a célula"],
    "qual tipo de micro-organismos é mais comum#realizar a fermentação?": ["*Bactérias e leveduras", "Somente bactérias", "Somente leveduras", "Somente vírus"],
    "o que acontece durante o processo de#respiração anaeróbica?": ["*A glicose é quebrada sem o uso de oxigênio, gerando produtos finais como ácido láctico ou etanol", "A glicose é convertida diretamente em ATP", "A célula utiliza oxigênio para quebrar a glicose", "A célula não quebra glicose, mas utiliza lipídios como fonte de energia"],
    "qual é o papel do NADH no metabolismo celular?": ["*Transportar elétrons para a cadeia de transporte de elétrons", "Formar glicose a partir de piruvato", "Armazenar oxigênio", "Armazenar ácido lático"],
"o que é necessário para cultivar micro-organismos#em laboratório?": ["*Nutrientes, temperatura adequada e condições de pH", "Apenas temperatura e luz", "Apenas nutrientes", "Somente um ambiente sem oxigênio"],
    "qual é o termo utilizado para descrever a multiplicação#de células bacterianas em um ambiente de cultura?": ["*Crescimento bacteriano", "Reprodução celular", "Metabolismo celular", "Fermentação"],
    "o que é um meio de cultura?": ["*Uma substância ou solução usada para promover o crescimento de micro-organismos", "Uma bactéria isolada em laboratório", "Um tipo de célula humana usada para cultura", "Uma solução com oxigênio e luz para crescimento celular"],
    "o que caracteriza o crescimento exponencial#de micro-organismos?": ["*A duplicação das células bacterianas a uma taxa constante", "O aumento da quantidade de nutrientes disponíveis", "O crescimento linear das células bacterianas", "A diminuição da taxa de divisão celular"],
    "qual é a principal diferença entre meios de#cultura seletivos e diferenciais?": ["*Meios seletivos favorecem o crescimento de algumas espécies, enquanto meios diferenciais permitem distinguir entre elas", "Meios seletivos podem crescer todas as espécies e diferenciais não", "Meios seletivos favorecem o crescimento de todas as espécies", "Meios diferenciais não possuem nutrientes suficientes"],
    "o que acontece durante a fase de latência do#crescimento bacteriano?": ["*As bactérias estão se adaptando ao ambiente, sem crescimento significativo", "As bactérias estão se dividindo rapidamente", "As bactérias estão morrendo devido à falta de nutrientes", "As bactérias estão consumindo nutrientes de forma máxima"],
    "qual é o efeito do aumento da temperatura no#crescimento microbiano?": ["*Pode acelerar o crescimento, até um limite de temperatura ótima", "Sempre desacelera o crescimento", "Não afeta o crescimento", "Aumenta a taxa de morte celular"],
    "o que é o tempo de duplicação em relação ao#crescimento bacteriano?": ["*É o tempo necessário para uma célula bacteriana se dividir e formar duas células", "É o tempo que as bactérias permanecem em fase de latência", "É o tempo que as bactérias consomem nutrientes", "É o tempo necessário para que todas as células morram"],
    "qual é a importância do pH nos meios de cultura?": ["*O pH afeta a atividade enzimática e o crescimento das células", "O pH não influencia o crescimento", "O pH afeta apenas a cor do meio de cultura", "O pH aumenta a concentração de oxigênio no meio"],
    "o que são culturas mistas no contexto microbiológico?": ["*Culturas contendo mais de uma espécie microbiana", "Culturas contendo apenas uma espécie microbiana", "Culturas com bactérias e fungos apenas", "Culturas apenas de organismos multicelulares"],
"o que é o DNA?": ["*Ácido desoxirribonucleico, responsável por armazenar informações genéticas", "Ácido ribonucleico, responsável pela síntese de proteínas", "Uma proteína envolvida na divisão celular", "Uma enzima que catalisa reações metabólicas"],
    "qual é a função principal do RNA mensageiro (mRNA)?": ["*Transportar informações genéticas do DNA para a síntese de proteínas", "Armazenar informações genéticas", "Catalisar reações químicas no interior da célula", "Transportar aminoácidos para o ribossomo"],
    "qual é a função da enzima DNA polimerase?": ["*Sintetizar novas cadeias de DNA durante a replicação", "Degradar o RNA durante a transcrição", "Fazer cortes no DNA durante a reparação", "Catalisar a formação de proteínas"],
    "o que é transcrição em biologia molecular?": ["*Processo de síntese de RNA a partir de um molde de DNA", "Processo de duplicação do DNA", "Processo de síntese de proteínas", "Processo de degradação do RNA"],
    "o que são ribossomos?": ["*Estruturas celulares responsáveis pela síntese de proteínas", "Enzimas que quebram ácidos nucleicos", "Organismos que realizam a respiração celular", "Componentes do citosol que ajudam na divisão celular"],
    "qual é a função do RNA transportador (tRNA)?": ["*Transportar aminoácidos para o ribossomo durante a tradução", "Formar o código genético no núcleo", "Catalisar a transcrição", "Armazenar informações genéticas no núcleo"],
    "qual é o processo de tradução em biologia molecular?": ["*Síntese de proteínas a partir do mRNA no ribossomo", "Duplicação do DNA", "Formação de RNA a partir do DNA", "Conversão de RNA em DNA"],
    "o que são exões e íntrons?": ["*Exões são partes codificantes do RNA, enquanto íntrons são regiões não codificantes", "Exões são regiões não codificantes, enquanto íntrons codificam proteínas", "Exões são proteínas e íntrons são lipídios", "Íntrons são partes do DNA, enquanto exões são regiões do RNA"],
    "o que é a replicação do DNA?": ["*Processo de duplicação do DNA para formar duas moléculas idênticas", "Processo de transcrição do RNA", "Processo de síntese de proteínas", "Processo de translação no ribossomo"],
    "o que é a estrutura do DNA?": ["*Uma dupla hélice formada por nucleotídeos", "Uma cadeia simples formada por aminoácidos", "Uma proteína complexa", "Um lipídio com estrutura em forma de espiral"],
"qual é o efeito do calor sobre os microrganismos?": ["*Pode desnaturar proteínas e matar microrganismos", "Aumenta a taxa de multiplicação sem matá-los", "Melhora a resistência a agentes antimicrobianos", "Não tem efeito sobre os microrganismos"],
    "qual é o efeito da radiação ultravioleta (UV)#sobre os microrganismos?": ["*Dá causa a mutações no DNA, matando ou inibindo a reprodução dos microrganismos", "Acelera o metabolismo bacteriano", "Estabiliza as membranas celulares", "Melhora a síntese de proteínas nas células"],
    "como os desinfetantes químicos atuam sobre os#microrganismos?": ["*Destróem ou inibem o crescimento de microrganismos", "Aumentam a atividade metabólica dos microrganismos", "Ajudam os microrganismos a se reproduzirem mais rapidamente", "Impedem a produção de proteínas nos microrganismos"],
    "qual é o efeito do álcool sobre os microrganismos?": ["*Desidrata e desnatura proteínas, matando os microrganismos", "Estimula o crescimento bacteriano", "Não tem efeito sobre os microrganismos", "Aumenta a resistência dos microrganismos a antibióticos"],
    "como a radiação ionizante afeta os microrganismos?": ["*Causa danos no DNA, levando à morte ou à incapacidade de reprodução", "Aumenta a taxa de crescimento bacteriano", "Inibe a síntese de proteínas, mas não mata os microrganismos", "Melhora a resistência aos antibióticos"],
    "qual é a função dos antibióticos?": ["*Inibir o crescimento ou matar microrganismos específicos", "Estimular a divisão celular dos microrganismos", "Aumentar a resistência dos microrganismos a outros agentes", "Proteger os microrganismos contra o calor"],
    "como os agentes oxidantes afetam os microrganismos?": ["*Causam danos nas membranas celulares e no material genético dos microrganismos", "Estimulam a produção de proteínas nos microrganismos", "Aumentam a resistência dos microrganismos ao calor", "Ajudam na síntese do DNA nos microrganismos"],
    "qual é o efeito dos solventes sobre os microrganismos?": ["*Dissolvem as membranas celulares e podem matar ou inibir o crescimento dos microrganismos", "Melhoram a reprodução dos microrganismos", "Ajudam na síntese de proteínas nos microrganismos", "Fortalecem as paredes celulares dos microrganismos"],
    "qual é a ação do calor úmido (autoclave)#sobre os microrganismos?": ["*Destrói microrganismos ao desnaturar proteínas e destruir estruturas celulares", "Aumenta a resistência dos microrganismos", "Melhora a reprodução dos microrganismos", "Aumenta a resistência dos microrganismos a agentes químicos"],
    "qual é o efeito da secagem sobre os microrganismos?": ["*Pode levar à desidratação e morte dos microrganismos", "Estimula o crescimento bacteriano", "Aumenta a multiplicação de fungos", "Não afeta os microrganismos"],
"o que é quimiorresistência em microrganismos?": ["*A capacidade dos microrganismos de resistir aos efeitos de substâncias químicas antimicrobianas", "A habilidade de microrganismos se adaptarem ao ambiente", "A resistência dos microrganismos ao calor", "A habilidade dos microrganismos de produzir toxinas para se defender"],
    "quais são os mecanismos pelos quais os microrganismos#podem desenvolver quimiorresistência?": ["*Alterações nas membranas celulares, bombas de efluxo, modificações enzimáticas", "Aumento da produção de radicais livres", "Reforço da parede celular", "Inibição da síntese de proteínas"],
    "qual é o principal mecanismo de resistência aos#antibióticos nos microrganismos?": ["*A produção de enzimas que inativam os antibióticos", "Alterações nas enzimas alvo do antibiótico", "Mutação genética", "Mudança na estrutura da membrana celular"],
    "o que são bombas de efluxo em microrganismos?": ["*Proteínas que bombeiam substâncias químicas para fora da célula, tornando-a resistente a antibióticos", "Enzimas que degradam os antibióticos", "Estruturas que aumentam a taxa de metabolismo do microrganismo", "Compostos que aumentam a penetração de antibióticos na célula"],
    "como as alterações nas membranas celulares#contribuem para a quimiorresistência?": ["*Alterações podem impedir a entrada de antibióticos na célula ou aumentar sua expulsão", "Elas aumentam a adesão do microrganismo ao hospedeiro", "Elas aumentam a produção de proteínas essenciais para o crescimento", "Elas reduzem a produção de proteínas de defesa"],
    "qual é o efeito da modificação enzimática na#quimiorresistência?": ["*As enzimas modificam a estrutura dos antibióticos, tornando-os ineficazes", "Elas aumentam a penetração dos antibióticos na célula", "Elas estimulam o crescimento do microrganismo", "Elas aumentam a produção de toxinas"],
    "como a resistência aos antibióticos pode ser#transferida entre microrganismos?": ["*Por meio de plasmídeos ou transferência horizontal de genes", "Por meio de mutações espontâneas", "Por aumento da produção de toxinas", "Por mudança no ciclo de vida do microrganismo"],
    "o que é resistência cruzada?": ["*Quando um microrganismo resistente a um antibiótico se torna resistente a outros antibióticos, mesmo que não tenha sido exposto a eles", "Quando o microrganismo perde sua capacidade de reprodução", "Quando o microrganismo altera sua morfologia", "Quando o microrganismo se adapta ao ambiente sem alterar sua resistência"],
    "quais fatores contribuem para o desenvolvimento#de quimiorresistência?": ["*Uso inadequado de antibióticos, mutações, e transferência de genes de resistência", "Alimentação inadequada do microrganismo", "Falta de exposição aos antibióticos", "Mudança no ciclo de vida dos microrganismos"],
    "qual é o impacto da quimiorresistência na#saúde pública?": ["*Aumento da dificuldade no tratamento de infecções, tornando algumas doenças difíceis de curar", "A diminuição dos casos de infecção", "A melhora da eficácia de tratamentos antibióticos", "Aumento da capacidade dos antibióticos de eliminar microrganismos"],
"o que é uma amostra representativa em microbiologia?": ["*Uma amostra que reflete com precisão as características da população microbiana", "Uma amostra coletada aleatoriamente sem controle", "Uma amostra com alta concentração de microrganismos", "Uma amostra isolada de um único tipo de microrganismo"],
    "quais são os principais tipos de amostras#em microbiologia?": ["*Amostras clínicas, ambientais e alimentícias", "Amostras de sangue e urina", "Amostras de fezes apenas", "Amostras de tecidos vivos"],
    "quais cuidados são necessários ao coletar#amostras clínicas?": ["*Uso de técnicas assépticas para evitar contaminação", "Coleta apenas em ambientes não controlados", "Não é necessário usar luvas ou equipamentos esterilizados", "Coleta somente de locais visíveis à vista"],
    "qual é o objetivo da coleta de amostras#microbiológicas?": ["*Isolar e identificar microrganismos presentes no local da coleta", "Proteger o paciente de infecções", "Destruir os microrganismos presentes", "Impedir a propagação de doenças"],
    "quais são os tipos de amostras alimentícias#usadas em microbiologia?": ["*Amostras de alimentos crus, cozidos e bebidas", "Somente amostras de alimentos crus", "Amostras de alimentos processados", "Somente amostras de alimentos líquidos"],
    "qual é o método mais comum para coleta de#amostras de sangue?": ["*Coleta por punção venosa ou arterial", "Coleta por amostra urinária", "Coleta de saliva", "Coleta de suor"],
    "como as amostras ambientais são coletadas#em microbiologia?": ["*Coleta de superfícies, ar e água para análise de contaminação microbiana", "Somente coleta de água", "Somente coleta de ar", "Coleta de alimentos expostos ao ambiente"],
    "quais são os cuidados na coleta de amostras#de fezes?": ["*Evitar contaminação com materiais externos e manter a amostra refrigerada", "Não é necessário refrigerar a amostra", "Coletar a amostra em qualquer recipiente", "Usar apenas frascos grandes para a coleta"],
    "quais tipos de tubos são usados para a coleta#de amostras de urina?": ["*Túbulos estéreis ou com conservantes específicos", "Túbulos com ágar", "Túbulos com corantes", "Túbulos com soro fisiológico"],
    "qual é o procedimento adequado para transportar#amostras microbiológicas?": ["*Usar recipientes estéreis e transportá-las em temperatura controlada", "Transportar em qualquer recipiente", "Usar sacos plásticos comuns", "Não há necessidade de temperatura controlada"],
"o que caracteriza a resistência inespecífica#do organismo?": ["*Defesas gerais contra patógenos, independentemente do tipo de microrganismo", "Resposta imune específica para cada patógeno", "Capacidade de produzir anticorpos direcionados", "Resposta apenas a vírus"],
    "qual é a principal função da barreira física#na resistência inespecífica?": ["*Impedir a entrada de microrganismos no organismo", "Ativar células do sistema imunológico", "Produzir anticorpos", "Destruir microrganismos dentro do corpo"],
    "quais são os principais componentes da resistência#inespecífica?": ["*Barreiras físicas, células fagocíticas e proteínas antimicrobianas", "Anticorpos, linfócitos T e B", "Células de memória", "Respostas inflamatórias específicas"],
    "como as células fagocíticas contribuem para a#resistência inespecífica?": ["*Eliminam microrganismos através da fagocitose", "Produzem anticorpos para eliminar patógenos", "Realizam a imunização passiva", "Ativam a resposta imune adaptativa"],
    "o que é a resposta inflamatória na resistência#inespecífica?": ["*Uma reação do corpo a lesões ou infecções para combater patógenos", "A produção de anticorpos específicos", "A ativação de linfócitos T", "A eliminação de células infectadas pelo vírus"],
    "quais células estão envolvidas na resposta#imune inespecífica?": ["*Macrófagos, neutrófilos e células dendríticas", "Linfócitos T e B", "Células de memória", "Células NK e células T CD8+"],
    "qual a função das células natural killer#(NK) na resistência inespecífica?": ["*Destruir células infectadas ou tumorais sem necessidade de reconhecimento específico", "Produzir anticorpos", "Ativar os linfócitos T", "Aumentar a produção de células de memória"],
    "quais proteínas são responsáveis #resistência inespecífica?": ["*Proteínas do sistema complemento que ajudam na destruição de patógenos", "Anticorpos produzidos pelas células B", "Proteínas específicas para cada patógeno", "Anticorpos IgA, IgM e IgG"],
    "como o sistema imunológico responde à infecção#de maneira inespecífica?": ["*Ativando a inflamação, fagocitose e a resposta do sistema complemento", "Produzindo anticorpos específicos para o patógeno", "Liberando antígenos", "Produzindo células T citotóxicas"],
    "quais são as fases da resposta imune do#hospedeiro durante uma infecção?": ["*Reconhecimento do patógeno, ativação da resposta imune e eliminação do patógeno", "Produção de linfócitos T e B apenas", "Resposta inicial de inflamação", "Produção de anticorpos"],
    "o que caracteriza a resposta imune específica#do hospedeiro?": ["*Resposta direcionada contra um patógeno específico", "Resposta contra todos os tipos de microrganismos", "Atividade do sistema complemento apenas", "Respostas inflamatórias inespecíficas"],
    "quais células são responsáveis pela resposta#imune específica?": ["*Linfócitos T e B", "Neutrófilos e macrófagos", "Células NK e dendríticas", "Células do sistema complemento"],
    "o que são os anticorpos na resposta#imune específica?": ["*Proteínas que se ligam a antígenos para neutralizar ou destruir patógenos", "Células que matam diretamente os patógenos", "Moléculas que ativam a resposta inflamatória", "Células que fagocitam os microrganismos"],
    "qual a função dos linfócitos T na resposta#imune específica?": ["*Destruir células infectadas e coordenar a resposta imune", "Fagocitar patógenos", "Produzir anticorpos", "Ativar células do sistema complemento"],
    "qual a função dos linfócitos B na resposta#imune específica?": ["*Produzir anticorpos contra patógenos específicos", "Destruir células infectadas", "Ajudar na ativação de linfócitos T", "Iniciar a inflamação local"],
    "o que são os antígenos no contexto da#defesa imunológica?": ["*Substâncias que são reconhecidas pelo sistema imunológico e induzem a produção de anticorpos", "Moléculas que matam os patógenos diretamente", "Células que apresentam a infecção ao sistema imunológico", "Substâncias produzidas pelas células T"],
    "como os linfócitos T CD8+ atuam na defesa#específica do hospedeiro?": ["*Eliminando células infectadas por vírus ou células tumorais", "Produzindo anticorpos", "Ativando linfócitos B", "Destruindo microrganismos diretamente"],
    "o que é a imunização ativa?": ["*Exposição ao antígeno para estimular a produção de memória imunológica e anticorpos", "Injeção de anticorpos prontos", "Ação de células NK para destruir patógenos", "Resposta imediata à infecção sem ativação de memória imunológica"],
    "o que caracteriza a imunização passiva?": ["*Transferência de anticorpos prontos para proteger contra doenças", "Ativação de linfócitos T e B", "Exposição direta ao patógeno", "Estímulo da memória imunológica"],
    "o que é a memória imunológica?": ["*Capacidade do sistema imunológico de lembrar e responder mais rapidamente a um patógeno previamente encontrado", "Resistência do hospedeiro a todos os tipos de patógenos", "Produção de anticorpos por células B", "Resposta imune imediata ao primeiro contato com um patógeno"],
"o que caracteriza uma reação de hipersensibilidade#do tipo I?": ["*Reação alérgica imediata mediada por IgE", "Reação alérgica mediada por células T", "Reação imunológica que envolve a produção de anticorpos IgM", "Resposta inflamatória crônica com envolvimento de macrófagos"],
    "qual é a principal substância liberada durante#uma reação de hipersensibilidade do tipo I?": ["*Histamina", "Interleucina-2", "Citoquinas inflamatórias", "Prostaglandinas"],
    "qual é o papel dos mastócitos nas reações#alérgicas?": ["*Liberação de mediadores inflamatórios como histamina", "Produção de anticorpos IgG", "Fagocitose de patógenos", "Estimulação de linfócitos T"],
    "qual é a principal característica das reações#de hipersensibilidade do tipo II?": ["*Dano celular mediado por anticorpos contra antígenos na superfície celular", "Resposta imune mediada por células T", "Ação de anticorpos IgE contra alérgenos", "Dano ao tecido causado pela ativação de complemento"],
    "o que ocorre nas reações de hipersensibilidade#do tipo III?": ["*Formação de complexos imunes que se depositam nos tecidos", "Destruição de células por linfócitos T", "Reação alérgica mediada por IgE", "Ativação do sistema complemento em excesso"],
    "qual é a principal característica da hipersensibilidade#do tipo IV?": ["*Resposta mediada por células T, sem a participação de anticorpos", "Produção de IgE em grande quantidade", "Resposta inflamatória imediata", "Reação alérgica mediada por anticorpos IgG"],
    "qual é o exemplo clássico de hipersensibilidade#do tipo I?": ["*Alergia a pólen ou alimentos", "Rejeição de enxertos", "Artrite reumatoide", "Doença celíaca"],
    "quais são os sintomas comuns da hipersensibilidade#do tipo I?": ["*Urticária, anafilaxia, asma", "Fadiga, febre e dor muscular", "Dor abdominal e diarreia", "Dificuldade para respirar e tosse crônica"],
    "o que é anafilaxia?": ["*Uma reação alérgica grave e imediata que pode levar à morte", "Uma reação inflamatória crônica nas articulações", "Uma resposta autoimune a células do próprio corpo", "Uma reação a medicamentos com formação de anticorpos IgG"],
    "qual é a principal diferença entre a hipersensibilidade#do tipo I e do tipo II?": ["*Tipo I envolve anticorpos IgE e reação imediata, enquanto tipo II envolve anticorpos IgG e ataque a células", "Tipo I é mediada por células T e tipo II por anticorpos IgM", "Tipo I é crônica e tipo II é aguda", "Tipo II envolve a liberação de histamina e tipo I não"],
    "qual é o tratamento mais comum para reações de#hipersensibilidade do tipo I?": ["*Antihistamínicos e corticosteróides", "Antibióticos", "Imunossupressores", "Anti-inflamatórios não esteroides"],
"qual é a principal propriedade dos microrganismos patogênicos#para causar doença?": ["*Habilidade de aderir e invadir células hospedeiras", "Produção de toxinas somente", "Capacidade de sobreviver em ambientes externos sem hospedeiro", "Habilidade de se replicar em grande velocidade"],
    "o que são fatores de virulência?": ["*Propriedades dos microrganismos que permitem a infecção e a colonização do hospedeiro", "Anticorpos produzidos pelo hospedeiro para combater infecções", "Resistência do hospedeiro a infecções", "Substâncias que matam as células do hospedeiro"],
    "qual é a função das cápsulas bacterianas em#microrganismos patogênicos?": ["*Evitar a fagocitose pelo sistema imunológico do hospedeiro", "Facilitar a aderência aos tecidos", "Produzir toxinas para danificar os tecidos do hospedeiro", "Impedir a replicação de células hospedeiras"],
    "como as toxinas bacterianas contribuem para#a patogênese?": ["*Causando dano direto às células hospedeiras ou ativando respostas inflamatórias excessivas", "Ajudando a aumentar a multiplicação bacteriana", "Estimulando o sistema imunológico a produzir mais anticorpos", "Inibindo a resposta imune do hospedeiro"],
    "o que são os fatores de adesão dos microrganismos?": ["*Estruturas ou moléculas que permitem aos microrganismos aderir às superfícies das células hospedeiras", "Enzimas que digerem os tecidos do hospedeiro", "Anticorpos produzidos pelo microrganismo", "Substâncias que destroem o sistema imunológico do hospedeiro"],
    "qual é o papel das enzimas extracelulares na#virulência dos microrganismos?": ["*Degradar tecidos do hospedeiro para facilitar a invasão e a disseminação", "Proteger o microrganismo da ação dos antibióticos", "Bloquear a fagocitose pelas células do hospedeiro", "Evitar a perda de nutrientes do hospedeiro"],
    "o que é a capacidade de invasão em microrganismos#patogênicos?": ["*Habilidade de penetrar e multiplicar-se dentro dos tecidos do hospedeiro", "Capacidade de produzir toxinas", "Facilidade de se transportar por via aérea", "Habilidade de se adaptar a diferentes tipos de ambientes"],
    "o que são as endotoxinas?": ["*Toxinas associadas à parede celular de bactérias Gram-negativas que causam inflamação quando liberadas", "Proteínas que promovem a adesão bacteriana", "Enzimas que auxiliam na invasão dos tecidos", "Moléculas que ajudam a neutralizar o sistema imunológico do hospedeiro"],
    "qual é o papel da resistência aos antibióticos para a#virulência dos microrganismos?": ["*Permitir que o microrganismo sobreviva e se multiplique mesmo na presença de tratamentos antimicrobianos", "Ajudar a estimular a produção de toxinas", "Aumentar a aderência do microrganismo ao hospedeiro", "Facilitar a fagocitose das células do hospedeiro"],
    "como os microrganismos patogênicos podem evadir o#sistema imunológico do hospedeiro?": ["*Modificando suas superfícies antigênicas ou produzindo substâncias que inibem a resposta imune", "Aumentando a produção de anticorpos", "Estimular a produção de células T no hospedeiro", "Ativando os macrófagos do hospedeiro"],
"o que caracteriza uma célula bacteriana?": ["*Ausência de núcleo definido, com material genético disperso no citoplasma", "Presença de organelas como mitocôndrias e cloroplastos", "Membrana plasmática dupla", "Presença de núcleo envolvido por membrana nuclear"],
    "quais são as formas básicas das bactérias?": ["*Coco, bacilo, espiral", "Esférica, cúbica, prismática", "Cilíndrica, cúbica, piramidal", "Filamentosa, esférica, cilíndrica"],
    "quais são as principais características da parede#celular bacteriana?": ["*Composta por peptidoglicano, responsável pela rigidez e forma", "Composta por lipídios e proteínas", "Possui uma camada de celulose", "É feita de material genético"],
    "quais tipos de bactérias possuem parede celular#espessa de peptidoglicano?": ["*Bactérias Gram-positivas", "Bactérias Gram-negativas", "Bactérias acidofílicas", "Bactérias aeróbias"],
    "o que são as bactérias Gram-negativas?": ["*Bactérias que possuem uma parede celular fina e uma membrana externa", "Bactérias que possuem parede celular espessa", "Bactérias que não possuem parede celular", "Bactérias que são incapazes de realizar respiração celular"],
    "como as bactérias se reproduzem?": ["*Por divisão binária", "Por mitose", "Por esporulação", "Por conjugação"],
    "quais são os meios de transmissão das bactérias?": ["*Contato direto, aerossóis, água e alimentos contaminados", "Somente por contato direto", "Apenas por transmissão sexual", "Somente através do ar"],
    "o que são esporos bacterianos?": ["*Estruturas de resistência formadas por algumas bactérias, permitindo sua sobrevivência em condições extremas", "Pequenas células que se formam para reprodução sexual", "Moléculas que ajudam as bactérias a se moverem", "Estruturas de defesa contra antibióticos"],
    "quais são as principais classificações das bactérias#quanto à sua coloração de Gram?": ["*Gram-positivas e Gram-negativas", "Ácido-alcool-resistentes e não-resistentes", "Aeróbias e anaeróbias", "Heterotróficas e autótrofas"],
    "qual é o objetivo da coloração de Gram?": ["*Diferenciar as bactérias em Gram-positivas e Gram-negativas com base nas características da parede celular", "Contar a quantidade de bactérias", "Verificar a presença de esporos", "Diferenciar as bactérias em aeróbias e anaeróbias"],
"quais são as principais características dos#cocos Gram-positivos?": ["*Possuem parede celular espessa com peptidoglicano", "Possuem membrana externa fina", "São imunes à coloração de Gram", "Não possuem parede celular"],
    "qual é o exemplo clássico de coco Gram-positivo?": ["*Staphylococcus aureus", "Escherichia coli", "Neisseria gonorrhoeae", "Salmonella typhi"],
    "quais são as principais características dos#cocos Gram-negativos?": ["*Possuem parede celular fina com uma membrana externa", "Possuem parede celular espessa", "São incolores na coloração de Gram", "São incapazes de formar esporos"],
    "qual é o exemplo clássico de coco#Gram-negativo?": ["*Neisseria gonorrhoeae", "Streptococcus pneumoniae", "Enterococcus faecalis", "Clostridium botulinum"],
    "quais cocos Gram-positivos são comumente associados#a infecções hospitalares?": ["*Staphylococcus aureus", "Neisseria gonorrhoeae", "Streptococcus pneumoniae", "Enterococcus faecalis"],
    "como as bactérias Gram-negativas se distinguem#na coloração de Gram?": ["*Elas aparecem coradas de rosa ou vermelhas", "Elas aparecem coradas de roxo", "Elas não reagem à coloração de Gram", "Elas aparecem coradas de verde"],
    "quais são os fatores de virulência mais comuns#de cocos Gram-positivos como o Staphylococcus aureus?": ["*Produção de toxinas e adesinas", "Resistência a antibióticos", "Produção de esporos", "Capacidade de formar biofilmes"],
    "qual a principal diferença entre os cocos Gram-positivos#e Gram-negativos em termos de parede celular?": ["*Cocos Gram-positivos têm parede celular espessa com peptidoglicano, enquanto os Gram-negativos têm uma camada fina de peptidoglicano e uma membrana externa", "Os cocos Gram-positivos possuem membrana externa, enquanto os Gram-negativos não possuem", "Os cocos Gram-negativos têm mais peptidoglicano que os Gram-positivos", "Cocos Gram-positivos são anaeróbios e os Gram-negativos são aeróbios"],
    "como as infecções por cocos Gram-negativos geralmente#se caracterizam?": ["*São mais resistentes a antibióticos devido à membrana externa", "São menos virulentas que as infecções Gram-positivas", "Não são causadas por contato direto", "Geralmente não causam inflamação nas mucosas"],
"o que caracteriza as enterobactérias?": ["*São bacilos Gram-negativos e anaeróbios facultativos", "São cocos Gram-positivos", "São bacilos Gram-positivos e anaeróbios obrigatórios", "São microaerofílicos"],
    "qual é o exemplo clássico de enterobactéria patogênica?": ["*Escherichia coli", "Salmonella enterica", "Enterococcus faecalis", "Staphylococcus aureus"],
    "qual é a principal característica de Escherichia coli?": ["*É uma enterobactéria coliforme que pode ser patogênica em algumas cepas", "É uma enterobactéria não patogênica", "É uma bactéria Gram-positiva", "É uma bactéria anaeróbia obrigatória"],
    "quais doenças podem ser causadas por enterobactérias?": ["*Diarreia, infecções urinárias, sepse", "Pneumonia e infecções respiratórias", "Infecções fúngicas e virais", "Infecções parasitárias e respiratórias"],
    "qual das enterobactérias é frequentemente associada a#infecções alimentares?": ["*Salmonella enterica", "Klebsiella pneumoniae", "Proteus vulgaris", "Serratia marcescens"],
    "qual é o principal mecanismo de virulência das#enterobactérias como a Salmonella?": ["*Produção de toxinas e capacidade de invadir células do hospedeiro", "Formação de esporos e resistência a antibióticos", "Produção de biofilmes e resistência ao sistema imune", "Capacidade de formar cistos e multiplicação intracelular"],
    "quais são as características dos testes laboratoriais#para identificar enterobactérias?": ["*Fermentação de glicose e produção de gás", "Fermentação de lactose com liberação de ácido", "Ausência de fermentação de glicose", "Produção de esporos em meio de cultivo"],
    "qual enterobactéria é a principal causadora de#infecções urinárias?": ["*Escherichia coli", "Klebsiella pneumoniae", "Proteus vulgaris", "Salmonella enterica"],
    "qual é a resistência mais comum das enterobactérias?": ["*Resistência a antibióticos como penicilinas e cefalosporinas", "Resistência a altas temperaturas", "Resistência a antibióticos como tetraciclina e quinolonas", "Resistência ao sistema imune do hospedeiro"],
    "como as enterobactérias são tipicamente transmitidas?": ["*Por ingestão de alimentos ou água contaminados", "Por contato com superfícies contaminadas", "Por picadas de insetos", "Por contato com secreções respiratórias"],
"quais são as características dos BGN não fermentadores?": ["*São bacilos Gram-negativos que não fermentam carboidratos", "São bacilos Gram-positivos que fermentam carboidratos", "São coccos Gram-negativos e fermentadores", "São bacilos Gram-negativos e anaeróbios"],
    "quais são as bactérias patogênicas gastroentéricas mais#comuns?": ["*Salmonella, Shigella e Escherichia coli", "Streptococcus pneumoniae e Staphylococcus aureus", "Pseudomonas aeruginosa e Klebsiella pneumoniae", "Clostridium tetani e Bacillus anthracis"],
    "quais são as características das BGP não esporuladas#aeróbicas?": ["*São bacilos Gram-positivos, não formam esporos e crescem em ambientes aeróbicos", "São bacilos Gram-negativos, não formam esporos e crescem em ambientes anaeróbicos", "São coccos Gram-positivos e esporulantes", "São bacilos Gram-negativos, formam esporos e crescem em ambientes aeróbicos"],
    "quais são as características das BGP esporuladas aeróbicas?": ["*São bacilos Gram-positivos que formam esporos e crescem em ambientes aeróbicos", "São bacilos Gram-negativos que formam esporos e crescem em ambientes anaeróbicos", "São coccos Gram-positivos, não formam esporos e crescem em ambientes aeróbicos", "São bacilos Gram-positivos, não formam esporos e crescem em ambientes anaeróbicos"],
    "quais são as características das BGP esporuladas anaeróbicas?": ["*São bacilos Gram-positivos que formam esporos e crescem em ambientes anaeróbicos", "São bacilos Gram-negativos que formam esporos e crescem em ambientes aeróbicos", "São coccos Gram-positivos que não formam esporos", "São bacilos Gram-negativos, não formam esporos e crescem em ambientes aeróbicos"],
    "quais são as características dos actinobactérias?": ["*São bactérias Gram-positivas, filamentosas e que formam esporos", "São bactérias Gram-negativas, esporulantes e anaeróbias", "São bactérias Gram-positivas, não esporulantes e aeróbias", "São bactérias Gram-negativas, filamentosas e anaeróbias"],
    "quais doenças são causadas por BGN não fermentadores?": ["*Infecções respiratórias, urinárias e sepse", "Infecções gastrointestinais e respiratórias", "Infecções cutâneas e neurológicas", "Infecções urinárias e genitais"],
    "quais doenças as bactérias patogênicas gastroentéricas#causam?": ["*Diarreia, cólera, febre tifóide e gastroenterite", "Meningite, pneumonia e infecções urinárias", "Infecções pulmonares e septicemia", "Infecções cutâneas e respiratórias"],
    "quais doenças podem ser causadas por BGP não esporulantes#aeróbicos?": ["*Endocardite, abscessos e infecções respiratórias", "Diarreia, infecções urinárias e meningite", "Infecções gastrointestinais e pulmonares", "Infecções respiratórias e urinárias"],
    "qual é a principal característica de actinobactérias?": ["*Sua capacidade de formar filamentos e esporos", "Sua capacidade de formar cápsulas e biofilmes", "Sua capacidade de fermentação de glicose", "Sua capacidade de formar toxinas exotóxicas"],
"quais são as características dos bacilos Gram-negativos#pleomórficos e pequenos?": ["*São bacilos Gram-negativos com formas variáveis e pequenas", "São coccos Gram-negativos e grandes", "São bacilos Gram-positivos e grandes", "São bacilos Gram-negativos, pleomórficos e grandes"],
    "quais são as principais características do gênero#Bacteroides spp.?": ["*São bactérias Gram-negativas anaeróbicas que fazem parte da flora intestinal", "São bactérias Gram-positivas aeróbicas", "São bactérias Gram-negativas que vivem no solo", "São bactérias Gram-positivas que fermentam carboidratos"],
    "qual é o principal modo de transmissão das rickettsias?": ["*Por picada de artrópodes, como carrapatos e pulgas", "Por via aérea", "Por ingestão de alimentos contaminados", "Por contato com secreções corporais"],
    "quais são as características das bactérias do#gênero Chlamydia spp.?": ["*São bactérias Gram-negativas intracelulares obrigatórias", "São bactérias Gram-positivas que fermentam carboidratos", "São bactérias Gram-negativas extracelulares", "São bactérias Gram-positivas aeróbicas"],
    "quais são as características das bactérias do#gênero Mycoplasma spp.?": ["*Não possuem parede celular e são muito pequenas", "Possuem parede celular espessa e são grandes", "São bactérias Gram-positivas, grandes e aeróbicas", "São bactérias Gram-negativas com cápsula"],
    "quais doenças são causadas pelo gênero#Mycoplasma spp.?": ["*Pneumonia atípica, uretrite e infecções genitais", "Diarreia e cólera", "Meningite e sepse", "Infecções respiratórias e urinárias"],
    "quais doenças são causadas pelas rickettsias?": ["*Febre maculosa, tifo e febre Q", "Gripe e resfriado comum", "Infecções respiratórias e urinárias", "Infecções intestinais e gástricas"],
    "quais são as características do gênero#Ureaplasma sp.?": ["*São microrganismos sem parede celular e causam infecções do trato urinário e genital", "São bactérias Gram-positivas que causam pneumonia", "São bactérias Gram-negativas anaeróbias", "São bactérias Gram-positivas que fermentam lactose"],
    "qual é a principal característica das bactérias#do gênero Bacteroides spp.?": ["*São anaeróbicas e fazem parte da microbiota intestinal", "São aeróbicas e patogênicas", "São gram-positivas e formam esporos", "São acidófilas e patogênicas"],
    "quais doenças podem ser causadas por Chlamydia spp.?": ["*Conjuntivite, uretrite e doenças sexualmente transmissíveis", "Pneumonia, meningite e infecções intestinais", "Febre, resfriados e infecções respiratórias", "Diarreia, cólera e gastroenterite"],
"quais são as características dos bacilos Gram-positivos#esporulados aeróbios?": ["*Possuem parede celular espessa e formam esporos", "São Gram-negativos e formam esporos", "São bacilos Gram-negativos sem parede celular", "São coccos Gram-positivos esporulados"],
    "qual é o gênero de bacilos Gram-positivos esporulados#aeróbios mais comum?": ["*Bacillus", "Clostridium", "Listeria", "Staphylococcus"],
    "quais doenças são causadas pelos bacilos do#gênero Bacillus?": ["*Antraz, intoxicação alimentar e outras infecções", "Tétano, botulismo e gangrena gasosa", "Infecções respiratórias e urinárias", "Diarreia, cólera e gastroenterite"],
    "qual é a principal característica dos bacilos#do gênero Bacillus?": ["*Formação de esporos e capacidade de sobrevivência em ambientes hostis", "Produção de toxinas e resistência a antibióticos", "Capacidade de fermentar carboidratos e causar infecções", "Resistência a altas temperaturas e à desidratação"],
    "qual bacilo Gram-positivo esporulado aeróbio#é conhecido por causar antraz?": ["*Bacillus anthracis", "Clostridium tetani", "Bacillus subtilis", "Clostridium perfringens"],
    "quais são as características do Bacillus anthracis?": ["*Causa antraz e forma esporos resistentes", "Causa tétano e é anaeróbio", "Forma toxinas que afetam o sistema nervoso", "Não forma esporos e é anaeróbio"],
    "qual é o mecanismo de transmissão do Bacillus#anthracis?": ["*Inalação, ingestão ou contato com esporos", "Transmissão sexual", "Por picada de insetos", "Por ingestão de alimentos contaminados"],
    "quais tipos de doenças podem ser causados por#Bacillus cereus?": ["*Intoxicação alimentar e diarreia", "Antraz e sepse", "Pneumonia e meningite", "Infecções urinárias e respiratórias"],
    "quais são as principais características de#Bacillus subtilis?": ["*É um bacilo esporulado comum no solo e em ambientes naturais", "É um patógeno anaeróbio", "É uma bactéria Gram-negativa", "É um patógeno intrahospitalar causador de sepse"],
    "quais são os fatores de virulência de Bacillus#anthracis?": ["*Produção de toxinas e formação de esporos", "Capacidade de fermentar carboidratos", "Produção de cápsula e capacidade de se dividir rapidamente", "Produção de enzimas digestivas"],
"quais são as principais características dos#microorganismos espirilares?": ["*São bactérias com forma de espiral, podem ser movidas por flagelos", "São bactérias esféricas com parede espessa", "Possuem forma de bastão e não possuem flagelos", "São bactérias Gram-negativas sem flagelos"],
    "qual gênero de microorganismos espirilares é#responsável pela sífilis?": ["*Treponema", "Leptospira", "Borrelia", "Campylobacter"],
    "qual é o agente causador da leptospirose?": ["*Leptospira", "Treponema", "Borrelia", "Spirochaeta"],
    "quais são as características do gênero Borrelia?": ["*São espirais grandes, causam doenças como a doença de Lyme e a febre recorrente", "São Gram-positivos, causam sífilis e herpes", "São não-esporulados e causam gastroenterites", "São anaeróbios e causam doenças respiratórias"],
    "quais doenças são causadas pelo Treponema pallidum?": ["*Sífilis", "Doença de Lyme", "Febre tifoide", "Leptospirose"],
    "qual é o principal modo de transmissão de Leptospira?": ["*Contato com água ou solo contaminado com urina de animais infectados", "Transmissão sexual", "Através do ar", "Pelo contato com alimentos contaminados"],
    "quais são as principais características do#Treponema pallidum?": ["*É um patógeno espiralado que causa sífilis, com movimento helicoidal", "É um bacilo curvo que causa pneumonia", "Possui forma de bastão e causa infecções intestinais", "É uma bactéria anaeróbia que causa meningite"],
    "qual é a doença mais comum causada por#Borrelia burgdorferi?": ["*Doença de Lyme", "Sífilis", "Gonorreia", "Leptospirose"],
    "qual é a característica comum das bactérias do#gênero Spirochaeta?": ["*Possuem uma forma espiralada e flagelos que permitem locomoção", "Possuem uma cápsula espessa e são imunes ao sistema imunológico", "São anaeróbias e causam infecções respiratórias", "São gram-negativas e produzem toxinas"],
    "quais características permitem a identificação#do gênero Borrelia?": ["*Forma espiralada e capacidade de causar febres recorrentes", "Forma bastonete e produção de esporos", "Forma esférica e fermentação de carboidratos", "Possuem parede espessa e causam tétano"],
"o que é a micologia?": ["*É o estudo dos fungos, incluindo suas propriedades, doenças e aplicação", "É o estudo das bactérias", "É o estudo dos vírus", "É o estudo das plantas"],
    "quais são as características gerais dos fungos?": ["*São organismos eucarióticos, podem ser unicelulares ou multicelulares, e se reproduzem por esporos", "São organismos procariotos, unicelulares e se reproduzem por divisão celular", "São organismos multicelulares, sem núcleo celular, e se reproduzem por brotamento", "São organismos autotróficos, possuem clorofila e se reproduzem por sementes"],
    "qual é a principal diferença entre fungos e#bactérias?": ["*Fungos são eucarióticos e bactérias são procariotos", "Fungos são unicelulares e bactérias são multicelulares", "Fungos não possuem núcleo, enquanto bactérias possuem núcleo", "Fungos se alimentam de luz e bactérias se alimentam de matéria orgânica"],
    "qual é a principal função dos fungos no ecossistema?": ["*Decompor matéria orgânica, reciclá-la e formar solos férteis", "Produzir oxigênio, como as plantas", "Causar doenças em plantas e animais", "Fixar nitrogênio no solo"],
    "quais são os tipos principais de fungos?": ["*Leveduras, bolores e cogumelos", "Bactérias, vírus e protozoários", "Algas, musgos e samambaias", "Plantas, fungos e líquens"],
    "qual tipo de reprodução os fungos podem realizar?": ["*Sexuada e assexuada, geralmente por esporos", "Somente assexuada, por fissão binária", "Somente sexuada, por divisão celular", "Somente por brotamento"],
    "qual é a estrutura dos fungos multicelulares?": ["*Filamentos chamados hifas, que formam uma rede chamada micélio", "Celulas únicas com núcleo", "Estrutura rígida de celulose", "Estruturas pequenas e redondas chamadas esporos"],
    "o que caracteriza as leveduras?": ["*São fungos unicelulares, que se reproduzem por brotamento ou gemulação", "São multicelulares, com filamentos visíveis a olho nu", "São fungos que se desenvolvem apenas em ambientes aquáticos", "São fungos que produzem esporos em grandes quantidades"],
    "qual é o papel dos fungos patogênicos?": ["*Causar doenças em humanos, animais e plantas", "Produzir alimentos como queijos e pães", "Gerar compostos nutritivos para outros organismos", "Reciclar matéria orgânica no solo"],
    "quais são os principais grupos de fungos#patogênicos para o ser humano?": ["*Leveduras, bolores e fungos dimórficos", "Bactérias, vírus e protozoários", "Bactérias, alga verde e líquens", "Artrópodes e nematoides"],
    "o que é a esporotricose?": ["*Uma micose subcutânea causada pelo fungo Sporothrix schenkii", "Uma infecção do sistema respiratório causada por Histoplasma capsulatum", "Uma infecção sistêmica causada por Cryptococcus neoformans", "Uma infecção cutânea causada por Candida albicans"],
    "como a esporotricose é adquirida?": ["*Geralmente por contato com material contaminado, como espinhos de plantas ou solo", "Por ingestão de alimentos contaminados com fungos", "Por inalação de esporos presentes no ar", "Por contato com água contaminada"],
    "qual é o agente causador da cromomicose?": ["*Fungos dematiáceos, como Fonsecaea pedrosoi e Cladophialophora carrionii", "Sporothrix schenkii", "Candida albicans", "Histoplasma capsulatum"],
    "como a cromomicose é transmitida?": ["*Através do contato com solo ou material contaminado", "Por via aérea, através da inalação de esporos", "Por ingestão de alimentos contaminados", "Por contato com água contaminada"],
    "quais são os sintomas mais comuns da esporotricose?": ["*Lesões cutâneas e linfáticas que podem evoluir para úlceras", "Febre alta, tosse e dificuldade respiratória", "Cefaleia e dor nas articulações", "Cefaleia e manchas vermelhas na pele"],
    "qual é o fungo responsável pela histoplasmose?": ["*Histoplasma capsulatum", "Cryptococcus neoformans", "Sporothrix schenkii", "Candida albicans"],
    "onde o Histoplasma capsulatum é comumente encontrado?": ["*Em solos ricos em excrementos de aves e morcegos", "Em águas contaminadas por fungos", "Em plantas e raízes", "Em alimentos contaminados"],
    "como a histoplasmose é adquirida?": ["*Por inalação de esporos do fungo presentes no ambiente", "Por contato direto com a pele infectada", "Por ingestão de alimentos contaminados", "Por contato com animais infectados"],
    "quais os sintomas da histoplasmose?": ["*Febre, tosse, dificuldade respiratória e linfadenopatia", "Dor abdominal e náuseas", "Lesões cutâneas e úlceras", "Dores musculares e fraqueza"],
    "qual é o agente causador da criptococose?": ["*Cryptococcus neoformans", "Histoplasma capsulatum", "Sporothrix schenkii", "Candida albicans"],
    "qual é a principal via de transmissão da criptococose?": ["*Por inalação de esporos do fungo, que são encontrados em fezes de aves, especialmente pombos", "Por ingestão de alimentos contaminados", "Por contato direto com lesões de pele", "Por contato com solo infectado"],
    "quais os sintomas da criptococose?": ["*Sintomas respiratórios, como tosse, dificuldade respiratória e febre, além de comprometimento neurológico", "Lesões de pele e dor abdominal", "Febre alta e dor nas articulações", "Tontura e perda de apetite"],
    "como é tratada a esporotricose?": ["*Com antifúngicos como itraconazol e terbinafina", "Com antibióticos como penicilina e amoxicilina", "Com antivirais como aciclovir", "Com medicamentos antiprotozoários"],
    "qual é o tratamento recomendado para a histoplasmose?": ["*Antifúngicos como itraconazol ou anfotericina B", "Antibióticos como tetraciclina", "Antivirais como os antirretrovirais", "Medicamentos antiparasitários"],
"qual é o agente causador da coccidioidomicose?": ["*Coccidioides immitis", "Aspergillus fumigatus", "Paracoccidioides brasiliensis", "Blastomyces dermatitidis"],
    "como a coccidioidomicose é adquirida?": ["*Por inalação de esporos presentes no solo, especialmente em regiões áridas", "Por ingestão de alimentos contaminados", "Por contato com animais infectados", "Por contato direto com lesões cutâneas"],
    "quais são os sintomas da coccidioidomicose?": ["*Febre, tosse, dor torácica e fadiga, com possibilidade de envolvimento pulmonar e disseminação sistêmica", "Cefaleia, náuseas e vômitos", "Dor abdominal e dificuldade para respirar", "Manchas vermelhas na pele e coceira"],
    "qual é o agente causador da paracoccidioidomicose?": ["*Paracoccidioides brasiliensis", "Coccidioides immitis", "Blastomyces dermatitidis", "Aspergillus fumigatus"],
    "quais são os sintomas da paracoccidioidomicose?": ["*Lesões pulmonares, linfadenopatia e lesões na mucosa oral e nasal", "Febre, calafrios e cefaleia", "Lesões cutâneas e falta de apetite", "Dores musculares e perda de peso"],
    "como a paracoccidioidomicose é adquirida?": ["*Por inalação de esporos presentes no solo e em matéria orgânica, comum em áreas rurais", "Por ingestão de água contaminada", "Por contato com animais infectados", "Por contato com objetos contaminados"],
    "qual é o agente causador da blastomicose?": ["*Blastomyces dermatitidis", "Aspergillus fumigatus", "Mucor", "Coccidioides immitis"],
    "como a blastomicose é adquirida?": ["*Por inalação de esporos do fungo presentes no solo, em áreas com vegetação", "Por ingestão de alimentos contaminados", "Por contato direto com lesões de pele infectadas", "Por contato com água contaminada"],
    "quais são os sintomas da blastomicose?": ["*Lesões pulmonares, febre, tosse e, em casos graves, disseminação para pele e ossos", "Cefaleia intensa, náuseas e vômitos", "Fadiga, febre baixa e perda de peso", "Manchas vermelhas na pele e coceira"],
    "qual é o agente causador da aspergilose?": ["*Aspergillus spp.", "Coccidioides immitis", "Mucor spp.", "Blastomyces dermatitidis"],
    "como a aspergilose é adquirida?": ["*Por inalação de esporos de Aspergillus presentes no ambiente", "Por ingestão de alimentos contaminados", "Por contato com lesões de pele infectadas", "Por contato com água contaminada"],
    "quais são os sintomas da aspergilose?": ["*Tosse, febre, falta de ar, e em casos graves, pode levar a infecção pulmonar e disseminação sistêmica", "Lesões cutâneas e dor abdominal", "Dores musculares e febre baixa", "Fadiga e perda de apetite"],
    "qual é o agente causador da mucormicose?": ["*Mucor spp.", "Coccidioides immitis", "Aspergillus fumigatus", "Blastomyces dermatitidis"],
    "como a mucormicose é adquirida?": ["*Por inalação de esporos de Mucor presentes no ambiente, especialmente em locais com matéria orgânica em decomposição", "Por ingestão de alimentos contaminados", "Por contato com água contaminada", "Por contato com lesões cutâneas infectadas"],
    "quais são os sintomas da mucormicose?": ["*Infecção pulmonar, sinusite, e em casos graves, necrose tecidual e disseminação para o cérebro", "Febre e calafrios", "Dor abdominal e dificuldade respiratória", "Cefaleia e náuseas"],
    "o que são as micoses oportunistas em pacientes#com SIDA?": ["*Infecções fúngicas que ocorrem com maior frequência em indivíduos imunocomprometidos, como os pacientes com HIV/SIDA", "Infecções causadas por bactérias resistentes a antibióticos", "Infecções virais em pacientes com sistema imunológico saudável", "Infecções causadas por parasitas em pessoas com doenças autoimunes"],
    "quais são os fungos oportunistas comuns em#pacientes com SIDA?": ["*Candida albicans, Aspergillus spp., Cryptococcus neoformans, Pneumocystis jirovecii", "Histoplasma capsulatum, Coccidioides immitis", "Sporothrix schenkii, Blastomyces dermatitidis", "Penicillium spp., Fusarium spp."],
    "qual é o fungo responsável pela pneumonia em#pacientes com SIDA?": ["*Pneumocystis jirovecii", "Cryptococcus neoformans", "Aspergillus fumigatus", "Mucor spp."],
"o que caracteriza os vírus?": ["*São agentes infecciosos acelulares que dependem de células hospedeiras para se replicar", "São organismos unicelulares que se replicam de forma independente", "São seres vivos autossuficientes que se alimentam de matéria orgânica", "São microrganismos que não necessitam de células para sua reprodução"],
    "quais são as duas partes principais de um vírus?": ["*Capsídeo e material genético", "Capsídeo e célula hospedeira", "Material genético e glicoproteínas", "Glicoproteínas e lipídios"],
    "como o material genético dos vírus pode ser?": ["*DNA ou RNA, podendo ser de cadeia simples ou dupla", "Somente RNA de cadeia dupla", "Somente DNA de cadeia simples", "Somente RNA de cadeia simples"],
    "os vírus podem ser classificados de acordo#com qual característica principal?": ["*O tipo de material genético (DNA ou RNA)", "O tamanho do capsídeo", "A forma da célula hospedeira", "A temperatura ambiente em que se proliferam"],
    "o que é um capsídeo viral?": ["*É a capa proteica que envolve o material genético do vírus", "É uma membrana lipídica que protege o vírus", "É a célula hospedeira infectada", "É a proteína que ajuda o vírus a se replicar na célula"],
    "os vírus são considerados seres vivos?": ["*Não, eles são considerados acelulares e dependem de células hospedeiras para replicação", "Sim, pois se replicam independentemente", "Sim, pois têm metabolismo próprio", "Não, pois são compostos apenas por proteínas"],
    "qual é a função do envelope viral?": ["*Proteger o material genético e facilitar a entrada do vírus na célula hospedeira", "Atuar como uma estrutura de suporte ao capsídeo", "Fornecer energia para a replicação do vírus", "Destruir a célula hospedeira para liberar novos vírus"],
    "como ocorre a replicação viral?": ["*O vírus se liga a uma célula hospedeira, entra nela e utiliza a maquinaria celular para produzir novos vírus", "O vírus se multiplica por divisão celular", "Os vírus se reproduzem fora das células hospedeiras", "Os vírus se replicam por meio de fissão binária"],
    "o que são as glicoproteínas virais?": ["*São proteínas localizadas na superfície do vírus, que ajudam na identificação e entrada nas células hospedeiras", "São proteínas que ajudam na replicação viral dentro da célula", "São proteínas que compõem o capsídeo viral", "São enzimas virais responsáveis pela digestão da célula hospedeira"],
    "quais são os principais tipos de vírus classificados#de acordo com seu material genético?": ["*Vírus de RNA e vírus de DNA", "Vírus de RNA apenas", "Vírus de RNA e vírus de proteínas", "Vírus de DNA e vírus de lipídios"],
"o que caracteriza o Herpesvírus?": ["*É um vírus de DNA com capacidade de latência no organismo, causando infecções recorrentes", "É um vírus de RNA que não pode causar infecções latentes", "É um vírus de RNA que só causa infecções cutâneas", "É um vírus de DNA que não causa latência"],
    "qual a principal característica do Poxvírus?": ["*É um vírus de DNA que causa doenças com lesões cutâneas e pode se replicar no citoplasma da célula hospedeira", "É um vírus de RNA que causa infecções respiratórias", "É um vírus de DNA que se replica no núcleo da célula hospedeira", "É um vírus de RNA que causa infecções no sistema nervoso"],
    "quais doenças são causadas pelo Herpesvírus?": ["*Herpes simples, varicela, mononucleose infecciosa, entre outras", "Gripe, hepatite e febre amarela", "Sarampo, rubéola e caxumba", "Pneumonia, meningite e dengue"],
    "quais doenças são causadas pelo Poxvírus?": ["*Varíola, molusco contagioso e cacema", "Hepatite, meningite e gripe", "Caxumba, sarampo e rubéola", "Herpes simples e herpes zoster"],
    "qual é a principal característica das infecções#por Herpesvírus?": ["*Capacidade de latência, com recorrência das infecções após reativação", "Infecções localizadas apenas na pele sem recorrência", "Infecções apenas no sistema nervoso central", "Capacidade de reinfetar o paciente de forma constante sem período de latência"],
    "o que é o ciclo lítico de replicação dos Herpesvírus?": ["*Fase em que o vírus se replica dentro da célula hospedeira, levando à morte da célula", "Fase em que o vírus entra em latência, sem replicação", "Fase em que o vírus fica no corpo sem infectar outras células", "Fase em que o vírus se replica sem afetar a célula hospedeira"],
    "qual a principal forma de transmissão do Herpesvírus?": ["*Contato direto com lesões ativas ou fluidos corporais de uma pessoa infectada", "Pelo ar, em gotículas respiratórias", "Por alimentos contaminados", "Pelo contato com objetos compartilhados, como roupas"],
    "qual a principal forma de transmissão do Poxvírus?": ["*Contato direto com lesões cutâneas ou secreções de uma pessoa infectada", "Através de gotículas respiratórias", "Por via fecal-oral", "Através de alimentos contaminados"],
    "como o Poxvírus se replica?": ["*No citoplasma da célula hospedeira, diferente de outros vírus de DNA", "No núcleo da célula hospedeira", "Em organelas celulares específicas, como os ribossomos", "Na superfície da célula hospedeira, sem entrar nela"],
    "o que caracteriza o ciclo de latência dos#Herpesvírus?": ["*O vírus permanece em um estado dormente em células nervosas, podendo se reativar em condições favoráveis", "O vírus se replica continuamente sem causar sintomas", "O vírus é eliminado do corpo após a infecção inicial", "O vírus causa sintomas permanentes na pessoa infectada"],
"o que caracteriza o Rhabdovirus?": ["*É um vírus de RNA com forma de bastão, responsável por doenças como a raiva", "É um vírus de DNA que causa doenças respiratórias", "É um vírus de RNA que causa infecções gastrointestinais", "É um vírus de DNA que afeta o sistema nervoso"],
    "qual doença é causadas pelo Rhabdovirus?": ["*Raiva", "Sarampo", "Hepatite", "Caxumba"],
    "como o Rhabdovirus se replica?": ["*No citoplasma da célula hospedeira", "No núcleo da célula hospedeira", "Nas mitocôndrias da célula", "No retículo endoplasmático da célula"],
    "qual é a principal forma de transmissão do#Rhabdovirus?": ["*Através da mordedura de animais infectados", "Por via aérea, em gotículas respiratórias", "Por ingestão de alimentos contaminados", "Por contato com fluidos corporais infectados"],
    "o que caracteriza o Papovírus?": ["*É um vírus de DNA, incluindo o Papilomavírus, responsável por causar verrugas e câncer", "É um vírus de RNA que afeta o sistema nervoso", "É um vírus de DNA que causa infecções respiratórias", "É um vírus de RNA que causa infecções gastrointestinais"],
    "qual é o principal tipo de infecção causado#pelo Papovírus?": ["*Verrugas e câncer, como câncer cervical", "Raiva e febre amarela", "Pneumonia e hepatite", "Hepatite e caxumba"],
    "qual a principal forma de transmissão do#Papovírus?": ["*Contato direto com pele ou mucosas infectadas", "Através de gotículas respiratórias", "Por ingestão de alimentos contaminados", "Por contato com superfícies contaminadas"],
    "qual é a principal característica do Parvovírus?": ["*É um vírus de DNA de cadeia simples, causando doenças como a eritema infeccioso", "É um vírus de RNA com formato esférico", "É um vírus de RNA que afeta o sistema nervoso", "É um vírus de DNA que afeta principalmente os pulmões"],
    "qual doença é associada ao Parvovírus?": ["*Eritema infeccioso, também conhecido como quinta doença", "Raiva", "Sarampo", "Varíola"],
    "como o Parvovírus se replica?": ["*No núcleo da célula hospedeira", "No citoplasma da célula hospedeira", "Em organelas celulares, como os ribossomos", "Na superfície da célula hospedeira"],
    "qual é a principal forma de transmissão do#Parvovírus?": ["*Por via respiratória, através de gotículas", "Através de mordeduras de animais infectados", "Por ingestão de alimentos contaminados", "Por contato com objetos contaminados"],

}

Questions_Patologia_Geral = {
  #Patologia Geral
"o que é patologia?": ["*É o estudo das doenças, suas causas, desenvolvimento e efeitos no organismo", "É o estudo da genética e suas mutações", "É o estudo do funcionamento dos sistemas do corpo", "É o estudo dos microrganismos e suas infecções"],
    "quais são as principais áreas de estudo#da patologia?": ["*Etiologia, patogênese, morfologia e manifestações clínicas", "Anatomia, histologia e embriologia", "Fisiologia, imunologia e genética", "Bioquímica, microbiologia e parasitologia"],
    "qual é a diferença entre patologia e fisiologia?": ["*Patologia estuda as doenças, enquanto fisiologia estuda os processos normais do corpo", "Patologia estuda os processos normais, enquanto fisiologia estuda as doenças", "Patologia e fisiologia são a mesma coisa", "Fisiologia estuda apenas o sistema nervoso, enquanto patologia estuda os órgãos"],
    "qual é a definição de etiologia na patologia?": ["*É o estudo das causas das doenças", "É o estudo dos efeitos das doenças no organismo", "É o estudo das manifestações clínicas das doenças", "É o estudo das células e tecidos afetados pela doença"],
    "o que é patogênese?": ["*É o processo pelo qual a doença se desenvolve e evolui no organismo", "É o estudo das células envolvidas na resposta imunológica", "É o estudo das causas das doenças", "É o processo de cura e regeneração celular"],
    "o que são manifestações clínicas?": ["*São os sinais e sintomas observados em uma pessoa com a doença", "São as causas das doenças", "São os fatores de risco para doenças", "São os tratamentos usados para curar as doenças"],
    "qual é a importância da patologia na medicina?": ["*Ajuda a compreender as causas das doenças e a desenvolver tratamentos eficazes", "Ajuda a melhorar a qualidade de vida das pessoas sem tratar doenças", "Ajuda a criar vacinas e medicamentos apenas para doenças infecciosas", "Ajuda a evitar o diagnóstico de doenças graves"],
    "o que caracteriza uma lesão patológica?": ["*Mudanças estruturais e funcionais nas células ou tecidos devido à doença", "Alterações no tamanho e formato dos órgãos", "Alterações apenas nas células musculares", "Mudanças temporárias e reversíveis no organismo"],
    "quais são os tipos de lesões patológicas?": ["*Lesões reversíveis e irreversíveis", "Lesões superficiais e profundas", "Lesões externas e internas", "Lesões benignas e malignas"],
    "como a patologia contribui para o diagnóstico#médico?": ["*Ela fornece informações sobre a natureza da doença e seus efeitos no organismo", "Ela ajuda a prever a eficácia dos tratamentos", "Ela define o tempo de duração da doença", "Ela apenas confirma a presença de um vírus no organismo"],
"o que caracteriza uma lesão celular?": ["*Alterações estruturais e funcionais na célula devido a estímulos agressivos", "Aumento do número de células saudáveis", "Redução do número de células anormais", "Alterações na função normal sem prejuízo estrutural"],
    "quais são os tipos de lesão celular?": ["*Lesões reversíveis e irreversíveis", "Lesões agudas e crônicas", "Lesões superficiais e profundas", "Lesões benignas e malignas"],
    "o que pode causar lesão celular?": ["*Fatores físicos, químicos, biológicos ou genéticos", "Exclusivamente a falta de oxigênio", "Exclusivamente a presença de radiação", "Apenas a infecção viral"],
    "o que é a morte celular?": ["*É a falha irreversível da célula em manter a homeostase", "É uma reação temporária da célula ao estresse", "É a alteração no número de células saudáveis", "É um processo reversível causado pela falta de nutrientes"],
    "quais são os tipos de morte celular?": ["*Necrose e apoptose", "Metaplasia e displasia", "Hiperplasia e atrofia", "Proliferação e diferenciação"],
    "qual é a diferença entre necrose e apoptose?": ["*Necrose é a morte celular não programada e resultante de lesões, enquanto apoptose é a morte celular programada e controlada", "Necrose é uma forma de apoptose", "Necrose ocorre apenas em células musculares, enquanto apoptose é comum em células nervosas", "Apoptose ocorre apenas em células cancerígenas, enquanto necrose é irreversível"],
    "o que é necrose?": ["*Morte celular não programada, geralmente associada a lesões agudas", "Morte celular programada que ocorre de forma controlada", "Aumento da divisão celular em resposta a estímulos", "Processo normal de diferenciação celular"],
    "quais são os tipos de necrose?": ["*Necrose coagulação, necrose liquefativa, necrose caseosa, necrose gordurosa e necrose fibrinóide", "Necrose celular, necrose epidérmica e necrose óssea", "Necrose crônica e necrose aguda", "Necrose benignas e malignas"],
    "o que é apoptose?": ["*É a morte celular programada e controlada, sem reação inflamatória", "É a morte celular que ocorre em resposta a infecções", "É a morte celular devido a falta de nutrientes", "É a morte celular causada por agentes físicos como calor ou radiação"],
    "qual é o papel da apoptose no organismo?": ["*Remover células danificadas ou desnecessárias sem causar inflamação", "Estimular a proliferação celular em tecidos saudáveis", "Aumentar a resposta inflamatória no corpo", "Reduzir o número de células do sistema imunológico"],
    "quais são as consequências da necrose para#o organismo?": ["*Pode causar inflamação e danos ao tecido circundante", "Promove a regeneração celular em áreas afetadas", "Acelera o processo de cura sem efeitos adversos", "Não causa danos aos tecidos, mas pode afetar a função celular"],
"o que caracteriza a lesão celular irreversível?": ["*A falha irreversível na homeostase celular, levando à morte celular", "Alterações temporárias sem comprometimento da função celular", "Recuperação total da célula após cessação do estímulo", "Aumento da função celular sem alteração estrutural"],
    "quais são os principais fatores que causam#a lesão celular irreversível?": ["*Falta de oxigênio, lesões químicas, radiação e agentes infecciosos", "Mudanças na pressão arterial", "Exposição a temperaturas baixas sem interrupção do fluxo sanguíneo", "Estímulos que não afetam a membrana celular"],
    "qual é o primeiro evento celular observado#em lesão irreversível?": ["*Danos nas membranas celulares, incluindo a membrana plasmática", "Alterações no citoplasma sem comprometimento da membrana", "Alteração no número de mitocôndrias", "Aumento no volume celular sem perda de função"],
    "o que ocorre com a mitocôndria durante a#lesão celular irreversível?": ["*A disfunção mitocondrial com perda de ATP e liberação de enzimas pró-apoptóticas", "Aumento da produção de ATP para recuperar a célula", "A mitocôndria se multiplica para compensar a lesão celular", "Não ocorre nenhuma alteração nas mitocôndrias durante a lesão irreversível"],
    "o que caracteriza a necrose celular?": ["*É a morte celular não programada, resultante de lesão irreversível, geralmente com inflamação", "É a morte celular programada que ocorre de forma controlada", "É uma resposta adaptativa à falta de nutrientes", "É um processo controlado de regeneração celular"],
    "quais as consequências da lesão irreversível#no tecido?": ["*Inflamação e danos estruturais no tecido adjacente", "Regeneração e recuperação do tecido danificado", "Aumento da funcionalidade no tecido afetado", "Nenhum efeito nas células circundantes"],
    "como a perda de ATP contribui para a lesão#celular irreversível?": ["*Prejudica a função das bombas iônicas, levando à despolarização celular", "Aumenta a produção de proteínas para a regeneração celular", "Melhora a função da membrana celular e evita danos", "Não tem efeito sobre a função celular"],
    "quais são os principais sinais morfológicos#da lesão celular irreversível?": ["*Inchaço celular, fragmentação de organelas, ruptura de membranas e liberação de enzimas intracelulares", "Aumento da atividade metabólica, com redução do volume celular", "Alteração na forma das mitocôndrias sem outras modificações", "Proliferação celular e aumento do número de mitocôndrias"],
    "o que é a necrose coagulação?": ["*É um tipo de necrose caracterizado pela preservação da arquitetura tecidual com perda das funções celulares", "É a necrose causada por infecções bacterianas", "É a necrose onde há um aumento da atividade mitocondrial", "É uma forma de morte celular programada que ocorre de maneira controlada"],
    "o que ocorre com a célula quando há lesão#irreversível na membrana plasmática?": ["*A célula perde a capacidade de controlar o transporte de íons, levando à morte celular", "A célula pode compensar o dano e continuar sua função normal", "A célula começa a proliferar mais rapidamente", "A célula ativa processos de reparo que previnem a morte celular"],
"o que caracteriza a lesão celular reversível?": ["*Alterações celulares que são temporárias e podem ser revertidas com a remoção do estímulo", "Danos irreversíveis às membranas celulares e organelas", "Morte celular imediata sem possibilidade de recuperação", "Alteração permanente no DNA celular"],
    "quais são os principais sinais de lesão#celular reversível?": ["*Inchaço celular, alteração na função das mitocôndrias e dilatação do retículo endoplasmático", "Perda total da função celular", "Danos graves nas membranas celulares", "Formação de necrose no tecido afetado"],
    "como a célula responde à falta de oxigênio#durante a lesão reversível?": ["*A célula reduz sua atividade metabólica e tenta restaurar o equilíbrio de energia", "A célula começa a morrer sem possibilidade de recuperação", "A célula ativa a necrose imediatamente", "A célula aumenta a produção de ATP para combater a falta de oxigênio"],
    "qual é o papel das mitocôndrias na lesão#celular reversível?": ["*As mitocôndrias podem ser danificadas temporariamente, mas ainda mantêm a produção de ATP", "As mitocôndrias se multiplicam para compensar a falta de energia", "As mitocôndrias entram em colapso e não conseguem gerar ATP", "As mitocôndrias não são afetadas em lesões celulares reversíveis"],
    "quais mudanças na membrana celular ocorrem#em lesão reversível?": ["*A membrana plasmática pode se dilatar ou ter um aumento da permeabilidade, mas sem ruptura", "A membrana plasmática é completamente destruída", "A membrana plasmática fica rígida e não permite mais trocas", "A membrana plasmática se fragmenta, levando à morte celular"],
    "quais são as causas mais comuns de lesão#celular reversível?": ["*Estresse físico ou químico, falta de oxigênio, toxinas e infecções leves", "Doenças genéticas que afetam permanentemente a função celular", "Infecções virais que causam morte celular imediata", "Mutação genética irreversível que afeta a estrutura celular"],
    "o que ocorre com o retículo endoplasmático#durante a lesão celular reversível?": ["*O retículo endoplasmático pode se dilatar devido ao acúmulo de proteínas não processadas, mas sem danos permanentes", "O retículo endoplasmático se rompe, causando a morte celular", "O retículo endoplasmático se multiplica para tentar compensar o dano", "O retículo endoplasmático não sofre alterações durante a lesão reversível"],
    "quais células são mais suscetíveis a#lesões reversíveis?": ["*Células com alta taxa de atividade metabólica, como hepatócitos e células musculares", "Células da pele que possuem baixa taxa de atividade metabólica", "Células nervosas que não possuem atividade metabólica", "Células com pouca capacidade de regeneração"],
    "o que acontece com a célula após a remoção#do estímulo lesivo?": ["*A célula pode retornar ao seu estado funcional normal se o dano não for grave", "A célula começa a morrer imediatamente", "A célula não sofre alteração e continua funcionando normalmente", "A célula se fragmenta e não pode mais se recuperar"],
    "como o aumento da permeabilidade celular afeta#a lesão reversível?": ["*A célula perde íons e água, levando a inchaço, mas sem destruição completa", "A célula se torna impermeável a substâncias essenciais, resultando em morte imediata", "A célula se torna totalmente impermeável, o que impede a troca de nutrientes", "A permeabilidade não é afetada durante a lesão reversível"],
"o que é inflamação?": ["*Resposta do tecido a lesões, infecções ou irritações, com sinais como vermelhidão, calor, dor e inchaço", "Processo de regeneração celular sem alteração no tecido", "Redução do fluxo sanguíneo nas áreas lesadas", "Resposta imediata que leva à morte celular"],
    "quais são os principais sinais da inflamação?": ["*Vermelhidão, calor, dor, inchaço e perda de função", "Aumento da pressão arterial e aumento do fluxo linfático", "Diminuição da temperatura local e dor intensa", "Necrose celular e perda da função orgânica"],
    "qual é o papel dos leucócitos na inflamação?": ["*Fagocitose de microorganismos e detritos celulares, além da liberação de mediadores inflamatórios", "Produção de anticorpos para combater a infecção", "Reparo de tecidos danificados sem envolver a fagocitose", "Redução da resposta imune para evitar inflamações crônicas"],
    "qual é a função das prostaglandinas na inflamação?": ["*Mediadores químicos que causam dor, febre e vasodilatação", "Inibem a resposta inflamatória e aceleram o processo de cura", "Diminuição da permeabilidade vascular", "Aumentam a função das células imunes e estimulam a regeneração celular"],
    "como o aumento da permeabilidade vascular contribui#para a inflamação?": ["*Permite que as células imunes e proteínas plasmáticas cheguem ao local da lesão", "Impedem a entrada de células imunes no local da lesão", "Reduzem a produção de proteínas inflamatórias", "Causam necrose nos tecidos próximos ao local da inflamação"],
    "qual é o principal tipo de célula envolvida na fase#inicial da inflamação aguda?": ["*Neutrófilos", "Linfócitos", "Macrófagos", "Eosinófilos"],
    "qual é a diferença entre inflamação aguda e crônica?": ["*A inflamação aguda é de curta duração e geralmente resolve-se após a remoção do agente causador, enquanto a crônica persiste por longos períodos e pode levar a danos nos tecidos", "A inflamação aguda dura meses, enquanto a crônica é uma resposta rápida", "Inflamação crônica é sempre mais intensa e dolorosa que a aguda", "A inflamação aguda nunca resulta em cicatrização do tecido"],
    "como a reparação tecidual ocorre após a inflamação?": ["*Por meio da regeneração celular ou da formação de tecido cicatricial (fibrose)", "Apenas por regeneração celular, sem formação de cicatrizes", "Por necrose celular e posterior remoção do tecido danificado", "Através da formação de novo epitélio sem qualquer alteração no tecido original"],
    "qual célula desempenha um papel importante na#reparação tecidual?": ["*Fibroblastos", "Leucócitos", "Eritrócitos", "Neurônios"],
    "qual é o papel do tecido de granulação no processo#de reparação?": ["*É formado durante a reparação, contendo vasos sanguíneos, fibroblastos e células inflamatórias, facilitando a cicatrização", "Preenche os espaços sem função nos tecidos lesionados", "Inibe a formação de cicatrizes e acelera a morte celular", "Reduz a inflamação e impede a regeneração tecidual"],
    "o que é uma cicatriz?": ["*Tecido de colágeno formado após a cura de uma lesão, substituindo o tecido original danificado", "Uma camada de tecido epitelial que restaura a pele danificada", "Tecido com alta concentração de células inflamatórias", "Novo tecido ósseo que substitui os tecidos danificados"],
"o que são distúrbios da imunidade?": ["*Condições em que o sistema imunológico responde de forma inadequada ou exagerada, levando a doenças autoimunes, alérgicas ou imunodeficiência", "Doenças causadas pela falta de nutrientes no organismo", "Respostas do sistema imunológico que protegem contra agentes patogênicos", "Disfunções do sistema nervoso que afetam a resposta imune"],
    "qual é a principal característica de uma#doença autoimune?": ["*O sistema imunológico ataca células do próprio organismo, reconhecendo-as como estranhas", "A falta de anticorpos no corpo para combater infecções", "O sistema imunológico é incapaz de reconhecer agentes patogênicos", "O sistema imunológico é incapaz de responder a estímulos externos"],
    "o que caracteriza uma reação alérgica?": ["*Uma resposta exagerada do sistema imunológico a substâncias geralmente inofensivas, como pólen ou poeira", "Uma infecção viral que afeta o sistema imunológico", "A falta de resposta do sistema imunológico a microorganismos patogênicos", "A produção de anticorpos contra células do próprio corpo"],
    "o que é imunodeficiência?": ["*Uma condição em que o sistema imunológico é incapaz de responder adequadamente a infecções ou outras ameaças", "Uma resposta imune exagerada a uma infecção", "A produção de anticorpos excessivos contra agentes patogênicos", "A resistência do corpo a doenças autoimunes"],
    "qual é a diferença entre imunodeficiência#primária e secundária?": ["*A primária é causada por defeitos genéticos no sistema imunológico, enquanto a secundária é resultado de infecções ou outros fatores externos", "A primária é mais comum em adultos, enquanto a secundária ocorre apenas em crianças", "A imunodeficiência primária é reversível, enquanto a secundária não é", "Ambas são causadas pela exposição a toxinas ambientais"],
    "qual é o papel dos anticorpos nas doenças#autoimunes?": ["*Eles podem atacar os próprios tecidos do corpo, resultando em inflamação e dano", "Eles ajudam a destruir microorganismos patogênicos", "Eles agem como imunossupressores, reduzindo a inflamação", "Eles impedem a ativação das células T, prevenindo danos aos tecidos"],
    "qual é o principal fator de risco para o#desenvolvimento de doenças autoimunes?": ["*Predisposição genética, embora fatores ambientais também desempenhem um papel", "Idade avançada", "Uso prolongado de antibióticos", "Dieta pobre em proteínas"],
    "qual condição está associada à imunodeficiência#primária?": ["*Síndrome de imunodeficiência combinada grave (SCID)", "Infecção pelo HIV", "Doenças autoimunes", "Reações alérgicas graves"],
    "qual é o papel da hipersensibilidade tipo I#nas reações alérgicas?": ["*Causar uma resposta exagerada do sistema imunológico a um alérgeno, levando à liberação de histamina e outros mediadores inflamatórios", "Aumentar a produção de anticorpos IgG para combater patógenos", "Destruir células infectadas por vírus", "Imunossupressão durante uma infecção bacteriana"],
    "como o HIV afeta o sistema imunológico?": ["*O HIV destrói as células T CD4+, enfraquecendo a resposta imunológica", "Ele ativa as células B para produzir anticorpos", "Ele estimula a produção de linfócitos T", "Ele causa uma resposta exagerada do sistema imunológico contra os tecidos do corpo"],
"quais são os tipos de imunodeficiência?": ["*Primária (genética) e secundária (adquirida)", "Apenas primária", "Apenas secundária", "Inata e adquirida"],
    "qual é a principal causa da imunodeficiência#secundária?": ["*Infecção pelo HIV, que destrói as células T CD4+", "Defeito genético nas células T", "Produção excessiva de anticorpos", "Exposição a radiação solar"],
    "qual é o exemplo de uma imunodeficiência primária?": ["*Síndrome de imunodeficiência combinada grave (SCID)", "Lúpus eritematoso sistêmico", "Asma", "Infecção por hepatite B"],
    "quais são os sintomas típicos da imunodeficiência?": ["*Infecções recorrentes e graves, especialmente por microrganismos oportunistas", "Dor muscular e febre", "Tosse seca e cansaço", "Inchaço e vermelhidão nas articulações"],
    "como a imunodeficiência primária é tratada?": ["*Com tratamentos para reforçar a função imunológica, como transplante de células-tronco ou terapia gênica", "Com medicamentos antibióticos de largo espectro", "Com vacina contra infecções comuns", "Com medicamentos antivirais específicos"],
    "qual é o principal objetivo do tratamento de#imunodeficiência secundária?": ["*Tratar a causa subjacente, como infecções ou câncer", "Estabilizar a resposta imunológica com corticosteroides", "Reduzir a produção de anticorpos", "Aumentar a inflamação para combater infecções"],
    "como a imunodeficiência relacionada ao HIV pode#ser controlada?": ["*Com terapias antirretrovirais (TAR) que controlam a replicação do HIV", "Com antibióticos de largo espectro", "Com vacina contra o HIV", "Com tratamentos hormonais"],
    "qual é o papel das células T CD4+ no sistema#imunológico?": ["*Elas ajudam a coordenar a resposta imunológica, ativando outras células imunes", "Elas produzem anticorpos", "Elas atacam diretamente células infectadas", "Elas inibem a inflamação"],
    "quais complicações podem surgir em uma pessoa#com imunodeficiência?": ["*Infecções graves e cânceres devido à falta de uma resposta imunológica eficaz", "Febre e dor muscular intensos", "Aumento na produção de linfócitos B", "Hipotensão e cansaço crônico"],
"o que é uma reação de autoinmunidade?": ["*Uma resposta imunológica em que o sistema imunológico ataca células e tecidos do próprio corpo", "Uma resposta imunológica excessiva a um agente infeccioso", "Uma falha na produção de anticorpos contra microrganismos", "Uma reação alérgica grave a substâncias externas"],
    "qual é a principal característica das doenças#autoimunes?": ["*O sistema imunológico ataca tecidos normais do corpo", "O sistema imunológico é excessivamente inibido", "Há uma produção inadequada de células T", "O sistema imunológico é incapaz de distinguir entre células do corpo e células estranhas"],
    "qual é a causa mais comum da tiroidite#linfocítica?": ["*É frequentemente associada a doenças autoimunes como a doença de Hashimoto", "Infecção viral", "Radiação excessiva", "Uso prolongado de medicamentos antiinflamatórios"],
    "qual é o principal tipo de célula envolvida na#tiroidite linfocítica?": ["*Linfócitos T", "Células B", "Macrófagos", "Células endoteliais"],
    "como a tiroidite linfocítica afeta a tireoide?": ["*Provoca inflamação da tireoide, podendo resultar em hipotireoidismo", "Causa aumento temporário dos níveis de hormônios tireoidianos", "Destrói as células da glândula adrenal", "Aumenta a produção de hormônios tiroideanos"],
    "qual é um sintoma comum da tiroidite linfocítica?": ["*Fadiga, ganho de peso e sensibilidade ao frio", "Febre alta e dor muscular", "Aumento da sudorese e perda de peso", "Aumento da pressão arterial"],
    "qual é o principal tratamento para a tiroidite#linfocítica?": ["*Substituição de hormônios tireoidianos em casos de hipotireoidismo", "Antibióticos para combater infecções", "Corticosteroides para reduzir a inflamação", "Antivirais para reduzir a atividade viral"],
    "qual é a relação entre tiroidite linfocítica e#outras doenças autoimunes?": ["*A tiroidite linfocítica pode ser uma manifestação de doenças autoimunes como a doença de Hashimoto", "A tiroidite linfocítica é uma forma de reação alérgica", "É uma doença infecciosa que afeta apenas a tireoide", "Não há relação com outras doenças autoimunes"],
    "o que é a doença de Hashimoto?": ["*É uma doença autoimune que causa hipotireoidismo devido à destruição da tireoide", "É uma doença viral que afeta a tireoide", "É uma doença bacteriana que causa hipertireoidismo", "É uma síndrome que resulta em aumento da produção de hormônios tireoidianos"],
    "quais exames podem ser usados para diagnosticar a#tiroidite linfocítica?": ["*Exames de função tireoidiana (TSH, T3, T4) e biópsia da tireoide", "Exames de sangue para detectar infecção bacteriana", "Exames de imagem para identificar infecções pulmonares", "Testes alérgicos para substâncias externas"],
"o que são distúrbios metabólicos?": ["*Condições que afetam o processo normal de conversão de alimentos em energia", "Doenças causadas por infecções virais no sistema digestivo", "Doenças autoimunes que atacam os músculos", "Distúrbios hormonais que afetam o sistema nervoso"],
    "qual é a causa mais comum de distúrbios#metabólicos?": ["*Desequilíbrios hormonais, como no diabetes e hipotireoidismo", "Infecções virais", "Deficiências nutricionais graves", "Doenças do sistema imunológico"],
    "o que caracteriza o diabetes mellitus tipo 1?": ["*A incapacidade do corpo em produzir insulina devido à destruição das células beta do pâncreas", "A resistência à insulina em células musculares e hepáticas", "A produção excessiva de insulina pela glândula adrenal", "A redução na absorção de glicose no intestino"],
    "qual é a principal característica do#diabetes tipo 2?": ["*Resistência à insulina e produção insuficiente de insulina", "Falta total de produção de insulina", "Excesso de produção de insulina", "Acúmulo de lipídios no pâncreas"],
    "o que é a síndrome metabólica?": ["*Um conjunto de condições que aumentam o risco de doenças cardíacas, derrame e diabetes tipo 2", "Uma doença infecciosa que afeta o metabolismo da glicose", "Uma doença genética rara que afeta o metabolismo lipídico", "Um tipo de câncer que afeta o metabolismo dos ossos"],
    "qual é o papel da insulina no metabolismo?": ["*Facilitar a absorção de glicose pelas células", "Aumentar a produção de glicose no fígado", "Inibir a lipólise e aumentar a síntese de proteínas", "Quebrar as proteínas para gerar energia"],
    "o que é a hipoglicemia?": ["*Quando os níveis de glicose no sangue caem abaixo do normal", "Quando os níveis de glicose no sangue aumentam acima do normal", "Uma condição em que há excesso de lipídios no sangue", "Quando o fígado não consegue armazenar glicose"],
    "o que é a fenilcetonúria?": ["*Um distúrbio metabólico genético que impede o metabolismo adequado do aminoácido fenilalanina", "Um distúrbio do fígado que afeta a produção de enzimas digestivas", "Uma doença autoimune que afeta os músculos", "Uma condição em que o corpo não consegue metabolizar carboidratos"],
    "o que caracteriza a doença de Gaucher?": ["*Acúmulo de lipídios nas células do corpo devido a uma deficiência enzimática", "Acúmulo de proteínas nas articulações", "Deficiência de vitaminas essenciais no metabolismo", "Produção excessiva de colesterol pelo fígado"],
    "quais são os sintomas comuns de distúrbios#metabólicos?": ["*Cansaço excessivo, ganho de peso, alterações no apetite, e dificuldade em controlar os níveis de glicose ou lipídios", "Febre alta, dores musculares e dificuldade respiratória", "Dor abdominal intensa, diarreia e vômitos", "Alterações no ritmo cardíaco, pressão arterial baixa e insônia"],
"o que são distúrbios metabólicos lipídicos?": ["*Condições que afetam o metabolismo de lipídios no corpo, resultando em desequilíbrios como dislipidemias", "Doenças que afetam a digestão de carboidratos", "Distúrbios causados por deficiências de vitaminas lipossolúveis", "Condições associadas ao aumento de proteínas no sangue"],
    "o que é a dislipidemia?": ["*Desequilíbrio nos níveis de lipídios no sangue, como colesterol e triglicerídeos", "Uma condição em que os lipídios são completamente ausentes no sangue", "Acúmulo de glicose no sangue", "Uma forma de câncer que afeta as células lipídicas"],
    "o que é o colesterol LDL?": ["*Conhecido como 'colesterol ruim', ele pode se acumular nas paredes dos vasos sanguíneos e aumentar o risco de doenças cardíacas", "Um tipo de colesterol benéfico que ajuda na digestão", "Uma forma de lipídio que não afeta o sistema cardiovascular", "Uma proteína que transporta vitaminas lipossolúveis no sangue"],
    "o que é o colesterol HDL?": ["*Conhecido como 'colesterol bom', ele ajuda a remover o excesso de colesterol das artérias", "Um tipo de colesterol que causa acúmulo nas paredes das artérias", "Uma forma de colesterol encontrado principalmente no fígado", "Uma proteína que transporta triglicerídeos para os músculos"],
    "o que é a hipercolesterolemia familiar?": ["*Uma condição genética que causa níveis elevados de colesterol LDL no sangue", "Uma doença autoimune que afeta a produção de lipídios", "Uma deficiência de enzimas que metabolizam lipídios", "Uma forma rara de obesidade genética"],
    "quais são os riscos da hiperlipidemia?": ["*Aumento do risco de doenças cardíacas, acidente vascular cerebral (AVC) e outros problemas vasculares", "Aumento da produção de glicose no corpo", "Excesso de perda de peso e baixa imunidade", "Problemas no metabolismo de carboidratos e proteínas"],
    "o que é a esteatose hepática (fígado gordo)?": ["*Acúmulo excessivo de gordura nas células do fígado, muitas vezes associado ao consumo excessivo de álcool ou obesidade", "Deficiência na produção de lipídios pelo fígado", "Uma doença autoimune que afeta o fígado", "Uma condição em que o fígado produz colesterol excessivo"],
    "o que são triglicerídeos?": ["*São a principal forma de gordura armazenada no corpo e fornecem energia", "Uma forma de lipídio encontrado exclusivamente nas células musculares", "Proteínas que transportam colesterol no sangue", "Vitaminas lipossolúveis armazenadas no fígado"],
    "como a obesidade está relacionada aos distúrbios#metabólicos lipídicos?": ["*A obesidade pode levar a desequilíbrios nos níveis de lipídios no sangue, aumentando o risco de doenças cardiovasculares", "A obesidade reduz os níveis de lipídios no sangue", "A obesidade está associada a uma diminuição no colesterol HDL", "A obesidade é uma consequência dos distúrbios lipídicos"],
    "qual é a relação entre os lipídios e as#doenças cardíacas?": ["*O acúmulo de lipídios, especialmente o colesterol LDL, nas artérias pode levar a aterosclerose e aumentar o risco de infarto e AVC", "Os lipídios ajudam a prevenir doenças cardíacas ao aumentar o colesterol HDL", "Os lipídios são usados para controlar a pressão arterial", "O excesso de lipídios não tem impacto no risco cardiovascular"],
"o que são transtornos circulatórios?": ["*Condições que afetam o fluxo sanguíneo normal no corpo, resultando em problemas como hipertensão, insuficiência venosa ou arterial", "Doenças que afetam os músculos esqueléticos", "Condições que afetam a digestão dos alimentos", "Distúrbios hormonais que afetam a produção de sangue"],
    "o que é a hipertensão?": ["*Aumento da pressão arterial que pode danificar vasos sanguíneos e órgãos ao longo do tempo", "Redução da pressão arterial que afeta a circulação sanguínea", "Uma condição em que a pressão sanguínea é normal mas a frequência cardíaca é elevada", "Uma doença genética que afeta os níveis de colesterol"],
    "quais são as causas da insuficiência venosa?": ["*Falta de eficiência nas válvulas das veias, dificultando o retorno do sangue ao coração", "Aumento do fluxo sanguíneo nas artérias", "Diminuição da produção de sangue no corpo", "Excesso de plaquetas no sangue"],
    "o que é a trombose venosa profunda (TVP)?": ["*Formação de um coágulo sanguíneo nas veias profundas, geralmente nas pernas, que pode se mover para os pulmões e causar embolia pulmonar", "Aumento do número de glóbulos vermelhos", "Uma condição em que os vasos sanguíneos se dilatam excessivamente", "Acúmulo de gordura nas artérias"],
    "quais são os sintomas de um acidente vascular#cerebral (AVC)?": ["*Fraqueza repentina em um lado do corpo, dificuldade para falar e perda de visão ou coordenação", "Aumento da pressão arterial e dificuldade respiratória", "Dores de cabeça intensas e febre alta", "Tontura e náuseas"],
    "o que é a aterosclerose?": ["*Acúmulo de placas de gordura nas artérias, que pode reduzir o fluxo sanguíneo e aumentar o risco de infarto ou AVC", "Uma condição em que os vasos sanguíneos se dilatam excessivamente", "Deficiência na produção de colesterol no fígado", "Aumento da formação de plaquetas no sangue"],
    "qual é a principal complicação da hipertensão#não tratada?": ["*Dano aos órgãos, como o coração, cérebro e rins, aumentando o risco de infarto, AVC e insuficiência renal", "Excesso de colesterol nas artérias", "Formação de coágulos sanguíneos nas veias", "Aumento da produção de glóbulos vermelhos"],
    "o que é a insuficiência cardíaca?": ["*Uma condição em que o coração não consegue bombear sangue de forma eficaz, resultando em acúmulo de fluido nos pulmões e outras partes do corpo", "Aumento do número de batimentos cardíacos sem consequências", "Aumento da pressão nas veias do pescoço", "Obstrução das artérias coronárias"],
    "o que são os aneurismas?": ["*Dilatação anormal de uma artéria devido a fraqueza na parede do vaso, podendo levar a ruptura e sangramentos graves", "Formação de coágulos nas artérias", "Obstrução das válvulas cardíacas", "Aumento da viscosidade do sangue"],
    "como a diabetes pode afetar a circulação sanguínea?": ["*A diabetes mal controlada pode danificar os vasos sanguíneos, aumentando o risco de aterosclerose, infarto e AVC", "A diabetes melhora o fluxo sanguíneo ao reduzir a viscosidade do sangue", "A diabetes não tem efeito sobre o sistema circulatório", "A diabetes ajuda na dilatação dos vasos sanguíneos"],
"o que são transtornos neoplásicos?": ["*Condições relacionadas ao crescimento anormal de células, levando ao desenvolvimento de tumores", "Doenças que afetam os músculos esqueléticos", "Distúrbios genéticos que alteram o DNA sem formação de tumores", "Problemas no sistema circulatório que causam dor muscular"],
    "o que é um tumor benigno?": ["*Um crescimento celular não cancerígeno que geralmente não se espalha para outras partes do corpo", "Um tumor que se espalha rapidamente para outros órgãos", "Células cancerígenas que se formam em um único órgão", "Uma infecção causada por vírus que cresce rapidamente"],
    "qual é a principal diferença entre um tumor#benigno e maligno?": ["*O tumor maligno é cancerígeno e tem a capacidade de se espalhar (metástase), enquanto o benigno não se espalha", "O tumor benigno é maior do que o maligno", "Tumores malignos são mais fáceis de tratar", "Tumores benignos podem causar metástase"],
    "o que é metástase?": ["*O processo pelo qual células cancerígenas se espalham de um local primário para outras partes do corpo", "A formação de tumores benignos", "Uma condição que impede a regeneração celular", "Aumento da quantidade de glóbulos vermelhos no sangue"],
    "quais são os tipos principais de câncer?": ["*Carcinomas, sarcomas, linfomas e leucemias", "Infecções virais e bacterianas", "Transtornos musculares e ósseos", "Doenças do sistema nervoso central"],
    "o que é carcinoma?": ["*Um câncer que se origina em células epiteliais, como pele, pulmões, fígado e outros órgãos", "Um câncer originado em células musculares", "Câncer que afeta as células do sangue", "Câncer que afeta os tecidos nervosos"],
    "qual é a principal causa do câncer?": ["*Mutação no DNA das células, que pode ser desencadeada por fatores ambientais, como tabagismo, radiação e produtos químicos", "Infecção por vírus", "Falta de nutrientes", "Falta de sono"],
    "o que são linfomas?": ["*Cânceres que se originam nas células do sistema linfático", "Tumores benignos do sistema nervoso", "Cânceres que afetam os ossos", "Tumores no fígado causados por álcool"],
    "o que é leucemia?": ["*Câncer dos tecidos formadores de sangue, como a medula óssea, que resulta na produção anormal de células sanguíneas", "Tumor que se desenvolve no sistema linfático", "Câncer da pele devido à exposição solar", "Um tipo de tumor muscular"],
    "quais são os fatores de risco para o câncer?": ["*Exposição a substâncias cancerígenas, histórico familiar, dieta pobre, tabagismo, e exposição à radiação", "Prática de atividades físicas", "Dieta rica em vegetais", "Ingestão excessiva de água"]
}
#Checked so far here
Questions_Psicologia_I = {
#Psicologia I
"o que é psicologia?": ["*A ciência que estuda o comportamento humano e os processos mentais", "O estudo das emoções e sentimentos humanos e as adaptações ambientais", "A arte de tratar distúrbios mentais relacionados ao ID, EGO e SuperEGO", "O estudo do cérebro e suas funções biológicas"],
    "quais são as principais abordagens da psicologia?": ["*Psicologia comportamental, psicologia cognitiva, psicologia humanista, psicologia psicodinâmica", "Psicologia educacional, psicologia organizacional, psicologia experimental", "Psicologia clínica, psicologia social, psicologia evolutiva", "Psicologia experimental, psicologia social, psicologia de grupo"],
    "qual é o foco da psicologia comportamental?": ["*Estudar o comportamento observável e como ele é influenciado pelo ambiente", "Estudar os processos internos de pensamento bem como a introspecção", "Analisar a relação entre comportamento e emoções que definem a personalidade", "Focar em mudanças cerebrais devido a transtornos mentais"],
    "o que a psicologia cognitiva estuda?": ["*Os processos mentais, como percepção, memória, pensamento e resolução de problemas", "A interação entre indivíduo e sociedade como o mesmo estabele as relações", "A relação entre comportamento e genética para fins diagnosticos de doenças mentais", "A influência do ambiente nas ações humanas"],
    "o que caracteriza a psicologia humanista?": ["*Foco no potencial humano, autocrescimento e autorrealização", "Análise do comportamento social, humanista e religioso que o homem experiencia", "Estudo das respostas fisiológicas ao estresse", "Estudo do comportamento em resposta ao treinamento"],
    "qual é o principal conceito da psicologia#psicodinâmica?": ["*O inconsciente influencia profundamente o comportamento humano", "Os indivíduos são moldados principalmente pela cultura e pelo ambiente social", "A mente humana pode ser compreendida observando o comportamento", "A interação entre emoção e pensamento é a chave para a saúde mental"],
    "quem é considerado o pai da psicanálise?": ["*Sigmund Freud", "Carl Rogers", "Jean Piaget", "B.F. Skinner"],
    "o que é o behaviorismo radical?": ["*Uma teoria que enfatiza a observação do comportamento externo", "Uma teoria que estuda as emoções humanas", "Uma abordagem que analisa a relação entre o ambiente e os instintos humanos", "Uma teoria focada na psicoterapia e intervenções emocionais"],
    "qual é a teoria de Piaget sobre o desenvolvimento#cognitivo?": ["*As crianças passam por estágios específicos de desenvolvimento cognitivo", "A cognição é influenciada apenas pela genética", "O desenvolvimento cognitivo é o mesmo para todos os indivíduos", "O desenvolvimento cognitivo depende apenas do ensino formal"],
    "o que é a psicologia social?": ["*Estudo de como o comportamento, pensamento e sentimentos das pessoas", "Análise do comportamento individual em ambientes controlados", "Foco no diagnóstico e tratamento de transtornos mentais", "Estudo da relação entre doenças psicológicas e ambiente biológico"],
                       "quais são as principais etapas do desenvolvimento humano#segundo Erik Erikson?": [
                           "*Infância, adolescência, juventude, vida adulta, velhice",
                           "Nascimento, infância, adolescência, idade adulta, morte",
                           "Fase sensório-motora, pré-operacional, operatório concreto, operatório formal",
                           "Fase oral, anal, fálica, latência, genital"],
                       "o que caracteriza a fase sensório-motora no#desenvolvimento infantil?": [
                           "*O desenvolvimento das capacidades sensoriais e motoras",
                           "A capacidade de realizar operações mentais lógicas",
                           "O desenvolvimento da linguagem e dos símbolos", "A formação da identidade de gênero"],
                       "o que ocorre na fase pré-operacional do desenvolvimento#infantil, segundo Piaget?": [
                           "*As crianças começam a usar símbolos e palavras, mas não operações lógicas",
                           "A criança desenvolve a capacidade de entender o conceito de conservação",
                           "A criança aprende a realizar operações matemáticas e raciocinio abstracto",
                           "A criança começa a interagir com o ambiente de forma abstrata"],
                       "o que é o conceito de conservação na teoria#de Piaget?": [
                           "*A compreensão de que a quantidade de algo permanece constante",
                           "A capacidade de raciocinar de forma lógica sobre situações concretas",
                           "A habilidade de classificar objetos e organizar em grupos",
                           "O desenvolvimento da teoria da mente"],
                       "quais são os estágios do desenvolvimento moral,#segundo Lawrence Kohlberg?": [
                           "*Estágio pré-convencional, convencional, pós-convencional",
                           "Estágio de socialização, introjeção, internalização",
                           "Estágio de comportamento egocêntrico, de egocentrismo social, de colaboração",
                           "Estágio de autodeterminação, manipulação, autoregulação"],
                       "o que acontece na adolescência de acordo com a#teoria do desenvolvimento de Erikson?": [
                           "*A formação da identidade e a busca por um sentido de quem se é",
                           "A transição da dependência para a independência financeira",
                           "A transição da infância para a vida adulta em termos de habilidades cognitivas",
                           "A capacidade de formar relacionamentos íntimos"],
                       "como Jean Piaget descreve o desenvolvimento#cognitivo durante a infância?": [
                           "*Através de estágios fixos: sensório-motor, pré-operacional, operatório concreto e operatório formal",
                           "Com base na teoria do reforço e punição incentivando o medo",
                           "Por meio do desenvolvimento de impulsos e habilidades sociais",
                           "A partir da análise de interações com os pais e a sociedade"],
                       "o que é a teoria do apego de John Bowlby?": [
                           "*A criança forma vínculos emocionais primários com os cuidadores, o que influencia seu desenvolvimento emocional e social",
                           "A criança se desenvolve basicamente por meio da interação com outras crianças",
                           "O apego é um comportamento aprendido durante a fase de socialização",
                           "Os vínculos emocionais não têm impacto significativo no desenvolvimento humano"],
                       "quais são as principais características da#fase adulta, segundo Erikson?": [
                           "*Estabelecimento de intimidade, trabalho e sentido de contribuição",
                           "Formação de uma identidade consolidada para que assim possa estabelecer relações sociais de qualidade livre de violencia",
                           "Desenvolvimento de habilidades cognitivas complexas",
                           "Transição para a velhice com novos desafios emocionais e físicos"],
                       "o que é a teoria de Piaget sobre as operações#concretas?": [
                           "*As crianças podem realizar operações mentais lógicas em situações concretas, mas têm dificuldade com abstrações",
                           "As crianças desenvolvem a capacidade de pensar de forma simbólica e criativa",
                           "As crianças ainda não conseguem distinguir entre realidade e fantasia",
                           "As crianças começam a usar raciocínio abstrato e hipotético"],
                       "como a teoria de Vygotsky explica o desenvolvimento#cognitivo?": [
                           "*O desenvolvimento é influenciado pela interação social e pela cultura",
                           "O desenvolvimento ocorre independentemente das interações sociais",
                           "As habilidades cognitivas são adquiridas exclusivamente através de aprendizado individual que melhoram o\ncoeficiente de inteligência",
                           "O desenvolvimento é um processo biológico e isolado da sociedade"],
                       "o que é atenção seletiva?": [
                           "*Focar a atenção em um estímulo específico enquanto ignora outros",
                           "A habilidade de manter a atenção por períodos longos sem distrações",
                           "A capacidade de alternar entre diferentes tarefas",
                           "A habilidade de lembrar detalhes sem esforço consciente"],
                       "quais fatores podem influenciar a atenção?": [
                           "*Fatores internos (como motivação e interesse) e fatores externos (como estímulos ambientais)",
                           "Somente fatores externos, como sons ou luzes", "Apenas a concentração mental do indivíduo",
                           "Apenas fatores relacionados à carga de trabalho cognitiva"],
                       "qual é a diferença entre atenção dividida e atenção#concentrada?": [
                           "*A atenção dividida envolve realizar mais de uma tarefa ao mesmo tempo, enquanto a concentrada foca em uma única tarefa",
                           "A atenção dividida é quando a mente se distrai, e a concentrada é quando a mente fica em repouso",
                           "A atenção concentrada é mais eficiente do que a dividida em todas as situações",
                           "A atenção dividida é mais focada e precisa do que a concentrada"],
                       "o que é o modelo de atenção de Broadbent?": [
                           "*É um modelo de atenção seletiva, no qual os estímulos são filtrados antes de serem processados em profundidade",
                           "É um modelo que defende que a atenção é uma capacidade ilimitada",
                           "É um modelo de atenção dividida onde o cérebro processa múltiplos estímulos ao mesmo tempo",
                           "É um modelo de atenção que descreve como o cérebro armazena informações a longo prazo"],
                       "o que caracteriza a atenção sustentada?": [
                           "*Manter o foco em uma tarefa ou estímulo por um período prolongado",
                           "Alternar rapidamente entre diferentes tarefas sustentando-a a medida que vai se adaptando",
                           "Focar em múltiplos estímulos ao mesmo tempo",
                           "Focar na resolução de problemas complexos e abstratos"],
                       "o que é a teoria da capacidade atencional?": [
                           "*A teoria que sugere que a atenção é um recurso limitado que deve ser alocado entre várias tarefas",
                           "A teoria que defende que a atenção pode ser aumentada com a prática",
                           "A teoria que afirma que a atenção é ilimitada e sem limites",
                           "A teoria que defende que a atenção é a capacidade de perceber todos os estímulos ao mesmo tempo"],
                       "como a atenção seletiva é afetada por estímulos#emocionais?": [
                           "*Estímulos emocionais podem aumentar a atenção seletiva para situações que envolvem risco ou recompensa",
                           "Estímulos emocionais têm pouco efeito na atenção seletiva",
                           "A atenção seletiva é prejudicada por estímulos emocionais, tornando difícil focar em algo específico",
                           "A atenção seletiva é automaticamente concentrada em estímulos emocionais irrelevantes"],
                       "qual é o efeito do treinamento da atenção?": [
                           "*O treinamento pode melhorar a capacidade de focar em uma tarefa específica e de realizar\nmultitarefas",
                           "O treinamento reduz a capacidade de realizar tarefas de atenção dividida",
                           "O treinamento tem pouco efeito sobre a eficiência atencional",
                           "O treinamento da atenção só melhora a memória de curto prazo"],
                       "como a distração afeta a atenção?": [
                           "*A distração reduz a capacidade de manter o foco, tornando o processamento de informações menos\neficiente",
                           "A distração aumenta a capacidade de processamento de múltiplos estímulos",
                           "A distração não tem impacto na capacidade atencional",
                           "A distração é benéfica para melhorar a atenção seletiva"],
                       "qual é a relação entre atenção e memória de#trabalho?": [
                           "*A atenção é necessária para manter e manipular informações na memória de trabalho",
                           "A memória de trabalho ocorre independentemente da atenção",
                           "A atenção pode melhorar a memória de longo prazo, mas não afeta a memória de trabalho",
                           "A memória de trabalho pode ocorrer sem a necessidade de atenção"],
"o que é sensação?": ["*É o processo inicial de captação de estímulos sensoriais pelos órgãos sensoriais", "É o processo mental de interpretar informações sensoriais", "É a percepção de um estímulo no cérebro", "É o processo de recordação de estímulos anteriores"],
    "qual é o papel dos receptores sensoriais na#sensação?": ["*Eles são responsáveis por detectar estímulos ambientais e convertê-los em sinais elétricos", "Eles interpretam os sinais sensoriais enviados ao cérebro em forma\nde potencial de acção", "Eles armazenam as informações sensoriais para memória de longo prazo", "Eles transmitem apenas estímulos visuais para o cérebro"],
    "quais são os tipos de estímulos que os receptores#sensoriais podem detectar?": ["*Estímulos como luz, som, pressão, temperatura e substâncias químicas", "Apenas estímulos visuais e auditivos como música, barulho, vozes, etc...", "Somente estímulos táteis e térmicos", "Estímulos de cor e forma de objetos"],
    "como a adaptação sensorial ocorre?": ["*É a diminuição da resposta dos receptores sensoriais a\nestímulos constantes ao longo do tempo", "É a capacidade de detectar estímulos novos com mais eficiência", "É o aumento da resposta a estímulos fortes", "É a capacidade de interpretar estímulos em diferentes contextos"],
    "qual é a diferença entre sensação e percepção?": ["*A sensação é a captação de estímulos, enquanto a percepção é a\ninterpretação desses estímulos pelo cérebro", "A sensação e a percepção são processos idênticos", "A sensação ocorre apenas nos órgãos sensoriais, enquanto a\npercepção acontece no cérebro", "A percepção é o processo inicial de detectar estímulos, enquanto a sensação é a interpretação"],
    "qual é o sentido responsável pela percepção de#estímulos químicos, como sabor e olfato?": ["*O sentido do paladar e olfato", "O sentido da visão", "O sentido do tato", "O sentido da audição"],
    "o que é a transdução sensorial?": ["*É o processo em que os receptores sensoriais convertem\nestímulos físicos em sinais elétricos", "É o processo de interpretar os sinais elétricos no cérebro", "É o processo de adaptação a estímulos constantes", "É a percepção da intensidade de um estímulo"],
    "qual é o papel da via neural na sensação?": ["*Ela transmite os sinais elétricos dos receptores\nsensoriais para o cérebro, onde são interpretados", "Ela impede que estímulos sensoriais cheguem ao cérebro", "Ela armazena informações sensoriais para utilização futura", "Ela converte estímulos sensoriais em respostas motoras"],
    "o que é a limiar de percepção?": ["*É a quantidade mínima de estímulo necessária para ser\ndetectada por um receptor sensorial", "É a intensidade máxima de um estímulo que pode ser percebido", "É a capacidade de processar estímulos complexos", "É a percepção de estímulos não conscientes"],
    "como a sensação de dor é percebida pelo corpo?": ["*A sensação de dor é percebida quando os nociceptores detectam estímulos prejudiciais e enviam sinais ao cérebro", "A dor é percebida pela percepção de estímulos visuais e auditivos", "A dor é uma sensação exclusiva dos órgãos sensoriais táteis", "A dor é gerada pela adaptação sensorial ao estímulo"],
"o que são necessidades humanas?": ["*São estados de carência ou desejo que motivam comportamentos\npara serem atendidos", "São desejos sem relação com a motivação comportamental", "São sentimentos que não influenciam o comportamento humano", "São objetivos que não têm impacto na motivação individual"],
    "qual teoria psicológica é mais associada à#hierarquia de necessidades humanas?": ["*Teoria de Maslow", "Teoria do condicionamento operante", "Teoria do desenvolvimento psicossocial de Erikson", "Teoria do comportamento social de Skinner"],
    "quais são os níveis da hierarquia de Maslow,#da base para o topo?": ["*Necessidades fisiológicas, segurança, sociais, estima e autorrealização", "Necessidades de estima, sociais, segurança, fisiológicas e autorrealização", "Segurança, autorrealização, necessidades fisiológicas, estima e sociais", "Autorrealização, segurança, necessidades fisiológicas, estima e sociais"],
    "quais são as necessidades fisiológicas na teoria#de Maslow?": ["*Comer, beber, dormir, manter a temperatura corporal", "Relacionamentos íntimos, afeto, amizade e amor", "Segurança financeira e saúde", "Reconhecimento, respeito, honra e autoaceitação"],
    "o que são necessidades de estima, segundo Maslow?": ["*Necessidades relacionadas ao reconhecimento social e autovalorização", "Necessidades de alimentação, repouso e ganho de energia", "Necessidades de segurança física", "Necessidades de afeto e relacionamentos íntimos"],
    "qual é a principal característica das necessidades#sociais de Maslow?": ["*Relacionam-se com o desejo de pertencer a um grupo\ne ter relacionamentos afetivos", "Relacionam-se com a autoaceitação e autoestima", "Relacionam-se com o desejo de poder e domínio", "Relacionam-se com a satisfação das necessidades biológicas"],
    "como as necessidades de segurança são descritas#por Maslow?": ["*São necessidades de proteção contra perigos físicos e\npsicológicos, estabilidade e segurança financeira", "São necessidades relacionadas à busca de status social", "São necessidades de realização pessoal e autoexpressão", "São necessidades de afeto e relações íntimas"],
    "o que é autorrealização na teoria de Maslow?": ["*É a necessidade de alcançar o pleno potencial pessoal e se\ntornaro melhor que se pode ser", "É a necessidade de afeto e aceitação social", "É a necessidade de encontrar segurança no ambiente", "É a necessidade de consumir alimentos e descansar adequadamente"],
    "qual é a diferença entre necessidades básicas e#necessidades superiores em Maslow?": ["*As necessidades básicas (fisiológicas e de segurança) precisam ser\natendidas antes das superiores (sociais, estima e autorrealização)", "As necessidades superiores são mais urgentes que as básicas", "As necessidades superiores são mais fáceis de satisfazer", "As necessidades básicas e superiores são atendidas ao mesmo tempo"],
    "como a teoria de Maslow pode ser aplicada em#contextos educacionais?": ["*Focando em atender as necessidades básicas dos alunos antes de estimular\nseu desenvolvimento intelectual e criativo", "Focando apenas em necessidades de autorrealização", "Focando em reconhecer apenas as necessidades físicas dos alunos", "Focando em promover o ensino sem considerar as necessidades dos alunos"],
"o que é motivação em psicologia?": ["*É o processo que inicia, direciona e sustenta comportamentos", "É a capacidade de entender as emoções dos outros", "É a habilidade de controlar os impulsos", "É o estado de prazer em realizar uma tarefa"],
    "qual é a principal diferença entre motivação#intrínseca e extrínseca?": ["*Motivação intrínseca vem de dentro da pessoa, enquanto \n extrínseca vem de recompensas externas", "Motivação intrínseca está ligada a recompensas externas", "Motivação extrínseca não tem impacto no comportamento", "Motivação intrínseca é sempre mais fraca que a extrínseca"],
    "quais são os tipos de motivação identificados#na teoria de Deci e Ryan?": ["*Motivação intrínseca, motivação extrínseca e amotivação", "Motivação social e motivação psicológica", "Motivação afetiva e motivação cognitiva", "Motivação emocional e motivação física"],
    "qual é a teoria motivacional de Maslow?": ["*A teoria da hierarquia das necessidades", "A teoria do reforço mental para seguir em frente\nem situações dificeis", "A teoria do condicionamento operante", "A teoria da autodeterminação"],
    "qual é o papel das recompensas na motivação#extrínseca?": ["*As recompensas externas incentivam o comportamento, mas podem\ndiminuir a motivação intrínseca", "Elas sempre aumentam a motivação intrínseca", "Elas não têm efeito sobre o comportamento", "As recompensas são mais eficazes quando não são oferecidas de forma imediata"],
    "como a motivação intrínseca afeta o desempenho#de uma tarefa?": ["*Ela tende a melhorar o desempenho devido ao prazer e satisfação\nderivados da própria tarefa", "Ela diminui o desempenho, pois a pessoa não se importa com a tarefa", "Ela não tem impacto no desempenho", "Ela só afeta o desempenho quando recompensada externamente"],
    "o que a teoria da autodeterminação propõe sobre#a motivação?": ["*Que a motivação é mais forte quando as pessoas sentem que\ntêm controle sobre suas ações", "Que a motivação é sempre externa", "Que a motivação não está relacionada ao controle", "Que a motivação é apenas uma reação ao ambiente"],
    "o que é a motivação de realização, segundo#McClelland?": ["*É a motivação para alcançar o sucesso, enfrentar desafios e\nsuperar obstáculos", "É a motivação para se conectar com os outros", "É a motivação para evitar falhas", "É a motivação para obter recompensas externas"],
    "como o conceito de motivação de poder se#relaciona com o comportamento humano?": ["*É a motivação de controlar ou influenciar os outros", "É a motivação de alcançar o sucesso pessoal", "É a motivação de ajudar os outros sem recompensa", "É a motivação de evitar o confronto"],
    "qual é a relação entre motivação e emoções?": ["*A motivação pode ser influenciada pelas emoções, e as emoções\npodem ser motivadas por metas e desejos", "Emoções e motivação não têm relação", "As emoções sempre diminuem a motivação", "A motivação nunca afeta as emoções"],
"o que é personalidade em psicologia?": ["*É o conjunto de características psicológicas que definem o\ncomportamento de uma pessoa", "É a habilidade de controlar as emoções", "É o estado emocional de uma pessoa em um dado momento", "É a forma como as pessoas se relacionam com os outros em sociedade"],
    "qual teoria da personalidade é associada#a Sigmund Freud?": ["*Teoria psicanalítica", "Teoria humanista", "Teoria comportamental", "Teoria cognitiva"],
    "o que propôs Carl Jung sobre a personalidade?": ["*Que a personalidade é formada por arquétipos e inconsciente\ncoletivo", "Que a personalidade é completamente determinada pelos fatores ambientais", "Que a personalidade é apenas o reflexo das emoções", "Que a personalidade se desenvolve apenas na infância"],
    "qual é a principal característica da teoria#humanista de Carl Rogers sobre personalidade?": ["*A busca pela autoatualização e congruência entre o self real e\no self ideal", "O comportamento é moldado exclusivamente por reforços e punições", "A personalidade é predestinada e imutável", "A personalidade é dividida entre consciente e inconsciente"],
    "quais são os três sistemas principais da#personalidade de Freud?": ["*Id, Ego e Superego", "Cognitivo, afetivo e comportamental", "Inconsciente, subconsciente e consciente", "Real, ideal e social"],
    "qual é a teoria de traços da personalidade?": ["*Propõe que a personalidade pode ser descrita por um conjunto de\ntraços estáveis ao longo do tempo", "A personalidade é moldada exclusivamente por fatores ambientais", "A personalidade é baseada em padrões de comportamento situacionais", "A teoria de traços não acredita na estabilidade da personalidade"],
    "o que é a teoria de aprendizagem social de#Bandura sobre a personalidade?": ["*A personalidade é formada por interações entre os fatores\ncognitivos, comportamentais e ambientais", "A personalidade é determinada unicamente pela genética", "A personalidade se desenvolve apenas por meio da aprendizagem observacional", "A personalidade é fixa e não muda ao longo da vida"],
    "como os traços de personalidade podem ser#medidos?": ["*Por meio de inventários e testes psicológicos padronizados", "Observando o comportamento da pessoa sem qualquer avaliação formal", "Apenas pela interação direta com a pessoa", "Por meio de entrevistas não estruturadas"],
    "qual é o conceito de 'self' na teoria humanista#de Carl Rogers?": ["*É a percepção que a pessoa tem de si mesma, incluindo seu\nideal e sua realidade", "É a parte do ego que controla as ações impulsivas", "É o instinto primário que rege o comportamento", "É a personalidade como um todo, sem distinção de componentes"],
    "o que é a teoria dos cinco grandes fatores#da personalidade?": ["*É uma teoria que propõe que a personalidade pode ser descrita em\ncinco grandes dimensões", "É uma teoria que foca na divisão da personalidade entre consciente e\ninconsciente", "É uma teoria que afirma que a personalidade é determinada pelos fatores\nbiológicos e hormonais", "É uma teoria que sugere que a personalidade é fixa e não pode ser mudada"]
}

dict_for_copy = [Questions_General_Questions, Questions_Histologia_I, Questions_Histologia_II, Questions_Anatomia_II,
                 Questions_Anatomia_III, Questions_Bioquímica_II, Questions_Embriologia_I, Questions_Embriologia_II, Questions_Fisiologia_I,
                 Questions_Fisiologia_II, Questions_Genética_Médica, Questions_Introdução_à_Clínica, Questions_Microbiologia, Questions_Patologia_Geral, Questions_Psicologia_I,
                 Questions_Informática_Médica_II, Questions_Médicina_Comunitária_I, Questions_Médicina_Comunitária_II]

Questions_root_deep = {}

def load_questions_root_deep():
    temp_dict = {}
    for d in dict_for_copy:
        for k, v in d.items():
            temp_dict[k] = v

    return temp_dict

Questions_root_deep = load_questions_root_deep()
Questions_root = {}
Questions_root = load_60_question(Questions_root_deep, dificuldade)

# Loading Images

bg_image = ImageTk.PhotoImage(Image.open("Assets/Images/Aureus background.png").resize((1430, 750)))
end_template = ImageTk.PhotoImage(Image.open("Assets/Images/End_template.png").resize((1440, 750)))
classic_bg_blue = ImageTk.PhotoImage(Image.open("Assets/Images/Bg_blue.jpg").resize((1600, 1024)))
about_bg = ImageTk.PhotoImage(Image.open("Assets/Images/about.page.png").resize((1410, 840)))

facil_template = ImageTk.PhotoImage(Image.open("Assets/Images/Fácil.png").resize((320, 500)))
normal_template = ImageTk.PhotoImage(Image.open("Assets/Images/Normal.png").resize((320, 500)))
difícil_template = ImageTk.PhotoImage(Image.open("Assets/Images/Dificil.png").resize((320, 500)))

teorico_template = ImageTk.PhotoImage(Image.open("Assets/Images/Teórico.png").resize((320, 500)))
prático_template = ImageTk.PhotoImage(Image.open("Assets/Images/Prático.png").resize((320, 500)))

bg_image_doctor = ImageTk.PhotoImage(Image.open("Assets/Images/Doctor_meu_nobre.jpg"))
user_img = ImageTk.PhotoImage(Image.open("Assets/Images/User.png").resize((150, 150)))

doctor_plate = ImageTk.PhotoImage(Image.open("Assets/Images/Anime_plate.png").resize((640, 280)))
Anime_doctor_img = ImageTk.PhotoImage(Image.open("Assets/Images/Anime doctor.png").resize((220, 220)))

back_button_img = ImageTk.PhotoImage(Image.open("Assets/Images/arrow-left-3099.png").resize((140, 140)))

# Card Images

first_year_lady_img = ImageTk.PhotoImage(Image.open("Assets/Images/apacucpel_ucpel_image_319-1024x960.jpeg"))
first_year_teenage_girl = ImageTk.PhotoImage(Image.open("Assets/Images/freepik__upload__79487.png"))
Second_year_template = ImageTk.PhotoImage(Image.open("Assets/Images/jovem-estudando-computador-estudar-jovem-negro-1621453944939_v2_450x450.jpg"))
Third_year_template = ImageTk.PhotoImage(Image.open("Assets/Images/dificuldade-para-estudar.png"))
Fourth_year_template = ImageTk.PhotoImage(Image.open("Assets/Images/15-livros-que-todo-estudante-deve-ler-antes-de-entrar-na-faculdade.jpg"))
Fifth_year_template = ImageTk.PhotoImage(Image.open("Assets/Images/médico.jpg"))
Sixth_year_template = ImageTk.PhotoImage(Image.open("Assets/Images/graduaotcnica.jpg"))

# Anatomy Pratical Images!

A_1 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_1.png"))
A_2 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_2.png").resize((375, 375)))
A_3 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_3.png").resize((375, 375)))
A_4 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_4.png").resize((375, 375)))
A_5 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_5.png").resize((375, 375)))
A_6 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_6.png").resize((375, 375)))
A_7 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_7.png").resize((375, 375)))
A_8 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_8.png").resize((375, 375)))
A_9 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_9.png").resize((375, 375)))
A_10 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_10.png").resize((375, 375)))
A_11 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_11.png").resize((375, 375)))
A_12 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_12.png").resize((375, 375)))
A_13 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_13.png").resize((375, 375)))
A_14 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_14.png").resize((375, 375)))
A_15 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_15.png").resize((375, 375)))
A_16 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_16.png").resize((375, 375)))
A_17 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_17.png").resize((375, 375)))
A_18 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_18.png").resize((375, 375)))
A_19 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_19.png").resize((375, 375)))
A_20 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_20.png").resize((375, 375)))
A_21 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_21.png").resize((375, 375)))
A_22 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_22.png").resize((375, 375)))
A_23 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_23.png").resize((375, 375)))
A_24 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_24.png").resize((375, 375)))
A_25 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_25.png").resize((375, 375)))
A_26 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_26.png").resize((375, 375)))
A_27 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_27.png").resize((375, 375)))
A_28 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_28.png").resize((375, 375)))
A_29 = ImageTk.PhotoImage(Image.open("Assets/Images/Anatomia I/A_29.png").resize((375, 375)))

# Icons

help_icon = ImageTk.PhotoImage(Image.open("Assets/Images/Button_help.png").resize((96, 96)))
help_icon_used = ImageTk.PhotoImage(Image.open("Assets/Images/Help_icon_used.png").resize((96, 96)))
home_icon = ImageTk.PhotoImage(Image.open("Assets/Images/Button_home.png").resize((96, 96)))
sound_icon = ImageTk.PhotoImage(Image.open("Assets/Images/Sound.png").resize((64, 64)))
no_sound_icon = ImageTk.PhotoImage(Image.open("Assets/Images/no-sound.png").resize((64, 64)))
cross_exit = ImageTk.PhotoImage(Image.open("Assets/Images/x-button.png").resize((64, 64)))

# Loading Sounds

Risada_do_Luan_1 = pygame.mixer.Sound("Assets/Audio/Risada do Luan.mp3")
Risada_do_Luan_2 = pygame.mixer.Sound("Assets/Audio/Risada do Luan Extensa 2.mp3")
Risada_do_Luan_3 = pygame.mixer.Sound("Assets/Audio/Risada do luan Extensa.mp3")
Risada_do_Luan_4 = pygame.mixer.Sound("Assets/Audio/Risada do luan Rápida.mp3")
Dumd_Ass = pygame.mixer.Sound("Assets/Audio/Você é burro você!!!.mp3")

Risada_do_Luan_1.set_volume(0.9)
Risada_do_Luan_2.set_volume(0.9)
Risada_do_Luan_3.set_volume(0.9)
Risada_do_Luan_4.set_volume(0.9)
Dumd_Ass.set_volume(0.9)

Random_audios = [Risada_do_Luan_1, Risada_do_Luan_2, Risada_do_Luan_3, Risada_do_Luan_4, Dumd_Ass]

bg_music = pygame.mixer.Sound("Assets/Audio/Socrátes é wey rijo Jovem!!_Trim.mp3")
bg_music.set_volume(0.7)
bg_music.play(-1)

right_answer_sound = pygame.mixer.Sound("Assets/Audio/Right_Answer.mp3")
right_answer_sound.set_volume(0.9)

success_sound = pygame.mixer.Sound("Assets/Audio/CORRECT ANSWER SOUND EFFECT _ NO COPYRIGHT.mp3")
success_sound.set_volume(0.8)

button_clicked_sound = pygame.mixer.Sound("Assets/Audio/Button click sound _ sound effect.mp3")
button_clicked_sound.set_volume(0.8)

pai_profeta = pygame.mixer.Sound("Assets/Audio/Pai_profeta.mp3")
pai_profeta.set_volume(1)

hey = pygame.mixer.Sound("Assets/Audio/Heyyy!!.mp3")
hey.set_volume(1)

Silvio_laugh = pygame.mixer.Sound("Assets/Audio/Sílvio _risada.mp3")
Silvio_laugh.set_volume(1)

Silvio_ta_bom = pygame.mixer.Sound("Assets/Audio/Sílvio Santos - E tá bom.mp3")
Silvio_ta_bom.set_volume(1)

# Global Variables

user_name = ""

nomes_ínvalidos = ["cona", "pipito", "vagina", "pênis", "foder", "fodedor", "puta", "caralho", "porra", "piça",
                   "esperma", "cú", "ânus", "catinga", "putaria", "merda", "P0rra", "cu", "cuzinho", "foda", "penis","puto", "put0", "pila", "buceta", "xobota", "xoxota", "pil@"]

text_size = 15
font_familly = "Arial"

title_font = "Great vibes"

keys = ["a", "b", "c", "d"]

Questions = {}

index = 0
points = 0
add = 0
diferrence = 0
ajudas = 3
qualification = ""
color_stats = ""
recycle_dict = dict()
wrong_dict = dict()
No_audio = False

# Pratical Questions

Pratical_Questions_Anatomia_I = {

    A_1: ["*Estrutura/Órgão: Osso etmoides", "Estrutura/Órgão: Osso esfenoides"],
    A_2: [
        "*Estrutura/Órgão: Osso frontal#Detatlhes assinalados:#1-Eminência frontal#2-Foramen supraorbital#3-Glabela#4-Margem supraorbital",
        "Estrutura/Órgão: Osso frontal#Detatlhes assinalados:#1-Porção escamosa#2-Foramen supraorbital#3-Porção nasal#4-Porção orbital"],
    A_3: [
        "*Estrutura/Órgão: Osso frontal#Porções assinaladas:#1-Porção escamosa#3-Porção nasal#4-Porção orbital#Detalhes assinalados:#2-Foramen supraorbital",
        "Estrutura/Órgão: Osso frontal#Porções assinaladas:#1-Eminência frontal#3-Glabela#4-Arco superciliar#Detalhes assinalados:#2-Foramen supraorbital"],
    A_4: ["*Estrutura/Órgão: Osso frontal(cara externa)#Detalhes assinalados:#1-Arco superciliar#2-Processo zigomático",
          "Estrutura/Órgão: Osso frontal(cara externa)#Detalhes assinalados:#1-Margem supaorbital#2-Processo zigomático"],
    A_5: ["*Estrutura/Órgão: Osso Vomer", "Estrutura/Órgão: Osso Palatino"],
    A_6: [
        "*Estrutura/Órgão: Osso frontal(cara interna)#Detalhes assinalados:#1-Sulco do seio sagital superior#2-Crista frontal#3-Foramen cego",
        "Estrutura/Órgão: Osso frontal(cara interna)#Detalhes assinalados:#1-Crista frontal#2-Sulco do seio sagital superior#3-Foramen cego"],
    A_7: [
        "*Estrutura/Órgão: Osso frontal(vista inferior)#Detalhes assinalados:#1-Espinho nasal#2-Fossita troclear#3-Orificio dos seios frontais#4-Fossa da glândula lacrimal",
        "Estrutura/Órgão: Osso frontal(vista inferior)#Detalhes assinalados:#1-Espinho nasal#2-Orificio dos seios frontais#3-Fossita troclear#4-Fossa da glândula lacrimal"],


    A_8: ["*Estrutura/Órgão: Osso Parietal(cara externa)#Detalhes assinalados:#1-Margem sagital#2-Margem frontal#3-Margem temporal#4-Margem occipital", "Estrutura/Órgão: Osso Temporal(cara externa)#1-Margem sagital#2-Margem frontal#3-Margem temporal#4-Margem occipital"],
    A_9: ["*Estrutura/Órgão: Osso Parietal(cara externa)#Detalhes assinalados:#1-Ângulo frontal#2-Ângulo esfenoidal#3-Ângulo mastoideo#4-Ângulo occipital", "Estrutura/Órgão: Osso Parietal(cara externa)#Detalhes assinalados:#1-Ângulo frontal#2-Ângulo estmoidal#3-Ângulo mastoideo#4-Ângulo occipital"],
    A_10: ["*Estrutura/Órgão: Osso Parietal(cara externa)#Detalhes assinalados:#1-Túber parietal#2-Linha temporal superior#3-Linha temporal inferior", "Estrutura/Órgão: Osso Temporal(cara externa)#Detalhes assinalados:#1-Túber temporal#2-Linha temporal superior#3-Linha temporal inferior"],
    A_11: ["*Estrutura/Órgão: Osso Parietal(cara interna)#Detalhes assinalados:#1-Fossitas granulosas#2-Sulco do seio sagital superior#3-Sulco da artéria meníngea média", "Estrutura/Órgão: Osso Temporal(cara interna)#Detalhes assinalados:#1-Fossitas granulosas#2-Sulco do seio sagital superior#3-Sulco da artéria meníngea média"],
    A_12: ["*Estrutura/Órgão: Osso Occipital(cara interna)#Detalhes assinalados:#1-Porção escamosa#2-Porção basilar#3-Porção lateral", "Estrutura/Órgão: Osso Occipital(cara interna)#Detalhes assinalados:#1-Porção escamosa#2-Porção lateral#3-Porção basilar"],
    A_13: ["*Estrutura/Órgão: Osso Occipital(cara externa)#Detalhes assinalados:#1-Protuberância occipital externa#2-Linha nucal superior#3-Crista occipital externa#4-Fossa condílea", "Estrutura/Órgão: Osso Occipital(cara externa)#Detalhes assinalados:#1-Protuberância occipital externa#2-Linha nucal superior#3-Crista occipital interna#4-Canal condilar"],
    A_14: ["*Estrutura/Órgão: Osso Occipital(cara externa)#Detalhes assinalados:#1-Linha nucal inferior#2-Incisuras jugulares#3-Túberculo faríngeo#4-Canal Condilar", "Estrutura/Órgão: Osso Occipital(cara externa)#Detalhes assinalados:#1-Linha nucal inferior#2-Túberculo faríngeo#3-Incisuras jugulares#4-Canal Condilar"],
    A_15: ["*Estrutura/Órgão: Osso Occipital(cara externa)#Detalhes assinalados:#1-Cóndilos", "Estrutura/Órgão: Osso Occipital(cara externa)#Detalhes assinalados:#1-Processo Atlanto-Occipital"],
    A_16: ["*Estrutura/Órgão: Osso Temporal(cara externa)#Detalhes assinalados:#1-Porção Escamosa#2-Porção Petrosa#3-Porção Timpânica",
                    "Estrutura/Órgão: Osso Temporal(cara externa)#Detalhes assinalados:#1-Porção Petrosa#2-Porção Escamosa#3-Porção Timpânica"],
    A_17: ["*Estrutura/Órgão: Osso Temporal(cara externa)#Detalhes assinalados:#1-Meato acústico externo#2-Poro acústico externo#3-Processo Mastóide#4-Fossa Mandibular",
                   "Estrutura/Órgão: Osso Temporal(cara externa)#Detalhes assinalados:#1-Meato acústico externo#2-Túberculo articular#3-Fossa Mandibular#4-Processo Mastóide"],

    A_18: ["*Estrutura/Órgão: Osso Temporal(cara externa)#Detalhes assinalados:#1-Processo zigomático#2-Tubérculo articular",
                   "Estrutura/Órgão: Osso Temporal(cara externa)#Detalhes assinalados:#1-Processo zigomático#2- Processo Mastóide"],

    A_19: ["*Estrutura/Órgão: Osso Temporal(cara interna)#Detalhes assinalados:#1-Impressão do trigêmio#2-Eminência arqueada#3-Teto do timpano#4-Poro acústico interno",
                   "Estrutura/Órgão: Osso Temporal(cara interna)#Detalhes assinalados:#1-Eminência arqueada#2-Teto do timpano#3-Impressão do trigêmio#4-Poro acústico interno"],

    A_20: ["*Estrutura/Órgão: Osso Temporal(cara interna)#Detalhes assinalados:#1-Processo estiloideo#2-Sulco do seio petroso superior",
            "Estrutura/Órgão: Osso Temporal(cara interna)#Detalhes assinalados:#1-Processo estiloideo#2-Sulco do seio petroso inferior"],

    A_21: [
        "*Estrutura/Órgão: Osso Esfenoide(vista posterior)#Detalhes assinalados:#1-Asas menores#2-Corpo#3-Asas maiores#4-Processos pterigoideos",
        "Estrutura/Órgão: Osso Esfenoide(vista posterior)#Detalhes assinalados:#1-Processos pterigoideos#2-Corpo#3-Asas maiores#4-Asas menores"],
    A_22: [
        "*Estrutura/Órgão: Osso Esfenoide(vista superior)#Detalhes assinalados:#1-Seia turca#2-Canal óptico#3-Fossita hipofisária#4-Sulco quiasmático",
        "Estrutura/Órgão: Osso Esfenoide(vista superior)#Detalhes assinalados:#1-Sulco quiasmático#2-Canal óptico#3-Fossita hipofisária#4-Seia turca"],

    A_23: [
        "*Estrutura/Órgão: Osso Esfenoide(vista superior)#Detalhes assinalados:#1-Forame oval#2-Dorso da seia turca#3-Processo clinoideo posterior#4-Sulco carotídeo",
        "*Estrutura/Órgão: Osso Esfenoide(vista superior)#Detalhes assinalados:#1-Forame oval#2-Processo clinoideo posterior#3-Sulco carotídeo#4-Dorso da seia turca"],

    A_24: [
        "*Estrutura/Órgão: Osso Esfenoide(vista posterior)#Detalhes assinalados:#1-Processo clinoideo anterior#2-Forame redondo#3-Fissura orital superior",
        "Estrutura/Órgão: Osso Esfenoide(vista posterior)#Detalhes assinalados:#1-Processo clinoideo posterior#2-Forame oval#3-Fissura orital superior", ],

    A_25: [
        "*Estrutura/Órgão: Osso Etmoides(vista anterior)#Detalhes assinalados:#1-Labirinto etmoidal#2-Lámina perpendicular",
        "Estrutura/Órgão: Osso Etmoides(vista posterior)#Detalhes assinalados:#1-Labirinto etmoidal#2-Lámina crivosa"],

    A_26: [
            "*Estrutura/Órgão: Osso Etmoides(vista superior)#Detalhes assinalados:#1-Crista Gali#2-Lámina crivosa#3-Lámina orbital#4-Massas laterais ou labirintos etmoidais",
            "Estrutura/Órgão: Osso Etmoides(vista superior)#Detalhes assinalados:#1-Crista Gali#2-Lámina crivosa#3-Lámina orbital#4-Massas laterais ou labirintos etmoidais"],

    A_27: [
            "*Estrutura/Órgão: Osso Etmoides(vista lateral)#Detalhes assinalados:#1-Crista de Gallo#2-Lámina Perpendicular",
            "Estrutura/Órgão: Osso Etmoides(vista lateral)#Detalhes assinalados:#1-Lámina Crivosa#2-Lámina Perpendicular"],

    A_28: [
            "*Estrutura/Órgão: Crânio (vista lateral)#Detalhes assinalados:#1-Osso nasal#2-Osso maxilar#3-Osso zigomático#4-Osso mandibular",
            "Estrutura/Órgão: Crânio (vista lateral)#Detalhes assinalados:#1-Osso nasal#2-Osso maxilar superior#3-Osso zigomático#4-Osso maxilar mentoniano"],

    A_29: [
            "*Estrutura/Órgão: Crânio (vista lateral)#Detalhes assinalados:#1-Osso lacrimal",
            "Estrutura/Órgão: Crânio (vista lateral)#Detalhes assinalados:#1-Osso etmoidal"]

}

Questions_pratical_root = {}
Questions_pratical_root = load_60_question(Pratical_Questions_Anatomia_I, dificuldade)

def Load_main_page():

    button_clicked_sound.play()

    main_page()

# Menu About Section
def top_menu():

    Menu_man = Menu(tela)

    about = Menu(Menu_man, tearoff=False)
    Menu_man.add_command(label="Sobre...", command= lambda : about_page())

    tela.configure(menu=Menu_man)


def spit_broken_row(row):

    Question = ""
    row_2 = []

    for r in row:
        for q_1 in r:
            if q_1 == "#":
                Question += "\n"
            else:
                Question += q_1

        row_2.append(Question)
        Question = ""

    return row_2

def about_page():

    top_menu()

    frame_about = ctk.CTkFrame(tela, fg_color="#0068b7", bg_color="#0068b7")

    label_bg = ctk.CTkLabel(frame_about, text="", image=about_bg)
    label_bg.place(x = 0, y =0, relheight = 1, relwidth = 1)

    x_it = ctk.CTkLabel(frame_about, text="", image=cross_exit, cursor = "hand2")
    x_it.place(relx = 0.92, rely = 0.09)

    x_it.bind("<Button-1>", lambda event: frame_about.destroy())

    frame_about.place(x = 0, y = 0, relwidth = 1, relheight = 1)


def Sound_manager(widget, master):

    global Random_audios, bg_music, right_answer_sound, success_sound, button_clicked_sound, No_audio

    if No_audio:
        No_audio = False
    else:
        No_audio = True

    if No_audio:

        bg_music.set_volume(0)
        right_answer_sound.set_volume(0)
        success_sound.set_volume(0)
        button_clicked_sound.set_volume(0)
        Risada_do_Luan_1.set_volume(0)
        Risada_do_Luan_2.set_volume(0)
        Risada_do_Luan_3.set_volume(0)
        Risada_do_Luan_4.set_volume(0)
        pai_profeta.set_volume(0)
        hey.set_volume(0)
        Silvio_laugh.set_volume(0)
        Silvio_ta_bom.set_volume(0)
        Dumd_Ass.set_volume(0)

        widget = ctk.CTkLabel(master, text="", image=no_sound_icon, cursor="hand2")

    else:
        bg_music.set_volume(0.7)
        right_answer_sound.set_volume(0.9)
        success_sound.set_volume(0.8)
        button_clicked_sound.set_volume(0.8)
        Risada_do_Luan_1.set_volume(0.9)
        Risada_do_Luan_2.set_volume(0.9)
        Risada_do_Luan_3.set_volume(0.9)
        Risada_do_Luan_4.set_volume(0.9)
        hey.set_volume(1)
        Silvio_laugh.set_volume(1)
        Silvio_ta_bom.set_volume(1)
        Dumd_Ass.set_volume(0.9)

        pai_profeta.set_volume(1)
        widget = ctk.CTkLabel(master, text="", image=sound_icon, cursor="hand2")

    widget.bind("<Button-1>", lambda event: Sound_manager(widget, master))
    widget.place(relx=0.03, rely=0.285)


def back_button():
    pass

def animate_right_answer(widget_animated, his_options, check_wrong, prático=""):

    global add, animation_over, points

    add += 1

    for widgets in tela.winfo_children():
        widgets.unbind("<Enter>")
        widgets.unbind("<Leave>")
        widgets.unbind("<Button-1>")


    if add % 2 == 0:
        widget_animated.configure(fg_color="#c3d128")
    else:
        widget_animated.configure(fg_color="#2E487D")

    if add <= 6:
        widget_animated.after(200, lambda: animate_right_answer(widget_animated, his_options, check_wrong))
    else:

        if his_options[0] == "*":
            widget_animated.configure(fg_color="#45D41E")
            right_answer_sound.play()
            points += 1

        else:
            widget_animated.configure(fg_color="#BF2615")
            Random_audios[randint(0, 4)].play()
            for k, v in check_wrong.items():
                if v[0] == "*":
                    k.configure(fg_color="#45D41E")


        tela.after(1650, lambda: Second_page(user_name))


def animate_right_answer_pratical(widget_animated, his_options, check_wrong, questions_frame):

    global add, animation_over, points

    add += 1

    # for widgets in tela.winfo_children():
    #     widgets.unbind("<Enter>")
    #     widgets.unbind("<Leave>")
    #     widgets.unbind("<Button-1>")

    for widget in questions_frame.winfo_children():
        widget.unbind("<Enter>")
        widget.unbind("<Leave>")
        widget.unbind("<Button-1>")

    if add % 2 == 0:
        widget_animated.configure(fg_color="#e0992d")#2E487D
    else:
        widget_animated.configure(fg_color="#2E487D") #c3d128

    if add <= 6:
        widget_animated.after(200, lambda: animate_right_answer_pratical(widget_animated, his_options, check_wrong, questions_frame))
    else:

        if his_options[0] == "*":
            widget_animated.configure(fg_color="#45D41E")
            right_answer_sound.play()
            points += 1

        else:
            widget_animated.configure(fg_color="#BF2615")
            Random_audios[randint(0, 4)].play()
            for k, v in check_wrong.items():
                if v[0] == "*":
                    k.configure(fg_color="#45D41E")

        tela.after(1850, lambda: Prático_Page())

def help(Current_question):

    global ajudas

    button_clicked_sound.play()

    Current_question = spit_broken_row(Current_question)

    if ajudas <= 0:
        messagebox.showinfo(f"Restam {ajudas} pedidos de ajuda {user_name}!!", f"{user_name}, já não tem mais pedidos de ajuda meu nobre\nvoce já esgotou todos os 3!!")
    else:
        for q in Current_question:
            if q[0] == "*":
                ajudas -= 1
                if ajudas != 1:
                    messagebox.showinfo(f"Restam {ajudas} pedidos de ajuda {user_name}!!", f"{user_name}, a resposta certa é: '{q[1:]}'")
                else:
                    messagebox.showinfo(f"Restam {ajudas} pedido de ajuda {user_name}!!",
                                        f"{user_name}, a resposta certa é: '{q[1:]}'")


def reset_questions():

    global Questions, points, diferrence, qualification, color_stats, ajudas, Questions_root, index, dificuldade

    points = 0
    index = 0
    diferrence = 0
    ajudas = 3
    qualification = ""
    color_stats = ""
    dificuldade = ""


def get_doc_stats(points, prático=""):

    global qualification, diferrence, color_stats

    # Estagiário #BF2615
    # Paramédico #C4C229
    # Médico #325be3
    # Médico Especialista #45D41E

    if prático == "":
        total = len(Questions_root)
    else:
        total = len(Questions_pratical_root)

    percentage = (points/total) * 100

    if percentage < 30:
        qualification = "Estagiário"
        color_stats = "#BF2615"
        pai_profeta.play()

    elif percentage >= 30 and percentage < 50:
        qualification = "Paramédico"
        color_stats = "#C4C229"
    elif 50 <= percentage < 80:
        qualification = "Médico"
        color_stats = "#325be3"
    else:
        qualification = "Médico Especialista"
        color_stats = "#45D41E"

    diferrence = total - points

    clear_screen()

    success_sound.play()

    bg_statics_label = ctk.CTkLabel(tela, text="Estatísticas", text_color="#C4C229", font=(title_font, 52))
    bg_statics_label.pack(fill = "x", expand = True)

    frame_stats = ctk.CTkFrame(tela, bg_color="#0068b7", fg_color="#0068b7", corner_radius=36)

    plate_border_lbl = ctk.CTkLabel(frame_stats, text="", image=doctor_plate)
    plate_border_lbl.place(x = 0, y = 0, relwidth = 1, relheight = 1)

    frame_1 = ctk.CTkFrame(frame_stats, bg_color="#D9D9D9", fg_color="#D9D9D9")

    label_1_1 = ctk.CTkLabel(frame_1, text="Respostas Certas: ", text_color="#45D41E", font=(font_familly, 23), anchor="w", bg_color="#D9D9D9", fg_color="#D9D9D9")
    label_1_1.pack(side = "left")

    label_1_2 = ctk.CTkLabel(frame_1, text=f"{points}", text_color="#000", font=(font_familly, 23), bg_color="#D9D9D9", fg_color="#D9D9D9")
    label_1_2.pack(side = "left")

    frame_1.pack(fill = "x", pady = (70, 15), padx = (100, 400))

    frame_2 = ctk.CTkFrame(frame_stats, bg_color="#D9D9D9", fg_color="#D9D9D9")

    label_2_1 = ctk.CTkLabel(frame_2, text="Respostas Erradas: ", text_color="#BF2615", font=(font_familly, 23), anchor="w", bg_color="#D9D9D9", fg_color="#D9D9D9")
    label_2_1.pack(side = "left")

    label_2_2 = ctk.CTkLabel(frame_2, text=f"{diferrence}", text_color="#000", font=(font_familly, 23), bg_color="#D9D9D9", fg_color="#D9D9D9")
    label_2_2.pack(side="left")

    frame_2.pack(fill = "x", pady = 15, padx = (100, 400))

    frame_3 = ctk.CTkFrame(frame_stats, bg_color="#D9D9D9", fg_color="#D9D9D9")

    label_3_1 = ctk.CTkLabel(frame_3, text="Qualificação: ", text_color="#000", font=(font_familly, 23), anchor="w", bg_color="#D9D9D9", fg_color="#D9D9D9")
    label_3_1.pack(side = "left")

    label_3_2 = ctk.CTkLabel(frame_3, text=f"{qualification}", text_color=f"{color_stats}", font=(font_familly, 23), bg_color="#D9D9D9", fg_color="#D9D9D9")
    label_3_2.pack(side="left")

    frame_3.pack(fill = "x", pady = 15, padx = (100, 260))

    frame_stats.pack(pady = 20, expand = True, fill = "both", padx = 300)

    btn = ctk.CTkButton(tela, text="Prosseguir!!", command=end_page,
                        text_color="#D9D9D9", fg_color="#2E487D", bg_color="#0068b7", font=(font_familly, 36),
                        border_color="#D9D9D9", border_width=4, width=120, height=80, corner_radius=16)

    btn.pack(pady = (0, 80), expand = True)


def wait_screen(type_of_questions, dificulty, prático=""):

    global Questions, Questions_root, Questions_pratical_root, dificuldade

    clear_screen()

    dificuldade = dificulty

    if prático == "":

        Questions_root.clear()
        Questions_root = load_60_question(type_of_questions, dificuldade)

        Questions.clear()
        Questions = copy.deepcopy(Questions_root)

        main_frame = ctk.CTkFrame(tela, bg_color="#242424", fg_color="#242424")

        lbl_text = ctk.CTkLabel(main_frame, text_color="#d9d3d2", text=f"Prepare-se {user_name}...", font=("Calibri", 72))
        lbl_text.pack(anchor="center", pady = 300)

        main_frame.place(x = 0, y =0 , relwidth = 1, relheight =1)

        tela.after(2000, lambda : Second_page(user_name))
    else:

        Questions_pratical_root.clear()
        Questions_pratical_root = load_60_question(type_of_questions, dificuldade)

        Questions.clear()
        # Questions = copy.deepcopy(Questions_pratical_root)
        Questions = Questions_pratical_root.copy()

        main_frame = ctk.CTkFrame(tela, bg_color="#242424", fg_color="#242424")

        lbl_text = ctk.CTkLabel(main_frame, text_color="#d9d3d2", text=f"Prepare-se {user_name}...",
                                font=("Calibri", 72))
        lbl_text.pack(anchor="center", pady=300)

        main_frame.place(x=0, y=0, relwidth=1, relheight=1)

        tela.after(2000, lambda: Prático_Page())


def load_easy(type_of_questions, dificulty, prático=""):

    button_clicked_sound.play()

    Silvio_laugh.play()

    wait_screen(type_of_questions, dificulty, prático)


def load_normal(types_of_questions, dificulty, prático=""):

    button_clicked_sound.play()

    Silvio_ta_bom.play()

    wait_screen(types_of_questions, dificulty, prático)


def load_hard(types_of_questions, dificulty, prático=""):

    button_clicked_sound.play()

    hey.play()

    wait_screen(types_of_questions, dificulty, prático)


def dificulty_page(types_of_questions, prático=""):

    clear_screen()

    button_clicked_sound.play()

    main_frame = Frame(tela, background="#C4C229")

    label_txt = ctk.CTkLabel(main_frame, text=f"Selecione a sua dificuldade {user_name}!!",
                             font=("Lucida Calligraphy", 46), text_color="black")
    label_txt.pack(side = "top", pady = (32, 0))

    lbl_img_facil = ctk.CTkLabel(main_frame, text="", image=facil_template, cursor="hand2")
    lbl_img_facil.place(relx = 0.08, rely = 0.2)

    lbl_img_normal = ctk.CTkLabel(main_frame, text="", image=normal_template, cursor="hand2")
    lbl_img_normal.place(relx=0.38, rely=0.2)

    lbl_img_difícil = ctk.CTkLabel(main_frame, text="", image=difícil_template, cursor="hand2")
    lbl_img_difícil.place(relx=0.68, rely=0.2)

    # back_button_lbl = ctk.CTkLabel(main_frame, text="", image=back_button_img, cursor="hand2")
    # back_button_lbl.place(relx=0.05, rely=0.2)

    lbl_img_facil.bind("<Button-1>", lambda event : load_easy(types_of_questions, "Fácil", prático))
    lbl_img_normal.bind("<Button-1>", lambda event : load_normal(types_of_questions, "Normal", prático))
    lbl_img_difícil.bind("<Button-1>", lambda event : load_hard(types_of_questions, "Difícil", prático))

    # back_button_lbl.bind("<Button-1>", lambda event : tela.quit())

    main_frame.place(x = 0, y = 0, relwidth = 1, relheight = 1)


def category_page(types_of_questions_teorico, types_of_questions_prático):

    clear_screen()

    button_clicked_sound.play()

    main_frame = Frame(tela, background="#C4C229")

    label_txt = ctk.CTkLabel(main_frame, text=f"Selecione a sua categória {user_name}!!",
                             font=("Lucida Calligraphy", 46), text_color="black")
    label_txt.pack(side = "top", pady = (32, 0))

    lbl_img_teorico = ctk.CTkLabel(main_frame, text="", image=teorico_template, cursor="hand2")
    lbl_img_teorico.place(relx=0.24, rely=0.2)

    lbl_img_prático = ctk.CTkLabel(main_frame, text="", image=prático_template, cursor="hand2")
    lbl_img_prático.place(relx=0.52, rely=0.2)

    lbl_img_teorico.bind("<Button-1>", lambda event : dificulty_page(types_of_questions_teorico))
    lbl_img_prático.bind("<Button-1>", lambda event : dificulty_page(types_of_questions_prático, "yes"))

    main_frame.place(x = 0, y = 0, relwidth = 1, relheight = 1)


def end_page():

    clear_screen()

    button_clicked_sound.play()

    frame = Frame(tela)
    game_over_label = ctk.CTkLabel(frame, image=end_template, text="")
    game_over_label.pack(expand = True, fill = "both")

    frame.pack(expand = True, fill = "both")

    tela.bind("<Key>", lambda event: main_page())


def shuffle_dict(dicionário):

    global Questions

    keys = []
    new_dict = {}

    for k in dicionário.keys():
        keys.append(k)

    shuffle(keys)
    for k in keys:
        new_dict[k] = ""

    for k, v in dicionário.items():
        for k2 in new_dict.keys():
            if k == k2:
                new_dict[k2] = v

    Questions = new_dict


def clear_screen():

    for widgets in tela.winfo_children():
        widgets.destroy()

    top_menu()


def main_page():

    global main_frame

    tela.unbind("<Key>")

    reset_questions()

    shuffle_dict(Questions)

    shuffle_dict(Pratical_Questions_Anatomia_I)

    clear_screen()

    main_frame = Frame(tela, background="#0068b7")

    bg_wallpaper = CTkLabel(main_frame, text="", image=bg_image)
    bg_wallpaper.place(x=0, y=0, relwidth=1, relheight=1)

    text_2 = ctk.CTkButton(main_frame, text="Jogar!", command= login_plate,
                           text_color="#D9D9D9", fg_color="#2E487D", bg_color="#0068b7", font=(font_familly, 36),
                           border_color="#D9D9D9", border_width=4, width=180, height=80, corner_radius=16) #login_plate
    text_2.pack(side="bottom", pady = (0, 30), padx= (0, 10))

    main_frame.pack(expand = True, fill = "both")

# Funções das Disciplinas (My God it's gonna be a lot...!😱)

def Histologia_I_Page():

    dificulty_page(Questions_Histologia_I)

def Histologia_II_Page():

    dificulty_page(Questions_Histologia_II)

def Prático_Page():

    global recycle_dict, user_name, points, add, wrong_dict, index, Questions

    tela.unbind("<Return>")

    clear_screen()

    add = 0

    # tela.config(background="#C4C229")

    def animate_button_enter(widget):
        widget.configure(font=(font_familly, 14), cursor="hand2",
                         fg_color="#e0992d", text_color="#ffffff", corner_radius=11)

    def animate_button_leave(widget):
        widget.configure(font=(font_familly, 14), cursor="hand2",
                         fg_color="#2E487D", text_color="#ffffff", corner_radius=11)

    def delete_already_seen_Question(Dict):

        global recycle_dict

        key = ""

        for k, v in recycle_dict.items():
            key = k

        for k, v in Questions.items():
            if key == k:
                del Questions[key]
                break

    def get_right_question_pratical(Questions, option, Current_Question, widget, wrong_dict_pass, questions_frame):

        global user_name, points, add

        delete_already_seen_Question(Questions)

        # Animation Section

        animate_right_answer_pratical(widget, option, wrong_dict_pass, questions_frame)

    # Questions flow

    if not Questions:

        get_doc_stats(points, "yes")

    else:

        page_frame = Frame(tela, background="#C4C229")

        upper_frame = Frame(page_frame, background="#C4C229")

        upper_title = ctk.CTkLabel(upper_frame,
                                   text=f"{user_name}, selecione a estrutura/órgão e o detalhe\n(indicado pela seta) correspondentes!",
                                   font=("Lucida Calligraphy", 30), text_color="Black")
        upper_title.pack(ipady=20, pady=3)

        anim_doc = ctk.CTkLabel(tela, text="", image=Anime_doctor_img, fg_color="#C4C229")
        anim_doc.place(relx=0.85, rely=0)
        anim_doc.lift()

        upper_frame.pack(fill="x", expand=False)

        mid_frame = Frame(page_frame, background="#C4C229")

        for k, v in Questions.items():

            img_question_lbl = ctk.CTkLabel(mid_frame, text="", image=k)
            img_question_lbl.place(relx=0.12, rely=0.07)

            recycle_dict = {k: shuffle(v)}
            options = v

            break

        options_frame = Frame(mid_frame, background="#C4C229")

        options = spit_broken_row(options)

        if options[0][0] == "*":
            option_1 = ctk.CTkLabel(options_frame, text=options[0][1:], bg_color="#C4C229",
                                    corner_radius=11, cursor="hand2", fg_color="#2E487D", text_color="#ffffff",
                                    font=(font_familly, 14))

        else:
            option_1 = ctk.CTkLabel(options_frame, text=options[0], bg_color="#C4C229",
                                    corner_radius=11, cursor="hand2", fg_color="#2E487D", text_color="#ffffff",
                                    font=(font_familly, 14))

        option_1.pack(side="left", padx=(0, 30), expand=True, fill="both", ipadx=10, ipady=55)

        if options[1][0] == "*":
            option_2 = ctk.CTkLabel(options_frame, text=options[1][1:], bg_color="#C4C229",
                                    corner_radius=11, cursor="hand2", fg_color="#2E487D", text_color="#ffffff",
                                    font=(font_familly, 14))
        else:
            option_2 = ctk.CTkLabel(options_frame, text=options[1], bg_color="#C4C229",
                                    corner_radius=11, cursor="hand2", fg_color="#2E487D", text_color="#ffffff",
                                    font=(font_familly, 14))


        option_2.pack(side="left", padx=(0, 10), expand=True, fill="both", ipadx=10, ipady=55)

        options_frame.place(relx=0.41, rely = 0.32)

        #Hover Effect and Right answer effects

        wrong_dict = {option_1: options[0], option_2: options[1]}

        option_1.bind("<Button-1>", lambda event: get_right_question_pratical(Questions, options[0], recycle_dict, option_1, wrong_dict, options_frame))
        option_1.bind("<Enter>", lambda event: animate_button_enter(option_1))
        option_1.bind("<Leave>", lambda event: animate_button_leave(option_1))

        option_2.bind("<Button-1>", lambda event: get_right_question_pratical(Questions, options[1], recycle_dict, option_2, wrong_dict, options_frame))
        option_2.bind("<Enter>", lambda event: animate_button_enter(option_2))
        option_2.bind("<Leave>", lambda event: animate_button_leave(option_2))

        mid_frame.pack(fill="both", expand=True)

        bottom_frame = Frame(page_frame, background="#C4C229")

        left_frame = Frame(bottom_frame, background="#C4C229")

        button_1 = ctk.CTkLabel(left_frame, text="", image=home_icon, cursor="hand2")
        button_1.pack(side="left", padx=(570, 7), anchor="nw")

        if ajudas <= 0:
            button_2 = ctk.CTkLabel(left_frame, text="", image=help_icon_used)
        else:
            button_2 = ctk.CTkLabel(left_frame, text="", image=help_icon, cursor="hand2")

        button_2.pack(padx=7, anchor="nw")

        left_frame.pack(side="left")

        right_footer = Frame(bottom_frame, background="#C4C229")

        footer_1 = ctk.CTkLabel(right_footer, text=f"Respostas Certas: {points}", font=(font_familly, 23), text_color="#000")
        footer_1.pack(pady = (0, 10))

        footer_2 = ctk.CTkLabel(right_footer, text=f"Perguntas Respondidas: {index} de {len(Pratical_Questions_Anatomia_I)}", font=(font_familly, 23), text_color="#000")
        footer_2.pack()

        right_footer.pack(side="right", padx=(0, 20))

        bottom_frame.pack(fill="x", expand=False, side="bottom", pady=(0, 8), ipady=11)

        # Low buttons actions

        button_1.bind("<Button-1>", lambda event: Load_main_page())

        if ajudas <= 0:
            button_2.unbind("<Button-1>")
        else:
            button_2.bind("<Button-1>", lambda event: help(options))

        if No_audio:
            sound_label = ctk.CTkLabel(bottom_frame, text="", image=no_sound_icon, cursor="hand2")
        else:
            sound_label = ctk.CTkLabel(bottom_frame, text="", image=sound_icon, cursor="hand2")

        sound_label.place(relx=0.03, rely=0.285)

        sound_label.bind("<Button-1>", lambda event: Sound_manager(sound_label, bottom_frame))

        page_frame.pack(fill="both", expand=True)

        index += 1

def Anatomia_II_Page():

    dificulty_page(Questions_Anatomia_II)

def Anatomia_III_Page():

    dificulty_page(Questions_Anatomia_III)

def Fisiologia_I_Page():

    dificulty_page(Questions_Fisiologia_I)

def Fisiologia_II_Page():

    dificulty_page(Questions_Fisiologia_II)

def Bioquímica_II_Page():

    dificulty_page(Questions_Bioquímica_II)

def Embriologia_I_Page():

    dificulty_page(Questions_Embriologia_I)

def Embriologia_II_Page():

    dificulty_page(Questions_Embriologia_II)

def Medicina_Comunitária_I_Page():

    dificulty_page(Questions_Médicina_Comunitária_I)

def Medicina_Comunitária_II_Page():

    dificulty_page(Questions_Médicina_Comunitária_II)

def Informática_Médica_II_Page():

    dificulty_page(Questions_Informática_Médica_II)

def Genética_Médica_Page():

    dificulty_page(Questions_Genética_Médica)

def Introdução_à_la_Clínica_Page():

    dificulty_page(Questions_Introdução_à_Clínica)

def Microbiologia_Page():

    dificulty_page(Questions_Microbiologia)

def Patologia_Geral_Page():

    dificulty_page(Questions_Patologia_Geral)

def Piscologia_I_Page():

    dificulty_page(Questions_Psicologia_I)

# Anos da FAU!

def Second_page(name):

    global Questions, recycle_dict, user_name, points, add, wrong_dict, index

    tela.unbind("<Return>")

    clear_screen()

    add = 0

    def animate_button_enter(widget):
        widget.configure(font=(font_familly, text_size), justify="right", cursor="hand2",
                         fg_color="#c3d128", text_color="#ffffff", anchor="w", corner_radius=23)

    def animate_button_leave(widget):
        widget.configure(font=(font_familly, text_size), justify="right", cursor="hand2",
                         fg_color="#2E487D", text_color="#ffffff", anchor="w", corner_radius=23)

    def delete_already_seen_Question(Dict):

        global recycle_dict

        key = ""

        for k, v in recycle_dict.items():
            key = k

        for k, v in Questions.items():
            if key == k:
                del Questions[key]
                break

    def get_right_question(Questions, option, Current_Question, widget, wrong_dict_pass):

        global user_name, points, add

        delete_already_seen_Question(Questions)

        # Animation Section

        animate_right_answer(widget, option, wrong_dict_pass)

    if not Questions:

        get_doc_stats(points)

    else:

        Question = ""

        for k, v in Questions.items():

            for i, q_1 in enumerate(k):
                if q_1 == "#":
                    Question += "\n"
                else:
                    Question += q_1

            if len(Question) >= 100:
                title = ctk.CTkLabel(tela, text=f"{name}, {Question}", fg_color="#C4C229", text_color="#000000",
                                     corner_radius=32, font=(font_familly, 20), bg_color="transparent")
                title.pack(pady=(30, 30), ipady=42, ipadx=20)


            elif len(Question) >= 34 and len(Question) < 100:
                title = ctk.CTkLabel(tela, text=f"{name}, {Question}", fg_color="#C4C229", text_color="#000000",
                                     corner_radius=32, font=(font_familly, 23), bg_color="transparent")

                title.pack(pady=(30, 45), ipady=48, ipadx=20)

            else:
                title = ctk.CTkLabel(tela, text=f"{name}, {Question}", fg_color="#C4C229", text_color="#000000",
                                     corner_radius=32, font=(font_familly, 26), bg_color="transparent")

                title.pack(pady = (30, 46), ipady=48, ipadx=20)

            recycle_dict = {k:shuffle(v)}
            options = v
            break


        if options[0][0] == "*":

            Q_1 = ctk.CTkLabel(tela, text=f"a-) {options[0][1:]}", font=(font_familly, text_size), justify="right", cursor="hand2", fg_color="#2E487D", text_color="#ffffff", anchor="w", width=250, corner_radius=23)
        else:
            Q_1 = ctk.CTkLabel(tela, text=f"a-) {options[0]}", font=(font_familly, text_size), justify="right", cursor="hand2", fg_color="#2E487D", text_color="#ffffff", anchor="w", width=250, corner_radius=23)


        if options[1][0] == "*":
            Q_2 = ctk.CTkLabel(tela, text=f"b-) {options[1][1:]}", font=(font_familly, text_size), justify="right", cursor="hand2", fg_color="#2E487D", text_color="#ffffff", anchor="w", corner_radius=23)
        else:
            Q_2 = ctk.CTkLabel(tela, text=f"b-) {options[1]}", font=(font_familly, text_size), justify="right", cursor="hand2", fg_color="#2E487D", text_color="#ffffff", anchor="w", corner_radius=23)


        if options[2][0] == "*":
            Q_3 = ctk.CTkLabel(tela, text=f"c-) {options[2][1:]}", font=(font_familly, text_size), justify="right", cursor="hand2", fg_color="#2E487D", text_color="#ffffff", anchor="w", corner_radius=23)
        else:
            Q_3 = ctk.CTkLabel(tela, text=f"c-) {options[2]}", font=(font_familly, text_size), justify="right", cursor="hand2", fg_color="#2E487D", text_color="#ffffff", anchor="w", corner_radius=23)


        if options[3][0] == "*":
            Q_4 = ctk.CTkLabel(tela, text=f"d-) {options[3][1:]}", font=(font_familly, text_size), justify="right", cursor="hand2", fg_color="#2E487D", text_color="#ffffff", anchor="w", corner_radius=23)

        else:
            Q_4 = ctk.CTkLabel(tela, text=f"d-) {options[3]}", font=(font_familly, text_size), justify="right", cursor="hand2", fg_color="#2E487D", text_color="#ffffff", anchor="w", corner_radius=23)


        Q_1.pack(pady=10, padx=200, fill="x", ipady=10)
        Q_2.pack(pady=10, padx=200, fill="x", ipady=10)
        Q_3.pack(pady=10, padx=200, fill="x", ipady=10)
        Q_4.pack(pady=10, padx=200, fill="x", ipady=10)

        wrong_dict = {Q_1 : options[0], Q_2 : options[1], Q_3 : options[2], Q_4 : options[3]}

        Q_1.bind("<Button-1>", lambda event: get_right_question(Questions, options[0], recycle_dict, Q_1, wrong_dict))
        Q_1.bind("<Enter>", lambda event: animate_button_enter(Q_1)) #c3d128
        Q_1.bind("<Leave>", lambda event: animate_button_leave(Q_1)) #2E487D

        Q_2.bind("<Button-1>", lambda event: get_right_question(Questions, options[1], recycle_dict, Q_2, wrong_dict))
        Q_2.bind("<Enter>", lambda event: animate_button_enter(Q_2))  # c3d128
        Q_2.bind("<Leave>", lambda event: animate_button_leave(Q_2))

        Q_3.bind("<Button-1>", lambda event: get_right_question(Questions, options[2], recycle_dict, Q_3, wrong_dict))
        Q_3.bind("<Enter>", lambda event: animate_button_enter(Q_3))  # c3d128
        Q_3.bind("<Leave>", lambda event: animate_button_leave(Q_3))

        Q_4.bind("<Button-1>", lambda event: get_right_question(Questions, options[3], recycle_dict, Q_4, wrong_dict))
        Q_4.bind("<Enter>", lambda event: animate_button_enter(Q_4))  # c3d128
        Q_4.bind("<Leave>", lambda event: animate_button_leave(Q_4))

        Anime_doctor_lbl = ctk.CTkLabel(tela, text = "", image=Anime_doctor_img)
        Anime_doctor_lbl.place(relx = 0.85, rely = 0)
        title.lift()

        frame_bottom = ctk.CTkFrame(tela, bg_color="#0068b7", fg_color="#0068b7")

        button_1 = ctk.CTkLabel(frame_bottom, text="", image=home_icon, cursor = "hand2")
        button_1.pack(side = "left", padx = (570, 7), pady = (0, 15), anchor = "nw")

        if ajudas <= 0:
            button_2 = ctk.CTkLabel(frame_bottom, text="", image=help_icon_used)
        else:
            button_2 = ctk.CTkLabel(frame_bottom, text="", image=help_icon, cursor="hand2")

        button_2.pack(padx = 7, pady = (0, 15), anchor = "nw")

        points_indicator = ctk.CTkLabel(frame_bottom, text=f"Respostas Certas: {points}", font=(font_familly, 23), text_color="#fff")
        points_indicator.place(relx = 0.73, rely = 0.185)

        questions_answered = ctk.CTkLabel(frame_bottom, text=f"Perguntas respondidas: {index} de {len(Questions_root)}",
                                        font=(font_familly, 23), text_color="#fff")
        questions_answered.place(relx=0.7, rely=0.6)

        if No_audio:
            sound_label = ctk.CTkLabel(frame_bottom, text="", image=no_sound_icon, cursor="hand2")
        else:
            sound_label = ctk.CTkLabel(frame_bottom, text="", image=sound_icon, cursor = "hand2")

        sound_label.place(relx = 0.03, rely = 0.285)

        sound_label.bind("<Button-1>", lambda event: Sound_manager(sound_label, frame_bottom))

        frame_bottom.pack(fill = "both", side = "bottom")

        button_1.bind("<Button-1>", lambda event: Load_main_page())

        if ajudas <= 0:
            button_2.unbind("<Button-1>")
        else:
            button_2.bind("<Button-1>", lambda event: help(options))

        index += 1


def first_year_panel():

    clear_screen()

    button_clicked_sound.play()

    left_frame = Frame(tela, background="#C4C229")

    label_title = ctk.CTkLabel(left_frame, text=f"Selecione a disciplina que quer\nenfrentar {user_name}!!",
                               font=("Lucida Calligraphy", 39),
                               text_color="Black")
    label_title.pack(pady=20)

    # Criando o Canvas

    Canvas_scroll = Canvas(left_frame, background="#C4C229", bg="#C4C229", highlightbackground="#C4C229")
    Canvas_scroll.pack(side="left", fill="both", expand=True)

    # Criar uma Scrollba1
    scrollbar = ctk.CTkScrollbar(left_frame, command=Canvas_scroll.yview)
    scrollbar.pack(side="right", fill="y")

    # Configurar o Canvas para funcionar com a Scrollbar
    Canvas_scroll.configure(yscrollcommand=scrollbar.set)

    # Criar um Frame dentro do Canvas para conter os widgets
    scrollable_frame = Frame(Canvas_scroll)
    scrollable_frame_id = Canvas_scroll.create_window((0, 1), window=scrollable_frame, anchor="center")

    # Ajustar a área de rolagem automaticamente
    def update_scrollregion(event):
        Canvas_scroll.configure(scrollregion=Canvas_scroll.bbox("all"))

    scrollable_frame.bind("<Configure>", update_scrollregion)

    # Adicionar evento de rolagem com o mouse
    def on_mouse_scroll(event):
        Canvas_scroll.yview_scroll(-1 * (event.delta // 120), "units")

    def center_frame(event=None):
        canvas_width = Canvas_scroll.winfo_width()
        canvas_height = Canvas_scroll.winfo_height()
        frame_width = scrollable_frame.winfo_reqwidth()
        frame_height = scrollable_frame.winfo_reqheight()

        x_position = (canvas_width - frame_width) // 2
        y_position = (canvas_height - frame_height) // 2

        Canvas_scroll.coords(scrollable_frame_id, max(0, x_position), max(0, y_position))
        update_scrollregion(event)

    # Vincular eventos para atualizar a posição do frame
    Canvas_scroll.bind("<Configure>", center_frame)
    scrollable_frame.bind("<Configure>", update_scrollregion)

    Canvas_scroll.bind_all("<MouseWheel>", on_mouse_scroll)

    Canvas_scroll.yview_moveto(0)

    box_frame = Frame(scrollable_frame, background="#C4C229")

    Subject_1 = ctk.CTkButton(box_frame, text="Anatomia I", corner_radius=23,
                               text_color="#C4C229", fg_color="#106620",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2", command=lambda: category_page(Questions_Anatomia_II, Pratical_Questions_Anatomia_I))

    Subject_1.pack(fill="x", padx=40, pady=(20, 10))

    Subject_2 = ctk.CTkButton(box_frame, text="Anatomia II", corner_radius=23,
                               text_color="#C4C229", fg_color="#106620",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2", command=Anatomia_II_Page)

    Subject_2.pack(fill="x", padx=40, pady=(10, 10))

    Subject_3 = ctk.CTkButton(box_frame, text="Histologia I", corner_radius=23,
                               text_color="#C4C229", fg_color="#106620",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2", command=Histologia_I_Page)

    Subject_3.pack(fill="x", padx=40, pady=(10, 10))

    Subject_4 = ctk.CTkButton(box_frame, text="Histologia II", corner_radius=23,
                               text_color="#C4C229", fg_color="#106620",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2", command=Histologia_II_Page)

    Subject_4.pack(fill="x", padx=40, pady=(10, 10))

    Subject_5 = ctk.CTkButton(box_frame, text="Bioquímica I", corner_radius=23,
                               text_color="#C4C229", fg_color="#106620",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2")

    Subject_5.pack(fill="x", padx=40, pady=(10, 10))

    Subject_6 = ctk.CTkButton(box_frame, text="Bioquímica II", corner_radius=23,
                               text_color="#C4C229", fg_color="#106620",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2", command=Bioquímica_II_Page)

    Subject_6.pack(fill="x", padx=40, pady=(10, 10))

    Subject_7 = ctk.CTkButton(box_frame, text="Medicina Comunitária I", corner_radius=23,
                               text_color="#C4C229", fg_color="#106620",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2", command=Medicina_Comunitária_I_Page)

    Subject_7.pack(fill="x", padx=40, pady=(10, 10))

    Subject_8 = ctk.CTkButton(box_frame, text="Embriologia I", corner_radius=23,
                               text_color="#C4C229", fg_color="#106620",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2", command=Embriologia_I_Page)

    Subject_8.pack(fill="x", padx=40, pady=(10, 10))

    Subject_9 = ctk.CTkButton(box_frame, text="Fisiologia I", corner_radius=23,
                               text_color="#C4C229", fg_color="#106620",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2", command=Fisiologia_I_Page)

    Subject_9.pack(fill="x", padx=40, pady=(10, 10))

    Subject_10 = ctk.CTkButton(box_frame, text="Informática Médica I", corner_radius=23,
                               text_color="#C4C229", fg_color="#106620",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2", command=Informática_Médica_II_Page)

    Subject_10.pack(fill="x", padx=40, pady=(10, 30))


    box_frame.pack(expand = True, fill = "both")

    left_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1)

    right_frame = Frame(tela, background="#2E487D")

    label_img = Label(right_frame, image=first_year_teenage_girl)
    label_img.place(x=0, y=0, relwidth=1, relheight=1)

    right_frame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)


def Second_year_panel():

    clear_screen()

    button_clicked_sound.play()

    left_frame = Frame(tela, background="#C4C229")

    label_title = ctk.CTkLabel(left_frame, text=f"Selecione a disciplina que quer\nenfrentar {user_name}!!",
                               font=("Lucida Calligraphy", 39),
                               text_color="Black")
    label_title.pack(pady=20)

    # Criando o Canvas

    Canvas_scroll = Canvas(left_frame, background="#C4C229", bg="#C4C229", highlightbackground="#C4C229")


    # Criar uma Scrollba1
    scrollbar = ctk.CTkScrollbar(left_frame, command=Canvas_scroll.yview)
    scrollbar.pack(side="right", fill="y")

    # Configurar o Canvas para funcionar com a Scrollbar
    Canvas_scroll.configure(yscrollcommand=scrollbar.set)

    # Criar um Frame dentro do Canvas para conter os widgets
    scrollable_frame = Frame(Canvas_scroll)
    scrollable_frame_id = Canvas_scroll.create_window((0, 1), window=scrollable_frame, anchor="center")

    # Ajustar a área de rolagem automaticamente
    def update_scrollregion(event):
        Canvas_scroll.configure(scrollregion=Canvas_scroll.bbox("all"))

    scrollable_frame.bind("<Configure>", update_scrollregion)

    # Adicionar evento de rolagem com o mouse
    def on_mouse_scroll(event):
        Canvas_scroll.yview_scroll(-1 * (event.delta // 120), "units")

    def center_frame(event=None):
        canvas_width = Canvas_scroll.winfo_width()
        canvas_height = Canvas_scroll.winfo_height()
        frame_width = scrollable_frame.winfo_reqwidth()
        frame_height = scrollable_frame.winfo_reqheight()

        x_position = (canvas_width - frame_width) // 2
        y_position = (canvas_height - frame_height) // 2

        Canvas_scroll.coords(scrollable_frame_id, max(0, x_position), max(0, y_position))
        update_scrollregion(event)

    # Vincular eventos para atualizar a posição do frame
    Canvas_scroll.bind("<Configure>", center_frame)
    scrollable_frame.bind("<Configure>", update_scrollregion)

    Canvas_scroll.bind_all("<MouseWheel>", on_mouse_scroll)

    box_frame = Frame(scrollable_frame, background="#C4C229")

    Subject_1 = ctk.CTkButton(box_frame, text="Anatomia III", corner_radius=23,
                              text_color="#C4C229", fg_color="#4F544E",
                              bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2", command=Anatomia_III_Page)

    Subject_1.pack(fill="x", pady=(10, 10), expand = True)

    Subject_2 = ctk.CTkButton(box_frame, text="Embriologia II", corner_radius=23,
                              text_color="#C4C229", fg_color="#4F544E",
                              bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2", command=Embriologia_II_Page)

    Subject_2.pack(fill="x", pady=(10, 10), expand = True)

    Subject_3 = ctk.CTkButton(box_frame, text="Fisiologia II", corner_radius=23,
                              text_color="#C4C229", fg_color="#4F544E",
                              bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2", command=Fisiologia_II_Page)

    Subject_3.pack(fill="x", pady=(10, 10), expand = True)

    Subject_4 = ctk.CTkButton(box_frame, text="Histologia III", corner_radius=23,
                              text_color="#C4C229", fg_color="#4F544E",
                              bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2")

    Subject_4.pack(fill="x", pady=(10, 10), expand = True)

    Subject_5 = ctk.CTkButton(box_frame, text="Informática Médica II", corner_radius=23,
                              text_color="#C4C229", fg_color="#4F544E",
                              bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2", command=Informática_Médica_II_Page)

    Subject_5.pack(fill="x", pady=(10, 10), expand = True)

    Subject_6 = ctk.CTkButton(box_frame, text="Médicina Comunitária II", corner_radius=23,
                              text_color="#C4C229", fg_color="#4F544E",
                              bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2", command=Medicina_Comunitária_II_Page)

    Subject_6.pack(fill="x", pady=(10, 10), expand = True)

    Subject_7 = ctk.CTkButton(box_frame, text="Genética Médica", corner_radius=23,
                              text_color="#C4C229", fg_color="#4F544E",
                              bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2", command=Genética_Médica_Page)

    Subject_7.pack(fill="x", pady=(10, 10), expand = True)

    Subject_8 = ctk.CTkButton(box_frame, text="Introdução à Clínica", corner_radius=23,
                              text_color="#C4C229", fg_color="#4F544E",
                              bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2", command=Introdução_à_la_Clínica_Page)

    Subject_8.pack(fill="x", pady=(10, 10), expand = True)

    Subject_9 = ctk.CTkButton(box_frame, text="Microbiologia", corner_radius=23,
                              text_color="#C4C229", fg_color="#4F544E",
                              bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2", command=Microbiologia_Page)

    Subject_9.pack(fill="x", pady=(10, 10), expand = True)

    Subject_10 = ctk.CTkButton(box_frame, text="Patologia Geral", corner_radius=23,
                               text_color="#C4C229", fg_color="#4F544E",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2", command=Patologia_Geral_Page)

    Subject_10.pack(fill="x", pady=(10, 10), expand = True)

    Subject_10 = ctk.CTkButton(box_frame, text="Psicologia I", corner_radius=23,
                               text_color="#C4C229", fg_color="#4F544E",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2", command=Piscologia_I_Page)

    Subject_10.pack(fill="x", pady=(10, 30), expand = True)


    box_frame.pack(expand=True, fill="both")

    Canvas_scroll.pack(side="left", fill="both", expand=True)

    left_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1)

    right_frame = Frame(tela, background="#2E487D")

    label_img = Label(right_frame, image=Second_year_template)
    label_img.place(x=0, y=0, relwidth=1, relheight=1)

    right_frame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)


def Third_year_panel():

    clear_screen()

    button_clicked_sound.play()

    left_frame = Frame(tela, background="#C4C229")

    label_title = ctk.CTkLabel(left_frame, text=f"Selecione o ano que vai\nenfrentar {user_name}!!",
                               font=("Lucida Calligraphy", 46),
                               text_color="Black")
    label_title.pack(pady=20)

    first_year = ctk.CTkButton(left_frame, text="Anatomia I", corner_radius=23,
                               text_color="#C4C229", fg_color="#7A0D0D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2")

    first_year.pack(fill="x", padx=80, pady=(20, 10))

    first_year = ctk.CTkButton(left_frame, text="Anatomia II", corner_radius=23,
                               text_color="#C4C229", fg_color="#7A0D0D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2")

    first_year.pack(fill="x", padx=80, pady=(10, 10))

    first_year = ctk.CTkButton(left_frame, text="Histologia I", corner_radius=23,
                               text_color="#C4C229", fg_color="#7A0D0D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2")

    first_year.pack(fill="x", padx=80, pady=(10, 10))

    first_year = ctk.CTkButton(left_frame, text="Histologia II", corner_radius=23,
                               text_color="#C4C229", fg_color="#7A0D0D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2")

    first_year.pack(fill="x", padx=80, pady=(10, 10))

    first_year = ctk.CTkButton(left_frame, text="Bioquímica I", corner_radius=23,
                               text_color="#C4C229", fg_color="#7A0D0D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2")

    first_year.pack(fill="x", padx=80, pady=(10, 10))

    first_year = ctk.CTkButton(left_frame, text="Bioquímica II", corner_radius=23,
                               text_color="#C4C229", fg_color="#7A0D0D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2")

    first_year.pack(fill="x", padx=80, pady=(10, 10))

    first_year = ctk.CTkButton(left_frame, text="Medicina Comunitária I", corner_radius=23,
                               text_color="#C4C229", fg_color="#7A0D0D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2")

    first_year.pack(fill="x", padx=80, pady=(20, 30))

    left_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1)

    right_frame = Frame(tela, background="#2E487D")

    label_img = Label(right_frame, image=Third_year_template)
    label_img.place(x=0, y=0, relwidth=1, relheight=1)

    right_frame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)


def Fourth_year_panel():

    clear_screen()

    button_clicked_sound.play()

    left_frame = Frame(tela, background="#C4C229")

    label_title = ctk.CTkLabel(left_frame, text=f"Selecione o ano que vai\nenfrentar {user_name}!!",
                               font=("Lucida Calligraphy", 46),
                               text_color="Black")
    label_title.pack(pady=20)

    first_year = ctk.CTkButton(left_frame, text="Anatomia I", corner_radius=23,
                               text_color="#C4C229", fg_color="#7A0D0D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2")

    first_year.pack(fill="x", padx=80, pady=(20, 10))

    first_year = ctk.CTkButton(left_frame, text="Anatomia II", corner_radius=23,
                               text_color="#C4C229", fg_color="#7A0D0D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2")

    first_year.pack(fill="x", padx=80, pady=(10, 10))

    first_year = ctk.CTkButton(left_frame, text="Histologia I", corner_radius=23,
                               text_color="#C4C229", fg_color="#7A0D0D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2")

    first_year.pack(fill="x", padx=80, pady=(10, 10))

    first_year = ctk.CTkButton(left_frame, text="Histologia II", corner_radius=23,
                               text_color="#C4C229", fg_color="#7A0D0D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2")

    first_year.pack(fill="x", padx=80, pady=(10, 10))

    first_year = ctk.CTkButton(left_frame, text="Bioquímica I", corner_radius=23,
                               text_color="#C4C229", fg_color="#7A0D0D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2")

    first_year.pack(fill="x", padx=80, pady=(10, 10))

    first_year = ctk.CTkButton(left_frame, text="Bioquímica II", corner_radius=23,
                               text_color="#C4C229", fg_color="#7A0D0D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2")

    first_year.pack(fill="x", padx=80, pady=(10, 10))

    first_year = ctk.CTkButton(left_frame, text="Medicina Comunitária I", corner_radius=23,
                               text_color="#C4C229", fg_color="#7A0D0D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2",
                               command=dificulty_page)

    first_year.pack(fill="x", padx=80, pady=(20, 30))

    left_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1)

    right_frame = Frame(tela, background="#2E487D")

    label_img = Label(right_frame, image=Fourth_year_template)
    label_img.place(x=0, y=0, relwidth=1, relheight=1)

    right_frame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)


def Fifth_year_panel():

    clear_screen()

    button_clicked_sound.play()

    left_frame = Frame(tela, background="#C4C229")

    label_title = ctk.CTkLabel(left_frame, text=f"Selecione o ano que vai\nenfrentar {user_name}!!",
                               font=("Lucida Calligraphy", 46),
                               text_color="Black")
    label_title.pack(pady=20)

    first_year = ctk.CTkButton(left_frame, text="Anatomia I", corner_radius=23,
                               text_color="#C4C229", fg_color="#7A0D0D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2")

    first_year.pack(fill="x", padx=80, pady=(20, 10))

    first_year = ctk.CTkButton(left_frame, text="Anatomia II", corner_radius=23,
                               text_color="#C4C229", fg_color="#7A0D0D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2")

    first_year.pack(fill="x", padx=80, pady=(10, 10))

    first_year = ctk.CTkButton(left_frame, text="Histologia I", corner_radius=23,
                               text_color="#C4C229", fg_color="#7A0D0D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2")

    first_year.pack(fill="x", padx=80, pady=(10, 10))

    first_year = ctk.CTkButton(left_frame, text="Histologia II", corner_radius=23,
                               text_color="#C4C229", fg_color="#7A0D0D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2")

    first_year.pack(fill="x", padx=80, pady=(10, 10))

    first_year = ctk.CTkButton(left_frame, text="Bioquímica I", corner_radius=23,
                               text_color="#C4C229", fg_color="#7A0D0D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2")

    first_year.pack(fill="x", padx=80, pady=(10, 10))

    first_year = ctk.CTkButton(left_frame, text="Bioquímica II", corner_radius=23,
                               text_color="#C4C229", fg_color="#7A0D0D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2")

    first_year.pack(fill="x", padx=80, pady=(10, 10))

    first_year = ctk.CTkButton(left_frame, text="Medicina Comunitária I", corner_radius=23,
                               text_color="#C4C229", fg_color="#7A0D0D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2",
                               command=dificulty_page)

    first_year.pack(fill="x", padx=80, pady=(20, 30))

    left_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1)

    right_frame = Frame(tela, background="#2E487D")

    label_img = Label(right_frame, image=Fifth_year_template)
    label_img.place(x=0, y=0, relwidth=1, relheight=1)

    right_frame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)


def Sixth_year_panel():

    clear_screen()

    button_clicked_sound.play()

    left_frame = Frame(tela, background="#C4C229")

    label_title = ctk.CTkLabel(left_frame, text=f"Selecione o ano que vai\nenfrentar {user_name}!!",
                               font=("Lucida Calligraphy", 46),
                               text_color="Black")
    label_title.pack(pady=20)

    first_year = ctk.CTkButton(left_frame, text="Anatomia I", corner_radius=23,
                               text_color="#C4C229", fg_color="#7A0D0D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2")

    first_year.pack(fill="x", padx=80, pady=(20, 10))

    first_year = ctk.CTkButton(left_frame, text="Anatomia II", corner_radius=23,
                               text_color="#C4C229", fg_color="#7A0D0D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2")

    first_year.pack(fill="x", padx=80, pady=(10, 10))

    first_year = ctk.CTkButton(left_frame, text="Histologia I", corner_radius=23,
                               text_color="#C4C229", fg_color="#7A0D0D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2")

    first_year.pack(fill="x", padx=80, pady=(10, 10))

    first_year = ctk.CTkButton(left_frame, text="Histologia II", corner_radius=23,
                               text_color="#C4C229", fg_color="#7A0D0D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2")

    first_year.pack(fill="x", padx=80, pady=(10, 10))

    first_year = ctk.CTkButton(left_frame, text="Bioquímica I", corner_radius=23,
                               text_color="#C4C229", fg_color="#7A0D0D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2")

    first_year.pack(fill="x", padx=80, pady=(10, 10))

    first_year = ctk.CTkButton(left_frame, text="Bioquímica II", corner_radius=23,
                               text_color="#C4C229", fg_color="#7A0D0D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2")

    first_year.pack(fill="x", padx=80, pady=(10, 10))

    first_year = ctk.CTkButton(left_frame, text="Medicina Comunitária I", corner_radius=23,
                               text_color="#C4C229", fg_color="#7A0D0D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2",
                               command=dificulty_page)

    first_year.pack(fill="x", padx=80, pady=(20, 30))

    left_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1)

    right_frame = Frame(tela, background="#2E487D")

    label_img = Label(right_frame, image=Sixth_year_template)
    label_img.place(x=0, y=0, relwidth=1, relheight=1)

    right_frame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)


def Year_Picker():

    clear_screen()

    left_frame = Frame(tela, background="#C4C229")

    label_title = ctk.CTkLabel(left_frame, text=f"Selecione o ano que vai\nenfrentar {user_name}!!", font=("Lucida Calligraphy", 46),
                               text_color="Black")
    label_title.pack(pady=20)

    first_year = ctk.CTkButton(left_frame, text="1º Ano", corner_radius=23,
                        text_color="#D9D9D9", fg_color="#2E487D",
                        bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2", command=first_year_panel)

    first_year.pack(fill="x", padx=80, pady=(20, 10))

    Second_year = ctk.CTkButton(left_frame, text="2º Ano", corner_radius=23,
                               text_color="#D9D9D9", fg_color="#2E487D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2", command=Second_year_panel)

    Second_year.pack(fill="x", padx=80, pady=(10, 10))

    Third_year = ctk.CTkButton(left_frame, text="3º Ano", corner_radius=23,
                               text_color="#D9D9D9", fg_color="#2E487D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2", command=Third_year_panel)

    Third_year.pack(fill="x", padx=80, pady=(10, 10))

    Fourth_year = ctk.CTkButton(left_frame, text="4º Ano", corner_radius=23,
                               text_color="#D9D9D9", fg_color="#2E487D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2", command=Fourth_year_panel)

    Fourth_year.pack(fill="x", padx=80, pady=(10, 10))

    Fifth_year = ctk.CTkButton(left_frame, text="5º Ano", corner_radius=23,
                               text_color="#D9D9D9", fg_color="#2E487D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2", command=Fifth_year_panel)

    Fifth_year.pack(fill="x", padx=80, pady=(10, 10))

    Sixth_year = ctk.CTkButton(left_frame, text="6º Ano", corner_radius=23,
                               text_color="#D9D9D9", fg_color="#2E487D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2", command=Sixth_year_panel)

    Sixth_year.pack(fill="x", padx=80, pady=(10, 10))

    General_Questions_year = ctk.CTkButton(left_frame, text="Perguntas Gerais", corner_radius=23,
                               text_color="#D9D9D9", fg_color="#2E487D",
                               bg_color="#C4C229", font=(font_familly, 18), height=40, cursor="hand2", command= lambda : dificulty_page(Questions_root_deep))

    General_Questions_year.pack(fill="x", padx=80, pady=(20, 30))


    left_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1)




    right_frame = Frame(tela, background="#2E487D")

    label_img = Label(right_frame, image=first_year_lady_img)
    label_img.place(x=0, y=0, relwidth=1, relheight=1)

    right_frame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)


# Tela de Login!
def login_plate():

    global user_name

    clear_screen()

    button_clicked_sound.play()

    def validade_name(nome):

        global ok, user_name

        ok = True

        val_name = nome.split(" ")

        for válido in val_name:

            if válido.lower() in nomes_ínvalidos:
                ok = False
                messagebox.showinfo("Nome Inválido", f"Por favor!! diga um nome válido, '{nome}' não é um nome válido!!")
                break
            elif válido.lower() == "":
                ok = False
                messagebox.showinfo("Nome Inválido!! Campo de entrada vazio", f"Por favor!! preencha o campo de entrada com um nome decente")
                break

            elif len(nome) >= 14:
                ok = False
                messagebox.showinfo("Nome Inválido!! Nome demasiado longo",
                                    f"Por favor!! preencha o campo de Entrada com um nome inferior ou igual à 14 caracteres")
                break
            else:
                ok = True

        if (not ok):
            pass

        if nome == "brunox2003":
            nome = "Mestre Bruno"
            messagebox.showinfo("Mestre Reconhecido", "Seja muito bem-vindo mestre Bruno de Jesus Brás Araújo. Altas reverências meu mestre!!")

        # if len(val_name) == 0:
        #     messagebox.showinfo("Nome Invalido", "Por favor preencha o campo de entrada de nome para poder continuar!!")

        nome = nome.split(" ")
        temp_list_name = []
        new_name = ""
        for n in nome:
            if n in ("de", "da", "dos", "das"):
                temp_list_name.append(" " + n + " ")
            else:
                temp_list_name.append(n.capitalize())

        for n in temp_list_name:
            new_name += n + " "

        return new_name.rstrip(" ")

    def get_name():

        global user_name

        button_clicked_sound.play()

        user_name = str(user_name_entry.get())
        user_name_entry.delete(0, tkinter.END)
        user_name = validade_name(user_name)

        if ok:
            # Second_page(user_name)
            Year_Picker()

    left_frame = Frame(tela, background="#C4C229")

    label_title = ctk.CTkLabel(left_frame, text="Diga o seu nome \nDoctor!!", font=("Lucida Calligraphy", 50), text_color="Black")
    label_title.pack(pady = 20)

    label_user_img = ctk.CTkLabel(left_frame, text="", image=user_img)
    label_user_img.pack(pady = (30, 60))

    grid_frame_entry = ctk.CTkFrame(left_frame, fg_color="#D9D9D9", corner_radius=23, width=1600)

    user_name_entry = ctk.CTkEntry(grid_frame_entry, corner_radius=23, fg_color="#707341",
                                   border_color="#707341", font=(font_familly, 18), height=40)
    user_name_entry.insert(0, "Anônimo")
    user_name_entry.pack(fill="x", padx=20, pady=(30, 20))

    confirm_button = ctk.CTkButton(grid_frame_entry, text="Entrar!", corner_radius=23,
                        command=get_name, text_color="#D9D9D9", fg_color="#2E487D",
                        bg_color="#D9D9D9", font=(font_familly, 18), height=40)

    confirm_button.pack(fill="x", padx=20, pady=(20, 30))

    grid_frame_entry.pack(pady=(5, 30), fill = "x", padx = 180, ipadx = 30)

    left_frame.place(relx = 0, rely = 0, relwidth = 0.5, relheight = 1)

    tela.bind("<Return>", lambda event: get_name())


    right_frame = Frame(tela, background="#2E487D")

    label_img = Label(right_frame, image=bg_image_doctor)
    label_img.place(x=0, y=0, relwidth=1, relheight=1)

    right_frame.place(relx = 0.5, rely = 0, relwidth = 0.5, relheight = 1)


main_page()

# category_page(Questions_Anatomia_II)

tela.mainloop()
