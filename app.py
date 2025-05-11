from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", imagen="")  # Página de inicio

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")  # Página de servicios

@app.route("/agenda")
def ubicacion():
    return render_template("agenda.html")  # Página de ubicación

#Gráfico de servicios estático
servicios = ['Limpieza Facial', 'Dermapen', 'Electrocauterización', 'Pink Glow', 'Valoración']
meses = ['Febrero', 'Marzo', 'Abril']
valores = np.array([
    [10, 9, 11],  # Limpieza Facial
    [12, 15, 14],  # Dermapen
    [25, 30, 28],  # Electrocauterización
    [20, 18, 22],   # Pink Glow
    [15, 17, 19]   # Valoración
])

# Posiciones para las barras agrupadas
bar_width = 0.2
y_pos = np.arange(len(servicios))

# Crear gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Colores de mi página
colores = ['#FC9E82', '#F7B49C', '#E28F77']

for i, mes in enumerate(meses):
    ax.barh(y_pos + i * bar_width, valores[:, i], height=bar_width, label=mes, color=colores[i])

# Personalización
ax.set_xlabel('Número de Solicitudes', fontsize=12)
ax.set_yticks(y_pos + bar_width)
ax.set_yticklabels(servicios)
ax.set_title('Servicios Más Solicitados – Últimos 3 Meses', fontsize=16, color='#732F29')
ax.legend()

# Quitar bordes y ajustar diseño
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()

# Guardar imagen
plt.savefig('static/servicios_mas_solicitados.png')
plt.close()

#gráfico de paquetes interactivo
@app.route("/paquetes")
def paquetes():
    labels = ["Pink Glow", "Masajes Reductores", "Terapia Capilar"]
    data = [25, 40, 33]
    return render_template("paquetes.html", labels=labels, data=data)

# Página del formulario de agendamiento
@app.route("/agenda", methods=["GET", "POST"])
def agenda():
    if request.method == "POST":
        datos = {
            "nombre": request.form["nombre"],
            "telefono": request.form["telefono"],
            "correo": request.form.get("correo", "No proporcionado"),
            "servicio": request.form["servicio"],
            "fecha": request.form["fecha"],
            "horario": request.form["horario"],
            "primera_vez": request.form["primera_vez"],
            "comentarios": request.form.get("comentarios", "Sin comentarios")
        }
        return render_template("confirmacion.html", datos=datos)
    return render_template("agenda.html")

if __name__ == '__main__':
    app.run(debug=True)