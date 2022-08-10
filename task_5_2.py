# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

from random import randint
import time


username = input("Здравствуй! Как тебя зовут? ")
time.sleep(2)
players = int(input(f"{username}, если хочешь поиграть со мной, нажми 1, если с другом - 2: "))

konfetu = 130
if players == 1:
   check = randint(0,1)
   if check == 1:
    print(f'Первый ход твой, {username}!')
   if check == 0:
    print('Игра - моя страсть. Мой ход первый...')
if players == 2:
   check = randint(1,2)
   if check == 1:
    print(f'Первый ход твой, {username}!')
   if check == 2:
    print('Первый ход второго игрока')

def checking_for_errors (n: int):
     if n > 28:
        time.sleep(2)
        print("Осознай свои проблемы и начни игру заново!")
        time.sleep(3)
        exit()
     if n <= 0:
        time.sleep(2)
        print("Ты так и не понял(а) условия игры!")
        time.sleep(3)
        exit()
     else: 
        return(n)
        
while konfetu > 0:
   if check == 1:
      print("Сколько конфет ты берешь ")
      player_1 = int(input())
      checking_for_errors (player_1)
      konfetu -= player_1
      print(f'Осталось {konfetu} конфет')
      if players == 2:
         check = 2
      if players == 1:
         check = 0
   elif check == 2:
      print("Сколько конфет хочет взять второй игрок ")
      player_2 = int(input())
      checking_for_errors (player_2)
      konfetu -= player_2
      time.sleep(1)
      print(f"Конфет теперь - {konfetu}")
      check = 1
   elif check == 0:   
      if konfetu % 29 != 0:
        player_2 = konfetu % 29
      else:
        player_2 = randint(1,28)
      print(f'Я беру {player_2}')
      konfetu -= player_2
      time.sleep(1)
      print(f"Конфет осталось - {konfetu}")
      check = 1

if konfetu == 0 and check == 1:
    print('________________________________________')
    print(f'Игра окончена! {username} проиграл(а)!')
    time.sleep(4)
if konfetu == 0 and check == 0:
    print('______________________')
    print(f'Победитель {username}!')
    time.sleep(4)
if konfetu == 0 and check == 2:
    print('________________________')
    print(f'Победитель {username}!')
    time.sleep(4)