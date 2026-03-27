# ========================================
# 第7章: 画像処理（Pillowを使った基礎）
# ========================================
# 実行: pip install Pillow
# ※ Phase②でOpenCVに本格移行する前の入門として

from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os

# ===== テスト用画像を生成 =====
def create_sample_image(path="sample.png", size=(400, 300)):
    """サンプル画像を生成する"""
    img = Image.new("RGB", size, color=(70, 130, 180))  # SteelBlue
    draw = ImageDraw.Draw(img)
    # 白い円（ボールのイメージ）
    draw.ellipse([150, 100, 250, 200], fill=(255, 255, 255), outline=(200, 200, 200), width=3)
    # テキスト
    draw.text((120, 220), "Python Image Processing", fill=(255, 255, 255))
    img.save(path)
    return img

# サンプル画像を作成
img = create_sample_image()
print(f"画像サイズ: {img.size}")   # → (400, 300)
print(f"モード: {img.mode}")       # → RGB

# ===== リサイズ =====
resized = img.resize((200, 150))
resized.save("resized.png")
print(f"リサイズ後: {resized.size}")   # → (200, 150)

# ===== クロップ（切り抜き）=====
# (left, upper, right, lower)
cropped = img.crop((100, 50, 300, 250))
cropped.save("cropped.png")
print(f"クロップ後: {cropped.size}")

# ===== グレースケール変換 =====
gray = img.convert("L")   # L = グレースケール
gray.save("gray.png")
print(f"グレースケール モード: {gray.mode}")   # → L

# ===== 画像の回転・反転 =====
rotated = img.rotate(45, expand=True)   # 45度回転
rotated.save("rotated.png")

flipped = img.transpose(Image.FLIP_LEFT_RIGHT)   # 左右反転
flipped.save("flipped.png")

# ===== フィルタ処理 =====
blurred = img.filter(ImageFilter.GaussianBlur(radius=3))
blurred.save("blurred.png")

sharpened = img.filter(ImageFilter.SHARPEN)
sharpened.save("sharpened.png")

# ===== ピクセル操作 =====
pixels = img.load()
width, height = img.size
# 左半分を赤みがかった色に変換
for x in range(width // 2):
    for y in range(height):
        r, g, b = pixels[x, y]
        pixels[x, y] = (min(r + 80, 255), g // 2, b // 2)
img.save("pixel_edit.png")

print("\n生成されたファイル:")
for f in ["sample.png", "resized.png", "cropped.png",
          "gray.png", "rotated.png", "blurred.png", "pixel_edit.png"]:
    if os.path.exists(f):
        print(f"  ✓ {f}")
        os.remove(f)   # 後片付け
