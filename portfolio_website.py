import streamlit as st
import google.generativeai as genai
 
api_key = st.secrets["GOOGLE_API_KEY"]
#api_key =""
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')
 
 
col1, col2 = st.columns(2)
 
with col1:
    st.subheader("Hola :wave:")
    st.title("Soy Pablo Andrés Gay")
 
with col2:
    st.image("images/miPerfil.jpg")
 
st.title(" ")
 
 
persona = """
        Tu eres el bot de IA de Pablo Gay. Tu ayudas a las personas a responder preguntas sobre tu persona
        (i.e Pablo Gay) responde como si tu estuvieras respondiendo. No respondas en segunda o tercera persona.
        Si no conoces la respuesta, tu simplemente responde: "Es un secreto"
        Aquí existe más información sobre Pablo Gay:
        
        Pablo Gay es un Programador/Educador/Asistente Tecnológico en el campo de la Programación Web, la Visión Computarizada y el Internet de las Cosas.
        Él ha dirigido a equipos de programadores que juntos desarrollaron diversas aplicaciones locales y 
        provinciales. Pablo Gay ha trabajado en varias instituciones educativas públicas y privadas, dictando cursos
        y talleres de programación de aplicaciones web y para dispositivos electrónicos. Pablo Gay estudio Sistemas 
        y luego, se especializó en TICs, Programación Web y Programación de Dispositivos Electrónicos. Él es también
        un autodidacta serial habiendo compartido sus conocimientos en varios emprendimientos de Asistencia Tecnológica
        que lanzó como el último denominado: Servicios Digitales Educativos. Priorizando el entrenamiento a jóvenes, 
        Pablo Gay ha dirigido y participado como asistente en varios proyectos institucionales de colegios 
        secundarios que llegaron a instancias nacionales en las competencias nacionales de Feria de Ciencias.         
        
        El Email de Pablo Gay: gpabloandres@gmail.com 
        El Github de Pablo Gay : https://github.com/gpabloandres
        Todos mis enlaces: https://linktr.ee/gpabloandres
        """
 
st.title("AI Bot de Pablo")
 
user_question = st.text_input("Pregunta algo sobre mi...")
if st.button("PREGUNTA", use_container_width=400):
    prompt = persona +"Aquí está la pregunta que el usuario hizo: " +  user_question
    response = model.generate_content(prompt)
    st.write(response.text)
 
st.title(" ")
 
col1, col2 = st.columns(2)
with col1:
    st.subheader("Mi Plataforma Online para Asistencias IT")
    st.write("- Diversos cursos y tutoriales para asistir en Tecnologías")
    st.write("- Más de 100 clientes")
    st.write("- Asistencias offline, online o híbridas")
    st.write("- Cientos de horas de videos")
 
with col2:
    st.video("https://youtu.be/ZZmnh65ZExc")
 
st.title(" ")
 
st.title("Mi Estudio")
st.image("images/setup.jpeg")
 
 
st.write(" ")
st.title("Mis habilidades")
st.slider("Programming", 0, 100, 70)
st.slider("Teaching", 0, 100, 95)
st.slider("IOTs", 0, 100, 75)
 
st.write(" ")
st.title("Galería")
 
col1, col2, col3 = st.columns(3)
 
with col1:
    st.image("images/g1.jpg")
    st.image("images/g2.jpg")
    st.image("images/g3.jpg")
 
with col2:
    st.image("images/g4.jpg")
    st.image("images/g5.jpg")
    st.image("images/g6.jpg")
 
st.subheader(" ")
st.write("CONTACTO")
st.title("Quedo atento a tus consultas vía email a:")
st.subheader("gpabloandres@gmail.com")