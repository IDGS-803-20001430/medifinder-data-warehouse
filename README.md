# Medifinder Data Warehouse

## Descripción General

Medifinder es una plataforma que conecta médicos y pacientes, permitiendo la gestión eficiente de citas y consultas médicas. Este repositorio contiene el conjunto de datos preprocesados que se utilizarán en el data warehouse de Medifinder.

## Preprocesamiento de Datos

Los datos han sido limpiados y normalizados para asegurar su calidad. Las técnicas aplicadas incluyen:

- **Identificación y Corrección de Errores**: Validación de formatos de correo electrónico, fechas y consistencia de datos.
- **Normalización de Datos**: Estandarización de nombres y direcciones.
- **Eliminación de Duplicados**: Detección y eliminación de registros duplicados.

## Instrucciones de Uso

### Importación de Datos

1. **Crear las Tablas**:
   - Ejecuta el script `scripts/create_tables.sql` para crear las tablas en la base de datos.

2. **Insertar Datos Limpiados**:
   - Ejecuta el script `scripts/insert_cleaned_data.sql` para insertar los datos preprocesados en las tablas correspondientes.

### Ejemplos de Consultas

```sql
-- Verificar que todos los médicos están registrados correctamente
SELECT * FROM Medico;

-- Consultar citas confirmadas
SELECT * FROM Cita WHERE Estatus = 'Confirmada';