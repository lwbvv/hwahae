import json


def noneRequiredKey(self,required_key,*keynames):
    no_required_key =""
    for key in keynames: #인자값으로 받은 keynames을 하나씩 대입
        if required_key != key: #리퀘스트의 키값에 키값이 있는지 확인
            no_required_key = f"{required_key} field is required"
    error = {"error":no_required_key}
    return error

def badRequiredValueCondition(self,required_value):
    dry = 'dry'
    oily = 'oily'
    sensitive = 'sensitive'
    no_required_key =""
    if required_value != dry and required_value != oily and required_value != sensitive:
        return True
    else:
        return False

def badRequiredValue(self,value):
    none_required_value =""
    required_value = ['dry','oily','sensitive']
    if not value in required_value: #리퀘스트의 키값에 키값이 있는지 확인
        none_required_value =\
         f"The skin type must choose one of the values {required_value[0]}, {required_value[1]}, or {required_value[2]}."
    error = {"error":{"input_value":value, "explanation":none_required_value}}
    return error



def jsonDumpsLoads(self,*arg,**kw):
    if str(arg) != "()":
        recommend_dict = json.loads(json.dumps(arg))
    elif str(kw) != "{}":
        recommend_dict = json.loads(json.dumps(kw))
    return recommend_dict

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
