# 🔢 Convertidor de Bases Numéricas y Calculadora

Una aplicación web desarrollada en Django que permite convertir números entre diferentes bases numéricas y realizar cálculos aritméticos en diversas bases.

## ✨ Características

### 🔄 Convertidor de Bases
- Conversión entre bases numéricas: **Decimal**, **Binario**, **Octal** y **Hexadecimal**
- Interfaz intuitiva con botón de intercambio de bases
- Validación de entrada y manejo de errores

### 🧮 Calculadora Aritmética
- Operaciones matemáticas básicas: **Suma**, **Resta**, **Multiplicación** y **División**
- Soporte para cálculos en diferentes bases numéricas
- Visualización de resultados tanto en la base original como en decimal

### 🌐 Características Adicionales  
- **Interfaz multiidioma**: Español e Inglés
- **Diseño responsivo** con Bootstrap 5
- **Interfaz de pestañas** para navegación fácil entre herramientas
- **Validación completa** de entradas del usuario

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. **Clona el repositorio**
   ```bash
   git clone <tu-repositorio>
   cd base-conversion
   ```

2. **Crea un entorno virtual**
   ```bash
   python -m venv venv
   ```

3. **Activa el entorno virtual**
   
   En Linux/macOS:
   ```bash
   source venv/bin/activate
   ```
   
   En Windows:
   ```bash
   venv\Scripts\activate
   ```

4. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

5. **Realiza las migraciones**
   ```bash
   cd django_app
   python manage.py migrate
   ```

6. **Recopila archivos estáticos**
   ```bash
   python manage.py collectstatic
   ```

7. **Inicia el servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

8. **Visita la aplicación**
   
   Abre tu navegador y ve a: `http://127.0.0.1:8000/converter/`

## 📋 Uso

### Convertidor de Bases Numéricas
1. Ingresa el número que deseas convertir
2. Selecciona la base de origen (Decimal, Binario, Octal, Hexadecimal)
3. Selecciona la base de destino
4. Haz clic en "Convertir"
5. Usa el botón de intercambio (⇄) para cambiar rápidamente entre bases

### Calculadora Aritmética
1. Ingresa los dos números para la operación
2. Selecciona la base en la que están los números
3. Elige la operación deseada (+, -, ×, ÷)
4. El resultado se mostrará en la base original y en decimal

## 🏗️ Estructura del Proyecto

```
base-conversion/
├── django_app/
│   ├── apps/
│   │   └── conversion_app/          # Aplicación principal
│   │       ├── templates/           # Plantillas HTML
│   │       │   └── partials/        # Componentes reutilizables
│   │       ├── static/              # Archivos estáticos
│   │       ├── views.py             # Lógica de vistas
│   │       └── urls.py              # Configuración de URLs
│   ├── locale/                      # Archivos de traducción
│   │   └── es/                      # Traducciones al español
│   ├── project_settings/            # Configuración del proyecto
│   └── manage.py                    # Script de administración Django
├── venv/                            # Entorno virtual
└── requirements.txt                 # Dependencias del proyecto
```

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django 4.2.1
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Servidor**: Gunicorn (producción)
- **Archivos estáticos**: WhiteNoise
- **Internacionalización**: Django i18n
- **Base de datos**: SQLite (desarrollo)

## 🌍 Internacionalización

La aplicación soporta múltiples idiomas:
- **Inglés** (por defecto)
- **Español**

Para cambiar el idioma del navegador o configurar tu preferencia de idioma en el navegador.

## 🎨 Capturas de Pantalla

La aplicación incluye:
- Una interfaz limpia y moderna con Bootstrap
- Pestañas para navegar entre herramientas
- Formularios intuitivos con validación
- Mensajes de error y éxito claros

## 🤝 Contribuir

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Notas de Desarrollo

- La aplicación maneja la división por cero y otros errores matemáticos
- Los resultados de división con decimales se muestran con 4 decimales de precisión
- Para bases no decimales, los resultados de división se redondean a enteros

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - vea el archivo [LICENSE](LICENSE) para más detalles.

---

Desarrollado con ❤️ usando Django 