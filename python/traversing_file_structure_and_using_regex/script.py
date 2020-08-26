import os
import re

pattern = 'https'
pattern1 = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"

for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      full_name = os.path.join(root, name)
      with open(full_name) as myfile:
          lines=myfile.read()
          output = re.findall(pattern1, lines)
          if(output):
            print(full_name)
            print("Output is {}".format(output))
          else:
            continue