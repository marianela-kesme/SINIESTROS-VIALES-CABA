                      DATA ANALITICS
SINIESTROS VIALES EN CIUDAD AUTÓNOMA DE BUENOS AIRES


Python Pandas Numpy Matplotlib Seaborn Power BI GitHub Jupyter Visual Studio Code

Introducción
Los siniestros viales y sus trágicas consecuencias son una preocupación constante para las autoridades locales y la comunidad en general. La necesidad de tomar medidas efectivas para reducir la cantidad de víctimas fatales en las carreteras es imperativa. En este contexto, se propone la elaboración de un proyecto de análisis de datos destinado a proporcionar información valiosa que permita a las autoridades de la Ciudad Autónoma de Buenos Aires (CABA), tomar medidas específicas y basadas en datos para abordar este problema crítico de seguridad vial.

Objetivo
Recopilación y Análisis de Datos: Recolectar y analizar datos relacionados con siniestros viales, incluyendo ubicación, tipo de vehículo, víctimas, acusados, tipos de calle y otras variables relevantes.

Elaboración de KPI's: Desarrollar indicadores claves de rendimiento que nos permitan realizar un seguimiento de los puntos más relevantes para el analisis y la reducción de accidentes de tránsito.

Identificación de Patrones y Tendencias: Identificar patrones y tendencias en los datos que puedan ayudar a comprender mejor las causas y circunstancias de los siniestros viales.

Localización de Puntos Críticos: Identificar áreas geográficas con una alta incidencia de siniestros fatales y analizar las causas subyacentes.

Perfil de las Víctimas: Crear perfiles demográficos de las víctimas fatales, incluyendo edad, género y cualquier otra característica relevante.

Contexto
Los accidentes de tránsito, una de las primeras causas de muerte en el mundo no son azarosos ni responden a ningún fatalismo. Son siempre consecuencia de una cadena causal de eventos y circunstancias en las que nosotros, como sociedad, podemos intervenir para evitarlos. Los choques y colisiones presentan características relacionadas con factores humanos, mecánicos y climáticos.

En Argentina, cada año mueren cerca de 4.000 personas en siniestros viales. Aunque muchas jurisdicciones han logrado disminuir la cantidad de accidentes de tránsito, esta sigue siendo la principal causa de muertes violentas en el país. Los informes del Sistema Nacional de Información Criminal (SNIC), del Ministerio de Seguridad de la Nación, revelan que entre 2018 y 2022 se registraron 19.630 muertes en siniestros viales en todo el país. Estas cifras equivalen a 11 personas por día que resultaron víctimas fatales por accidentes de tránsito.

La Ciudad Autónoma de Buenos Aires, cuenta actualmenta según el censo 2022, con 3.120.612 habitantes.

Causas que contribuyen a los accidentes:

Incumplimiento de la Ley de Tránsito.
Exceso de velocidad.
No respetar las señales de tránsito.
No usar cinturón de seguridad o apoya cabezas.
Conducir con cansancio.
Viajar con niños en asiento delantero.
Ingerir alcohol y/u otros estimulantes.
Detener vehículos en lugares inapropiados.
Usar el teléfono celular mientras conducís.
Usar equipos de audio a alto volumen.
Falta de respeto de/a los ciclistas y motociclistas.
No usar casco.
Cruzar la calle sin mirar, por lugares inapropiados y sin respetar el semáforo.
No realizar el debido mantenimiento de tu vehículo.
Factores climáticos: niebla, lluvia, granizo, vientos.
Dejamos a disposición del lector, la siguiente guía práctica la cual tiene como objetivo brindar información básica sobre cómo actuar ante la ocurrencia de un siniestro vial. Dicho documento es suministrado por el gobierno de la Ciudad de Buenos Aires.

Datasets
Para la realización del proyecto, nos disponibilizan un dataset sobre homicidios en siniestros viales acaecidos en la Ciudad de Buenos Aires durante el periodo 2016-2021. El dataset original se encuentra en el siguiente link.

Este dataset contiene dos hojas llamadas: hechos y víctimas.

Asimismo, se incluye un documento que sirve de guía para un mayor entendimiento de la data analizada. Dicho documento se encuentra en el siguiente link.

Herramientas utilizadas
Para el desarrollo del proyecto utilizamos distintas herramientas las que incluyen:

ETL y análisis de datos:

Python
Pandas
MatplotLib
Seaborn
Visualización de datos y Dashboard:

PowerBI
NovyPro (en este link se encuentra el tablero desarrollado) EN DESARROLLO
Análisis exploratorio de datos (EDA)
El análisis exploratorio se divide en dos, uno para la tabla de hechos y otro para la tabla de victimas.

