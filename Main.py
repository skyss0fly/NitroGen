import time, random, string
def __init__self():
  print("Hey, Welcome to Sky's Nitro Grenerator:)")
  time.sleep(1)
  print("Before you begin, Do you agree to The Terms of Service shown in this program? Y/N")
  eula = input("")
 if eula == "Y":
  amount = input("say a number bigger then zero and ill generate for you \n>> ")

  while amount != 0:
  cid = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
  print("https://discord.gift/",cid)
  

  time.sleep(1)
 if eula == "N":
  print("Exiting Program")
  self.quit()
