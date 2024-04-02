import base64
import io
import random
import string
import cv2


import numpy as np
import urllib3
# from botocore.exceptions import NoCredentialsError
# from flask import request, jsonify
# from PIL import Image, UnidentifiedImageError

# from headswapper import HeadSwapObj
# from headswapper.headswapper import HeadSwapper
# from headswapper.utils.img_debug_helper import timer_main
# from headswapper.head_mask_creator import HeadMaskCreator
from time import time

from collections import OrderedDict

import json


# def read_encoded_img(encoded_img):
#     img = base64.b64decode(encoded_img)
#     return img

# from flask import Flask, jsonify

import cv2
import base64
def encode_img(img):
    _, img_buffer = cv2.imencode('.webp', img)
    encoded_img = base64.b64encode(img_buffer)
    # return encoded_img
    return encoded_img.decode('utf-8')


def decode_img(encoded_img,mask=False):
    decoded_img = base64.b64decode(encoded_img)
    img_np_arr = np.frombuffer(decoded_img, np.uint8)
    if mask:
        img = cv2.imdecode(img_np_arr,cv2.IMREAD_UNCHANGED)
        if img is not None and len(img.shape) == 3 and img.shape[2] == 2:
            pass
        else:
            img= img[:,:,2]
    else:
         img = cv2.imdecode(img_np_arr, cv2.IMREAD_COLOR)
    return img



# def make_headswapObj_from_json(headswapObj_json, iie, encoded=True):
#     img=decode_img(headswapObj_json["head_img"])
#
#     headswapObj = HeadSwapObj(
#         img,
#         iie,
#         FD_coordinates=headswapObj_json["FD_coordinates"],
#         LM_coordinates=headswapObj_json["LM_coordinates"],
#         headselection_mask=decode_img(headswapObj_json["headselection_mask"], mask=True),
#         skincolor=headswapObj_json["skincolor"]
#     )
#     headswapObj.betweeneyes_coordinates = headswapObj_json["LM_coordinates"]["betweeneyes"]
#     headswapObj.nose_coordinates = headswapObj_json["LM_coordinates"]["nose_coordinats"]
#     headswapObj.cheek_coordinates = headswapObj_json["LM_coordinates"]["cheek_coordinates"]
#     headswapObj.chin_coordinates = headswapObj_json["LM_coordinates"]["chin_coordinates"]
#     headswapObj.eye_distance = headswapObj_json["LM_coordinates"]["eye_distance"]
#     headswapObj.eyegap_chin_distance = headswapObj_json["LM_coordinates"]["eyegap_chin_distance"]
#     headswapObj.FACE_EXIST=True
#     headswapObj.LM_CALCULATED=True
#     headswapObj.LANDMARK_EXIST=True
#     HeadSwapObj.COMPATIBLE_IMAGE= True
#     HeadSwapObj.skincolor_CALCULATED= True
#     return headswapObj


    # head = headswapObj_json["head_img"]
    # headselection_mask = headswapObj_json["headselection_mask"]
    # FD_coordinates = headswapObj_json["FD_coordinates"]
    # LM_coordinates = headswapObj_json["LM_coordinates"]
    # skincolor = headswapObj_json["skincolor"]
    #
    # head = decode_img(head)
    # headselection_mask = decode_img(headselection_mask)
    #
    # headswapObj = HeadSwapObj(
    #     head,
    #     iie,
    #     FD_coordinates=FD_coordinates,
    #     LM_coordinates=LM_coordinates,
    #     headselection_mask=headselection_mask,
    #     skincolor=skincolor
    # )

    # headswapObj.nose_coordinates = LM_coordinates["nose_coordinats"]
    # headswapObj.cheek_coordinates = LM_coordinates["cheek_coordinates"]
    # headswapObj.chin_coordinates = LM_coordinates["chin_coordinates"]
    # headswapObj.eye_distance = LM_coordinates["eye_distance"]
    # headswapObj.eyegap_chin_distance = LM_coordinates["eyegap_chin_distance"]
    #
    # return headswapObj
#
# def prepare_response_for_MANIPULATE_DOM_IMAGE(iie, ch, incoming_data, logger):
#     ASD, domain, source_headswapObjs, format, mode, data, package_sent_time = incoming_data
#
#     source=make_headswapObj_from_json(source_headswapObjs, iie, encoded=True)
#
#     img = data["images"]
#
#     if mode == "encoded":
#         img = decode_img(img)
#         target = HeadSwapObj(img, iie)
#
#         HS = HeadSwapper(source, target, ch, debugging=False, logger=logger)
#         encoded_result_image = encode_img(HS.result)
#         response = {
#             "status": "1 ",
#             "data_package": [{"image": encoded_result_image}],
#             "time": "24-OCT-1994 04:31:17.01",
#             "counter": "2",
#         }
#
#
#         return response
#     elif format == "url":
#         pass

