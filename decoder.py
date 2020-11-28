
# "Autobox" dongle driver for HTML 'streaming'
# Created by Colin Munro, December 2019
# See README.md for more information

"""Simple utility code to decode an h264 stream to a series of PNGs."""

import subprocess, threading, os, fcntl, queue
import time
class Decoder:
	class _Thread(threading.Thread):
		def __init__(self, owner):
			super().__init__()
			self.owner = owner
			self.running = threading.Event()
			self.shutdown = False

		def run(self):
			pass
			# while not self.shutdown:
			# 	pass


	def __init__(self):	
		# self.child = subprocess.Popen(["ffplay", "-threads", "4", "-"], stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)	
		self.child = subprocess.Popen(["mpv", "--hwdec=rpi", "--demuxer-rawvideo-fps=60", "--fps=60", "-"], stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, bufsize=1)	

		self.thread = self._Thread(self)
		self.thread.start()

	def stop(self):
		print("Decoder: stop")
		self.child.terminate()
		self.thread.shutdown = True
		self.thread.join()

	def send(self, data):
		self.child.stdin.write(data)
		self.child.stdin.flush()
		# self.thread.running.set()

	def on_frame(self, png):
		"""Callback for when a frame is received [called from a worker thread]."""
		pass
