import speedtest

def checkspeed():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    
    return s.results

def printresults(results):
    print('Download: {:.2f} Mb/s\n'.format(results.download / 1024 / 1024))
    print('Upload: {:.2f} Mb/s\n'.format(results.upload / 1024 / 1024))
    print('Ping: ', results.ping)

if __name__ == "__main__":
    results = checkspeed()
    printresults(results)
