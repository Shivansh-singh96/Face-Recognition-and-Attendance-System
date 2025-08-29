import cv2
import face_recognition
import pickle
import os
import albumentations as A

# Folder containing student images
folderPath = 'D:/Project Agumentation/Students'
PathList = os.listdir(folderPath)
print("Images found:", PathList)

imgList = []
StudentName = []
skipped_files = []

# Create a debug folder for inspection
debug_folder = 'D:/Project New/Debug'
os.makedirs(debug_folder, exist_ok=True)

# Load original images
for path in PathList:
    img = cv2.imread(os.path.join(folderPath, path))
    if img is None:
        print(f"Failed to load image: {path}")
        skipped_files.append(path)
        continue
    imgList.append(img)
    StudentName.append(os.path.splitext(path)[0])

# Define a minimal augmentation pipeline
augmentations = A.Compose([
    A.Rotate(limit=20, p=0.5),              # Rotate ±20 degrees
    A.HorizontalFlip(p=0.5),                # Flip horizontally
    A.RandomBrightnessContrast(p=0.5),      # Adjust brightness/contrast
    A.GaussNoise(p=0.3),                    # Add noise
    A.HueSaturationValue(p=0.5),            # Change color properties
    A.Blur(blur_limit=3, p=0.3),            # Slight blur
])

# Function to augment and encode images
def augment_and_encode(imagesList, names, num_augmentations=3):
    encodeList = []
    augmented_names = []
    
    for img, name in zip(imagesList, names):
        # Convert to RGB for face_recognition
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Save original image for debugging
        cv2.imwrite(os.path.join(debug_folder, f"{name}_original.jpg"), img)
        
        # Encode original image with increased robustness
        try:
            encode = face_recognition.face_encodings(img_rgb, num_jitters=10)[0]
            encodeList.append(encode)
            augmented_names.append(name)
            print(f"Encoded چهEncoded original image: {name}")
        except IndexError:
            print(f"Face not detected in original image: {name} - Skipping student")
            skipped_files.append(f"{name}.jpg")
            continue  # Skip if original fails
        
        # Generate and encode augmented versions
        for i in range(num_augmentations):
            augmented_img = augmentations(image=img_rgb)['image']
            # Save augmented image for debugging
            cv2.imwrite(os.path.join(debug_folder, f"{name}_aug_{i}.jpg"), cv2.cvtColor(augmented_img, cv2.COLOR_RGB2BGR))
            try:
                encode = face_recognition.face_encodings(augmented_img, num_jitters=10)[0]
                encodeList.append(encode)
                augmented_names.append(f"{name}_aug_{i}")
                print(f"Encoded augmented image: {name}_aug_{i}")
            except IndexError:
                print(f"Face not detected in augmented image: {name}_aug_{i} - Skipping this augmentation")
                skipped_files.append(f"{name}_aug_{i}")
    
    return encodeList, augmented_names

# Augment and encode images
print("Augmentation and Encoding Started...")
EncodeListKnown, AugmentedStudentNames = augment_and_encode(imgList, StudentName, num_augmentations=3)
if skipped_files:
    print("Skipped files:", skipped_files)
print(f"Encoding Completed: {len(EncodeListKnown)} faces encoded")

# Save encodings to pickle file
try:
    with open("Encodefile.p", 'wb') as file:
        pickle.dump([EncodeListKnown, AugmentedStudentNames], file)
    print("File Saved")
except Exception as e:
    print(f"Failed to save file: {e}")