## Generates a time stamp and joins it to the base filename
import datetime
def fileNameGen():
  basename = "voicerec.wav"
  prefix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
  fullname = "_".join([prefix, basename])
  print(fullname)
  return fullname
