import pywhatkit as pw

text = """pywhatkit is a Python library that simplifies the process of automating tasks like sending WhatsApp messages, performing Google searches, playing YouTube videos, converting images to ASCII art, and more. It is user-friendly and designed to integrate smoothly into Python scripts, enabling developers to perform a variety of tasks with minimal code. Ideal for both beginners and experienced developers, 'pywhatkit' provides an efficient way to enhance the functionality of your Python projects."""

pw.text_to_handwriting(text, "pywhatkit_Text.png", [0,0,138])

print("Your file is saved on destination.")