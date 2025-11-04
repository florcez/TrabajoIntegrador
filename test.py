'''#TESTING

from config import *

root = tk.Tk()
root.geometry('500x300')

frame = tk.Frame(root)
canvas = tk.Canvas(frame)
scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
frame_scroll = tk.Frame(canvas)

frame_scroll.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=frame_scroll, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

for i in range(100):
    tk.Label(frame_scroll, text="Sample scrolling label").pack(fill='x')

scrollbar.pack(side="right", fill="y")
frame.pack(fill='both')
canvas.pack(side="left", fill="both", expand=True)

root.mainloop()'''

'''import tkinter as tk

# Crear ventana principal
root = tk.Tk()
root.geometry('500x300')
root.title("Biblioteca de música")
root.resizable(width=False,height=False)

# Frame principal que contiene el canvas y el scrollbar
main_frame = tk.Frame(root)
main_frame.pack(fill='both', expand=True)

# Canvas (lienzo desplazable)
canvas = tk.Canvas(main_frame)
canvas.pack(side='left', fill='both', expand=True)

# Scrollbar vertical
scrollbar = tk.Scrollbar(main_frame, orient='vertical', command=canvas.yview)
scrollbar.pack(side='right', fill='y')

# Vincular el canvas con el scrollbar
canvas.configure(yscrollcommand=scrollbar.set)

# Frame interno dentro del canvas (donde van los botones)
scroll_frame = tk.Frame(canvas)
frame_window = canvas.create_window((0, 0), window=scroll_frame, anchor='nw')

# --- Actualización automática ---
def update_scrollregion(event):
    """Actualiza el área desplazable según el tamaño del contenido."""
    canvas.configure(scrollregion=canvas.bbox('all'))

def resize_inner_frame(event):
    """Ajusta el ancho del frame interno al ancho visible del canvas."""
    canvas.itemconfig(frame_window, width=event.width)

scroll_frame.bind('<Configure>', update_scrollregion)
canvas.bind('<Configure>', resize_inner_frame)
# --------------------------------

# --- Soporte para scroll con la rueda del ratón ---
def on_mousewheel(event):
    # Para Windows y Linux
    canvas.yview_scroll(-int(event.delta / 120), "units")

# Vincular
root.bind_all("<MouseWheel>", on_mousewheel)     # Windows / Linux
# ---------------------------------------------------

# Crear cuadrícula de botones (3 por fila)
cols = 3
for i in range(120):
    fila, col = divmod(i, cols)
    tk.Button(scroll_frame, text=f'Botón {i+1}', height=8).grid(row=fila, column=col, padx=5, pady=5, sticky='nsew')

# Hacer que las columnas crezcan proporcionalmente
for c in range(cols):
    scroll_frame.grid_columnconfigure(c, weight=1)

root.mainloop()'''

from config import *

# --- Configuración base ---
root = tk.Tk()
root.geometry('600x400')
root.title("Galería dinámica con scroll")

main_frame = tk.Frame(root)
main_frame.pack(fill='both', expand=True)

canvas = tk.Canvas(main_frame)
canvas.pack(side='left', fill='both', expand=True)

scrollbar = tk.Scrollbar(main_frame, orient='vertical', command=canvas.yview)
scrollbar.pack(side='right', fill='y')
canvas.configure(yscrollcommand=scrollbar.set)

scroll_frame = tk.Frame(canvas)
frame_window = canvas.create_window((0, 0), window=scroll_frame, anchor='nw')

# --- Ajustes automáticos ---
def update_scrollregion(event):
    canvas.configure(scrollregion=canvas.bbox('all'))

def resize_inner_frame(event):
    canvas.itemconfig(frame_window, width=event.width)

scroll_frame.bind('<Configure>', update_scrollregion)
canvas.bind('<Configure>', resize_inner_frame)

def on_mousewheel(event):
    canvas.yview_scroll(-int(event.delta / 120), "units")

root.bind_all("<MouseWheel>", on_mousewheel)
# ---------------------------------------------------

# --- Configuración de la cuadrícula ---
cols = 3           # cantidad de columnas por fila
imagenes = []      # lista de imágenes cargadas
botones = []       # referencia a los botones creados

# --- Imagen base (placeholder gris 100x100) ---
base_img = Image.new("RGB", (100, 100), (180, 180, 180))
img_tk = ImageTk.PhotoImage(base_img)

# --- Función para agregar un nuevo elemento ---
def agregar_item():
    """Agrega una nueva imagen con etiqueta en la cuadrícula."""
    i = len(botones)  # índice del nuevo elemento
    fila, col = divmod(i, cols)
    
    # Frame que contendrá imagen + etiqueta
    item_frame = tk.Frame(scroll_frame)
    item_frame.grid(row=fila, column=col, padx=10, pady=10, sticky='nsew')
    
    # Crear botón con imagen
    btn = tk.Button(item_frame, image=img_tk, width=100, height=100, relief='raised',
                    command=lambda n=i: print(f"Botón {n+1} presionado"))
    btn.image = img_tk  # mantener referencia
    btn.pack()
    
    # Etiqueta debajo del botón
    tk.Label(item_frame, text=f"Imagen {i+1}").pack(pady=(5, 0))
    
    # Guardar referencia
    botones.append(btn)

# --- Botón para agregar elementos ---
tk.Button(root, text="➕ Agregar imagen", command=agregar_item).pack(pady=10)

# --- Configurar columnas expansibles ---
for c in range(cols):
    scroll_frame.grid_columnconfigure(c, weight=1)

root.mainloop()
