import time


HELP = """
help  - список команд
add   - добавить задачу
show  - показать задачи
done  - убрать выполненную задачу
exit  - закрыть приложение
"""

todo = {}

def checkDate(date):
  try:
    time.strptime(date, "%d.%m.%Y")
    return True
  except ValueError:
    print("Error. Неправильный формат даты")
    return False

print ("Введите команду, введите help для вывода списка команд")

while True:
  userAnswer = input()

  if userAnswer == "add":
    userDate = input( "Введите дату:\n" )
    userTask = input( "Что нужно сделать?" )

    if userDate in todo.keys():
      todo[ userDate ].append( userTask )
    else:
      todo[ userDate ] = [ userTask ]
    print(f"[ {userDate} ] - добавлена задача '{userTask}'")
  elif userAnswer == "help":
    print(HELP)
  elif userAnswer == "show":
    for date in sorted( todo.keys() ):
      for tasks in todo[ date ]:
        print( f"[ {date} ] - {tasks}" )
  elif userAnswer == "exit":
    break
  elif userAnswer == "done":
    print("Работает\n") 
