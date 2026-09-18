# 💻 Programmer's Diary (Diario del Programador)

Una aplicación web interactiva desarrollada con **Flask** que permite a los usuarios registrarse, iniciar sesión y gestionar sus propias entradas o notas personales con un diseño moderno en modo oscuro e integración de un widget meteorológico.

---

## 🚀 Características

- **Autenticación de Usuarios:** Sistema completo de registro e inicio de sesión con aislamiento de datos por usuario (cada usuario solo ve sus propias entradas).
- **Gestión de Entradas:** Creación y visualización de tarjetas de notas personales con título, subtítulo y contenido.
- **Widget de Clima Integrado:** Muestra la información meteorológica en tiempo real mediante un contenedor adaptable.
- **Base de Datos Dinámica:** Creación e inicialización automática de tablas utilizando SQLite y SQLAlchemy.
- **Interfaz Moderna:** Diseño oscuro (Dark Mode) responsivo con estilos en CSS puro.

---

## 🛠️ Tecnologías Utilizadas

- **Backend:** Python 3, Flask, Flask-SQLAlchemy
- **Base de Datos:** SQLite
- **Frontend:** HTML5, CSS3, Jinja2 (Plantillas de Flask)

---

## 📂 Estructura del Proyecto

```text
diary-en-main/
│
├── instance/
│   └── diary.db             # Base de datos SQLite (generada automáticamente)
├── static/
│   ├── css/
│   │   └── style.css        # Estilos CSS de la interfaz
│   └── img/                 # Recursos gráficos (logos e íconos)
├── templates/
│   ├── card.html            # Vista individual de una tarjeta
│   ├── create_card.html     # Formulario para crear una nueva entrada
│   ├── index.html           # Panel principal de tarjetas y widget de clima
│   ├── login.html           # Pantalla de inicio de sesión
│   └── registration.html    # Pantalla de registro
└── main.py                  # Servidor principal de Flask y modelos SQLAlchemy