def  prepare_meta_dict( success, error_code,debug_log, package_sent_time, extra_field):
        meta= { "success":success,
                "error_code": error_code,
                "debug_log": debug_log,
                "package_sent_time": package_sent_time,
                "extra_field":extra_field
            }

        return meta



def prepare_data_dict_MAN_DOM( encoded_result_image, et):
    data_dict = {
        "images": [{"result": encoded_result_image}],
        "total_time": et,

    }


    response = json.dumps(data_dict, cls=NumpyEncoder)
    return response


def extract_meta_information():
    pass

def check_metadata_validity(meta_data):
    return True



# def digest_package_content_and_make_headswap(iie, ch,  config, data, logger):
#     # ASD, domain, source_headswapObjs, format, mode, data, package_sent_time = package_content
#
#     elapsed_time = OrderedDict()
#     time0= time()
#
#     source1_data=data["source_headswapObjs"][0]
#     source_pose1 = make_headswapObj_from_json( source1_data, iie, encoded=True)
#     # source_pose2 = make_headswapObj_from_json(source1_data, iie, encoded=True)
#     # source_pose3 = make_headswapObj_from_json(source1_data, iie, encoded=True)
#
#     time1= time()


    # if  config["return_img_format"] == "encoded":
    #
    #     img = decode_img(data["target_image"])
    #     time2 = time()
    #
    #     target = HeadSwapObj(img, iie)
    #     time3 = time()
    #
    #     COMPATIBLE, details = target.check_compatibility()
    #     encoded_result_image = None
    #
    #     if COMPATIBLE:
    #         target.tick_compatibility()
    #
    #         HS = HeadSwapper(source_pose1, target, ch, debugging=False, logger=logger)
    #         time4 = time()
    #         encoded_result_image = encode_img(HS.result)
    #         time5= time()
    #     else:
    #          pass



    # elapsed_time["Total_ImgOp_Time"] =  round(time5-time0 ,3)
    # # elapsed_time["data_processing_start_time"] = time0
    # elapsed_time["source_heads_creation"] =  round(time1 - time0,3)
    # elapsed_time["decoding_target_img"] =  round(time2 - time1,3)
    # elapsed_time["creating_target_headswapObj"] = round( time3 - time2,3)
    # elapsed_time["headswapping"] =  round(time4 - time3 ,3)
    # elapsed_time["encoding_result_img"] =  round(time5 - time4 ,3)
    #
    # return (COMPATIBLE,details), encoded_result_image, elapsed_time

def preprocess_package_content():
    pass
# def digest_package_content_and_extract_head(iie,encoded_img, logger):
#     elapsed_time = OrderedDict()
#     time0 = time()
#
#     decoded_img = decode_img(encoded_img)
#     time1 = time()
#     source = HeadSwapObj(decoded_img, iie,  used_as_source=True)
#     time2 = time()
#     IS_COMPATIBLE, DETAILS=source.check_compatibility()
#
#     if IS_COMPATIBLE:
#
#         logger.debug( " " * 20 + "Img is compatible "   )
#         HE = HeadMaskCreator(source, CROP_Head=True, logger=logger)
#         time3 = time()
#         source = HE.headswapObj
#         logger.debug(" " * 20 + "HeadMask prepared ")
#
#     elapsed_time["Total_ImgOp_Time"] = round( time3 - time0 , 3)
#     elapsed_time["decoding_img"] = round( time1 - time0, 3)
#     elapsed_time["create_headswapObj"] =round(  time2 - time1, 3)
#     elapsed_time["create_headmask"] = round( time3 - time2, 3)
#
#     return (IS_COMPATIBLE,DETAILS), source ,elapsed_time


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NumpyEncoder, self).default(obj)

def prepare_data_dict(source, et):
    a = encode_img(source.img)
    b = encode_img(source.headselection_mask)
    c = encode_img(source.transparent_head)

    data_dict= {
        "images":{
              "head":  a,
              "headselection_mask":b,
              "head_transparent": c
        } ,
        "FD_coordinates": source.FD_coordinates,
        "LM_coordinates":
            {
                "betweeneyes": source.betweeneyes_coordinates,
                "nose_coordinats": source.nose_coordinates,
                "cheek_coordinates": source.cheek,
                "chin_coordinates": source.chin_coordinates,
                "eye_distance": source.eye_distance,
                "eyegap_chin_distance": source.eyegap_chin_distance,
            }
        ,
        "skincolor": source.skincolor,
        "total_time":et




    }
    response = json.dumps(data_dict, cls=NumpyEncoder)
    return response


