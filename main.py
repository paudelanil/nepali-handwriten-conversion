import os

from src.handwritten_document_conversion.text_recognition import TextRecognition
from src.handwritten_document_conversion.text_detection import TextDetection

file_path = os.path.dirname(os.path.abspath(__file__))
OG_IMG_DIR = os.path.join(file_path,  'images', 'original')
RESIZED_IMG_DIR = os.path.join(file_path, 'images', 'resized')
TEXT_FILE_DIR = os.path.join(file_path, 'txt')

def pipeline_function(img_file):
    text_det_obj = TextDetection(image_file=img_file)
    text_rec_obj = TextRecognition()

    _, cropped_images_file_name = text_det_obj.return_cropped_images()

    texts = []
    for cropped_image in cropped_images_file_name:
        generated_text = text_rec_obj.return_generated_text(image=os.path.join(RESIZED_IMG_DIR, cropped_image))
        texts.append(generated_text)


    with open(os.path.join(TEXT_FILE_DIR, "predicted_test.txt"), 'w') as file:
        for text in texts:
            file.write(text)
            file.write(' ')


if __name__ == "__main__":
    pipeline_function(img_file='test_2.jpg')
