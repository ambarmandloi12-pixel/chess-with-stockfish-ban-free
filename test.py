import sys
import os
import time
import pyautogui
import keyboard
import chess
import chess.engine
from PIL import ImageChops, ImageStat

VENV_LIB = r'C:\Users\srw\Desktop\cheat-\Lib\site-packages'
sys.path.insert(0,VENV_LIB)

ENGINE_PATH = r'C:\Users\srw\Desktop\cheat-\stockfish.exe'

BOARD_REGION = (162, 159, 481, 483) 
board = chess.Board()
last_screenshot = None 
ORIENTATION = 'normal'

engine_instance = None

def start_engine():
    global engine_instance
    current_folder = os.path.dirname(os.path.abspath(__file__))
    
    try:
        if os.path.exists(target_exe):
            engine_instance = chess.engine.SimpleEngine.popen_uci(target_exe)
            print(f" SUCCESS: Stockfish loaded from {target_exe}")
        else:
            print(f" ERROR: Cannot find stockfish.exe in {current_folder}")
    except Exception as e:
        print(f" STARTUP CRASH: {e}")


def get_best_move(fen):
    global engine_instance
    if engine_instance is None:
        return "Engine Not Running"
    try:
        result = engine_instance.play(chess.Board(fen), chess.engine.Limit(time=0.1))
        return result.move
    except Exception as e:
        return f"Engine Error: {e}"

def scan():
    global last_screenshot, ORIENTATION
    print(f"\n[Scanning... Turn: {'White' if board.turn == chess.WHITE else 'Black'}]")
    
    current_img = pyautogui.screenshot(region=BOARD_REGION)

    if last_screenshot is None:
        last_screenshot = current_img
        print(" Baseline Set. Make your move!")
        return

    w, h = current_img.size
    sq_w, sq_h = w / 8, h / 8
    changed_squares = []

    for row in range(8):
        for col in range(8):
            margin = 12
            box = (int(col*sq_w+margin), int(row*sq_h+margin), int((col+1)*sq_w-margin), int((row+1)*sq_h-margin))
            sq_old = last_screenshot.crop(box)
            sq_new = current_img.crop(box)
            if sum(ImageStat.Stat(ImageChops.difference(sq_old, sq_new)).mean) > 12: 
                f, r = (chr(ord('a')+(7-col)), str(row+1)) if ORIENTATION == 'flipped' else (chr(ord('a')+col), str(8-row))
                changed_squares.append(f + r)

    if not changed_squares:
        print(" No changes detected.")
        return

    print(f"Changes: {changed_squares}")
    
    found_move = None
    for s in changed_squares:
        for e in changed_squares:
            if s == e: continue
            move = chess.Move.from_uci(s + e)
            for m in [move, chess.Move.from_uci(s + e + "q")]:
                if m in board.legal_moves:
                    found_move = m
                    break
            if found_move: break
    
    if found_move:
        print(f"ACCEPTED: {found_move}")
        board.push(found_move)
        
        best = get_best_move(board.fen())
        print(f"<:::::||==o NEXT MOVE ({'White' if board.turn == chess.WHITE else 'Black'}): {best}")
        
        last_screenshot = current_img 
    else:
        print(" Invalid Move. Mouse on board?")

if __name__ == "__main__":
    print("--- STEALTH BOT V8 ---")
    start_engine()
    ans = input("Is Rank 8 at Top? (Y/N): ").lower()
    ORIENTATION = 'normal' if ans == 'y' else 'flipped'
    
    try:
        while True:
            if keyboard.is_pressed('`'):
                scan()
                time.sleep(0.8)
            if keyboard.is_pressed('r'):
                board.reset()
                last_screenshot = None
                print(" Reset.")
                time.sleep(0.8)
            time.sleep(0.01)
    except KeyboardInterrupt:
        if engine_instance: engine_instance.quit()
        sys.exit()