El mismo consiste en los siguientes pasos:

Ingesta de datos: se importan librerias y se leen los datos a trabajar.

Inspección preliminar: se analiza el dataset correspondiente con el objetivo de interpretar que información tenemos, la calidad de sus datos, entre otras cosas.

Duplicados: se busca la existencia de registros duplicados y se decide que hacer con ellos.

Valores faltantes: al igual que con los duplicados, buscamos valores faltantes y determianamos como vamos a trabajar con ellos.

Outliers: se rastrea dentro de los datasets, la posible existencia de outliers con el objetivo de eliminarlos si fuera necesario y que eso no altere la calidad del análisis.

Gráficos (variables cuantitativas): se identifican las variables numéricas y se busca correlación entre ellas para evitar sesgamientos e inconsistencias. Además, se analiza la distribución de las mismas mediante la utilización de gráficos con el objetivo de identificar tendencias y comportamientos en los datos que puedan ser de utilidad para el análisis posterior y la creación del dashboard.

Gráficos (variables cualitativas): de las misma manera que con las variables cuantitativas, analizamos las variables categóricas con el mismo objetivo que el anterior.

Creación CSV: disponibilizamos un archivo CSV para usar de base en la creación del dashboard.

La información detallada del paso a paso realizado se encuentra en los siguientes enlaces: EDA Hechos y EDA Victimas

Observaciones generales de los datos
Hechos

En su gran mayoría, aproximadamente el 97% de los casos, los siniestros viales resultan en una sola víctima fatal, mientras que los casos con 2 o 3 homicidios son notoriamente menos frecuentes.

El año 2016 registró la mayor cantidad de siniestros, con valores similares a los años 2017 y 2018. A partir de 2019, hubo una disminución significativa debido a la pandemia, que redujo el tráfico y la cantidad de accidentes.

Diciembre es el mes con más siniestros, probablemente debido al aumento del tráfico durante las festividades de fin de año.

Se observa un pico de siniestros en las primeras horas de la mañana, relacionado con los horarios laborales y la congestión del tráfico. También se nota un aumento después de las 13, cuando las personas regresan del trabajo.

Los siniestros son más frecuentes en avenidas debido al mayor tráfico, velocidad promedio, intersecciones complejas y concentración de actividades.

Los siniestros más comunes involucran a peatones y pasajeros de transporte público, como colectivos. En la Ciudad Autónoma de Buenos Aires, hay actualmente 137 líneas de colectivos, 33 de las cuales operan completamente en la ciudad.

Las víctimas más frecuentes de estos siniestros son motociclistas y peatones, lo que se relaciona con la alta cantidad de motos y el tráfico en la ciudad.

Autos y colectivos de pasajeros son los vehículos más frecuentemente acusados en los siniestros viales, posiblemente debido a su mayor número y tamaño.

Las comunas 1, 4, 7, 8 y 9 son las que experimentan el mayor volumen de siniestros viales en la Ciudad Autónoma de Buenos Aires.

Víctimas

La edad más común de las víctimas se encuentra en el rango de 20 a 40 años, posiblemente relacionado con la edad mínima para obtener una licencia de conducir. La cantidad de víctimas disminuye en edades superiores a 40 años.

Antes de la pandemia, hubo un nivel constante de víctimas en los años anteriores, pero después de la aparición de la pandemia y el bloqueo, disminuyeron los accidentes y las víctimas.

La mayoría de las víctimas fatales son conductores, seguidos por peatones en términos de roles involucrados en los siniestros.

Entre los conductores que resultan víctimas, destacan los motociclistas seguidos por los conductores de automóviles, que suman el 80% de los casos.

En aproximadamente el 76% de los casos, las víctimas fatales son hombres, con un porcentaje mucho menor de mujeres.

En los accidentes donde la víctima es el conductor, en su mayoría, el sexo del conductor es masculino.

Indicadores de rendimiento clave (KPI)
Se proponen 3 indicadores claves, determinados a partir del analísis y la intepretación realizada en el punto anterior.

Reducir en un 10% la tasa de homicidios en siniestros viales de los últimos seis meses, en CABA, en comparación con la tasa de homicidios en siniestros viales del semestre anterior

Definimos a la tasa de homicidios en siniestros viales como el número de víctimas fatales en accidentes de tránsito por cada 100,000 habitantes en un área geográfica durante un período de tiempo específico. Su fórmula es: (Número de homicidios en siniestros viales / Población total) * 100,000

Nro de homicidios: obtenido del dataset hechos.

