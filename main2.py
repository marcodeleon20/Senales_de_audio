#CODIGO DE: https://github.com/antonioam82/reproductor-WAV/blob/master/wavPlayer.py

#IMPORTAMOS RECURSOS NECESARIOS.
import pyaudio  
import wave 
from tkinter import Tk
import numpy as np
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename
   
chunk = 50000

root = Tk()
root.withdraw

root.geometry("500x500")


#ABRIMOS UBICACIÓN DEL AUDIO.  

file_path = askopenfilename(filetypes=[("WAV files", "*.wav")])

f = wave.open(file_path,"rb")

#INICIAMOS PyAudio.
p = pyaudio.PyAudio()  


#ABRIMOS STREAM
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)

#LEEMOS INFORMACIÓN  
data = f.readframes(chunk)  

#REPRODUCIMOS "stream"  
while data:  
    stream.write(data)  
    data = f.readframes(chunk)  

#PARAMOS "stream".  
stream.stop_stream()  
stream.close()  

#FINALIZAMOS PyAudio  
p.terminate()  

frames = []
audio_dato =  b''.join(frames)
arreglo = np.frombuffer(audio_dato, dtype=np.int16)

canales = f.getnchannels()
frame2 = f.getframerate()

duracion = len(arreglo)/frame2

tiempo = np.linspace(0., duracion, len(arreglo))

plt.plot(tiempo, arreglo)
plt.xlabel("Tiempo(s): ")
plt.ylabel("Amplitud: ")
plt.title("Señal de audio")
plt.show()
 