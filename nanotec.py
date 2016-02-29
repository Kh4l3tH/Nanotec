'''
Created on Jun 16, 2011

@author: maxim
'''
import io

class Nanotec(object):
  def __init__(self, comPort, tries = 3):
    self.tries = tries
    self.comPort = io.TextIOWrapper(io.BufferedRWPair(comPort, comPort, newline='\r'))
    self.setMotor(1)
    self.connected = True

  def executeCmd(self, command, value = ''):
    "Befehl zur SMCI schicken."
    try:
      strCmd = str(command)
      strVal = str(value)
    except ValueError:
      raise ValueError("Uebergebene Werte koennen nicht in Strings konvertiert werden.")
      return False

    counter = 0
    if strCmd[0] == ':':
      strCmd = strCmd + '=' #Bei einem langen Befehl muss ein = angefuegt werden
    cmd = self.motor+strCmd+strVal+'\r'
    while counter < self.tries:
      try:
        self.comPort.write('#'+cmd)
        self.comPort.flush()
        line = self.comPort.readline()
      except OSError:
        self.connected = False
        raise ValueError('OSError ?????')
        return False
      if line == cmd:
        return True
      else:
        counter += 1
    print line
    raise ValueError("Die Anzahl der Versuche wurde ueberschritten.")
    return False

  def getVal(self, command, value = ''):
    try:
      strCmd = str(command)
      strVal = str(value)
    except ValueError:
      raise ValueError("Uebergebene Werte koennen nicht in Strings konvertiert werden.")
      return False

    counter = 0
    if strCmd[0] != ':' or (strCmd[0] == ':' and (strCmd[1] == 'b' or strCmd[1] == 'B')):
      strCmd = 'Z' + strVal + strCmd #Bei einem kurzen Befehl ein Z anhaengen
    cmd = '#'+self.motor+strCmd+'\r'
    while counter < self.tries:
      counter += 1
      try:
        self.comPort.write(cmd)
        self.comPort.flush()
        wholeCmd = self.comPort.readline()
      except OSError:
        self.connected = False
        raise ValueError('OSError ?????')
        return False
      if wholeCmd != '':
        splitCmd = wholeCmd.split(' ')
        sign = 0
        if splitCmd[0] == wholeCmd:
          splitCmd = wholeCmd.split('+')
          sign = 1
        if splitCmd[0] == wholeCmd:
          splitCmd = wholeCmd.split('-')
          sign = -1
        if splitCmd[0] != self.motor+strCmd:
          print splitCmd[0]
          raise ValueError('Falscher Befehl!')
          return -1
        if sign > 0 or sign < 0:
          try:
            value = int(splitCmd[1])
          except ValueError:
            print "ValueError2"
            raise ValueError(splitCmd)
            return -1
          return sign*value
        else:
          return splitCmd[1]
      if counter == self.tries:
        raise ValueError('Timeout')
        return -1

  def getState(self):
    '''
    Diese Funktion holt den Status der Nanotec-Karte und gibt ihn zurueck.
    '''
    counter = 0
    cmd = '#'+self.motor+'$\r'

    while counter < self.tries:
      counter += 1
      try:
        self.comPort.write(cmd)
        self.comPort.flush()
        wholeCmd = self.comPort.readline()
      except OSError:
        self.connected = False
        raise ValueError('OSError ?????')
        return False
      if wholeCmd != '':
        splitCmd = wholeCmd.split('$')
        try:
          motorVal = int(splitCmd[0])
          stateVal = int(splitCmd[1])
        except ValueError:
          print "ValueError2"
          raise ValueError(splitCmd)
          return False
        return stateVal
    if counter == self.tries:
      raise ValueError('Timeout')
      return False

  def setMotor(self, motor):
    '''
    Diese Funktion setzt den Motor, an den alle Funktionen gesendet werden sollen.\n
    Der Rueckgabewert legt fest, ob der Motor zugewiesen werden konnte.
    '''
    if isinstance(motor, int):
      if motor > 0 and motor < 256:
        self.motor = str(motor)
        return True
      else:
        raise ValueError("Motor-ID ausserhalb des Breichs.")
    if isinstance(motor, str):
      if motor == '*':
        self.motor = motor
        return True
      else:
        raise ValueError("Als String fuer eine Motor-ID ist einzig * moeglich.")
    raise ValueError(motor)
    return False

  def getMotor(self):
    try:
      return int(self.motor)
    except ValueError:
      return self.motor

  def setTries(self, tries):
    "Setzt die Anzahl der Versuche zur Kommunikation."
    self.tries = tries

  def getTimeout(self):
    return self.comPort.timeout

  def setTimeout(self, time):
    self.comPort.timeout = time