Población total: se decidió utilizar la población del censo 2022.

Este KPI nos permite comparar la tasa de homicidios de un semestre específico contra el semestre inmediatamente anterior. Se definió la reducción como un valor positivo. Esto quiere decir que si el KPI nos da un valor mayor que 0, se debe a que el semestre actual disminuyó la cantidad de homidicios en comparación con el anterior. Si esa disminución es mayor que el 10%, entonces se concluye que el objetivo está cumplido. Podemos observar además, que tan cerca o que tan lejos del objetivo se encuentra la situación del semestre actual vs el anterior.

Reducir en un 7% la cantidad de accidentes mortales de motociclistas en el último año, en CABA, respecto al año anterior

Definimos a la cantidad de accidentes mortales de motociclistas en siniestros viales como el número absoluto de accidentes fatales en los que estuvieron involucradas víctimas que viajaban en moto en un determinado periodo temporal. Su fórmula para medir la evolución de los accidentes mortales con víctimas en moto es: (Número de accidentes mortales con víctimas en moto en el año anterior - Número de accidentes mortales con víctimas en moto en el año actual) / (Número de accidentes mortales con víctimas en moto en el año anterior) * 100

Cantidad de accidentes mortales de motociclistas: obtenido del dataset hechos, filtrando las victimas por "MOTO".

Este KPI nos permite comparar la cantidad de accidentes mortales en motocicleta de un año específico contra el año inmediatamente anterior. Se definió la reducción como un valor positivo. Esto quiere decir que si el KPI nos da un valor mayor que 0, se debe a que el año actual disminuyó la cantidad de accidentes mortales en motocicleta en comparación con el año anterior. Si esa disminución es mayor que el 7%, entonces se concluye que el objetivo está cumplido. De la misma manera que en el KPI anterior, podemos observar que tan cerca o que tan lejos del objetivo se encuentra la situación del año actual vs el anterior.

Reducir en un 10% la cantidad de accidentes mortales de PEATONES en el último año, en CABA, respecto al año anterior.

KPI

Conclusiones generales
A partir de las observaciones y datos presentados en el análisis de siniestros viales, se pueden extraer varias conclusiones importantes. Estas conclusiones proporcionan una visión integral de la situación y pueden ser fundamentales para la toma de decisiones y la formulación de políticas orientadas a mejorar la seguridad vial en la Ciudad Autónoma de Buenos Aires:

Perfil de los Siniestros Viales: Los siniestros viales con una sola víctima fatal son abrumadoramente predominantes, representando aproximadamente el 97% de los casos. Esto sugiere que la mayoría de los incidentes son de naturaleza no múltiple y, por lo tanto, pueden estar relacionados con factores individuales o comportamientos del conductor.

Impacto de la Pandemia: El año 2016 marcó el pico en la cantidad de siniestros, pero a partir de 2019, con el inicio de la pandemia, se observa una disminución significativa. La relación directa entre la pandemia, el bloqueo y la reducción del tráfico en las calles es evidente, lo que indica que las medidas de confinamiento tuvieron un impacto positivo en la reducción de siniestros.

Temporalidad y Siniestros: Diciembre es el mes con más siniestros, lo que sugiere una correlación con las festividades de fin de año y el aumento del tráfico durante este período. Este hallazgo puede respaldar la necesidad de medidas de seguridad específicas durante las festividades.

Patrones de Horarios: Lo concluido durante el analisis sugiere la importancia de gestionar y regular el tráfico durante las horas críticas.

Ubicación de los Siniestros: se concluye que existe una urgente necesidad de enfocar los esfuerzos de control y regulación sobre avenidas.

Tipo de Vehículo: Las motocicletas son los vehículos más frecuentemente involucrados en siniestros, seguidas por los automóviles. Esto refuerza la necesidad de medidas específicas para mejorar la seguridad de los motociclistas y reducir los accidentes que involucran automóviles.

Distribución Geográfica: Las comunas 1, 4, 7, 8 y 9 tienen un mayor volumen de siniestros viales en la Ciudad Autónoma de Buenos Aires. Esto destaca la importancia de la focalización de esfuerzos y recursos en estas áreas concretas para abordar el problema de manera efectiva.

Estas conclusiones respaldan la necesidad de políticas y acciones concretas orientadas a mejorar la seguridad vial en la Ciudad Autónoma de Buenos Aires, teniendo en cuenta factores como la temporalidad, la ubicación, los roles de los involucrados y las edades de las víctimas. La recopilación y el análisis de datos son herramientas fundamentales para identificar el problema y generar soluciones a la problematica.
