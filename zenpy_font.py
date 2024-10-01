import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


# 파일과 폴더를 이동시키는 함수
def move_files():
    # 이 파이썬 파일과 동일한 디렉터리 경로
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 이동할 파일과 폴더 경로 고정
    file_to_move = os.path.join(current_dir, 'zenpy_change_font.rpy')
    folder_to_move = os.path.join(current_dir, 'zen_fonts')
    
    dir_to_copy = os.path.join(current_dir, 'source')


    if not os.path.exists(dir_to_copy):
        messagebox.showerror("에러", f"{dir_to_copy} 폴더가 존재하지 않습니다.")
        return
    
    # 디렉터리 선택
    dest_dir = filedialog.askdirectory(title="렌파이 폴더를 선택하세요")
    if not dest_dir:
        messagebox.showwarning("경고", "디렉터리가 선택되지 않았습니다.")
        return

    #디렉터리가 렌파이 폴더인지 확인
    is_renpy_dir = os.path.join(dest_dir, 'renpy')
    if not os.path.exists(is_renpy_dir):
        messagebox.showwarning("경고", "렌파이 디렉터리가 아닙니다.")
        return
    else:
        messagebox.showinfo("선택", f"선택된 디렉터리 {dest_dir}")


    # 파일과 폴더를 이동
    try:
        
        #렌파이 폴더 내부 경로
        dest_dir = dest_dir + "/game/tl/ko_zenpy"
        os.makedirs(dest_dir,exist_ok=True)


        #파일 복사
        shutil.copytree(dir_to_copy, dest_dir, dirs_exist_ok=True)
        messagebox.showinfo("성공", f"파일을 {dest_dir}로 복사했습니다.")
        
    except Exception as e:
        messagebox.showerror("에러", f"파일을 복사하는 중 에러가 발생했습니다: {e}")

# GUI 창 설정
root = tk.Tk()
root.title("파일 및 폴더 이동기")
root.geometry("300x250")

# 버튼 추가
move_button = tk.Button(root, text="파일 및 폴더 이동", command=move_files)
move_button.pack(pady=100)

# GUI 실행
root.mainloop()
