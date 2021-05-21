# # formatting : %d %f %s %c
#
# alphas = 20; digit=30
# height = 179.33
# string = 'python'
# print(f'alphas : {alphas:d}, digit : {digit:10d}, height : {height:.1f}')
#
# print(f'{string:<10}')
# print(f'{string:>10}')
# print(f'{string:^10}')
# print(f'{string:-^10}')
# print(string.ljust(10))
# print(string.rjust(10))
# print(string.center(10))

#날짜, 시간 출력 포맷
# from datetime import date, datetime, timedelta
#
# today = date.today()
# print(today.year)
# print(today.month)
# print(today.day)
#
# cur_time = datetime.now().time()
# print(cur_time)
# print(cur_time.hour)
# print(cur_time.minute)
# print(cur_time.second)
# print(cur_time.microsecond)
#
# cur_time = datetime.now()
#
# print(today + timedelta(days=-1))
# print(today + timedelta(days=7))
# print(cur_time + timedelta(days=1, hours=2))
