def cities():
  # print('task_1')
  geo_logs = [
      {'visit1': ['Москва', 'Россия']},
      {'visit2': ['Дели', 'Индия']},
      {'visit3': ['Владимир', 'Россия']},
      {'visit4': ['Лиссабон', 'Португалия']},
      {'visit5': ['Париж', 'Франция']},
      {'visit6': ['Лиссабон', 'Португалия']},
      {'visit7': ['Тула', 'Россия']},
      {'visit8': ['Тула', 'Россия']},
      {'visit9': ['Курск', 'Россия']},
      {'visit10': ['Архангельск', 'Россия']}
  ]
  rus = 'Россия'
  for id in geo_logs:
    if rus not in list(id.values())[-1]:
      id.popitem()
  return [d for d in geo_logs if d]
# print(*[d for d in geo_logs if d], sep='\n') 
rus_city = cities()


# print('\ntask_2')
def geo_id():
  ids = {'user1': [213, 213, 213, 15, 213], 
        'user2': [54, 54, 119, 119, 119], 
        'user3': [213, 98, 98, 35]}
  return (list(set(sum(ids.values(),[]))))
  # print(list(set(sum(ids.values(),[]))))


def max_rate():
  # print('\ntask_3')
  stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
  max_value = 0
  max_key = None
  for key_, value_ in stats.items():
    if value_ > max_value:
      max_value = value_
      max_key = key_
  return(max_key)