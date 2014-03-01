#
#   Written for Python 2.7.x
#
#   tPyLE - The tiny Python Line Editor
#   Copyright (C) 2014  Austin Roberge
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

def main():

    ### Globals and definitions ###

    fileLoaded = False
    fileWritten = False
    textBuffer = []

    def openFile():
      FILENAME = raw_input("File: ")
      f = open(FILENAME, 'r+')
      textBuffer = f.read()
      print "File loaded.\n"
      fileLoaded = True
      return textBuffer
      
    def writeFile():
        fileName = str(raw_input("File to write: "))
        FILE = open(fileName, 'w')
        toWriteBuf = ""
        
        for i in range(0, len(textBuffer)):
            toWriteBuf += str(textBuffer[i])
            if i == len(textBuffer) - 1:
                break
            toWriteBuf += "\n"
            
        FILE.write(toWriteBuf)
        print "Wrote", len(textBuffer), "lines to file", "'" + fileName + "'"
        FILE.close()
        fileWritten = True
        return fileWritten

    def inputMode(buf):
      while True:
        lineInput = str(raw_input())
        if lineInput == ".":
          return buf
        else:
          buf.append(str(lineInput))
          fileWritten = False

    def printLine(buf, lineNum):
        if abs(lineNum) > len(buf):
            print "Line does not exist!"
        elif lineNum < 0:        #if it's negative make it x from the end of the file
            lineNum = len(buf) - abs(lineNum)
        elif lineNum == "":
            print "What line?"
        else:
            print buf[lineNum -1]


  #################
  ### MAIN LOOP ###
  #################
  
    print "Welcome to tiny Python Line Editor!\n"
    prompt = ":: "
    while True:
        promptInput = raw_input(prompt)

        # help #
        if promptInput.lower() in ("help", "h"):
            print "HELP\n\
           Open or o - Open a file.\n\
          Write or w - Write a file.\n\
                  pb - Print current buffer.\n\
                  pl - Print line in buffer.\n\
               Reset - Reset buffer.\n\
           Help or h - This help text.\n\
           Quit or q - Quit the program.\n\
                  q! - Quit and lose changes.\n"
        
        # quit #
        elif promptInput.lower() in ("quit", "q", "q!"):
            if textBuffer == [] or fileWritten:
                quit()
            elif promptInput == "q!":
                quit()
            else:
                print "Use q! to exit without saving changes."
                
        # open file #
        elif promptInput.lower() in ("open", "o"):
            openFile()
        
        # input mode #
        elif promptInput.lower() == "i":
            if fileLoaded == False:
                inputMode(textBuffer)
        
        # print buffer #
        elif promptInput.lower() == "pb":
            if textBuffer == []:
                print "Buffer empty"
            else:
                for i in range(0, len(textBuffer)):
                    print textBuffer[i]
        
        # print line #
        elif promptInput == "pl":
            try:
                lineNum = int(raw_input("Line Number: "))
            except ValueError:
                print "Please enter a number."
            else:        
                printLine(textBuffer, int(lineNum))
        
        # reset/clear buffer #
        elif promptInput.lower() == "reset":
            textBuffer = []
            print "Buffer reset.\n"
        
        # write to file #
        elif promptInput.lower() in ("write", "w"):
            writeFile()
            
        else:
            print "?"
            
            
if __name__ == '__main__':
    main()
