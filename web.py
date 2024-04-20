# Importa las bibliotecas necesarias
import streamlit as st
import functions
import datetime


# Obtiene la lista de 'todos' de un archivo usando una función del módulo 'functions'
todos = functions.get_todos()

# Inicializa 'new_todo' en 'st.session_state' si aún no se ha inicializado
if "new_todo" not in st.session_state:
    st.session_state.new_todo = ""

# Define la función 'add_todo' que agrega un nuevo 'todo' a la lista y luego limpia el campo de texto
def add_todo():
    # Obtiene la fecha y hora actuales
    now = datetime.datetime.now()
    # Formatea la fecha y hora en el formato deseado
    timestamp = now.strftime("%d/%m/%Y a las %I:%M%p")

    todo = st.session_state["new_todo"]
    # Agrega la fecha y hora de creación al 'todo'
    todo_with_timestamp = f"{todo} creado el {timestamp}\n"

    # Verifica si el 'todo' ya existe en la lista
    if todo_with_timestamp in todos:
        # Si el 'todo' ya existe, muestra un mensaje al usuario
        st.warning("¡Este 'todo' ya está en tu lista!")
    else:
        # Si el 'todo' no existe, lo agrega a la lista
        todos.append(todo_with_timestamp)
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""  # Limpia el campo de texto

# Crea el título de la página
st.title("My todo App")
# Crea el subtítulo de la página
st.subheader("This is my todo app.")
# Añade un texto a la página
st.write("this app is to increase your productivity")

# Crea checkboxes para cada 'todo' en la lista
for index,todo in enumerate(todos):
   # Crea un checkbox con el 'todo' como etiqueta
   checkbox = st.checkbox(todo, key=todo)
   # Si el checkbox está marcado, elimina el 'todo' de la lista y del 'st.session_state'
   if checkbox:
       # Elimina el 'todo' de la lista
       todos.pop(index)
       # Escribe la lista de 'todos' actualizada en un archivo
       functions.write_todos(todos)
       # Elimina el 'todo' del 'st.session_state'
       del st.session_state[todo]
       # Vuelve a ejecutar la aplicación para actualizar la interfaz de usuario
       st.experimental_rerun()

# Crea un campo de texto para agregar un nuevo 'todo'
st.text_input(label="", value=st.session_state["new_todo"], 
              placeholder="Add new todo...", 
              on_change=add_todo, 
              key="new_todo")
