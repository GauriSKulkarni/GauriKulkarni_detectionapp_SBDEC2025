import os
import shutil

# ==========================
# ✅ UPDATE THESE PATHS
# ==========================
images_dir = r"D:\Cleaned Dataset\stc_cl dataset\images"
labels_dir = r"D:\Cleaned Dataset\stc_cl dataset\labels"

matched_images_dir = r"D:\code work\matched\images"
matched_labels_dir = r"D:\code work\matched\labels"
unmatched_dir = r"D:\code work\unmatched"

# ==========================
# ✅ CREATE OUTPUT FOLDERS
# ==========================
os.makedirs(matched_images_dir, exist_ok=True)
os.makedirs(matched_labels_dir, exist_ok=True)
os.makedirs(unmatched_dir, exist_ok=True)

# ==========================
# ✅ GET FILE LISTS
# ==========================
image_files = os.listdir(images_dir)
label_files = os.listdir(labels_dir)

image_basenames = {os.path.splitext(f)[0]: f for f in image_files}
label_basenames = {os.path.splitext(f)[0]: f for f in label_files}

matched = 0
unmatched = 0

# ==========================
# ✅ PROCESS MATCHED FILES
# ==========================
for name in image_basenames:
    if name in label_basenames:
        img_src = os.path.join(images_dir, image_basenames[name])
        lbl_src = os.path.join(labels_dir, label_basenames[name])

        shutil.copy(img_src, matched_images_dir)
        shutil.copy(lbl_src, matched_labels_dir)

        matched += 1
    else:
        # Image without label
        img_src = os.path.join(images_dir, image_basenames[name])
        shutil.move(img_src, unmatched_dir)
        unmatched += 1

# ==========================
# ✅ PROCESS UNMATCHED LABELS
# ==========================
for name in label_basenames:
    if name not in image_basenames:
        lbl_src = os.path.join(labels_dir, label_basenames[name])
        shutil.move(lbl_src, unmatched_dir)
        unmatched += 1

# ==========================
# ✅ SUMMARY
# ==========================
print("✅ Matching Completed!")
print(f"✅ Matched Pairs: {matched}")
print(f"⚠ Unmatched Files Moved: {unmatched}")
print("📁 Unmatched files saved in:", unmatched_dir)