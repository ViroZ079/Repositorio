import speech_recognition as sr 
class Microfone:
	def __init__():
		global falou
		r = sr.Recognizer() 
		with sr.Microphone() as source:                                                                       
			print("Pronta para comandar")                                                                                   
			audio = r.listen(source) 
		try:
			print("Você disse " + r.recognize_google(audio, language="pt-BR"))
			falou = r.recognize_google(audio, language="pt-BR")
		except sr.UnknownValueError:
			print("Não entendi")
		except sr.RequestError as e:
			print("Sem requests; {0}".format(e))