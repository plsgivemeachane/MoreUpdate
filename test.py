from explict import *
import time
import os
import requests

#@parallel
@Queuing
def long(times,name="Bob"):
	start = time.time()
	for i in range(times):
		requests.get("https://google.com")
	stop = time.time()
	print(f"[{name}] Took : {stop - start}ms")


def long2(times,name="Bob"):
	start = time.time()
	for i in range(times):
		requests.get("https://google.com")
	stop = time.time()
	print(f"[{name}] Took : {(stop - start)*1000}ms")




MAX = 5
RUN = 10
if __name__ == '__main__':
	timer1 = Timer()
	timer2 = Timer()
	timer1.start()
	#####################
	for i in range(RUN):
		long(MAX,"Process 1")
	Queue.start()
	#####################
	time1 = timer1.stop()
	timer2.start()
	#####################
	for i in range(RUN):
		long2(MAX,"Process 2")
	#####################
	time2 = timer2.stop()
	print(f"Process 1 Took : {time1*1000}ms ~ {time1}s")
	print(f"Process 2 Took : {time2*1000}ms ~ {time2}s")
	if time1 < time2:
		print("Process 1 faster than Process 2")
	elif time1 > time2:
		print("Process 2 faster than Process 1")
