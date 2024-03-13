team_1 = 'Мастера кода'
team_2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
print('В команде %s участников: %s!'%(team_1, team1_num))
print('Итого сегодня в командах участников:%s и %s!'%(team1_num, team2_num))

score_2 = 42
team2_time = 1234
print('Команда {} решила задач: {}!'.format(team_2, score_2))
print('Команда {} справилась с решением задач за: {} c!'.format(team_2, team2_time))

score_1 = 37
print(f'Команды решили: {score_1} и {score_2} задач.')

def challenge_result():
    if score_1 > score_2:
        print(f'Результат битвы: Победа {team_1}')
    return print(f'Результат битвы: Победа {team_2}')
challenge_result()

task_total = score_1 + score_2
team1_time = 1432
time = [team1_time, team2_time]
time_avg = sum(time) / task_total
print(f'Сегодня было решено {task_total} задач. Среднее время на задачу {round(time_avg, 2)} секунды.')