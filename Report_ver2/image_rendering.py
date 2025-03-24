import google.generativeai as genai
import cv2
import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
model_version = os.getenv("Model_Version")
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_version)


def select_image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    return file_path

def capture_image():
    output_path = "image.jpg"
    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        print("Không tìm thấy camera thật, thử chuyển sang camera ảo OBS...")
        cap = cv2.VideoCapture(1)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        instructions = "Nhan 'C' de chup hoac 'Q' de thoat"
        cv2.putText(frame, instructions, (20, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow("Camera", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('c'):  # Nhấn 'c' để chụp ảnh
            cv2.imwrite(output_path, frame)
            break
        elif key == ord('q'):  # Nhấn 'q' để thoát
            break

    cap.release()
    cv2.destroyAllWindows()

    return output_path if os.path.exists(output_path) else None


def process_image(image_path):
    """ Gửi ảnh đến Gemini để xử lý và trả về kết quả """
    if not image_path:
        return None

    img = Image.open(image_path)
    input_text = """
    Trích xuất văn phạm chính quy trong hình ảnh và trả về text có dạng như sau: 
    8
    S
    S -> A B C | D E
    A -> a | B C | epsilon
    B -> b | C D | epsilon
    C -> c | D E
    D -> d | E F
    E -> e | F G
    F -> f | G H
    G -> g | H I"

    Trả về chỉ biểu thức chính quy dạng trên không giải thích gì thêm, biết trong đó dòng đầu tiên là số luật sinh, bạn có thể đếm số dòng trong hình ảnh,
    dòng tiếp theo là ký tự bắt đầu, những dòng kế tiếp lần lượt là các luật sinh. Lưu ý nếu luật sinh có 2 ký tự đứng cạnh nhau thì ngăn cách bằng dấu cách ' '
    """

    response = model.generate_content([input_text, img], stream=True)
    response.resolve()

    return response.text


