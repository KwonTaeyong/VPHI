from django.shortcuts import render
import qrcode


def sub02_01(request):
    return render(request, "VPHI/sub02/sub02_01.html")


def sub02_02(request):
    context = {
    }

    if request.POST:
        CodeUrl = request.POST['CodeUrl']

        if (len(CodeUrl)) == 0:
            CodeUrl = "https://www.google.com"

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(CodeUrl)
        img = qr.make_image()
        qrlink = 'static/img/qr1.png'
        img.save(qrlink)
        context["success"] = True
        context["qrlink"] = qrlink
        context["CodeUrl"] = CodeUrl
    else:
        context["success"] = False

    return render(request, "VPHI/sub02/sub02_02.html", context)


def sub02_03(request):
    return render(request, "VPHI/sub02/sub02_03.html")


def sub02_04(request):
    return render(request, "VPHI/sub02/sub02_04.html")


def sub02_05(request):
    return render(request, "VPHI/sub02/sub02_05.html")


# def barcode_reader(request):
#     import cv2
#     import pyzbar.pyzbar as pyzbar
#     from playsound import playsound
#     import VideoCapture
#     from cv2 import waitKey
#
#     data_list = []
#     used_codes = []
#
#     try:
#         f = open('grbarcode_data.txt', "r", encoding="utf8")
#         data_list = f.readlines()
#     except FileNotFoundError:
#         pass
#     else:
#         f.close()
#
#     cap = cv2.VideoCapture(0)
#
#     for i in data_list:
#         used_codes.append(i.rsplit('\n'))
#
#     while True:
#         success, frame = cap.read()
#
#         if success:
#             for code in pyzbar.decode(frame):
#                 my_code = code.data.decode('utf-8')
#                 if my_code not in used_codes:
#                     print("인식 성공 : ", my_code)
#                     playsound("짧은 비프.mp3")
#                     used_codes.append(my_code)
#
#                     f2 = open("grbarcode_data.txt", "a", encoding="utf8")
#                     f2.write(my_code + '\n')
#                     f2.close()
#                 else:
#                     print("이미 인식된 코드입니다")
#                     playsound("짧은 비프.mp3")
#
#             cv2.imshow('cam', frame)
#
#             key = cv2.waitKey(1)
#             if key == 27:
#                 break
#
#     cap.release()
#     cv2.destroyAllWindows()
#     return render(request, "VPHI/sub02/sub02_02.html")
