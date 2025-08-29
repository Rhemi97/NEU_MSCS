translations = {
  'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
  'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
  'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
}

def translator(language):
    def translate_word(word):
      return translations[language].get(word, f"[{word} not found]")

    return translate_word


translate_to_spanish = translator('italian')
print(translate_to_spanish('thank you'))  # Output: hola
