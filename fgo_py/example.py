from fgo_py import *
import traceback
try:
    #draw()
    print(getTime())
    setSkillInfo('lancer')
    #oneBattle((0,0,1))
    #main(danger=(0,0,1))
    #oneBattle((0,2,1))
    main(110,2,danger=(0,2,1))
except BaseException as e:
    print(e)
    traceback.print_exc()
finally:
    playSound()
    os.system("pause");

