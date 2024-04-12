
# download external data 
!wget -r -nH -nd -np -P /path/to/save/folder https://motchallenge.net/data/HT21.zip

# clone github repo
!git clone https://github.com/Sentient07/HeadHunter--T /content/drive/MyDrive/_projects/HeadHunter


# copy file
!cp "/content/drive/My Drive/TAI-sorted.zip"  "/content/json"

## unzip metadate file
!tar -xvf  '/content/drive/My Drive/dataSet/danbooru2019/metadata.json.tar.xz' -C '/content/drive/My Drive/dataSet/danbooru2019/metadata'
!unzip "/content/drive/My Drive/TAI-important.zip" -d "/content"

# compress folder
!zip -r "e_images.zip" "/content/e_img" 

# kaggle
!pip install -q kaggle
!pip install -q kaggle-cli
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!kaggle datasets list -s tagged-anime-illustrations
!kaggle datasets download -d mylesoneill/tagged-anime-illustrations

## download images folder in original folder
for x in range(99,100):
  !rsync --recursive --verbose rsync://78.46.86.149:873/danbooru2019/original/00{x} "/content/drive/My Drive/dataSet/danbooru2019/original"
  
