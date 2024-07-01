import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder

# Cargar el dataset de médicos
data = pd.read_csv('medicos_cleaned.csv')

# Exploración del dataset
print(data.head())  # Verificar las primeras filas para identificar columnas

# Visualización y Análisis Exploratorio
# Seleccionar una variable relevante para analizar su tendencia
especialidad_counts = data['Id_Especialidad'].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=especialidad_counts.index, y=especialidad_counts.values)
plt.title('Distribución de Médicos por Especialidad')
plt.xlabel('Id de Especialidad')
plt.ylabel('Número de Médicos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Modelo de Regresión
# Ejemplo de regresión utilizando los honorarios de los médicos
X_reg = data[['Id_Especialidad']]  # Variable predictora (Id_Especialidad)
y_reg = data['Honorarios']     # Variable objetivo (Honorarios)

X_reg_train, X_reg_test, y_reg_train, y_reg_test = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

regression_model = LinearRegression()
regression_model.fit(X_reg_train, y_reg_train)

y_reg_pred = regression_model.predict(X_reg_test)

mse_regression = mean_squared_error(y_reg_test, y_reg_pred)
print(f'Mean Squared Error (Regresión): {mse_regression}')

plt.figure(figsize=(10, 6))
plt.scatter(X_reg_test, y_reg_test, color='blue', label='Datos de prueba')
plt.plot(X_reg_test, y_reg_pred, color='red', linewidth=2, label='Línea de regresión')
plt.title('Regresión Lineal: Especialidad vs Honorarios del Médico')
plt.xlabel('Id de Especialidad')
plt.ylabel('Honorarios del Médico')
plt.legend()
plt.show()

# Modelo de Clasificación
# Ejemplo de clasificación utilizando la especialidad y el país de los médicos
# Convertir variables categóricas a numéricas
label_encoder = LabelEncoder()
data['Pais'] = label_encoder.fit_transform(data['Pais'])

X_clf = data[['Id_Especialidad', 'Pais']]  # Variables predictoras
y_clf = data['Num_Cedula']  # Variable objetivo (ejemplo hipotético)

X_clf_train, X_clf_test, y_clf_train, y_clf_test = train_test_split(X_clf, y_clf, test_size=0.2, random_state=42)

clf_model = RandomForestClassifier(random_state=42)
clf_model.fit(X_clf_train, y_clf_train)

y_clf_pred = clf_model.predict(X_clf_test)

accuracy = accuracy_score(y_clf_test, y_clf_pred)
print(f'Accuracy (Clasificación): {accuracy}')

plt.figure(figsize=(10, 8))
sns.heatmap(confusion_matrix(y_clf_test, y_clf_pred), annot=True, cmap='Blues', fmt='d')
plt.title('Matriz de Confusión: Modelo de Clasificación')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

print('Reporte de Clasificación:')
print(classification_report(y_clf_test, y_clf_pred))
