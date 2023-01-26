import requests

# Scoring system
scorePoints = {
  "multiple10": 2,
  "multiple11": 2,
  "multiple1111": 10,
  "suiteOfNumbers": 8,
  "suiteOfDecimals": 6,
  "favorite2digits": 3,
  "favorite4digits": 6,
  "multiple2digits": 4,
  "multiple4digits": 20
}

### Add your favorites numbers to complete the scoring system ###
favorite2digits = ["21"]
favorite4digits = ["0012"]

### Get the phone numbers ###
print("Get the phone numbers...")
phone_list = []
for i in range(1, 20):
    url = f"https://buy.gomo.sg/api/hybrid/v1/numbers/{i}"
    response = requests.get(url)
    print(f"{i} => {url}")
    for el in response.json().get("content", []):
        phone_list.append({
            "number": el["number"],
            "id": el["id"]
        })

### Parse the phone numbers ###
print("Parse the phone numbers...")
# Split the numbers by 2 and 4
for i in range(len(phone_list)):
  s = phone_list[i]["number"]
  phone_list[i]["by2"] = [s[i:i+2] for i in range(0, len(s), 2)]
  phone_list[i]["by4"] = [s[i:i+4] for i in range(0, len(s), 4)]


### Score the phone numbers ###
print("Score the phone numbers...")
def score_phone_number(phone_number):
  score = 0

  # Check if multiple of 10 or 11 (2 digits)
  for num in phone_number["by2"]:
    if int(num) % 10 == 0:
      score += scorePoints["multiple10"]
    if int(num) % 11 == 0:
      score += scorePoints["multiple11"]
  
  # Check if multiple of 1111 (4 digits)
  for num in phone_number["by4"]:
    if int(num) % 1111 == 0:
      score += scorePoints["multiple1111"]

  #  Check if suite if numbers exists (4 digits) (ex: 1234, 5432) ascending and descending
  for num in phone_number["by4"]:
    if num == "".join(sorted(s)) or s == "".join(sorted(s, reverse=True)):
      score += scorePoints["suiteOfNumbers"]

  # Check if suite of decimal exists (2 digits) (ex: 21, 22) only ascending
  for i in range(len(phone_number["by2"])-1):
        if int(phone_number["by2"][i]) + 1 == int(phone_number["by2"][i+1]):
            score += scorePoints["suiteOfDecimals"]


  # Check if favorite numbers exists (2 digits and 4 digits)
  for num in phone_number["by2"]:
    if num in favorite2digits:
      score += scorePoints["favorite2digits"]
  
  for num in phone_number["by4"]:
    if num in favorite4digits:
      score += scorePoints["favorite4digits"]

  # Check if numbers appears multiple times (2 digits and 4 digits)
  for num in phone_number["by2"]:
    if phone_number["by2"].count(num) > 1:
      score += scorePoints["multiple2digits"]
  
  for num in phone_number["by4"]:
    if phone_number["by4"].count(num) > 1:
      score += scorePoints["multiple4digits"]
  
  return score
    

for i in range(len(phone_list)):
  phone_list[i]["score"] = score_phone_number(phone_list[i])

phone_list = sorted(phone_list, key=lambda k: k['score'])

### Show top 40 ###
print("Top 40")
for num in phone_list[-40:]:
  print(str(num["number"]) + " => " + str(num["score"]))
