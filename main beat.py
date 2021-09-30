from earsketch import *
# Cory / Malia
init()
setTempo(120)

# Instruments
intro808=RD_RNB_808MAINBEAT_2
intro=RD_POP_PADCHORD_2
main808=RD_RNB_808MAINBEAT_3
kick=CIARA_SET_KICK_1
main=RD_POP_PADCHORD_7
bells=YG_NEW_HIP_HOP_BELLS_1
mainbass=RD_EDM_WARMBASSLINE_1

# Tracks
fitMedia(intro808,1,1,5)
fitMedia(intro,2,1,9)
fitMedia(intro,2,35.5,43)
fitMedia(main808,1,9,25)
fitMedia(main808,1,29,35)
fitMedia(kick,4,9,12)
fitMedia(kick,4,13,25)
fitMedia(main,5,11,35)
fitMedia(bells,6,15.5,16)
fitMedia(bells,6,17.5,18)
fitMedia(bells,6,19.5,20)
fitMedia(bells,6,21.5,22)
fitMedia(mainbass,7,15,15.25)
fitMedia(mainbass,7,17,17.25)
fitMedia(mainbass,7,19,19.25)
fitMedia(mainbass,7,21,21.25)
fitMedia(main808,1,43,50)
fitMedia(main,5,43,50)
fitMedia(bells,6,45.5,46)
fitMedia(intro,2,50,53)


# Fills
fillA = "0---0-0-00--0000"
fillB = "0--0--0--0--0-0-"
fillC = "--000-00-00-0-00"
fillD = "000-000-0-0-0"
fillRev = reverseString(fillC)
makeBeat(OS_SNARE03, 3, 4, fillA)
makeBeat(OS_SNARE03, 3, 8, fillC)
makeBeat(OS_SNARE03, 3, 26, fillC)
makeBeat(OS_SNARE03, 3, 28, fillRev)
makeBeat(OS_SNARE03, 3, 34.25, fillD)
makeBeat(OS_SNARE03, 3, 42, fillC)

# Effects
setEffect(4, VOLUME, GAIN, 1, 13)
setEffect(4, VOLUME, GAIN, -10, 15.25)
setEffect(4, VOLUME, GAIN, 1, 16)
setEffect(4, VOLUME, GAIN, -10, 17.25)
setEffect(4, VOLUME, GAIN, 1, 18)

finish()
