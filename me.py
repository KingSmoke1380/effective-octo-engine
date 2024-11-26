import qrcode

# لینک‌ها یا اطلاعات برای بارکد
data = """
Telegram: https://t.me/Sina_N1380
Instagram: https://www.instagram.com/mr.sina._.noori/
LinkedIn: https://www.linkedin.com/in/sina-nouri-b04a112a2/
"""

# ایجاد بارکد
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# ذخیره تصویر بارکد
img = qr.make_image(fill_color="black", back_color="white")
img.save("my_qr_code.png")
