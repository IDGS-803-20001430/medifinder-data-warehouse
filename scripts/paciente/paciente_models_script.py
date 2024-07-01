import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from datetime import datetime

# Cargar el dataset de pacientes
data = pd.read_csv('paciente_cleaned.csv')

# Calcular la edad de los pacientes a partir de la fecha de nacimiento
data['Fecha_Nacimiento'] = pd.to_datetime(data['Fecha_Nacimiento'])
data['Edad'] = datetime.now().year - data['Fecha_Nacimiento'].dt.year

# Visualización y Análisis Exploratorio
# Distribución de la edad de los pacientes
plt.figure(figsize=(10, 6))
sns.histplot(data['Edad'], bins=10, kde=True)
plt.title('Distribución de la Edad de los Pacientes')
plt.xlabel('Edad')
plt.ylabel('Número de Pacientes')
plt.tight_layout()
plt.show()

# Distribución de la edad por sexo
plt.figure(figsize=(10, 6))
sns.boxplot(x='Sexo', y='Edad', data=data)
plt.title('Distribución de la Edad por Sexo')
plt.xlabel('Sexo')
plt.ylabel('Edad')
plt.tight_layout()
plt.show()

# Distribución de la edad por estatus
plt.figure(figsize=(10, 6))
sns.boxplot(x='Estatus', y='Edad', data=data)
plt.title('Distribución de la Edad por Estatus')
plt.xlabel('Estatus')
plt.ylabel('Edad')
plt.tight_layout()
plt.show()

# Modelo de Regresión Mejorado
# Intentaremos predecir la edad del paciente utilizando sexo y estatus
X_reg = data[['Sexo', 'Estatus']]
X_reg = pd.get_dummies(X_reg, columns=['Sexo'], drop_first=True)  # Convertir sexo a variables dummy

y_reg = data['Edad']

X_reg_train, X_reg_test, y_reg_train, y_reg_test = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

regression_model = LinearRegression()
regression_model.fit(X_reg_train, y_reg_train)

y_reg_pred = regression_model.predict(X_reg_test)

mse_regression = mean_squared_error(y_reg_test, y_reg_pred)

# Generar el reporte de regresión
reporte_regresion = f"""
Reporte de Regresión:
Mean Squared Error (Regresión): {mse_regression}
"""
print(reporte_regresion)

# Visualización del modelo de regresión
plt.figure(figsize=(10, 6))
plt.scatter(y_reg_test, y_reg_pred, color='blue')
plt.plot([y_reg.min(), y_reg.max()], [y_reg.min(), y_reg.max()], linestyle='--', color='red', linewidth=2)
plt.title('Regresión Lineal: Edad Real vs Edad Predicha')
plt.xlabel('Edad Real')
plt.ylabel('Edad Predicha')
plt.tight_layout()
plt.show()

# Predicciones del modelo de regresión
predicciones_regresion = pd.DataFrame({'Edad Real': y_reg_test, 'Edad Predicha': y_reg_pred})
print(predicciones_regresion)
