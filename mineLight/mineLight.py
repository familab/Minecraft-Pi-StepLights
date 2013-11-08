import minecraft
import block
import serial
import time

mineLight = serial.Serial('/dev/ttyACM0')
mineLight.baudrate = 9600

mc = minecraft.Minecraft.create()
loop1 = 1
color = 'M'
oldColor = 'D'


while loop1 == 1:
    playerPos = mc.player.getTilePos()

    curBlock = mc.getBlockWithData(playerPos.x,playerPos.y - 1,playerPos.z)
    blockUnderPlayer = curBlock.id
    blockState = curBlock.data
    #time.sleep(.5)
    print "Block Type: " + str(blockUnderPlayer) + ":" + str(blockState)
        
    if blockUnderPlayer == 0:
        color = 'M'
    elif  blockUnderPlayer == 1:
        color = 'D'
    elif  blockUnderPlayer == 2:
        color = 'G'
    elif  blockUnderPlayer == 3:
        color = 'U'
    elif  blockUnderPlayer == 4:
        color = 'D'                
    elif  blockUnderPlayer == 5:
        color = 'U'
    elif  blockUnderPlayer == 6:
        color = 'G'
    elif  blockUnderPlayer == 7:
        color = 'D'
    elif  blockUnderPlayer == 8:
        color = 'B'
    elif  blockUnderPlayer == 9:
        color = 'B'
    elif  blockUnderPlayer == 10:
        color = 'O'
    elif  blockUnderPlayer == 11:
        color = 'O'
    elif  blockUnderPlayer == 12:
        color = 'Y'
    elif  blockUnderPlayer == 13:
        color = 'D'
    elif  blockUnderPlayer == 14:
        color = 'D'
    elif  blockUnderPlayer == 15:
        color = 'D'                
    elif  blockUnderPlayer == 16:
        color = 'D'
    elif  blockUnderPlayer == 17:
        color = 'U'
    elif  blockUnderPlayer == 18:
        color = 'G'
    elif  blockUnderPlayer == 19:
        color = 'Y'
    elif  blockUnderPlayer == 20:
        color = 'W'
    elif  blockUnderPlayer == 21:
        color = 'B'
    elif  blockUnderPlayer == 22:
        color = 'B'
    elif  blockUnderPlayer == 23:
        color = 'D'
    elif  blockUnderPlayer == 24:
        color = 'Y'
    elif  blockUnderPlayer == 25:
        color = 'R'
    elif  blockUnderPlayer == 26:
        color = 'R'                
    elif  blockUnderPlayer == 27:
        color = 'R'
    elif  blockUnderPlayer == 28:
        color = 'R'
    elif  blockUnderPlayer == 29:
        color = 'Y'
    elif  blockUnderPlayer == 30:
        color = 'W'
    elif  blockUnderPlayer == 31:
        color = 'G'
    elif  blockUnderPlayer == 32:
        color = 'U'
    elif  blockUnderPlayer == 33:
        color = 'U'
    elif  blockUnderPlayer == 34:
        color = 'U'
    elif  blockUnderPlayer == 35:
        if blockState == 1:
         color = 'O'
        elif blockState == 2:
         color = 'P'
        elif blockState == 3:
         color = 'B'
        elif blockState == 4:
         color = 'Y'
        elif blockState == 5:
         color = 'G'
        elif blockState == 6:
         color = 'R'
        elif blockState == 7:
         color = 'M'
        elif blockState == 8:
         color = 'D'
        elif blockState == 9:
         color = 'B'
        elif blockState == 10:
         color = 'P'
        elif blockState == 11:
         color = 'B'
        elif blockState == 12:
         color = 'U'
        elif blockState == 13:
         color = 'G'
        elif blockState == 14:
         color = 'R'
        elif blockState == 15:
         color = 'M'                           
    elif  blockUnderPlayer == 36:
        color = 'U'
    elif  blockUnderPlayer == 37:
        color = 'Y'                
    elif  blockUnderPlayer == 38:
        color = 'R'
    elif  blockUnderPlayer == 39:
        color = 'U'
    elif  blockUnderPlayer == 40:
        color = 'R'
    elif  blockUnderPlayer == 41:
        color = 'Y'
    elif  blockUnderPlayer == 42:
        color = 'D'
    elif  blockUnderPlayer == 43:
        color = 'R'
    elif  blockUnderPlayer == 44:
        color = 'D'
    elif  blockUnderPlayer == 45:
        color = 'R'
    elif  blockUnderPlayer == 46:
        color = 'R'
    elif  blockUnderPlayer == 47:
        color = 'U'                
    elif  blockUnderPlayer == 48:
        color = 'U'
    elif  blockUnderPlayer == 49:
        color = 'P'
    elif  blockUnderPlayer == 50:
        color = 'Y'
    elif  blockUnderPlayer == 51:
        color = 'O'
    elif  blockUnderPlayer == 52:
        color = 'B'
    elif  blockUnderPlayer == 53:
        color = 'U'
    elif  blockUnderPlayer == 54:
        color = 'U'
    elif  blockUnderPlayer == 55:
        color = 'R'
    elif  blockUnderPlayer == 56:
        color = 'B'
    elif  blockUnderPlayer == 57:
        color = 'B'                
    elif  blockUnderPlayer == 58:
        color = 'U'
    elif  blockUnderPlayer == 59:
        color = 'G'
    elif  blockUnderPlayer == 60:
        color = 'U'
    elif  blockUnderPlayer == 61:
        color = 'D'
    elif  blockUnderPlayer == 62:
        color = 'D'
    elif  blockUnderPlayer == 63:
        color = 'U'
    elif  blockUnderPlayer == 64:
        color = 'U'
    elif  blockUnderPlayer == 65:
        color = 'U'
    elif  blockUnderPlayer == 66:
        color = 'U'
    elif  blockUnderPlayer == 67:
        color = 'D'                
    elif  blockUnderPlayer == 68:
        color = 'U'
    elif  blockUnderPlayer == 69:
        color = 'U'
    elif  blockUnderPlayer == 70:
        color = 'D'
    elif  blockUnderPlayer == 71:
        color = 'D'
    elif  blockUnderPlayer == 72:
        color = 'U'
    elif  blockUnderPlayer == 73:
        color = 'R'
    elif  blockUnderPlayer == 74:
        color = 'R'
    elif  blockUnderPlayer == 75:
        color = 'R'
    elif  blockUnderPlayer == 76:
        color = 'R'
    elif  blockUnderPlayer == 77:
        color = 'D'                
    elif  blockUnderPlayer == 78:
        color = 'W'
    elif  blockUnderPlayer == 79:
        color = 'B'
    elif  blockUnderPlayer == 80:
        color = 'W'
    elif  blockUnderPlayer == 81:
        color = 'G'
    elif  blockUnderPlayer == 82:
        color = 'D'
    elif  blockUnderPlayer == 83:
        color = 'G'
    elif  blockUnderPlayer == 84:
        color = 'U'
    elif  blockUnderPlayer == 85:
        color = 'U'
    elif  blockUnderPlayer == 86:
        color = 'O'
    elif  blockUnderPlayer == 87:
        color = 'R'                
    elif  blockUnderPlayer == 88:
        color = 'U'
    elif  blockUnderPlayer == 89:
        color = 'Y'
    elif  blockUnderPlayer == 90:
        color = 'P'
    elif  blockUnderPlayer == 91:
        color = 'O'
    elif  blockUnderPlayer == 92:
        color = 'R'
    elif  blockUnderPlayer == 93:
        color = 'D'
    elif  blockUnderPlayer == 94:
        color = 'D'
    elif  blockUnderPlayer == 95:
        color = 'U'
    elif  blockUnderPlayer == 96:
        color = 'U'
    elif  blockUnderPlayer == 97:
        color = 'D'                
    elif  blockUnderPlayer == 98:
        color = 'D'
    elif  blockUnderPlayer == 99:
        color = 'R'
    elif  blockUnderPlayer == 108:
        color = 'R'        
    elif  blockUnderPlayer == 155:
        color = 'W'         
    else:
        color = 'M'

    if color != oldColor:
     mineLight.write(color)
     oldColor = color

    
