device_ven = ''
device_prod = ''
device_rev = ''
serial = ''
date = ''

deviceInfoStart = 'Device Install (Hardware initiated) - SWD'
searchDateStart = '2021/04/08 21'
searchDateEnd = '2021/04/08 23'

device_list = list()

with open('setupapi.dev.log') as in_file:
    for line in in_file:
        if deviceInfoStart in line and ('Ven_' in line or 'Vid_' in line):
            dateLine = next(in_file)

            info = line.split('#')
            deviceInfo = info[1].split('&')

            try:
                device_ven = (deviceInfo[1])[4:]
            except IndexError:
                device_ven = ''
            
            try:
                device_prod = (deviceInfo[2])[5:]
            except IndexError:
                device_prod = ''

            try:
                device_rev = (deviceInfo [3])[4:]
            except IndexError:
                device_rev = ''

            try:
                serial = info[2]
            except IndexError:
                serial = ''

            try:
                date = dateLine[19:]
            except ValueError:
                date = ''

            device_list.append([device_ven, device_prod, device_rev, serial, date])

for i in range(len(device_list)):
    print('[INFO ' + str(i+1) + '] Vendor:        ' + device_list[i][0])
    print('[INFO ' + str(i+1) + '] Product ID:    ' + device_list[i][1])
    print('[INFO ' + str(i+1) + '] Revision:      ' + device_list[i][2])
    print('[INFO ' + str(i+1) + '] Serial number: ' + device_list[i][3])
    print('[INFO ' + str(i+1) + '] Date:          ' + device_list[i][4])

for i in range(len(device_list)):
    targetTime_Start = searchDateStart[11:13]
    targetTime_End = searchDateEnd[11:13]
    targetDate = searchDateEnd[:10]

    deviceTime = (device_list[i][4])[11:13]
    deviceDate = (device_list[i][4])[:10]

    if ((deviceDate in targetDate) and (targetTime_Start <= deviceTime) and (targetTime_End >= deviceTime)):
        print('[RESULT] FOUND SEARCHED DEVICE')
        print('[RESULT] *** Device Info:')
        print('[RESULT] ******** Vendor: ' + device_list[i][0])
        print('[RESULT] **** Product ID: ' + device_list[i][1])
        print('[RESULT] *****  Revision: ' + device_list[i][2])
        print('[RESULT] * Serial number: ' + device_list[i][3])
        print('[RESULT] ***** Date used: ' + device_list[i][4])