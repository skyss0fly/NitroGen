import time, random, string
amount = input("say a number bigger then zero and ill generate foryou \n>> ")

while amount != 0:
  cid = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(11))
  print("https://discord.gift/",cid)
  

  time.sleep(1)
