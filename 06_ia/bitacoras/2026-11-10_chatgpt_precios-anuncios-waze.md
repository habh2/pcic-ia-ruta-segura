# Precios de anuncios en Waze

Herramienta: ChatGPT. Fecha: 2026-11-10.

Enlace público: https://chatgpt.com/share/6af3b553-c820-83e8-b292-e6341a7a9347

## Conversación completa

```text
Costo de anuncios Waze
======================

Tú:
cuanto cobra waze a los negocios por impresiones visibilidad

ChatGPT:
Voy a revisar las tarifas actuales de Waze Ads y si en México cobran por impresiones, clics o mediante un presupuesto de campaña.

ChatGPT:
Actualmente, en México (noviembre de 2026), Waze no publica una tarifa fija por impresión. La publicidad se gestiona mediante Google Ads, utilizando campañas de Máximo rendimiento (Performance Max) orientadas a visitas a negocios físicos. 
Sin embargo, existen referencias de precios por cada 1,000 impresiones (CPM) en México.
1. ¿Cuánto cuesta anunciarse en Waze?
Encontré un contrato público de la Ciudad de México de 2024 que incluye estas tarifas históricas:



Tipo de anuncio
CPM sin IVA
CPM con IVA



Pin Rich (ubicación destacada)
$105 MXN
$121.80 MXN


Arrow (flecha promocional)
$160 MXN
$185.60 MXN


Rich Takeover (banner)
$485 MXN
$562.60 MXN


Fuente: Contrato público de publicidad digital, CDMX, 2024. Son precios de referencia de un contrato, no tarifas oficiales vigentes de Waze.
2. ¿Cuánto costarían diferentes cantidades de impresiones?
Tomando como referencia el CPM histórico de $105 MXN para pines promocionados, sin IVA:



Impresiones
Costo estimado



1,000
$105


10,000
$1,050


50,000
$5,250


100,000
$10,500


500,000
$52,500


1,000,000
$105,000


{@body const [imps,setImps] = DIL.useState(10000)}
{@body const fmt = n => new Intl.NumberFormat("es-MX",{style:"currency",currency:"MXN",maximumFractionDigits:0}).format(n)}

  Simulador de costos por impresiones
  
    Impresiones
    {imps.toLocaleString("es-MX")}
  
  
  
    
      Costo sin IVA
      
    
    
      Costo con IVA
      
    
  
  Simulación con el CPM histórico de Pin Rich; no es una cotización actual.

3. ¿Cómo cobra Waze actualmente?
Desde su integración con Google Ads, el modelo cambió:

Los negocios pueden aparecer mediante pines promocionados en las rutas de los conductores.
Se utiliza un presupuesto compartido de Google Ads, no necesariamente exclusivo de Waze.
El costo efectivo depende de las pujas, la competencia, la ubicación y las interacciones.
Google contempla cobros CPC en anuncios locales y CPM para determinados pines en Google Maps. No publica un CPM específico vigente para Waze.

4. ¿Dónde contratarlo?
Puedes consultar Google Ads y configurar una campaña de Máximo rendimiento con objetivos en tiendas. México está entre los países donde están disponibles los anuncios de Waze. 
Una pregunta: ¿Quieres conocer estos precios porque buscas anunciar tu negocio en Waze o porque estás desarrollando una plataforma de publicidad geolocalizada y quieres establecer cuánto cobrar por impresiones?
Dependiendo del caso, puedo ayudarte a calcular un CPM competitivo y un modelo de ingresos.

If you want, I can:

Explícame cómo calcular un CPM competitivo para anuncios en Waze
Dame un resumen práctico para desarrollar una plataforma de publicidad geolocalizada
Ayúdame a simular distintos escenarios de costos por impresiones para Waze
```
