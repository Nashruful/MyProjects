from random import randint
import time

sentences = "time is time if u don't consume it well so make sure to consume it very well okay",

print("Get ready to type this sentence:")
print(sentences)
time.sleep(1)
print("in 3 ", end=" ")
time.sleep(1)
print("2 ", end=" ")
time.sleep(1)
print("1 ", end=" ")
time.sleep(1)
print("Go!", end=" ")


def calculate_wpm(time, words):
    minutes = time / 60
    wpm = words / minutes
    return wpm


start_time = time.time()
user_input = input()
end_time = time.time()

if user_input == sentences:
    words = len(sentences.split())
    wpm = calculate_wpm(end_time - start_time, words)
    print(wpm)
else:
    print("wrong..")
