'''
Created on Jun 17, 2011

@author: maxim
'''
from nanotecConst import *
import nanotec
import serial

class Commands(object):
  def __init__(self, com):
    self.com = com

  def setTries(self, tries):
    "Setzt die Anzahl der Versuche zur Kommunikation."
    self.com.setTries(tries)

  def setMotor(self, motor):
    return self.com.setMotor(motor)

  def getMotor(self):
    return self.com.getMotor()

  def getIDs(self):
    motor = self.getMotor()
    time = self.com.getTimeout()
    self.com.setTimeout(0.05)
    ids = []
    for i in range(1,4):
      print i
      self.setMotor(i)
      if self.getVersion() != -1:
        ids.append(i)
    self.com.setTimeout(time)
    self.setMotor(motor)
    return ids


  def getStatusByte(self):
    '''
    Mit dieser Funktion kann das Statusbyte der Steuerung abgefragt werden.
    '''
    return self.com.getState()

  def isMotorReady(self):
    '''
    Diese Funktion liefert true zurueck, wenn das Bit 0 im Statusbyte gesetzt
    ist (Steuerung ist bereit).
    '''
    if self.com.getState() & 1 == 1:
      return True
    else:
      return False

  def isAtReferencePosition(self):
    '''
    Diese Funktion liefert true zurueck, wenn das Bit 1 im Statusbyte gesetzt ist
    (Nullposition erreicht).
    '''
    if self.com.getState() & 2 == 2:
      return True
    else:
      return False

  def hasPositionError(self):
    '''
    Diese Funktion liefert true zurueck, wenn das Bit 2 im Statusbyte gesetzt ist
    (Positionsfehler).
    '''
    if self.com.getState() & 4 == 4:
      return True
    else:
      return False

  def hasEndedTravelProfileAndStartInputStllActive(self):
    '''
    Diese Funktion liefert true zurueck, wenn das Bit 3 im Statusbyte gesetzt ist (Eingang 1
    ist gesetzt, waehrend Steuerung wieder bereit ist).
    '''
    if self.com.getState() & 8 == 8:
      return True
    else:
      return False

  def isPositionModeActive(self):
    '''
    Diese Funktion liefert true zurueck, wenn der Positionsmodus aktiv ist.
    '''
    posMod = self.com.getVal(POSITIONSMODUS)
    if posMod >= 1 and posMod <= 4:
      return True
    return False

  def isSpeedModeActive(self):
    '''
    Noch nicht getestet!
    Diese Funktion liefert true zurueck, wenn der Drehzahlmodus aktiv ist.
    '''
    posMod = self.com.getVal(POSITIONSMODUS)
    if posMod == 5:
      return True
    return False

  def isFlagPositionModeActive(self):
    '''
    Noch nicht getestet!
    Diese Funktion liefert true zurueck, wenn der Flagpositionsmodus aktiv ist.
    '''
    posMod = self.com.getVal(POSITIONSMODUS)
    if posMod == 6:
      return True
    return False

  def isClockDirectionModeActive(self):
    '''
    Noch nicht getestet!
    Diese Funktion liefert true zurueck, wenn der Takt-Richtungsmodus aktiv ist.
    '''
    posMod = self.com.getVal(POSITIONSMODUS)
    if posMod >= 7 and posMod <= 10:
      return True
    return False

  def isJoyStickModeActive(self):
    '''
    Noch nicht getestet!
    Diese Funktion liefert true zurueck, wenn der Joystickmodus aktiv ist.
    '''
    posMod = self.com.getVal(POSITIONSMODUS)
    if posMod == 12:
      return True
    return False

  def isAnalogModeActive(self):
    '''
    Noch nicht getestet!
    Diese Funktion liefert true zurueck, wenn der Analogmodus aktiv ist.
    '''
    posMod = self.com.getVal(POSITIONSMODUS)
    if posMod == 11:
      return True
    return False

  def isTorqueModeActive(self):
    '''
    Noch nicht getestet!
    Diese Funktion liefert true zurueck, wenn der Drehmomentmodus aktiv ist.
    '''
    posMod = self.com.getVal(POSITIONSMODUS)
    if posMod == 15:
      return True
    return False

  def startTravelProfile(self):
    '''
    Noch nicht getestet!
    Mit dieser Funktion kann das Fahrprofil gestartet werden.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(START)

  def stopTravelProfile(self):
    '''
    Noch nicht getestet!
    Mit dieser Funktion kann das Fahrprofil gestoppt werden.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(STOP, 1)

  def quickStopTravelProfile(self):
    '''
    Noch nicht getestet!
    Mit dieser Funktion kann das Fahrprofil schnell gestoppt werden.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(STOP)

  def increaseFrequency(self):
    '''
    Noch nicht getestet!
    Diese Funktion erhoeht die Frequenz des Motors.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(FREQUENZ_ERHOEHEN)

  def decreaseFrequency(self):
    '''
    Noch nicht getestet!
    Diese Funktion erniedrigt die Frequenz des Motors.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(FREQUENZ_SENKEN)

  def triggerOn(self):
    '''
    Noch nicht getestet!
    Diese Funktion sendet den Trigger-Befehl an den Motor.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(TRIGGER)

  def setRamp(self, ramp):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die Beschleunigungsrampe.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(BESCHLEUNIGUNGSRAMPE, ramp)

  def setBreak(self, breakTime):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die Pausenzeit in Millisekunden.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(SATZPAUSE, breakTime)

  def chooseRecord(self, recordNumber):
    '''
    Noch nicht getestet!
    Diese Funktion laedt einen bestimmten Satz.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(SATZLADEN, recordNumber)

  def getRamp(self, recordNumber):
    '''
    Noch nicht getestet!
    Diese Funktion liest die Beschleunigungsrampe des ausgewaehlten Satzes aus.
    '''
    return self.com.getVal(BESCHLEUNIGUNGSRAMPE, recordNumber)

  def getBreak(self, recordNumber):
    '''
    Noch nicht getestet!
    Diese Funktion liest die Pausenzeit in Millisekunden des ausgewaehlten Satzes aus.
    '''
    return self.com.getVal(SATZPAUSE, recordNumber)

  def setDirection(self, direction):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die Drehrichtung des Motors nach links (0) oder nach rechts (1).\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(DREHRICHTUNG, direction)

  def getDirection(self, recordNumber):
    '''
    Noch nicht getestet!
    Diese Funktion liest die Drehrichtung des Motors aus.\n
    0 - links\n
    1 - rechts
    '''
    return self.com.getVal(DREHRICHTUNG, recordNumber)

  def setMaxFrequency(self, maxFrequency):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die Zielfrequenz.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(MAX_FREQUENZ, maxFrequency)

  def getMaxFrequency(self, recordNumber):
    '''
    Noch nicht getestet!
    Diese Funktion liest die Zielfrequenz des ausgewaehlten Satzes.
    '''
    return self.com.getVal(MAX_FREQUENZ, recordNumber)

  def setRotationMode(self, rotationMode):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Drehgeberueberwachungsmodus:\n
    0 - ausgeschaltet\n
    1 - Pruefen am Ende\n
    2 - Pruefen waehrend der Fahrt\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(UEBERWACHUNGSMODUS, rotationMode)

  def getRotationMode(self):
    '''
    Noch nicht getestet!
    Diese Funktion liest den Drehgeberueberwachungsmodus.\n
    0 - ausgeschaltet\n
    1 - Pruefen am Ende\n
    2 - Pruefen waehrend der Fahrt
    '''
    return self.com.getVal(UEBERWACHUNGSMODUS)

  def resetPositionError(self, useEncoderValue, position=0):
    '''
    Noch nicht getestet!
    Diese Funktion kann ein Positionsfehler zurueckgesetzt und der Wert des Positionszaehlers
    gesetzt werden.\n
    useEncoderValue = TRUE - Positionszaehler auf Wert des Drehgebers setzen\n
    useEncoderValue = FALSE - Positionszaehler auf Wert von Position setzen\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    if useEncoderValue:
      return self.com.executeCmd(RESET_POSITIONSFEHLER)
    else:
      return self.com.executeCmd(RESET_POSITIONSFEHLER, position)

  def resetAllSettings(self):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die Einstellungen der Steuerung auf die Defaultwerte.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(RESET_EINSTELLUNGEN)

  def getVersion(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Versionsstring zurueck.
    '''
    return self.com.getVal(VERSION)

  def setSendStatusWhenCompleted(self, sendStatus):
    '''
    Noch nicht getestet!
    Diese Funktion schaltet das selbstaendige Senden eines Status am Ende einer Fahrt:\n
    0 - ausgeschaltet\n
    1 - automatisches Senden\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(STATUS_ENDE_FAHRT, sendStatus)

  def getSendStatusWhenCompleted(self):
    '''
    Noch nicht getestet!
    Diese Funktion liest, ob das selbstaendige Senden eines Status am Ende einer Fahrt eingeschaltet ist:\n
    0 - ausgeschaltet\n
    1 - automatisches Senden
    '''
    return self.com.getVal(STATUS_ENDE_FAHRT)

  def getPosition(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Wert des Positionszaehlers aus.
    '''
    return self.com.getVal(POSITION)

  def getIO(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Status der Eingaenge als Integer-Wert zurueck.
    '''
    return self.com.getVal(IO)

  def setIO(self, ioState):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Status der Ausgaenge ueber einen Integer-Wert.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(IO, ioState)

  def setInputMaskEdge(self, ioMask):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die Polaritaet der Ein- und Ausgaenge.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(IOMASKE, ioMask)

  def getInputMaskEdge(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt die aktuelle Polaritaet der Ein- und Ausgaenge zurueck.
    '''
    return self.com.getVal(IOMASKE)

  def setRecord(self, recordNumber):
    '''
    Noch nicht getestet!
    Diese Funktion speichert die zuvor gesetzten Satzparameter in dem Satz mit der
    uebergebenen Nummer.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(SATZ_SPEICHERN, recordNumber)

  def setPlay(self, play):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Totbereich des Analogeingangs.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(TOTBEREICH, play)

  def getPlay(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Wert fuer den Totbereich des Analogeingangs zurueck.
    '''
    return self.com.getVal(TOTBEREICH)

  def setDebounceTime(self, debounceTime):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die Entprellzeit fuer die Eingaenge in Millisekunden.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(ENTPRELLZEIT, debounceTime)

  def getDebounceTime(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt die Entprellzeit fuer die Eingaenge in Millisekunden zrueck.
    '''
    return self.com.getVal(ENTPRELLZEIT)

  def setSoftwareFilter(self, softwareFilter):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Wert fuer den Filter des Analogeingangs.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(ANALOGFILTER, softwareFilter)

  def getSoftwareFilter(self):
    '''
    Noch nicht getestet!
    Diese Funktion liest den Wert fuer den Filter des Analogeingangs aus.
    '''
    return self.com.getVal(ANALOGFILTER)

  def setStepMode(self, stepMode):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Schrittmodus:\n
    1 - Vollschritt\n
    2 - Halbschritt\n
    4 - Viertelschritt\n
    :\n
    64 - 64tel Schritt\n
    254 - Vorschubkonstante\n
    255 - Adaptiver Mikroschritt\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(SCHRITTMODUS, stepMode)

  def getStepMode(self):
    '''
    Noch nicht getestet!
    Diese Funktion liest den aktuellen Schrittmodus aus:\n
    1 - Vollschritt\n
    2 - Halbschritt\n
    4 - Viertelschritt\n
    :\n
    64 - 64tel Schritt\n
    254 - Vorschubkonstante\n
    255 - Adaptiver Mikroschritt\n
    '''
    return self.com.getVal(SCHRITTMODUS)

  def setMotorAddress(self, newMotorAddress):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die Motoradresse.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(MOTORADRESSE, newMotorAddress)

  def getMotorAddress(self, selectedMotor):
    '''
    Noch nicht getestet!
    Diese Funktion liest die Motoradresse aus. Der uebergebene Wert ist egal,
    da der Befehl an alle Busteilnehmer geschickt wird.\n
    ES SOLLTE NUR EINE STEUERUNG AM RS-485 BUS ANGESCHLOSSEN SEIN.
    '''
    return self.com.getVal(MOTORADRESSE, selectedMotor)

  def getErrorAddress(self):
    '''
    Noch nicht getestet!
    Diese Funktion liest die Fehleradresse aus, an der sich der letzte Fehlercode befindet.
    '''
    return self.com.getVal(ERRORADRESSE)

  def getError(self, errorAddress):
    '''
    Noch nicht getestet!
    Diese Funktion liest den Fehler (Status) an der uebergebenen Adresse.
    '''
    return self.com.getVal(ERRORADRESSE, errorAddress)

  def setEnableAutoCorrect(self, recordNumber, autoCorrect):
    '''
    Noch nicht getestet!
    Diese Funktion konfigueriert die automatische Fehlerkorrektur des Motors.\n
    Der Wert von autoCorrect gibt an, ob eine Korrektur stattfinden soll.\n
    Der Parameter recordNumber ist dabei die Satznummer, mit der ein eventueller Fehler
    korrigiert werden soll.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    if autoCorrect:
      return self.com.executeCmd(AUTOKORREKTUR, autoCorrect)
    else:
      return self.com.executeCmd(AUTOKORREKTUR, 0)

  def getEnableAutoCorrect(self, recordNumber):
    '''
    Noch nicht getestet!
    Diese Funktion liest aus, welcher Satz fuer die automatische Fehlerkorrektur gesetzt ist.
    '''
    return self.com.getVal(AUTOKORREKTUR, recordNumber)

  def setSwingOutTime(self, swingOutTime):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die Ausschwingzeit.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(AUSSCHWINGZEIT, swingOutTime)

  def getSwingOutTime(self):
    '''
    Noch nicht getestet!
    Diese Funktion liest die Ausschwingzeit.
    '''
    return self.com.getVal(AUSSCHWINGZEIT)

  def setNextOperation(self, recordNumber):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Folgesatz.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(FOLGESATZ, recordNumber)

  def getNextOperation(self, recordNumber):
    '''
    Noch nicht getestet!
    Diese Funktion liest die Nummer des Folgesatzes.
    '''
    return self.com.getVal(FOLGESATZ, recordNumber)

  def setPhaseCurrent(self, phaseCurrent):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Phasenstrom in Prozent. Werte ueber 100 sollten vermieden werden.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(PHASENSTROM, phaseCurrent)

  def getPhaseCurrent(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Phasenstrom in Prozent zurueck.
    '''
    return self.com.getVal(PHASENSTROM)

  def setCurrentReduction(self, currentReduction):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Phasenstrom bei Stillstand in Prozent. Werte ueber 100 sollten
    vermieden werden.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(PHASENSTROM_STILLSTAND, currentReduction)

  def getCurrentReduction(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Phasenstrom bei Stillstand in Prozent zurueck.
    '''
    return self.com.getVal(PHASENSTROM_STILLSTAND)

  def setLimitSwitchBehavior(self, data):
    '''
    Noch nicht getestet!
    Diese Funktion setzt das Endschalterverhalten.\n
    refBehaviorsInternal - Verhalten des internen Endschalters bei Referenzfahrt\n
    norBehaviorsInternal - Verhalten des internen Endschalters bei Normalfahrt\n
    refBehaviorsExternal - Verhalten des externen Endschalters bei Referenzfahrt\n
    norBehaviorsExternal - Verhalten des externen Endschalters bei Normalfahrt\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    behavior = data[0] | data[1] | data[2] | data[3]
    return self.com.executeCmd(ENDSCHALTERVERHALTEN, behavior)

  def getLimitSwitchBehavior(self):
    '''
    Noch nicht getestet!
    Diese Funktion liest das Endschalterverhalten aus.\n
    refBehaviorsInternal - Verhalten des internen Endschalters bei Referenzfahrt\n
    norBehaviorsInternal - Verhalten des internen Endschalters bei Normalfahrt\n
    refBehaviorsExternal - Verhalten des externen Endschalters bei Referenzfahrt\n
    norBehaviorsExternal - Verhalten des externen Endschalters bei Normalfahrt\n
    '''
    behavior = self.com.getVal(ENDSCHALTERVERHALTEN)
    refBehaviorsInternal = behavior & (2**0 + 2**1) #Bit 0 - 1
    norBehaviorsInternal = behavior & (2**2 + 2**3 + 2**4 + 2**5) #Bit 2 - 5
    refBehaviorsExternal = behavior & (2**9 + 2**10) #Bit 9 - 10
    norBehaviorsExternal = behavior & (2**11 + 2**12 + 2**13 + 2**14) #Bit 11 - 14
    return refBehaviorsInternal, norBehaviorsInternal, refBehaviorsExternal, norBehaviorsExternal

  def setReverseClearance(self, reverseClearance):
    '''
    Noch nicht getestet!
    Diese Funktion setzt das Umkehrspiel in Schritten.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(UMKEHRSPIEL, reverseClearance)

  def getReverseClearance(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt das Umkehrspiel in Schritten aus.
    '''
    return self.com.getVal(UMKEHRSPIEL)

  def setAnalogueMin(self, analogueMin):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die minimale Spannung fuer den Analogeingang.\n
    Erlaubte Werte -100 - +100, wobei 100 == 10V.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(ANALOG_MIN_SPANNUNG, analogueMin)

  def getAnalogueMin(self):
    '''
    Diese Funktion gibt die minimale Spannung fuer den Analogeingang aus.\n
    Erlaubte Werte -100 - +100, wobei 100 == 10V.
    '''
    return self.com.getVal(ANALOG_MIN_SPANNUNG)

  def setAngleDeviationMax(self, deviation):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die maximale Winkelabweichung zwischen Sollposition und Drehgeberwert.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(MAX_WINKELABWEICHUNG, deviation)

  def getAngleDeviationMax(self):
    '''
    Diese Funktion gibt die maximale Winkelabweichung zwischen Sollposition und Drehgeberwert aus.
    '''
    return self.com.getVal(MAX_WINKELABWEICHUNG)

  def setAnalogueMax(self, analogueMax):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die maximale Spannung fuer den Analogeingang.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(ANALOG_MAX_SPANNUNG, analogueMax)

  def getAnalogueMax(self):
    '''
    Diese Funktion gibt die maximale Spannung fuer den Analogeingang aus.
    '''
    return self.com.getVal(ANALOG_MAX_SPANNUNG)

  def setSteps(self, steps):
    '''
    Diese Funktion setzt die Anzahl der Schritte.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(VERFAHRWEG, steps)

  def getSteps(self, recordNumber):
    '''
    Diese Funktion liest die Anzahl der Schritte aus.
    '''
    return self.com.getVal(VERFAHRWEG, recordNumber)

  def setStartFrequency(self, startFrequency):
    '''
    Diese Funktion setzt die Startfrequenz.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(STARTFREQUENZ, startFrequency)

  def getStartFrequency(self, recordNumber):
    '''
    Diese Funktion gibt die Startfrequenz aus.
    '''
    return self.com.getVal(STARTFREQUENZ, recordNumber)

  def setMaxFrequency2(self, maxFrequency):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die obere Maximalfrequenz.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(MAX_FREQUENZ2, maxFrequency)

  def getMaxFrequency2(self, recordNumber):
    '''
    Noch nicht getestet!
    Diese Funktion gibt die obere Maximalfrequenz aus.
    '''
    return self.com.getVal(MAX_FREQUENZ2, recordNumber)

  def setSuppressResponse(self, suppress):
    '''
    Noch nicht getestet!
    Diese Funktion aktiviert oder deaktiviert die Antwortunterdrueckung beim Senden:\n
    0 - Antwortunterdrueckung ein\n
    1 - Antwortunterdrueckung aus\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(ANTWORTUNTERDRUECKUNG, suppress)

  def setDirectionReverse(self, directionReverse):
    '''
    Diese Funtkion setzt die Drehrichtungsumkehr.\n
    1 - aktiviert\n
    0 - deaktiviert\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(DREHRICHTUNGSUMKEHR, directionReverse)

  def getDirectionReverse(self, recordNumber):
    '''
    Diese Funktion liest die Drehrichtungsumkehr aus.\n
    1 - aktiviert\n
    0 - deaktiviert
    '''
    return self.com.getVal(DREHRICHTUNGSUMKEHR, recordNumber)

  def setEncoderDirection(self, encoderDirection):
    '''
    Diese Funktion setzt die Encoderdrehrichtung. Ist der Parameter 1, so wird die Richtung
    des Drehencoders umgekehrt.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(ENCODERRICHTUNG, encoderDirection)

  def getEncoderDirection(self):
    '''
    Diese Funktion gibt aus, ob die Encoderrehrichtung umgekehrt wird.
    '''
    return self.com.getVal(ENCODERRICHTUNG)

  def getEncoderRotary(self):
    '''
    Diese Funktion liest die Encoderposition aus.
    '''
    return self.com.getVal(ENCODERPOSITION)

  def setRampType(self, rampType):
    '''
    Diese Funktion setzt den Rampentyp.\n
    0 - Trapezrampe\n
    1 - Sinusrampe\n
    2 - Jerkfreerampe\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(RAMPENTYP, rampType)

  def getRampType(self):
    '''
    Diese Funktion gibt den Rampentyp aus:\n
    0 - Trapezrampe\n
    1 - Sinusrampe\n
    2 - Jerkfreerampe
    '''
    return self.com.getVal(RAMPENTYP)

  def setJerk(self, jerk):
    '''
    Funktioniert nicht!
    Diese Funktion setzt den Ruck in 100/s**2.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(RUCK, jerk)

  def getJerk(self, recordNumber=''):
    '''
    Funktioniert nicht!
    Diese Funktion gibt den Ruck in 100/s**2 aus.
    '''
    return self.com.getVal(RUCK, recordNumber)

  def setBrakeRamp(self, rampBrake):
    '''
    Diese Funktion setzt die Bremsrampe.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(BREMSRAMPE, rampBrake)

  def getBrakeRamp(self, recordNumber=''):
    '''
    Diese Funktion liest die Bremsrampe aus.
    '''
    return self.com.getVal(BREMSRAMPE, recordNumber)

  def setBrakeJerk(self, jerk=''):
    '''
    Funktioniert nicht!
    Diese Funktion setzt den Bremsruck in 100/s**2.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(BREMSRUCK, jerk)

  def getBrakeJerk(self, recordNumber=''):
    '''
    Funktioniert nicht!
    Diese Funktion gibt den Bremsruck in 100/s**2 aus.
    '''
    return self.com.getVal(BREMSRUCK, recordNumber)

  def setQuickStoppRamp(self, rampQuickStopp):
    '''
    Diese Funktion setzt die Quickstoprampe.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(QUICKSTOPRAMPE, rampQuickStopp)

  def getQuickStoppRamp(self, recordNumber):
    '''
    Diese Funktion liest die Quickstoprampe aus.
    '''
    return self.com.getVal(QUICKSTOPRAMPE, recordNumber)

  def setRepeat(self, repeats):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die Anzahl der Wiederholungen.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(WIEDERHOLUNGEN, repeats)

  def getRepeat(self, recordNumber):
    '''
    Noch nicht getestet!
    Diese Funktion liest die Anzahl der Wiederholungen aus.
    '''
    return self.com.getVal(WIEDERHOLUNGEN, recordNumber)

  def setPositionType(self, positionType):
    '''
    Diese Funktion setzt den Positionstyp.\n
    1 - relative Positionierung\n
    2 - absolute Positionierung\n
    3 - interne Referenzfahrt\n
    4 - externe Referenzfahrt\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(POSITIONSMODUS, positionType)

  def getPositionType(self, recordNumber):
    '''
    Diese Funktion gibt den Positionstyp aus.\n
    1 - relative Positionierung\n
    2 - absolute Positionierung\n
    3 - interne Referenzfahrt\n
    4 - externe Referenzfahrt\n
    '''
    return self.com.getVal(POSITIONSMODUS, recordNumber)


  def setKalibrierModus(self):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Operationsmodus 17, welcher den Kalibrierlauf des
    Assistenten durchfuehrt.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.setPositionType(17)

  def setClosedLoop(self, value):
    '''
    Diese Funktion aktiviert oder deaktiviert den Closed Loop Modus.\n
    1 - an\n
    0 - aus\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(CLOSED_LOOP, value)

  def getClosedLoop(self):
    '''
    Diese Funktion gibt aus, ob der Closed Loop Modus aktiviert ist.
    '''
    return self.com.getVal(CLOSED_LOOP)

  def getCLLoadAngle(self, tripleNumber):
    '''
    Noch nicht getestet!
    Diese Funktion liest einen Lastwinkel des Motors aus dem Closed-Loop-Testlauf aus.\n
    Der Parameter ist dabei die Nummer (0-9) des Werts, der gelesen werden soll.
    '''
    return self.com.getVal(LASTWINKEL[tripleNumber])

  def getClosedLoopOlaCurrent(self, tripleNumber):
    '''
    Noch nicht getestet!
    Diese Funktionen liest einen Korrekturwert des Stromreglers aus dem Closed-Loop-Testlauf aus.\n
    Der Parameter ist dabei die Nummer (0-6) des Werts, der gelesen werden soll.
    '''
    return self.com.getVal(STROMREGLER[tripleNumber])

  def getClosedLoopOlaVelocity(self, tripleNumber):
    '''
    Noch nicht getestet!
    Diese Funktion liest einen Korrekturwert des Geschwindigkeistreglers aus dem Closed-Loop-Testlauf aus.\n
    Der Parameter ist dabei die Nummer (0-6) des Werts, der gelesen werden soll.
    '''
    return self.com.getVal(GESCHWINDIGKEITSREGLER[tripleNumber])

  def getClosedLoopOlaLoadAngle(self, tripleNumber):
    '''
    Noch nicht getestet!
    Diese Funktion liest einen Korrekturwert des Positionsreglers aus dem Closed-Loop-Testlauf aus.\n
    Der Parameter ist dabei die Nummer (0-6) des Werts, der gelesen werden soll.
    '''
    return self.com.getVal(POSITIONSREGLER[tripleNumber])

  def setPositionWindow(self, positionWindow):
    '''
    Diese Funktion setzt das Toleranzfenster fuer die Endposition im Closed-Loop-Betrieb.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(TOLERANZFENSTER, positionWindow)

  def getPositionWindow(self):
    '''
    Diese Funktion gibt den Wert fuer das Toleranzfenster fuer die Endposition im
    Closed-Loop-Betrieb aus.
    '''
    return self.com.getVal(TOLERANZFENSTER)

  def setPositionWindowTime(self, time):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die Zeit fuer das Toleranzfenster der Endposition im Closed-Loop-Betrieb.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(TOLERANZFENSTER_ZEIT, time)

  def getPositionWindowTime(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Wert fuer die Zeit fuer das Toleranzfenster der Endposition
    im Closed-Loop-Betrieb aus.
    '''
    return self.com.getVal(TOLERANZFENSTER_ZEIT)

  def setFollowingErrorWindow(self, followingErrorWindow):
    '''
    Diese Funktion setzt den maximal erlaubten Schleppfehler im Closed-Loop-Betrieb.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(CL_SCHLEPPFEHLER, followingErrorWindow)

  def getFollowingErrorWindow(self):
    '''
    Diese Funktion gibt den Wert fuer den maximal erlaubten Schleppfehler im Closed-Loop-Betrieb aus.
    '''
    return self.com.getVal(CL_SCHLEPPFEHLER)

  def setSpeedErrorWindow(self, speedErrorWindow):
    '''
    Diese Funktion setzt die maximal erlaubte Drehzahlabweichung im Closed-Loop-Betrieb.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(CL_DREHZAHLABWEICHUNG, speedErrorWindow)

  def getSpeedErrorWindow(self):
    '''
    Diese Funktion gibt den Wert fuer die maximal erlaubte Drehzahlabweichung im Closed-Loop-Betrieb aus.
    '''
    return self.com.getVal(CL_DREHZAHLABWEICHUNG)

  def setFollowingErrorTimeout(self, timeout):
    '''
    Diese Funktion setzt die Zeit fuer den maximal erlaubten Schleppfehler im Closed-Loop-Betrieb.
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(CL_SCHLEPPFEHLER_ZEIT, timeout)

  def getFollowingErrorTimeout(self):
    '''
    Diese Funktion gibt die Zeit fuer den maximal erlaubten Schleppfehler im Closed-Loop-Betrieb aus.
    '''
    return self.com.getVal(CL_SCHLEPPFEHLER_ZEIT)

  def setSpeedErrorTimeout(self, timeout):
    '''
    Diese Funktion setzt die Zeit fuer die maximal erlaubte Drehzahlabweichung im Closed-Loop-Betrieb.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(CL_DREHZAHLABWEICHUNG_ZEIT, timeout)

  def getSpeedErrorTimeout(self):
    '''
    Diese Funktion gibt den Wert fuer die Zeit fuer die maximal erlaubte Drehzahlabweichung im Closed-
    Loop-Betrieb aus.
    '''
    return self.com.getVal(CL_DREHZAHLABWEICHUNG_ZEIT)

  def setRotencInc(self, rotencInc):
    '''
    Diese Funktion setzt die Inkremente des Drehgebers.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(CL_INK_DREHGEBER, rotencInc)

  def getRotencInc(self):
    '''
    Diese Funktion gibt die Anzahl der Inkremente des Drehgebers aus.
    '''
    return self.com.getVal(CL_INK_DREHGEBER)

  def setBrakeTA(self, brake):
    '''
    Diese Funktion setzt die Wartezeit fuer das Abschalten der Bremsspannung.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(BREMSSPANNUNG_ABSCHALTEN, brake)

  def getBrakeTA(self):
    '''
    Diese Funktion gibt die Wartezeit fuer das Abschalten der Bremsspannung aus.
    '''
    return self.com.getVal(BREMSSPANNUNG_ABSCHALTEN)

  def setBrakeTB(self, brake):
    '''
    Diese Funktion setzt die Zeit zwischen dem Abschalten der Bremsspannung und dem Erlauben
    einer Motorbewegung.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(BREMSSPANNUNG_MOTORBEWEGUNG, brake)

  def getBrakeTB(self):
    '''
    Diese Funktion gibt die Zeit zwischen dem Abschalten der Bremsspannung und dem Erlauben
    einer Motorbewegung aus.
    '''
    return self.com.getVal(BREMSSPANNUNG_MOTORBEWEGUNG)

  def setBrakeTC(self, brake):
    '''
    Diese Funktion setzt die Wartezeit fuer das Abschalten des Motorstroms.\n
    Der Motorstrom wird durch Ruecksetzen des Freigabe-Signals abgeschaltet.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(MOTORSTROM_ABSCHALTEN, brake)

  def getBrakeTC(self):
    '''
    Diese Funktion gibt die Wartezeit fuer das Abschalten des Motorstroms aus.\n
    Der Motorstrom wird durch Ruecksetzen des Freigabe-Signals abgeschaltet.
    '''
    return self.com.getVal(MOTORSTROM_ABSCHALTEN)

  def setKPsZ(self, value):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Zaehler des P-Anteils des Positionsreglers.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(ZAEHLER_P_POSITIONSREGLER, value)

  def getKPsZ(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Zaehler des P-Anteils des Positionsreglers aus.
    '''
    return self.com.getVal(ZAEHLER_P_POSITIONSREGLER)

  def setKPsN(self, value):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Nenner des P-Anteils des Positionsreglers.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(NENNER_P_POSITIONSREGLER, value)

  def getKPsN(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Nenner des P-Anteils des Positionsreglers aus.
    '''
    return self.com.getVal(NENNER_P_POSITIONSREGLER)

  def setKIsZ(self, value):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Zaehler des I-Anteils des Positionsreglers.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(ZAEHLER_I_POSITIONSREGLER, value)

  def getKIsZ(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Zaehler des I-Anteils des Positionsreglers aus.
    '''
    return self.com.getVal(ZAEHLER_I_POSITIONSREGLER)

  def setKIsN(self, value):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Nenner des I-Anteils des Positionsreglers.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(NENNER_I_POSITIONSREGLER, value)

  def getKIsN(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Nenner des I-Anteils des Positionsreglers aus.
    '''
    return self.com.getVal(NENNER_I_POSITIONSREGLER)

  def setKDsZ(self, value):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Zaehler des D-Anteils des Positionsreglers.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(ZAEHLER_D_POSITIONSREGLER, value)

  def getKDsZ(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Zaehler des D-Anteils des Positionsreglers aus.
    '''
    return self.com.getVal(ZAEHLER_D_POSITIONSREGLER)

  def setKDsN(self, value):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Nenner des D-Anteils des Positionsreglers.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(NENNER_D_POSITIONSREGLER, value)

  def getKDsN(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Nenner des D-Anteils des Positionsreglers aus.
    '''
    return self.com.getVal(NENNER_D_POSITIONSREGLER)

  def setKPvZ(self, value):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Zaehler des P-Anteils des Geschwindigkeitsreglers.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(ZAEHLER_P_GESCHWINDIGKEITSREGLER, value)

  def getKPvZ(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Zaehler des P-Anteils des Geschwindigkeitsreglers aus.
    '''
    return self.com.getVal(ZAEHLER_P_GESCHWINDIGKEITSREGLER)

  def setKPvN(self, value):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Nenner des P-Anteils des Geschwingkeitsreglers.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(NENNER_P_GESCHWINDIGKEITSREGLER, value)

  def getKPvN(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Nenner des P-Anteils des Geschwingkeitsreglers aus.
    '''
    return self.com.getVal(NENNER_P_GESCHWINDIGKEITSREGLER)

  def setKIvZ(self, value):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Zaehler des I-Anteils des Geschwingkeitsreglers.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(ZAEHLER_I_GESCHWINDIGKEITSREGLER, value)

  def getKIvZ(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Zaehler des I-Anteils des Geschwingkeitsreglers aus.
    '''
    return self.com.getVal(ZAEHLER_I_GESCHWINDIGKEITSREGLER)

  def setKIvN(self, value):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Nenner des I-Anteils des Geschwingkeitsreglers.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(NENNER_I_GESCHWINDIGKEITSREGLER, value)

  def getKIvN(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Nenner des I-Anteils des Geschwingkeitsreglers aus.
    '''
    return self.com.getVal(NENNER_I_GESCHWINDIGKEITSREGLER)

  def setKDvZ(self, value):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Zaehler des D-Anteils des Geschwingkeitsreglers.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(ZAEHLER_D_GESCHWINDIGKEITSREGLER, value)

  def getKDvZ(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Zaehler des D-Anteils des Geschwingkeitsreglers aus.
    '''
    return self.com.getVal(ZAEHLER_D_GESCHWINDIGKEITSREGLER)

  def setKDvN(self, value):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Nenner des D-Anteils des Geschwingkeitsreglers.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(NENNER_D_GESCHWINDIGKEITSREGLER, value)

  def getKDvN(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Nenner des D-Anteils des Geschwingkeitsreglers aus.
    '''
    return self.com.getVal(NENNER_D_GESCHWINDIGKEITSREGLER)

  def setKPcssZ(self, value):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Zaehler des P-Anteils des kaskadierenden Positionsreglers.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(ZAEHLER_P_KASK_POSITIONSREGLER, value)

  def getKPcssZ(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Zaehler des P-Anteils des kaskadierenden Positionsreglers aus.
    '''
    return self.com.getVal(ZAEHLER_P_KASK_POSITIONSREGLER)

  def setKPcssN(self, value):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Nenner des P-Anteils des kaskadierenden Positionsreglers.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(NENNER_P_KASK_POSITIONSREGLER, value)

  def getKPcssN(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Nenner des P-Anteils des kaskadierenden Positionsreglers aus.
    '''
    return self.com.getVal(NENNER_P_KASK_POSITIONSREGLER)

  def setKIcssZ(self, value):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Zaehler des I-Anteils des kaskadierenden Positionsreglers.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(ZAEHLER_I_KASK_POSITIONSREGLER, value)

  def getKIcssZ(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Zaehler des I-Anteils des kaskadierenden Positionsreglers aus.
    '''
    return self.com.getVal(ZAEHLER_I_KASK_POSITIONSREGLER)

  def setKIcssN(self, value):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Nenner des I-Anteils des kaskadierenden Positionsreglers.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(NENNER_I_KASK_POSITIONSREGLER, value)

  def getKIcssN(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Nenner des I-Anteils des kaskadierenden Positionsreglers aus.
    '''
    return self.com.getVal(NENNER_I_KASK_POSITIONSREGLER)

  def setKDcssZ(self, value):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Zaehler des D-Anteils des kaskadierenden Positionsreglers.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(ZAEHLER_D_KASK_POSITIONSREGLER, value)

  def getKDcssZ(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Zaehler des D-Anteils des kaskadierenden Positionsreglers aus.
    '''
    return self.com.getVal(ZAEHLER_D_KASK_POSITIONSREGLER)

  def setKDcssN(self, value):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Nenner des D-Anteils des kaskadierenden Positionsreglers.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(NENNER_D_KASK_POSITIONSREGLER, value)

  def getKDcssN(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Nenner des D-Anteils des kaskadierenden Positionsreglers aus.
    '''
    return self.com.getVal(NENNER_D_KASK_POSITIONSREGLER)

  def setKPcsvZ(self, value):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Zaehler des P-Anteils des kaskadierenden Geschwindigkeitsreglers.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(ZAEHLER_P_KASK_GESCHWINDIGKEITSREGLER, value)

  def getKPcsvZ(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Zaehler des P-Anteils des kaskadierenden Geschwindigkeitsreglers aus.
    '''
    return self.com.getVal(ZAEHLER_P_KASK_GESCHWINDIGKEITSREGLER)

  def setKPcsvN(self, value):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Nenner des P-Anteils des kaskadierenden Geschwindigkeitsreglers.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(NENNER_P_KASK_GESCHWINDIGKEITSREGLER, value)

  def getKPcsvN(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Nenner des P-Anteils des kaskadierenden Geschwindigkeitsreglers aus.
    '''
    return self.com.getVal(NENNER_P_KASK_GESCHWINDIGKEITSREGLER)

  def setKIcsvZ(self, value):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Zaehler des I-Anteils des kaskadierenden Geschwindigkeitsreglers.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(ZAEHLER_I_KASK_GESCHWINDIGKEITSREGLER, value)

  def getKIcsvZ(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Zaehler des I-Anteils des kaskadierenden Geschwindigkeitsreglers aus.
    '''
    return self.com.getVal(ZAEHLER_I_KASK_GESCHWINDIGKEITSREGLER)

  def setKIcsvN(self, value):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Nenner des I-Anteils des kaskadierenden Geschwindigkeitsreglers.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(NENNER_I_KASK_GESCHWINDIGKEITSREGLER, value)

  def getKIcsvN(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Nenner des I-Anteils des kaskadierenden Geschwindigkeitsreglers aus.
    '''
    return self.com.getVal(NENNER_I_KASK_GESCHWINDIGKEITSREGLER)

  def setKDcsvZ(self, value):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Zaehler des D-Anteils des kaskadierenden Geschwindigkeitsreglers.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(ZAEHLER_D_KASK_GESCHWINDIGKEITSREGLER, value)

  def getKDcsvZ(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Zaehler des D-Anteils des kaskadierenden Geschwindigkeitsreglers aus.
    '''
    return self.com.getVal(ZAEHLER_D_KASK_GESCHWINDIGKEITSREGLER)

  def setKDcsvN(self, value):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Nenner des D-Anteils des kaskadierenden Geschwindigkeitsreglers.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(NENNER_D_KASK_GESCHWINDIGKEITSREGLER, value)

  def getKDcsvN(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Nenner des D-Anteils des kaskadierenden Geschwindigkeitsreglers aus.
    '''
    return self.com.getVal(NENNER_D_KASK_GESCHWINDIGKEITSREGLER)

  def setInput1Selection(self, inputSelection):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die Funktion fuer den Digitaleingang 1.\n
    0 - Benutzerdefiniert
    1 - Starte Satz / Fehlerreset
    2-6 - Satzauswahl Bit 0-4
    7 - Externer Referenzschalter
    8 - Trigger
    9 - Richtung
    10 - Freigabe
    11 - Takt
    12 - Taktrichtungsmodus 1
    13 - Taktrichtungsmodus 2\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(FUNKTION_EINGANG1, inputSelection)

  def getInput1Selection(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt die Funktion fuer den Digitaleingang 1 aus.\n
    0 - Benutzerdefiniert
    1 - Starte Satz / Fehlerreset
    2-6 - Satzauswahl Bit 0-4
    7 - Externer Referenzschalter
    8 - Trigger
    9 - Richtung
    10 - Freigabe
    11 - Takt
    12 - Taktrichtungsmodus 1
    13 - Taktrichtungsmodus 2\n
    '''
    return self.com.getVal(FUNKTION_EINGANG1)

  def setInput2Selection(self, inputSelection):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die Funktion fuer den Digitaleingang 2.\n
    0 - Benutzerdefiniert
    1 - Starte Satz / Fehlerreset
    2-6 - Satzauswahl Bit 0-4
    7 - Externer Referenzschalter
    8 - Trigger
    9 - Richtung
    10 - Freigabe
    11 - Takt
    12 - Taktrichtungsmodus 1
    13 - Taktrichtungsmodus 2\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(FUNKTION_EINGANG2, inputSelection)

  def getInput2Selection(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt die Funktion fuer den Digitaleingang 2 aus.\n
    0 - Benutzerdefiniert
    1 - Starte Satz / Fehlerreset
    2-6 - Satzauswahl Bit 0-4
    7 - Externer Referenzschalter
    8 - Trigger
    9 - Richtung
    10 - Freigabe
    11 - Takt
    12 - Taktrichtungsmodus 1
    13 - Taktrichtungsmodus 2\n
    '''
    return self.com.getVal(FUNKTION_EINGANG2)

  def setInput3Selection(self, inputSelection):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die Funktion fuer den Digitaleingang 3.\n
    0 - Benutzerdefiniert
    1 - Starte Satz / Fehlerreset
    2-6 - Satzauswahl Bit 0-4
    7 - Externer Referenzschalter
    8 - Trigger
    9 - Richtung
    10 - Freigabe
    11 - Takt
    12 - Taktrichtungsmodus 1
    13 - Taktrichtungsmodus 2\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(FUNKTION_EINGANG3, inputSelection)

  def getInput3Selection(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt die Funktion fuer den Digitaleingang 1 aus.\n
    0 - Benutzerdefiniert
    1 - Starte Satz / Fehlerreset
    2-6 - Satzauswahl Bit 0-4
    7 - Externer Referenzschalter
    8 - Trigger
    9 - Richtung
    10 - Freigabe
    11 - Takt
    12 - Taktrichtungsmodus 1
    13 - Taktrichtungsmodus 2\n
    '''
    return self.com.getVal(FUNKTION_EINGANG3)

  def setInput4Selection(self, inputSelection):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die Funktion fuer den Digitaleingang 4.\n
    0 - Benutzerdefiniert
    1 - Starte Satz / Fehlerreset
    2-6 - Satzauswahl Bit 0-4
    7 - Externer Referenzschalter
    8 - Trigger
    9 - Richtung
    10 - Freigabe
    11 - Takt
    12 - Taktrichtungsmodus 1
    13 - Taktrichtungsmodus 2\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(FUNKTION_EINGANG4, inputSelection)

  def getInput4Selection(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt die Funktion fuer den Digitaleingang 4 aus.\n
    0 - Benutzerdefiniert
    1 - Starte Satz / Fehlerreset
    2-6 - Satzauswahl Bit 0-4
    7 - Externer Referenzschalter
    8 - Trigger
    9 - Richtung
    10 - Freigabe
    11 - Takt
    12 - Taktrichtungsmodus 1
    13 - Taktrichtungsmodus 2\n
    '''
    return self.com.getVal(FUNKTION_EINGANG4)

  def setInput5Selection(self, inputSelection):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die Funktion fuer den Digitaleingang 5.\n
    0 - Benutzerdefiniert
    1 - Starte Satz / Fehlerreset
    2-6 - Satzauswahl Bit 0-4
    7 - Externer Referenzschalter
    8 - Trigger
    9 - Richtung
    10 - Freigabe
    11 - Takt
    12 - Taktrichtungsmodus 1
    13 - Taktrichtungsmodus 2\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(FUNKTION_EINGANG5, inputSelection)

  def getInput5Selection(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt die Funktion fuer den Digitaleingang 5 aus.\n
    0 - Benutzerdefiniert
    1 - Starte Satz / Fehlerreset
    2-6 - Satzauswahl Bit 0-4
    7 - Externer Referenzschalter
    8 - Trigger
    9 - Richtung
    10 - Freigabe
    11 - Takt
    12 - Taktrichtungsmodus 1
    13 - Taktrichtungsmodus 2\n
    '''
    return self.com.getVal(FUNKTION_EINGANG5)

  def setInput6Selection(self, inputSelection):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die Funktion fuer den Digitaleingang 6.\n
    0 - Benutzerdefiniert
    1 - Starte Satz / Fehlerreset
    2-6 - Satzauswahl Bit 0-4
    7 - Externer Referenzschalter
    8 - Trigger
    9 - Richtung
    10 - Freigabe
    11 - Takt
    12 - Taktrichtungsmodus 1
    13 - Taktrichtungsmodus 2\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(FUNKTION_EINGANG6, inputSelection)

  def getInput6Selection(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt die Funktion fuer den Digitaleingang 6 aus.\n
    0 - Benutzerdefiniert
    1 - Starte Satz / Fehlerreset
    2-6 - Satzauswahl Bit 0-4
    7 - Externer Referenzschalter
    8 - Trigger
    9 - Richtung
    10 - Freigabe
    11 - Takt
    12 - Taktrichtungsmodus 1
    13 - Taktrichtungsmodus 2\n
    '''
    return self.com.getVal(FUNKTION_EINGANG6)

  def setInput7Selection(self, inputSelection):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die Funktion fuer den Digitaleingang 7.\n
    0 - Benutzerdefiniert
    1 - Starte Satz / Fehlerreset
    2-6 - Satzauswahl Bit 0-4
    7 - Externer Referenzschalter
    8 - Trigger
    9 - Richtung
    10 - Freigabe
    11 - Takt
    12 - Taktrichtungsmodus 1
    13 - Taktrichtungsmodus 2\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(FUNKTION_EINGANG7, inputSelection)

  def getInput7Selection(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt die Funktion fuer den Digitaleingang 7 aus.\n
    0 - Benutzerdefiniert
    1 - Starte Satz / Fehlerreset
    2-6 - Satzauswahl Bit 0-4
    7 - Externer Referenzschalter
    8 - Trigger
    9 - Richtung
    10 - Freigabe
    11 - Takt
    12 - Taktrichtungsmodus 1
    13 - Taktrichtungsmodus 2\n
    '''
    return self.com.getVal(FUNKTION_EINGANG7)

  def setInput8Selection(self, inputSelection):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die Funktion fuer den Digitaleingang 8.\n
    0 - Benutzerdefiniert
    1 - Starte Satz / Fehlerreset
    2-6 - Satzauswahl Bit 0-4
    7 - Externer Referenzschalter
    8 - Trigger
    9 - Richtung
    10 - Freigabe
    11 - Takt
    12 - Taktrichtungsmodus 1
    13 - Taktrichtungsmodus 2\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(FUNKTION_EINGANG8, inputSelection)

  def getInput8Selection(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt die Funktion fuer den Digitaleingang 8 aus.\n
    0 - Benutzerdefiniert
    1 - Starte Satz / Fehlerreset
    2-6 - Satzauswahl Bit 0-4
    7 - Externer Referenzschalter
    8 - Trigger
    9 - Richtung
    10 - Freigabe
    11 - Takt
    12 - Taktrichtungsmodus 1
    13 - Taktrichtungsmodus 2\n
    '''
    return self.com.getVal(FUNKTION_EINGANG8)

  def setOutput1Selection(self, inputSelection):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die Funktion fuer den Digitalausgang 1.\n
    0 - Benutzerdefiniert
    1 - Bereit
    2 - Fahrend
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(FUNKTION_AUSGANG1, inputSelection)

  def getOutput1Selection(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt die Funktion fuer den Digitalausgang 1 aus.\n
    0 - Benutzerdefiniert
    1 - Bereit
    2 - Fahrend
    '''
    return self.com.getVal(FUNKTION_AUSGANG1)

  def setOutput2Selection(self, inputSelection):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die Funktion fuer den Digitalausgang 2.\n
    0 - Benutzerdefiniert
    1 - Bereit
    2 - Fahrend
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(FUNKTION_AUSGANG2, inputSelection)

  def getOutput2Selection(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt die Funktion fuer den Digitalausgang 2 aus.\n
    0 - Benutzerdefiniert
    1 - Bereit
    2 - Fahrend
    '''
    return self.com.getVal(FUNKTION_AUSGANG2)

  def setOutput3Selection(self, inputSelection):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die Funktion fuer den Digitalausgang 3.\n
    0 - Benutzerdefiniert
    1 - Bereit
    2 - Fahrend
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(FUNKTION_AUSGANG3, inputSelection)

  def getOutput3Selection(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt die Funktion fuer den Digitalausgang 3 aus.\n
    0 - Benutzerdefiniert
    1 - Bereit
    2 - Fahrend
    '''
    return self.com.getVal(FUNKTION_AUSGANG3)

  def setOutput4Selection(self, inputSelection):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die Funktion fuer den Digitalausgang 4.\n
    0 - Benutzerdefiniert
    1 - Bereit
    2 - Fahrend
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(FUNKTION_AUSGANG4, inputSelection)

  def getOutput4Selection(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt die Funktion fuer den Digitalausgang 4 aus.\n
    0 - Benutzerdefiniert
    1 - Bereit
    2 - Fahrend
    '''
    return self.com.getVal(FUNKTION_AUSGANG4)

  def setOutput5Selection(self, inputSelection):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die Funktion fuer den Digitalausgang 5.\n
    0 - Benutzerdefiniert
    1 - Bereit
    2 - Fahrend
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(FUNKTION_AUSGANG5, inputSelection)

  def getOutput5Selection(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt die Funktion fuer den Digitalausgang 5 aus.\n
    0 - Benutzerdefiniert
    1 - Bereit
    2 - Fahrend
    '''
    return self.com.getVal(FUNKTION_AUSGANG5)

  def setOutput6Selection(self, inputSelection):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die Funktion fuer den Digitalausgang 6.\n
    0 - Benutzerdefiniert
    1 - Bereit
    2 - Fahrend
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(FUNKTION_AUSGANG6, inputSelection)

  def getOutput6Selection(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt die Funktion fuer den Digitalausgang 6 aus.\n
    0 - Benutzerdefiniert
    1 - Bereit
    2 - Fahrend
    '''
    return self.com.getVal(FUNKTION_AUSGANG6)

  def setOutput7Selection(self, inputSelection):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die Funktion fuer den Digitalausgang 7.\n
    0 - Benutzerdefiniert
    1 - Bereit
    2 - Fahrend
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(FUNKTION_AUSGANG7, inputSelection)

  def getOutput7Selection(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt die Funktion fuer den Digitalausgang 7 aus.\n
    0 - Benutzerdefiniert
    1 - Bereit
    2 - Fahrend
    '''
    return self.com.getVal(FUNKTION_AUSGANG7)

  def setOutput8Selection(self, inputSelection):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die Funktion fuer den Digitalausgang 8.\n
    0 - Benutzerdefiniert
    1 - Bereit
    2 - Fahrend
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(FUNKTION_AUSGANG8, inputSelection)

  def getOutput8Selection(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt die Funktion fuer den Digitalausgang 8 aus.\n
    0 - Benutzerdefiniert
    1 - Bereit
    2 - Fahrend
    '''
    return self.com.getVal(FUNKTION_AUSGANG8)

  def setFeedConstNum(self, feedConstNum):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Zaehler der Vorschubkonstanten.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(ZAEHLER_VORSCHUBKONSTANTE, feedConstNum)

  def getFeedConstNum(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Zaehler der Vorschubkonstanten aus.
    '''
    return self.com.getVal(ZAEHLER_VORSCHUBKONSTANTE)

  def setFeedConstDenum(self, feedConstDenum):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Nenner der Vorschubkonstanten.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(NENNER_VORSCHUBKONSTANTE, feedConstDenum)

  def getFeedConstDenum(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Nenner der Vorschubkonstanten aus.
    '''
    return self.com.getVal(NENNER_VORSCHUBKONSTANTE)

  def setCurrentPeak(self, currentPeak):
    '''
    Noch nicht getestet!
    Diese Funktion setzt den Strom-Spitzenwert fuer BLDC.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(BLDC_STROM_SPITZENWERT, currentPeak)

  def getCurrentPeak(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt den Strom-Spitzenwert fuer BLDC aus.
    '''
    return self.com.getVal(BLDC_STROM_SPITZENWERT)

  def setCurrentTime(self, currentTime):
    '''
    Noch nicht getestet!
    Diese Funktion setzt die Strom-Zeitkonstante fuer BLDC.\n
    Ueber den Rueckgabewert der Funktion kann geprueft werden, ob der Befehl korrekt von
    der Steuerung erkannt wurde.
    '''
    return self.com.executeCmd(BLDC_STROM_ZEITKONSTANTE, currentTime)

  def getCurrentTime(self):
    '''
    Noch nicht getestet!
    Diese Funktion gibt die Strom-Zeitkonstante fuer BLDC aus.
    '''
    return self.com.getVal(BLDC_STROM_ZEITKONSTANTE)

def main():
  comPort = serial.Serial('/dev/ttyUSB0', baudrate=115200, timeout=0.5)
  comInterface = nanotec.Nanotec(comPort)
  cmd = Commands(comInterface)
  print cmd.setRamp(1000)
  print cmd.setStepMode(1)
  print cmd.setSteps(100)
  print cmd.setMaxFrequency(10000)
  print cmd.startTravelProfile()

if __name__ == '__main__':
  main()
