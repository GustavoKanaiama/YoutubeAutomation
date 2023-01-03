from PIL import Image, ImageDraw, ImageFont
from json import load

cl2=(211,233,233)
cl1=(24,25,26)


font_type = ImageFont.truetype('get_images/assets/verdanab.ttf', 40)

font_type_data = ImageFont.truetype('get_images/assets/verdanab.ttf', 30)

HORIZONTAL_SPACE_VALUE = 20
VERTICAL_SPACE_VALUE = 25
HORIZONTAL_BOUNDARY_MULTILINETEXT = 820 #pixels, fixed in xy=(100, y_location)

def breakline_text(text, max_width_px):

    comment_words_list = text.split(" ")

    temp_phrase = ""
    len_comment_words_list = len(comment_words_list)
    final_phrase_list = []
    temp_phrase_len_px = 0

    for j in range(len_comment_words_list):
            
 
        temp_phrase += comment_words_list[j] + " "
        temp_phrase_len_px = font_type.getsize(temp_phrase)[0] + font_type.getsize(comment_words_list[j])[0] #tamanho da frase + tamanho da palavra que receberá
        
        
        if temp_phrase_len_px >= max_width_px:
            final_phrase_list.append(temp_phrase)
            temp_phrase = ""

        # Em casos de max_width_px = 400, essa linha ajusta o comment_words_list[j] que sobra, ela da um append nele
        if (temp_phrase == (comment_words_list[j] + " ")) and (j == len_comment_words_list-1) : final_phrase_list.append(comment_words_list[j])
    

    final_phrase = '\n'.join(final_phrase_list)
    return final_phrase


def drawImage(json_obj, y_location=100):


    for i in range(len(json_obj)):
        image = Image.new('RGB', (1080,1920), color=cl1)
        draw = ImageDraw.Draw(image)

        font_type_size = font_type.getsize(json_obj[i]['autor']) #return (x,y)
        font_type_size_data = font_type_data.getsize(json_obj[i]['data']) #return (x,y)

        draw.text(xy=(100, y_location), text=json_obj[i]['autor'], fill=(89, 161, 210), font=font_type, anchor='ls')
        
        draw.text(xy=(100+font_type_size[0]+HORIZONTAL_SPACE_VALUE, y_location), text="• "+json_obj[i]['data'], fill=(110, 125, 135), font=font_type_data, anchor='ls')

        final_phrase = breakline_text(json_obj[i]['comentario'], HORIZONTAL_BOUNDARY_MULTILINETEXT)
        draw.multiline_text(xy=(100, y_location + VERTICAL_SPACE_VALUE), text=final_phrase, fill=(cl2), font=font_type)


        #cada n caracteres, inclui \n (caso nao venha com a linha quebrada)

        image.save("get_images/images/image_test" + str(i) +".jpeg")


# Opening JSON file
with open('comments_script.json', 'r') as openfile:
    json_object = load(openfile) #json.load()

#text_manipulation = json_obj[i]['comentario']
#breakline_text(text_manipulation, HORIZONTAL_BOUNDARY_MULTILINETEXT)
drawImage(json_object)



