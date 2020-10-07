import speedtest
from datetime import datetime

def checkSpeed():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    
    return s.results

def printResults(results):
    print('Download: {:.2f} Mb/s\n'.format(results.download / 1024 / 1024))
    print('Upload: {:.2f} Mb/s\n'.format(results.upload / 1024 / 1024))
    print('Ping: ', results.ping)

def fileWrite(results):
    todays_date = datetime.now()
    todays_date_full = todays_date.strftime("%Y-%m-%d %H:%M")
    todays_date_simplified = todays_date.strftime("%Y-%m-%d")
    
    file = open(todays_date_simplified + ".txt", "a")
    file.write(todays_date_full + "\n")
    file.write('Download: {:.2f} Mb/s\n'.format(results.download / 1024 / 1024))
    file.write('Upload: {:.2f} Mb/s\n'.format(results.upload / 1024 / 1024))
    file.write('Ping: ' + str(results.ping) + '\n')
    file.write("--------\n")
    file.write("\n")
    file.close()

if __name__ == "__main__":
    
    results = checkSpeed()
    printResults(results)
    fileWrite(results)
