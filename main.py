#kahvin osto
# jos rahaa taskussa >=5
# osta latte
# jos ei mutta rahaa taskussa >=3
# osta normi kahvi
# muuten
# lähde pois

rahaa_taskussa = int(input('Paljonko sinulla on rahaa?'))
maistuuko_kahvi = input('Maistuuko kahvi?')
laten_hinta = 5
kahvin_hinta = 3
teen_hinta = 2

if rahaa_taskussa >= laten_hinta and maistuuko_kahvi == 'Joo':
    print('Osta latte')
    print('Juo latte')
    rahaa_taskussa = rahaa_taskussa - laten_hinta
elif rahaa_taskussa >= kahvin_hinta and maistuuko_kahvi == 'Joo':
    print('Osta normi kahvi')
    rahaa_taskussa = rahaa_taskussa - kahvin_hinta
elif rahaa_taskussa >= teen_hinta:
    print('Ota tee')
    rahaa_taskussa = rahaa_taskussa - teen_hinta
else:
    print('Lähde kotiin')

if rahaa_taskussa == 0:
    print('Rahat loppu')
else:
    print(f'Sinulla on vielä {rahaa_taskussa} euroa taskussa.')



