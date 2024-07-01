import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error, accuracy_score, confusion_matrix, classification_report

# Cargar el dataset
data = pd.read_csv('historial_clinico_cleaned.csv')

# Análisis exploratorio y visualización
# Gráfico de correlación para variables numéricas (Peso_Paciente, Talla_Paciente)
correlation_matrix = data[['Peso_Paciente', 'Talla_Paciente']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Matriz de correlación: Peso y Talla del Paciente')
plt.xlabel('Peso del Paciente')
plt.ylabel('Talla del Paciente')
plt.show()
print("Este gráfico muestra la correlación entre el peso y la talla del paciente. Cuanto más cercano a 1 el valor, mayor es la correlación positiva entre las variables.")

# Gráfico de dispersión de variables numéricas (Peso_Paciente vs Talla_Paciente)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Peso_Paciente', y='Talla_Paciente', data=data)
plt.title('Gráfico de dispersión: Peso vs Talla del Paciente')
plt.xlabel('Peso del Paciente')
plt.ylabel('Talla del Paciente')
plt.show()
print("Este gráfico muestra la distribución de los pacientes según su peso y talla. Permite observar si existe alguna relación visual entre ambas variables.")

# Modelo de regresión
# Definir variables predictoras (X) y variable objetivo (y) para regresión
X_reg = data[['Peso_Paciente']]  # Variable predictora (Peso_Paciente)
y_reg = data['Talla_Paciente']   # Variable objetivo (Talla_Paciente)

# Dividir en conjunto de entrenamiento y prueba para regresión
X_reg_train, X_reg_test, y_reg_train, y_reg_test = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

# Inicializar y ajustar el modelo de regresión lineal
regression_model = LinearRegression()
regression_model.fit(X_reg_train, y_reg_train)

# Predecir en el conjunto de prueba para regresión
y_reg_pred = regression_model.predict(X_reg_test)

# Evaluar el modelo de regresión
mse_regression = mean_squared_error(y_reg_test, y_reg_pred)
print(f'Mean Squared Error (Regresión): {mse_regression}')

# Visualización de la regresión en conjunto de entrenamiento
plt.figure(figsize=(8, 6))
plt.scatter(X_reg_train, y_reg_train, color='blue', label='Datos de entrenamiento')
plt.plot(X_reg_train, regression_model.predict(X_reg_train), color='red', linewidth=2, label='Línea de regresión')
plt.title('Regresión Lineal: Peso vs Talla del Paciente (Conjunto de entrenamiento)')
plt.xlabel('Peso del Paciente')
plt.ylabel('Talla del Paciente')
plt.legend()
plt.show()
print("Este gráfico muestra la relación entre el peso y la talla del paciente. La línea roja representa la regresión lineal ajustada a los datos de entrenamiento.")

# Visualización de la regresión en conjunto de prueba
plt.figure(figsize=(8, 6))
plt.scatter(X_reg_test, y_reg_test, color='blue', label='Datos de prueba')
plt.plot(X_reg_test, regression_model.predict(X_reg_test), color='red', linewidth=2, label='Línea de regresión')
plt.title('Regresión Lineal: Peso vs Talla del Paciente (Conjunto de prueba)')
plt.xlabel('Peso del Paciente')
plt.ylabel('Talla del Paciente')
plt.legend()
plt.show()
print("Este gráfico muestra la evaluación de la regresión lineal en el conjunto de prueba. Compara los datos reales (puntos azules) con las predicciones del modelo (línea roja).")

# Modelo de clasificación
# Definir variables predictoras (X) y variable objetivo (y) para clasificación
X_clf = data[['Peso_Paciente', 'Talla_Paciente']]  # Variables predictoras (Peso_Paciente, Talla_Paciente)
y_clf = data['Diagnostico']   # Variable objetivo (Diagnostico)

# Dividir en conjunto de entrenamiento y prueba para clasificación
X_clf_train, X_clf_test, y_clf_train, y_clf_test = train_test_split(X_clf, y_clf, test_size=0.2, random_state=42)

# Inicializar y ajustar el modelo de clasificación (Random Forest)
clf_model = RandomForestClassifier(random_state=42)
clf_model.fit(X_clf_train, y_clf_train)

# Predecir en el conjunto de prueba para clasificación
y_clf_pred = clf_model.predict(X_clf_test)

# Evaluar el modelo de clasificación
accuracy = accuracy_score(y_clf_test, y_clf_pred)
print(f'Accuracy (Clasificación): {accuracy}')

# Matriz de confusión para evaluación
plt.figure(figsize=(10, 8))
sns.heatmap(confusion_matrix(y_clf_test, y_clf_pred), annot=True, cmap='Blues', fmt='d')
plt.title('Matriz de Confusión: Modelo de Clasificación')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()
print("Esta matriz de confusión muestra la comparación entre las clases reales (filas) y las clases predichas por el modelo (columnas).")

# Reporte de clasificación
print('Reporte de Clasificación:')
print(classification_report(y_clf_test, y_clf_pred))
