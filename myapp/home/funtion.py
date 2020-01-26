
class ImageParse:
    baseUrl = "https://grepp-programmers-challenges.s3.ap-northeast-2.amazonaws.com/2020-birdview/"
    thumbnail = "thumbnail/"
    def fullImage(self,str):
        fullImage = "image/"
        str = ImageParse.baseUrl + fullImage +str+".jpg"
        return str

    def thumbnailImage(self,str):
        thumbnail = "thumbnail/"
        str = ImageParse.baseUrl + thumbnail +str+".jpg"
        return str
