import os, shutil

if not os.path.isdir('./datasets'):
    os.mkdir('./datasets')

original_dataset_dir = './datasets/(데이터 셋 원본 경로)'

base_dir = './datasets/pos_in_bed'
if not os.path.isdir(base_dir):
    os.mkdir(base_dir)
 nb
# 훈련, 검증, 테스트 분할을 위한 디렉터리
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')
test_dir = os.path.join(base_dir, 'test')

';ui
if not os.path.isdir(train_dir):
    os.mkdir(train_dir)
if not os.path.isdir(validation_dir):
    os.mkdir(validation_dir)
if not os.path.isdir(test_dir):
    os.mkdir(test_dir)

# 훈련용 침대 위 행동 패턴 사진 디렉터리
train_lefts_dir = os.path.join(train_dir, 'lefts')
train_faces_dir = os.path.join(train_dir, 'faces')
train_rights_dir = os.path.join(train_dir, 'rights')
train_sits_dir = os.path.join(train_dir, 'sits')
train_safebars_dir = os.path.join(train_dir, 'safebars')

if not os.path.isdir(train_lefts_dir):
    os.mkdir(train_lefts_dir)
if not os.path.isdir(train_faces_dir):
    os.mkdir(train_faces_dir)
if not os.path.isdir(train_rights_dir):
    os.mkdir(train_rights_dir)
if not os.path.isdir(train_sits_dir):
    os.mkdir(train_sits_dir)
if not os.path.isdir(train_safebars_dir):
    os.mkdir(train_safebars_dir)

# 검증용 침대 위 행동 패턴 사진 디렉터리
validation_lefts_dir = os.path.join(validation_dir, 'lefts')
validation_faces_dir = os.path.join(validation_dir, 'faces')
validation_rights_dir = os.path.join(validation_dir, 'rights')
validation_sits_dir = os.path.join(validation_dir, 'sits')
validation_safebars_dir = os.path.join(validation_dir, 'safebars')

if not os.path.isdir(validation_lefts_dir):
    os.mkdir(validation_lefts_dir)
if not os.path.isdir(validation_faces_dir):
    os.mkdir(validation_faces_dir)
if not os.path.isdir(validation_rights_dir):
    os.mkdir(validation_rights_dir)
if not os.path.isdir(validation_sits_dir):
    os.mkdir(validation_sits_dir)
if not os.path.isdir(validation_safebars_dir):
    os.mkdir(validation_safebars_dir)

# 테스트용 침대 위 행동 패턴 사진 디렉터리
test_lefts_dir = os.path.join(test_dir, 'lefts')
test_faces_dir = os.path.join(test_dir, 'faces')
test_rights_dir = os.path.join(test_dir, 'rights')
test_sits_dir = os.path.join(test_dir, 'sits')
test_safebars_dir = os.path.join(test_dir, 'safebars')

if not os.path.isdir(test_lefts_dir):
    os.mkdir(test_lefts_dir)
if not os.path.isdir(test_faces_dir):
    os.mkdir(test_faces_dir)
if not os.path.isdir(test_rights_dir):
    os.mkdir(test_rights_dir)
if not os.path.isdir(test_sits_dir):
    os.mkdir(test_sits_dir)
if not os.path.isdir(test_safebars_dir):
    os.mkdir(test_safebars_dir)