import streamlit as st

def main():
  st.title("Clasificación de la base de datos mnist")
  st.markdown("Subir imagen para ser clasificada")

uploaded_file = st.file_uploaded("Selecciona una imagen (PNG, JPG, JPEG...)", type = ["jpg", "png", "jpeg"])


if __name__=="__main__":
  main()
