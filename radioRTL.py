class Radio():

    runRadio = False
    frequence = 87.5
    minFreq = 22.0
    maxFreq = 1100.0
    modulat = 'wbfm'
    sampled = 48000
    resampled = 24000
    cmd = ''
    running = ''
    command = None
    saveFile = 'data/RadioList.rsl'
    radioList = [['91.0Mhz - RTS', 91.0, 'wbfm'],
                 ['91.6Mhz - COULEUR3', 91.6, 'wbfm'],
                 ['102.4Mhz - ROUGE FM', 102.4, 'wbfm']]

    def play(self, listNumber = 0):
        if listNumber:
            self.frequence = self.radioList[listNumber-1][1]
            self.madulat = self.radioList[listNumber-1][2]
        self.cmd = self.createcmd()
        if self.runRadio:
            if self.running != self.cmd:
                self.stop()
                print(self.cmd)
                self.running = self.cmd
                self.runRadio = True
            else:
                self.stop()
        else:
            print(self.cmd)
            self.running = self.cmd
            self.runRadio = True
        self.update()
        return

    def stop(self):
        print('killall rtl_fm')
        self.running = ''
        self.runRadio = False
        return

    def previous(self):
        if self.runRadio:
            self.stop()
            self.frequence = round(self.frequence - 0.1, 1)
            self.checkMinMax()
            self.play()
        else:
            self.frequence = round(self.frequence - 0.1, 1)
            self.checkMinMax()
        self.update()
        return

    def next(self):
        if self.runRadio:
            self.stop()
            self.frequence = round(self.frequence + 0.1, 1)
            self.checkMinMax()
            self.play()
        else:
            self.frequence = round(self.frequence + 0.1, 1)
            self.checkMinMax()
        self.update()
        return

    def shiftL(self):
        if self.runRadio:
            self.stop()
            self.frequence -= 1
            self.checkMinMax()
            self.play()
        else:
            self.frequence -= 1
            self.checkMinMax()
        self.update()
        return

    def shiftR(self):
        if self.runRadio:
            self.stop()
            self.frequence += 1
            self.checkMinMax()
            self.play()
        else:
            self.frequence += 1
            self.checkMinMax()
        self.update()
        return

    def update(self, commandNumber = 0):
        if self.command:
            if commandNumber != 0:
                self.command[commandNumber]()
            elif type(self.command) == list:
                for x in range(len(self.command)):
                    self.command[x]()
            else:
                self.command()
        return

    def config(self, frequence=None, modulation=None, sample=None, resample=None, command=None, play=False):
        if frequence:
            self.frequence = frequence
        if modulation:
            self.modulat = modulation
        if sample:
            self.sampled = sample
        if resample:
            self.resampled = resample
        if command:
            self.command = command
        if play or self.runRadio:
            self.play()
        return

    def createcmd(self):
        return 'rtl_fm -f %s -M %s -s %s -r %s | aplay -f S16_LE -r %s &' %(int(self.frequence*1000000), self.modulat, self.sampled, self.resampled, self.resampled)

    def checkMinMax(self):
        if self.frequence >= self.maxFreq:
            self.frequence = self.maxFreq
        if self.frequence <= self.minFreq:
            self.frequence = self.minFreq

    def removeSave(self, index):
        self.radioList.pop(index)

    def saveRadio(self):
        radio = ['%sMhz'%self.frequence, self.frequence, self.modulat]
        self.radioList.append(radio)

    def __init__(self, frequence=87.5, modulation='wbfm', sample=48000, resample=24000, command=None, saveFile='data/RadioList.rsl'):

        def readSave():
            try:
                file = open(self.saveFile, mode='r')
                read = file.readlines()
                parti = read.split('\n')
                for li in part:
                    sav = li.split(',')
                    sav[1] = float(sav[1])
                    self.radioList.append(sav)
            except:
                file = open(self.saveFile, mode='w')
                file.close
                
        self.frequence = frequence
        self.modulat = modulation
        self.sampled = sample
        self.resampled = resample
        self.command = command
        self.saveFile = saveFile
        readSave()
        return
