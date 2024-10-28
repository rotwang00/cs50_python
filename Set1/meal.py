from math import ceil

def main():
  time = input("What time is it (HH:MM): ")
  converted_time = convert(time)
  if converted_time >= 7 and converted_time <= 8:
    print("breakfast time")
  if converted_time >= 12 and converted_time <= 13:
    print("lunch time")
  if converted_time >= 18 and converted_time <= 19:
    print("dinner time")


def convert(time):
  hours, minutes = time.split(":")
  hours = int(hours)
  minutes = int(minutes)
  minutes_float = ceil((minutes / 60) * 10) / 10
  return hours + minutes_float


if __name__ == "__main__":
  main()