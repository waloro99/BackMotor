import pandas as pd
import numpy as np

def recomend(review): 
     #obtener el data frame de la informacion del archivo csv
    df = pd.Cov = pd.read_csv("./data/uploaded_file.csv", header=None)
    df.columns = ["ID", "movie_title", "color", "plot_keywords", "genres", "director_name", "num_critic_for_reviews" , "actor_1_name", "actor_2_name", "imdb_score", "title_year"]
    max_review = df["num_critic_for_reviews"].max()
    df["popularity"] = ((df["num_critic_for_reviews"]/max_review)) * (df["imdb_score"])
    df["popularity"] = (df['popularity']-df['popularity'].min())/(df['popularity'].max()-df['popularity'].min())
    df["title_year"] = df["title_year"].fillna(0)
    #crear tabla que contenga los id y prob para recomendar
    recome_peli = {}
    for i in df.index:
        k = str(df['ID'][i])
        v = 0
        recome_peli[k] = v

    # Obtener los gustos del usuario
    color = []
    color_no = []
    keywords = []
    keywords_no = []
    generos = []
    generos_no = []
    director = []
    director_no = []
    actor1 = []
    actor1_no = []
    actor2 = []
    actor2_no = []
    year = []
    year_no = []

    def gustos_usu(gustos):
        for value in gustos:
            liked = value["liked"]
            movie = value["movie"]
            data_peli = df.loc[df['ID'] == movie]
            if liked == True:
                if str(data_peli['color'].values[0])  != "nan":
                    color.append(data_peli['color'].values[0])
                if str(data_peli['plot_keywords'].values[0])  != "nan":
                    for value in data_peli['plot_keywords'].values[0].split('|'):
                        keywords.append(value)
                if str(data_peli['genres'].values[0])  != "nan":
                    for value in data_peli['genres'].values[0].split('|'):
                        generos.append(value)
                if str(data_peli['director_name'].values[0])  != "nan":
                    director.append(data_peli['director_name'].values[0])
                if str(data_peli['actor_1_name'].values[0])  != "nan":
                    actor1.append(data_peli['actor_1_name'].values[0])
                if str(data_peli['actor_2_name'].values[0])  != "nan":
                    actor2.append(data_peli['actor_2_name'].values[0])
                if str(data_peli['title_year'].values[0])  != "nan":
                    year.append(data_peli['title_year'].values[0])
            else:
                if str(data_peli['color'].values[0])  != "nan":
                    color_no.append(data_peli['color'].values[0])
                if str(data_peli['plot_keywords'].values[0])  != "nan":
                    for value in data_peli['plot_keywords'].values[0].split('|'):
                        keywords_no.append(value)
                if str(data_peli['genres'].values[0])  != "nan":
                    for value in data_peli['genres'].values[0].split('|'):
                        generos_no.append(value)
                if str(data_peli['director_name'].values[0])  != "nan":
                    director_no.append(data_peli['director_name'].values[0])
                if str(data_peli['actor_1_name'].values[0])  != "nan":
                    actor1_no.append(data_peli['actor_1_name'].values[0])
                if str(data_peli['actor_2_name'].values[0])  != "nan":
                    actor2_no.append(data_peli['actor_2_name'].values[0])
                if str(data_peli['title_year'].values[0])  != "nan":
                    year_no.append(data_peli['title_year'].values[0])

    gustos_usu(review)
    # Metodo para campos con varios valores
    # Funcion que sirve para obtener la frecuencia de todos los valores [ej: 'Comedy':1000 , 'Action':200 , ...]
    def crear_tabla_frecuencias(parametro):
        frecuencias = {}
        for item in parametro:
            if str(item)  != "nan":
                for token in item:
                    if token not in frecuencias.keys():
                        frecuencias[token] = 1
                    else:
                        frecuencias[token] += 1
        return frecuencias 

    # Funcion que sirve para obtener la cantidad total de datos que vienen en el campo [ej: 1000]
    def contar_palabras(corpus):
        frecuencia = 0
        for oracion in corpus:
            if str(oracion)  != "nan":
                frecuencia += len(oracion)
        return frecuencia

    # Funcion que sirve para obtener la frecuencia individual si le gusta o no le gusta el valor del campo segun sus gustos [ej: le_gusta { 'Comedy':2 }]
    def obtener_gustos(generos,frecuencia):
        frecuencia_nueva = {}
        for k,v in frecuencia.items():
            frecuencia_nueva[k] = 0
        for genero in generos:
            frecuencia_nueva[genero] =+ 1
        return frecuencia_nueva

    # Funcion que sirve para transformar el valor de frecuencia en probabilidad [ej: 'Comedy': 0.00051231]
    def transformar_frecuencia_probabilidad(frecuencias, total):
        cpt_equivalente = {}
        for k,v in frecuencias.items():
            if v == 0:
                probabilidad = 0.0001
            else:
                probabilidad = v / total[k]
            cpt_equivalente[k] = probabilidad
        return cpt_equivalente

    # Funcion que sirve para Naive Bayes para obtener probabilidad de que tanto le gusta [ej: P(le guste | generos que le gustan)]
    def obtener_prob_gustos(valores,cpt_le_gusta,cpt_no_le_gusta,p_gusta,p_no_gusta):
        genero_le_gusta = 1
        genero_no_le_gusta = 1
        for valor in valores[0].split("|"):
            if str(valor)  != "nan":
                genero_le_gusta *= cpt_le_gusta[valor]     
                genero_no_le_gusta *= cpt_no_le_gusta[valor] 
        prob_genero = (p_gusta * genero_le_gusta) / (p_gusta * genero_le_gusta + p_no_gusta * genero_no_le_gusta)
        return prob_genero

    # Funcion que sirve para Naive Bayes para obtener probabilidad de que tanto le gusta [ej: P(le guste | generos que le gustan)]
    def obtener_prob_gustos_year(valores,cpt_le_gusta,cpt_no_le_gusta,p_gusta,p_no_gusta):
        genero_le_gusta = 1
        genero_no_le_gusta = 1
        for valor in valores:
            genero_le_gusta *= cpt_le_gusta[valor]     
            genero_no_le_gusta *= cpt_no_le_gusta[valor] 
        prob_genero = (p_gusta * genero_le_gusta) / (p_gusta * genero_le_gusta + p_no_gusta * genero_no_le_gusta)
        return prob_genero

    # Funcion que sirve para obtener el peso del campo respecto a una pelicula
    def peso_campo(le_gusta,peso):
        probabilidad = (le_gusta * peso ) * 100
        return probabilidad

    # Metodo para campos con unico valor

    # Funcion que sirve para obtener la frecuencia de todos los valores [ej: 'Comedy':1000 , 'Action':200 , ...]
    def crear_tabla_frecuencias_unica(parametro):
        frecuencias = {}
        if str(parametro)  != "nan":
            for token in parametro:
                if token not in frecuencias.keys():
                    frecuencias[token] = 1
                else:
                    frecuencias[token] += 1
        return frecuencias 

    # Funcion que sirve para obtener la cantidad total de datos que vienen en el campo [ej: 1000]
    def contar_palabras_unica(corpus):
        frecuencia = 0
        for oracion in corpus:
            if str(oracion)  != "nan":
                frecuencia += len(oracion)
        return frecuencia

    #Probabilidad con campo color
    frecuencia_total_color = crear_tabla_frecuencias_unica(df['color'])
    total_color = contar_palabras_unica(df['color'])
    frecuencia_le_gusta_color = obtener_gustos(color,frecuencia_total_color)
    frecuencia_no_le_gusta_color = obtener_gustos(color_no,frecuencia_total_color)
    p_color = len(color) / len(frecuencia_total_color.keys())
    p_no_color = len(color_no) / len(frecuencia_total_color.keys())
    cpt_color_le_gusta = transformar_frecuencia_probabilidad(frecuencia_le_gusta_color, frecuencia_total_color)
    cpt_color_no_le_gusta = transformar_frecuencia_probabilidad(frecuencia_no_le_gusta_color, frecuencia_total_color)

    #Probabilidad con campo plot_keywords
    frecuencia_total_keywords = crear_tabla_frecuencias(df['plot_keywords'].str.split("|"))
    total_keywords = contar_palabras(df['plot_keywords'].str.split("|"))
    frecuencia_le_gusta_keywords = obtener_gustos(keywords,frecuencia_total_keywords)
    frecuencia_no_le_gusta_keywords = obtener_gustos(keywords_no,frecuencia_total_keywords)
    p_keywords = len(keywords) / len(frecuencia_total_keywords.keys())
    p_no_keywords = len(keywords_no) / len(frecuencia_total_keywords.keys())
    cpt_keywords_le_gusta = transformar_frecuencia_probabilidad(frecuencia_le_gusta_keywords, frecuencia_total_keywords)
    cpt_keywords_no_le_gusta = transformar_frecuencia_probabilidad(frecuencia_no_le_gusta_keywords, frecuencia_total_keywords)

    #Probabilidad con campo genero
    frecuencia_total_genero = crear_tabla_frecuencias(df['genres'].str.split("|"))
    total_genero = contar_palabras(df['genres'].str.split("|"))
    frecuencia_le_gusta_genero = obtener_gustos(generos,frecuencia_total_genero)
    frecuencia_no_le_gusta_genero = obtener_gustos(generos_no,frecuencia_total_genero)
    p_generos = len(generos) / len(frecuencia_total_genero.keys())
    p_no_generos = len(generos_no) / len(frecuencia_total_genero.keys())
    cpt_genero_le_gusta = transformar_frecuencia_probabilidad(frecuencia_le_gusta_genero, frecuencia_total_genero)
    cpt_genero_no_le_gusta = transformar_frecuencia_probabilidad(frecuencia_no_le_gusta_genero, frecuencia_total_genero)

    #Probabilidad con campo director_name
    frecuencia_total_director = crear_tabla_frecuencias_unica(df['director_name'])
    total_director = contar_palabras_unica(df['director_name'])
    frecuencia_le_gusta_director = obtener_gustos(director,frecuencia_total_director)
    frecuencia_no_le_gusta_director = obtener_gustos(director_no,frecuencia_total_director)
    p_director = len(director) / len(frecuencia_total_director.keys())
    p_no_director = len(director_no) / len(frecuencia_total_director.keys())
    cpt_director_le_gusta = transformar_frecuencia_probabilidad(frecuencia_le_gusta_director, frecuencia_total_director)
    cpt_director_no_le_gusta = transformar_frecuencia_probabilidad(frecuencia_no_le_gusta_director, frecuencia_total_director)

    #Probabilidad con campo actor_1_name
    frecuencia_total_actor1 = crear_tabla_frecuencias_unica(df['actor_1_name'])
    total_actor1 = contar_palabras_unica(df['actor_1_name'])
    frecuencia_le_gusta_actor1 = obtener_gustos(actor1,frecuencia_total_actor1)
    frecuencia_no_le_gusta_actor1 = obtener_gustos(actor1_no,frecuencia_total_actor1)
    p_actor1 = len(actor1) / len(frecuencia_total_actor1.keys())
    p_no_actor1 = len(actor1_no) / len(frecuencia_total_actor1.keys())
    cpt_actor1_le_gusta = transformar_frecuencia_probabilidad(frecuencia_le_gusta_actor1, frecuencia_total_actor1)
    cpt_actor1_no_le_gusta = transformar_frecuencia_probabilidad(frecuencia_no_le_gusta_actor1, frecuencia_total_actor1)

    #Probabilidad con campo actor_2_name
    frecuencia_total_actor2 = crear_tabla_frecuencias_unica(df['actor_2_name'])
    total_actor2 = contar_palabras_unica(df['actor_2_name'])
    frecuencia_le_gusta_actor2 = obtener_gustos(actor2,frecuencia_total_actor2)
    frecuencia_no_le_gusta_actor2 = obtener_gustos(actor2_no,frecuencia_total_actor2)
    p_actor2 = len(actor2) / len(frecuencia_total_actor2.keys())
    p_no_actor2 = len(actor2_no) / len(frecuencia_total_actor2.keys())
    cpt_actor2_le_gusta = transformar_frecuencia_probabilidad(frecuencia_le_gusta_actor2, frecuencia_total_actor2)
    cpt_actor2_no_le_gusta = transformar_frecuencia_probabilidad(frecuencia_no_le_gusta_actor2, frecuencia_total_actor2)

    #Probabilidad con campo title_year
    frecuencia_total_year = crear_tabla_frecuencias_unica(df['title_year'])
    frecuencia_le_gusta_year = obtener_gustos(year,frecuencia_total_year)
    frecuencia_no_le_gusta_year = obtener_gustos(year_no,frecuencia_total_year)
    p_year= len(year) / len(frecuencia_total_year.keys())
    p_no_year = len(year_no) / len(frecuencia_total_year.keys())
    cpt_year_le_gusta = transformar_frecuencia_probabilidad(frecuencia_le_gusta_year, frecuencia_total_year)
    cpt_year_no_le_gusta = transformar_frecuencia_probabilidad(frecuencia_no_le_gusta_year, frecuencia_total_year)

    #ciclo para obtener pelicula por pelicula
    def obtener_peli(recomendarpeli , data):
        for i in data.index:
            prob = 0
            prob = definir_prob(str(data["color"][i]),str(data["plot_keywords"][i]),str(data["genres"][i]),str(data["director_name"][i]),str(data["actor_1_name"][i]),str(data["actor_2_name"][i]),data["title_year"][i],data["popularity"][i])
            recome_peli[str(data["ID"][i])] = prob
            
        top_peliculas = []
        import operator
        top_peliculas = sorted(recomendarpeli.items(), key=operator.itemgetter(1), reverse=True)
        return top_peliculas

    #--------------------- Hacer un ciclo para ir obteniendo 1 por 1 las peliculas y su prob para agregarla a todos lo campos y luego a la tabla final
    def definir_prob(color,keywords,genero,director,actor1,actor2,year,popularity):
        #Prob de que guste la pelicula de color - pelicula 1 por 1
        p_color_leguste = obtener_prob_gustos([color],cpt_color_le_gusta,cpt_color_no_le_gusta,p_color,p_no_color)
        pf_color =  peso_campo(p_color_leguste,0.05)

        #Prob de que guste la pelicula de palabras clave - pelicula 1 por 1
        p_keywords_leguste = obtener_prob_gustos([keywords],cpt_keywords_le_gusta,cpt_keywords_no_le_gusta,p_keywords,p_no_keywords)
        pf_keywords =  peso_campo(p_keywords_leguste,0.20)

        #Prob de que guste la pelicula de accion - pelicula 1 por 1
        p_genero_leguste = obtener_prob_gustos([genero],cpt_genero_le_gusta,cpt_genero_no_le_gusta,p_generos,p_no_generos)
        pf_genres =  peso_campo(p_genero_leguste,0.35)

        #Prob de que guste la pelicula de director - pelicula 1 por 1
        p_director_leguste = obtener_prob_gustos([director],cpt_director_le_gusta,cpt_director_no_le_gusta,p_director,p_no_director)
        pf_director =  peso_campo(p_director_leguste,0.10)

        #Prob de que guste la pelicula de actor1 - pelicula 1 por 1
        p_actor1_leguste = obtener_prob_gustos([actor1],cpt_actor1_le_gusta,cpt_actor1_no_le_gusta,p_actor1,p_no_actor1)
        pf_actor1 =  peso_campo(p_actor1_leguste,0.10)

        #Prob de que guste la pelicula de actor2 - pelicula 1 por 1
        p_actor2_leguste = obtener_prob_gustos([actor2],cpt_actor2_le_gusta,cpt_actor2_no_le_gusta,p_actor2,p_no_actor2)
        pf_actor2 =  peso_campo(p_actor2_leguste,0.09)

        #Prob de que guste la pelicula de cierto año - pelicula 1 por 1
        p_year_leguste = obtener_prob_gustos_year([year],cpt_year_le_gusta,cpt_year_no_le_gusta,p_year,p_no_year)
        pf_year =  peso_campo(p_year_leguste,0.01)
        
        res = suma_prob(pf_color,pf_keywords,pf_genres,pf_director,pf_actor1,pf_actor2,pf_year,popularity)
        return res

    #sumatoria de todas las probabilidades de cada columna
    def suma_prob(color, keywords, genres, director, actor1, actor2, year, popularity):
        # score = 0.05 + critic = 0.05 = 0.10
        popu = popularity * 0.10
        res = color + keywords + genres + director + actor1 + actor2 + year + popu
        if np.isnan(res):
            res = 1
        return res

    peliculas_final = obtener_peli(recome_peli,df)

    return peliculas_final


def getDefaultTop10():
    df = pd.Cov = pd.read_csv("./data/uploaded_file.csv", header=None)
    df.columns = ["ID", "movie_title", "color", "plot_keywords", "genres", "director_name", "num_critic_for_reviews" , "actor_1_name", "actor_2_name", "imdb_score", "title_year"]
    return df[['ID', 'imdb_score']].sort_values(by='imdb_score', ascending=False).head(10)["ID"].to_list()