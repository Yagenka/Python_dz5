# Напишите программу,
# удаляющую из текста все слова, содержащие ""абв""

word = 'Платонабв мне друг, абв ноабв истинаабв дороже'
bad = 'абв'

def delete_word (word: str, bad: str):
  res = list(filter(lambda x: not bad in x, word.split()))
  print (' '.join(res))

delete_word (word, bad)