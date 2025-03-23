from guiqt import *
import sys
from pyautogui import alert, FAILSAFE, screenshot, click, moveTo
import cv2
import numpy as np
from time import sleep
from threading import Thread

FAILSAFE = True
state = True
app = QtWidgets.QApplication(sys.argv)
windows = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(windows)
windows.setFixedSize(704, 374)
windows.show()

def info():
    alert("The AutoSkip program is designed to automate actions.\n"
          "On the left, you’ll find the Image Search section and the Percentage field.\n"
          "Here’s an example of how to input image search paths:\n"
          "files/rm/wef/file.png\n"
          "files3/rm1/we3f/file2.png\n"
          "File paths should be entered on the next line using the Enter key.\n"
          "Below the Image Search section, there is the Interval Pause field, which specifies the time in seconds to wait after clicking a button.\n"
          "To the right, there is the Percentage field, which indicates the image match accuracy in percent.\n"
          "In the middle, you’ll see the Interval field, specifying the time in seconds to search for a button based on the image.\n"
          "Just below, there is the Start button.\n"
          "Please note: This is an open-source program.\n"
          "Telegram: @DISHACKER")

def styleoff():
	ui.active.setText("OFF")
	ui.active.setStyleSheet("color: red;")
def styleon():
	ui.active.setText("ON")
	ui.active.setStyleSheet("color: green;")
def stop():
	global state
	state = False
	styleoff()

def start():
	global state
	state = True
	styleon()
	try:
		match_text = int(ui.match_text.toPlainText())
		if match_text > 100 or match_text <= 0:
			alert("your chance of a match is greater than 100 or less than 0 = 0")
			ui.match_text.setPlainText("90")
		threshold = match_text/100
	except ValueError:
		alert("you didn't specify the number")
		ui.match_text.setPlainText("90")
		match_text = 90
	try:
		interval = int(ui.interval.toPlainText())
	except ValueError:
		alert("you didn't specify the number")
		ui.interval.setPlainText("3")
		interval = 3
	try:
		interval_pause = int(ui.interval_pause.toPlainText())
	except ValueError:
		alert("you didn't specify the number")
		ui.interval_pause.setPlainText("180")
		interval_pause = 180

	image_search = ui.imagesearch.toPlainText()
	images = image_search.splitlines()
	images = [line.strip() for line in images if line.strip()]
	while state:
		sleep(interval)
		for image_path in images:
			try:
				if find_and_click(image_path, threshold):
					sleep(interval_pause)
			except Exception as e:
				alert(f"Processing error {image_path}: {str(e)}")
				styleoff()
				state = False
 
def find_and_click(image_path, threshold):
	global state
	screen = screenshot()
	screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
	template = cv2.imread(image_path)
	if template is None:
		alert(f"Failed to load image: {image_path}")
		styleoff()
		state = False
		return False
	h, w = template.shape[:2]
	result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
	locations = np.where(result >= threshold)
	if len(locations[0]) > 0:
		max_loc = (locations[1][0], locations[0][0])       
		click_x = max_loc[0] + w//2
		click_y = max_loc[1] + h//2
		moveTo(click_x, click_y, duration=0.2)
		click()
		return True
	return False

def start_th():
	Thread(target=start).start()

ui.infobtn.clicked.connect(info)
ui.startbtn.clicked.connect(start_th)
ui.stopbtn.clicked.connect(stop)
sys.exit(app.exec())