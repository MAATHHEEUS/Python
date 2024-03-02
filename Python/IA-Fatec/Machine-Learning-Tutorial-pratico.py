# pelo longo
# perna curta
# faz auau
porco1 = [0, 1, 0]
porco2 = [0, 1, 1]
porco3 = [0, 0, 0]

dog1 = [0, 1, 1]
dog2 = [1, 0, 1]
dog3 = [1, 1, 1]

treino_x = [porco1, porco2, porco3, dog1, dog2, dog3]
treixo_y = [1, 1, 1, 0, 0, 0] # 0 = cachorro, 1 = porco

from sklearn.svm import LinearSVC

modelo = LinearSVC()
modelo.fit(treino_x, treixo_y)

animal_misterioso = [1, 1, 1]
modelo.predict([animal_misterioso])

misterio1 = [1, 1, 1]
misterio2 = [1, 1, 0]
misterio3 = [0, 1, 1]

teste_x = [misterio1, misterio2, misterio3]
teste_y = [0, 1, 1]

previsoes = modelo.predict(teste_x)
previsoes

from sklearn.metrics import accuracy_score

accuracy_score(teste_y, previsoes)