import os
import subprocess
robotList = ['myChinarobot','myBhutanrobot','myBurmarobot','myIndiarobot','myJapanrobot','myNKorearobot',
             'mySKorearobot','mySrilankarobot', 'myVietnamrobot', 'myIranrobot', 'myIraqrobot', 'myIsraelrobot',
             'myJordanrobot','myTaiwanrobot', 'myOmanrobot', 'myNepalrobot', 'myQatarrobot', 'myYemenrobot','myThailandrobot']
for i in robotList:
    print (i)

proc = subprocess.Popen(["hostname"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
print('*'*40)
print ("program output:", out)
print('above line should be hostname')