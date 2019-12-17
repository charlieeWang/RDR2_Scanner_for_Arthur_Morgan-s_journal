import os
import cv2
import numpy as np
import mapper

class Scan():
    def scan_from_directory(self, source_path, output_path):
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        files = os.listdir(source_path)
        for file in files:
            img_path = os.path.join(source_path, file)
            scanned = self.scan_journal(img_path)
            cv2.imwrite(os.path.join(output_path, file), scanned)


    def scan_journal(self, img_path):
        image = cv2.imread(img_path)
        origin_img = image.copy()

        # 左下->右下->左上->右上
        source_left_page = np.array([[190., 971.], [900., 959.], [240., 65.], [900., 95.]], dtype = "float32")
        source_right_page = np.array([[990., 958.], [1650., 959.], [990., 100.], [1660., 77.]], dtype = "float32")

        # map
        target_points = np.array([[0, 800], [680, 800], [0, 0], [680, 0]], dtype = "float32")

        left = self.transform(origin_img, source_left_page, target_points)
        right = self.transform(origin_img, source_right_page, target_points)

        # concatenate
        concate = np.concatenate((left, right), axis=1)

        return self.remove_shadow(concate)

    def transform(self, img, source, target, targer_size=(680, 800)):
        transform_img = cv2.getPerspectiveTransform(source, target)
        target = cv2.warpPerspective(img, transform_img, targer_size)
        return target

    def remove_shadow(self, img):
        # from https://stackoverflow.com/questions/44752240/how-to-remove-shadow-from-scanned-images-using-opencv
        rgb_planes = cv2.split(img)

        result_planes = []
        result_norm_planes = []
        for plane in rgb_planes:
            dilated_img = cv2.dilate(plane, np.ones((9, 9), np.uint8))
            bg_img = cv2.medianBlur(dilated_img, 21)
            diff_img = 255 - cv2.absdiff(plane, bg_img)
            norm_img = cv2.normalize(diff_img, None, alpha=0, beta=270, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
            result_planes.append(diff_img)
            result_norm_planes.append(norm_img)

        result = cv2.merge(result_planes)
        result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
        result_norm = cv2.merge(result_norm_planes)
        result_norm = cv2.cvtColor(result_norm, cv2.COLOR_BGR2GRAY)

        return result_norm


if __name__=='__main__':
    scanner = Scan()
    # scanner.scan_journal('20191213162042_1.jpg')
    scanner.scan_from_directory('test', 'output/')
