# Sistema Comunitario de Préstamo de Herramientas


---

## ⚙️ Funcionalidades principales

### 👤 Gestión de usuarios
- Registrar vecino
- Listar vecinos
- Buscar vecino por ID
- Actualizar información
- Eliminar vecino (solo administrador)

### 🛠️ Gestión de herramientas
Cada herramienta registra:
- ID
- Nombre
- Categoría (construcción, jardinería, etc.)
- Cantidad disponible
- Estado (activa, en reparación, fuera de servicio)
- Valor estimado

Operaciones:
- Crear
- Listar
- Buscar
- Actualizar
- Inactivar herramientas

### 🔄 Gestión de préstamos
- Registrar préstamos
- Verificar disponibilidad
- Descontar stock automáticamente
- Registrar devoluciones
- Restaurar stock
- Control de estados (Activo, Devuelto, Vencido)

### 📊 Consultas y reportes
- Herramientas con stock bajo
- Préstamos activos y vencidos
- Historial de préstamos por usuario
- Herramientas más solicitadas
- Usuarios que más herramientas han solicitado

### 🧾 Registro de eventos (logs)
- Inicio de sesión
- Errores del sistema
- Intentos sin permisos
- Acciones importantes (crear, eliminar, prestar, devolver)

---

## 💾 Persistencia de datos
El sistema utiliza **archivos JSON** para almacenar la información:

- `vecino.json`
- `herramientas.json`
- `prestamos.json`

Los eventos del sistema se registran en:
- `logs.txt`

---



### Ejecución
```bash
python main.py



