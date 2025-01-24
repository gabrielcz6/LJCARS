import streamlit as st
import time
import pandas as pd
from streamlit_option_menu import option_menu
import os



def consulta_servicio():
    st.header("Panel para ver servicios")

        
    placa = st.text_input("Ingrese la placa del vehículo")
    buscar = st.button("Buscar")
    
     # Título
    a=st.text_input("Ingrese la placa del vehícular")
    if placa =="ADE239":
       # Título
       st.title("Servicio de Mantenimiento")
       
       # Detalle del servicio
       st.header("Cambio de Retenes de Eje de Levas")
       
       # Fecha en un cuadro
       st.info("📅 **Fecha del servicio:** 2 de septiembre de 2024")
       
       # Lista de actividades incluidas
       st.subheader("Incluye:")
       st.write("- Cambio de retenes de eje de levas")
       st.write("- Revisión y mantenimiento de distribución (d/m distribución)")
       st.write("- Instalación de 2 retenes de eje de levas")
       st.write("- Uso de insumos de limpieza especializados")
       
       # Llamado a la acción
       st.success("**servicio encontrado!**")
                         
                  

    
    

# Función principal
def app():
    # Título de la aplicación
    st.title("SISTEMA LJ CARS")
    
    with st.sidebar:
    # Barra lateral (Sidebar)
    # Imagen en la barra lateral
     st.sidebar.image("ljcars.jpg", width=290)

    # Menú lateral con opciones (usando streamlit-option-menu)
     menu = option_menu(
     menu_title='Menu',  # Título del menú
     options=['Ver Servicio'],  # Opciones del menú
     icons=['person-plus'],  # Iconos de las opciones
     menu_icon="list",  # Ícono del menú lateral
     default_index=0,  # Índice por defecto
     styles={  # Estilos personalizados
        "container": {"padding": "5!important", "background-color": "black"},  # Fondo del menú
        "icon": {"color": "#E91E63", "font-size": "23px"},  # Íconos en palo rosa
        "nav-link": {
            "color": "#F8BBD0",  # Texto en palo rosa claro
            "font-size": "20px",
            "text-align": "left",
            "margin": "0px",
            "--hover-color": "#F48FB1"  # Color al pasar el cursor (palo rosa intermedio)
        },
        "nav-link-selected": {"background-color": "#F06292"},  # Fondo de opción seleccionada (palo rosa suave)
    }
)
    # Lógica según la opción seleccionada
    if menu == "Ver Servicio":
        consulta_servicio()

 

# Ejecutar la aplicación
if __name__ == "__main__":
    app()


