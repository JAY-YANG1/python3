# 날씨예보
print('날씨 정보를 입력하세요')
date = input('날짜(월일) : ')
day = input('요일 : ')
minTemp = int(input('최저기온 : '))
maxTemp = int(input('최고기온 : '))
rainProp = int(input('강수확률 : '))
airRate = input('미세먼지 : ')
sunrise = input('일출시간 : ')
sunset = input('일몰시간 : ')
swave = float(input('남해 해수면(m) : '))
ewave = float(input('동해 해수면(m) : '))
wwave = float(input('서해 해수면(m) : '))
dayDate = date + ' ' + day

print('-----------------------------')
print('내일 날씨 예보입니다')
print(day + '요일인 ' + date +
      '의 아침 최저 기온은 ' + str(minTemp) + '도, 낮 최고 기온은 ' +
      str(maxTemp) + '도로 예보되었습니다')
print('비올 확률은 ' + str(rainProp) + '%이고, 미세먼지는 ' +
      airRate + ' 수준일것으로 예상됩니다')
print('일출시간은 ' + sunrise +
      '이고, 일몰시간은 ' + sunset + '입니다')
print('바다의 물결은 남해 앞바다 ' + str(swave) +
      'm, 동해 앞바다 ' + str(ewave) + 'm, 서해 앞바다 ' +
      str(wwave) + 'm 높이로 일겠습니다')
print('지금까지 ' + dayDate + ' 요일 날씨 예보였습니다')

print('---------------------------')
print('내일 날씨 예보입니다.')
print('{0}요일인 {1}의 아침 최저 기온은 {2}도, 낮 최고 기온은 {3}도로 예보됐습니다.'.format(day, date, minTemp, maxTemp))
print('비올 확률은 {0}%이고, 미세먼지는 {1} 수준일 것으로 예상됩니다.'.format(rainProp, airRate))
print('일출 시간은 {0}이고, 일몰 시간은 {1}입니다.'.format(sunrise, sunset))
print('바다의 물결은 남해 앞바다 {0}m, 동해 앞바다 {1}m, 서해 앞바다 {2}m 높이로 일겠습니다.'.format(swave, ewave, wwave))
print('지금까지 {0}요일 날씨 예보였습니다.'.format(dayDate))

print('---------------------------')
print('내일 날씨 예보입니다.')
print('%s요일인 %s의 아침 최저 기온은 %d도, 낮 최고 기온은 %d도로 예보됐습니다.' % (day, date, minTemp, maxTemp))
print('비올 확률은 %d 이고, 미세먼지는 %s 수준일 것으로 예상됩니다.' % (rainProp, airRate))
print('일출 시간은 %s이고, 일몰 시간은 %s입니다.' % (sunrise, sunset))
print('바다의 물결은 남해 앞바다 %.1fm, 동해 앞바다 %.1fm, 서해 앞바다 %.1fm 높이로 일겠습니다.' % (swave, ewave, wwave))
print('지금까지 %s요일 날씨 예보였습니다.' % dayDate)


print('---------------------------')
yebo = f'내일 날씨 예보입니다.\n{day}요일인 {date}의 아침 최저 기온은 {minTemp}도, ' \
       f'낮 최고 기온은 {maxTemp}도로 예보됐습니다.\n비올 확률은 {rainProp}%이고, ' \
       f'미세먼지는 {airRate} 수준일 것으로 예상됩니다.\n일출 시간은 {sunrise}이고, ' \
       f'일몰 시간은 {sunset}입니다.\n바다의 물결은 남해 앞바다 {swave}m, ' \
       f'동해 앞바다 {ewave}m, 서해 앞바다 {wwave}m 높이로 일겠습니다.\n지금까지 {dayDate}요일 날씨 예보였습니다.'

print(yebo)
