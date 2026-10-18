Estructura de las Variables Inyectadas
Monto_USD: Variable continua. Valor de la factura internacional.

Num_Items_Facturados: Variable discreta. Cantidad de productos o líneas arancelarias distintas en una sola factura.

Region_Destino: Variable categórica (LATAM, Europa, Asia).

Plataforma_Emision: Variable categórica (Sistema_Legacy, Sistema_Cloud). Diferencia entre el software viejo y la nueva nube.

Estado_Cumplimiento: Variable objetivo categórica/dicotómica (1 = Inconsistencia/Riesgo de multa, 0 = Factura correcta). Base para modelar con la distribución Binomial.

Guía del Docente (Storytelling y Solución de los Casos)
Este es el trasfondo analítico de cada dataset para la "Fase 6: Storytelling Estadístico" de tus estudiantes:

Dataset 1: Proceso Estable (Falso positivo para la compra de software)

Perfil: El proceso de facturación actual funciona bien. La probabilidad general de inconsistencia ronda el 5%.

Qué deben descubrir: Al calcular la probabilidad esperada en un lote de 15 documentos, verán que es muy raro encontrar 2 o más facturas con errores. Las estadísticas de las demás variables son homogéneas y no muestran correlaciones de riesgo.

Recomendación Financiera: No se justifica la millonaria inversión en un nuevo software de validación. La tasa de multas actual entra dentro del margen de riesgo operativo aceptable (es más barato pagar las raras multas que comprar el software).

Dataset 2: Alta Variabilidad (El problema está localizado)

Perfil: La tasa global de error parece manejable y engañosa si no se desglosa.

Qué deben descubrir: Al segmentar los errores (Estado = 1) mediante tablas cruzadas o un Diagrama de Pareto, los estudiantes encontrarán un pico crítico: las facturas enviadas a "Asia" procesadas por el "Sistema_Legacy" fallan más de la mitad de las veces (riesgo ~55%).

Recomendación Financiera: No es necesario comprar un software global. La recomendación debe ser auditar las reglas arancelarias de la región de Asia en el sistema antiguo, o migrar exclusivamente ese flujo de trabajo al Sistema Cloud.

Dataset 3: Complejidad Operativa (Fallo sistémico por volumen)

Perfil: Hay un número altísimo de multas y la varianza de la variable Num_Items_Facturados es muy alta.

Qué deben descubrir: Los estudiantes deben notar una fuerte correlación: a medida que el Num_Items_Facturados crece, el riesgo de que la factura sea catalogada como defectuosa (Estado = 1) se dispara casi al 90%. El proceso manual o el sistema actual colapsa cuando se manejan listas de empaque complejas.

Recomendación Financiera: El proceso actual no es seguro para grandes clientes. Si la empresa maneja volúmenes altos (muchos ítems por factura), es urgente la compra e integración del nuevo software de automatización, ya que el costo de las multas proyectadas excederá rápidamente la inversión tecnológica.