#
# def prepare_post_answer_for_MANIPULATE_USR_IMAGE(iie,encoded_img, logger):
#     decoded_img = decode_img(encoded_img)
#     source = HeadSwapObj(decoded_img, iie)
#
#     if source.COMPATIBLE_IMAGE:
#
#         HE = HeadMaskCreator(source, CROP_Head=True, logger=logger)
#         source = HE.headswapObj
#
#         a=encode_img(source.img)
#         b=encode_img(source.headselection_mask)
#
#         status = "success"
#         # time = time()
#         counter = -99
#
#         return {
#             "status": status,
#             "encoded_image": [a, b],
#             "landmarks": [
#                 {
#                     "nose_coordinats": source.nose_coordinates,
#                     "cheek_coordinates": source.cheek_coordinates,
#                     "chin_coordinates": source.chin_coordinates,
#                     "eye_distance": source.eye_distance,
#                     "eyegap_chin_distance": source.eyegap_chin_distance,
#                 }
#             ],
#             "skincolor": (255, 0, 0),
#             "time": "time",
#             "counter": counter,
#         }
#
#     else:
#         status = 0
#         # time = time()
#         counter = -99
#
#         return {
#             "status": status,
#             "encoded_image": [],
#             "landmarks": [],
#             "time": time,
#             "counter": counter,
#         }


# def upload_to_aws(s3, local_file, bucket, s3_file):
#     # s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
#     #                   aws_secret_access_key=SECRET_KEY)
#
#     try:
#         s3.upload_file(local_file, bucket, s3_file)
#         # print("Upload Successful")
#         return True
#     except FileNotFoundError:
#         # print("The file was not found")
#         return False
#     except NoCredentialsError:
#         # print("Credentials not available")
#         return False


def create_random_name(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str


def create_felix_image_dict(src, manipulated_image_url):
    image_dict = {
        "id": 0,
        "src": src,
        "left": 0,
        "top": 0,
        "manipulatedImage": manipulated_image_url,
    }
    return image_dict


# @timer_main
# def read_img_with_user_agent(url):
#     user_agent = {"user-agent": "Mozilla/5.0 (Windows NT 6.3; rv:36.0) .."}
#     http = urllib3.PoolManager(10, headers=user_agent)
#     r1 = http.urlopen("GET", url)
#     LINK_IS_IMAGE = False
#     im2arr = []
#     try:
#         image = Image.open(io.BytesIO(r1.data))
#         im2arr = np.array(image)
#         LINK_IS_IMAGE = True
#     except UnidentifiedImageError:
#         pass
#     return im2arr, LINK_IS_IMAGE


# def extract_image_urls_from_post_call():
#     json = request.get_json()
#     length = len(json["images"])
#     print("num of images:", length)
#     # print(" json['images']:",json['images'])
#
#     list_of_image_links = []
#
#     for i in range(length):
#         temp = json["images"][i]["src"]
#         list_of_image_links.append(temp)
#         # print(" img:",i," ",temp)
#
#     return list_of_image_links


# def save_and_get_local_links_of_images(list_of_images,server_folder_path, local_host_path ):
#         list_manipulated_image_links=[]
#         for img in list_of_images :
#             counter=0
#             save_path=server_folder_path+str(counter)+".jpg"
#             list_manipulated_image_links.append(local_host_path +str(counter)+".jpg")
#             cv2.imwrite(save_path, cv2.cvtColor(img, cv2.COLOR_RGB2BGR) )
#             counter=counter+1
#         return list_manipulated_image_links

# def create_felix_return_package(list_manipulated_image_links,list_of_org_image_links):
#         list_of_image_dicts=[]
#         for url, i in enumerate(list_manipulated_image_links):

#             image_dict=create_felix_image_dict(list_of_org_image_links[i],url)
#             list_of_image_dicts.append(image_dict)
#         return list_of_image_dicts

# def create_felix_return_package(list_manipulated_image_links,list_of_org_image_links):
#         list_of_image_dicts=[]
#         for url, i in enumerate(list_manipulated_image_links):

#             image_dict=create_felix_image_dict(list_of_org_image_links[i],url)
#             list_of_image_dicts.append(image_dict)
#         return list_of_image_dicts


def save_and_get_local_links_of_images(
    list_of_images,
    save_folder_path,
):
    list_manipulated_image_links = []
    names = []
    for img in zip(list_of_images):
        filename = create_random_name(8)
        full_save_path = save_folder_path + filename + ".jpg"
        list_manipulated_image_links.append(full_save_path)
        names.append(filename)
        cv2.imwrite(full_save_path, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))

    return list_manipulated_image_links, names
