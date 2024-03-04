import logging
logging.basicConfig(level=logging.INFO, filename="py_log7.log", filemode="w")

input_list = []
max_length = 3
while True:
   try:
       while len(input_list) < max_length:
          item = int(input('вводим число : '))
          input_list.append(item)
       print(sum(input_list)/len(input_list))
       break
   except ValueError:
       print('вводите цифры')
       logging.error('ValueError', exc_info=True)