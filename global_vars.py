FILE_REGEX = "satImage_%d"

NUM_CHANNELS = 3 # RGB images
PIXEL_DEPTH = 255
NUM_LABELS = 2
TRAINING_SIZE = 80
VALIDATION_SIZE = 5  # Size of the validation set.
SEED = 66478  # Set to None for random seed.
BATCH_SIZE = 16 # 64
NUM_EPOCHS = 10
RESTORE_MODEL = False # If True, restore existing model instead of training a new one
TRAIN_PREDICTIONS = False # If True, restore existing model instead of training a new one
RECORDING_STEP = 1000

# Set image patch size in pixels
# IMG_PATCH_SIZE should be a multiple of 4
# image size should be an integer multiple of this number!
IMG_PATCH_SIZE = 16

# Border for enhanced context.
IMG_BORDER = 4

IMG_TOTAL_SIZE = IMG_PATCH_SIZE + 2 * IMG_BORDER