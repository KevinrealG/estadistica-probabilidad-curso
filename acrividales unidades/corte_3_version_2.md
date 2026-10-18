Estructura de las Variables Inyectadas
Para enriquecer el análisis descriptivo y probabilístico (como indica el skill), se han incluido las siguientes variables:

Tiempo_Fijacion_Visual_s: Variable continua (Métrica de Eye-Tracking). Segundos que el participante miró directamente el producto o logo.

Num_Menciones_Competencia: Variable discreta. Cuántas veces el sujeto mencionó a una marca rival durante la entrevista.

Segmento_Edad: Variable categórica (Joven / Adulto).

Dispositivo: Variable categórica (Movil / PC).

Estado_Recuerdo: Variable objetivo categórica/dicotómica (1 = Éxito/Recuerda, 0 = Fracaso/No recuerda), ideal para modelar con la Distribución Binomial.

Guía del Docente (Storytelling y Solución de los Casos)
Aquí tienes el "secreto" detrás de cada dataset para guiar la Fase de Análisis Descriptivo y la Fase 6 de Storytelling de tus estudiantes:

Dataset 1: Campaña Estable (El escenario ideal)

Perfil: El anuncio funciona perfectamente. La probabilidad de éxito (recuerdo) global ronda el 75%.

Qué deben descubrir los estudiantes: Al calcular el p de la muestra, les dará alto. Las medidas de tendencia central del tiempo de fijación visual están estables (~15 segundos) en todos los segmentos (Jóvenes, Adultos, Móvil, PC). Es el dataset ideal para predecir probabilidades muy positivas en los Focus Groups usando la Distribución Binomial.

Dataset 2: Falla de UX (Alta variabilidad por segmento)

Perfil: La tasa de recuerdo global bajará engañosamente a cerca del 50-60%.

Qué deben descubrir los estudiantes: Si solo sacan la media general, se perderán el problema. Si cruzan Estado_Recuerdo o Tiempo_Fijacion_Visual_s por Segmento_Edad y Dispositivo (usando tablas dinámicas o gráficos de barras agrupadas), descubrirán que los Adultos que vieron el anuncio en un Móvil tienen tiempos de atención bajísimos (~5 segundos) y un recuerdo casi nulo (15%).

Recomendación Ejecutiva (Fase 6): El anuncio no se adapta bien a pantallas pequeñas para personas mayores (texto pequeño, botones confusos). Se requiere rediseño responsivo, no cambiar la idea central.

Dataset 3: "El Efecto Vampiro" (Sesgo sistemático y distracción)

Perfil: La campaña es un fracaso en recuerdo de marca (éxito < 30%), a pesar de que el anuncio captura mucho la atención.

Qué deben descubrir los estudiantes: Notarán que el Tiempo_Fijacion_Visual_s es el más alto de los tres datasets (~18 segundos), pero la variable Num_Menciones_Competencia se dispara (media > 3). Al correlacionar, verán que a mayor mención de la competencia, menor es el recuerdo de nuestra marca (Estado = 0).

Recomendación Ejecutiva (Fase 6): En psicología publicitaria esto se llama "Efecto Vampiro". El anuncio tiene un elemento (un actor famoso, una canción pegajosa, o un chiste) que "chupa" toda la atención cognitiva del espectador, haciendo que olviden qué marca les está hablando, e incluso confundiendo el anuncio con el de la competencia. ¡No se debe lanzar a nivel nacional sin cambiar el enfoque!