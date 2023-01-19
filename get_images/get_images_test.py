from PIL import Image, ImageDraw, ImageFont
from json import load
from math import ceil


def breakline_text(text, max_width_px):

    font_type = ImageFont.truetype('get_images/assets/verdanab.ttf', 40)

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
        if (j == len_comment_words_list-1): 
            final_phrase_list.append(temp_phrase)

    final_phrase = '\n'.join(final_phrase_list)
    return final_phrase

def drawImage(json_obj, y_location=100, horiz_space=20, vert_space=25, horiz_boundary_multLineText=820):

    VERTICAL_LIMIT = 650

    cl1=(24,25,26)
    cl2=(211,233,233)

    HORIZONTAL_SPACE_VALUE = horiz_space
    VERTICAL_SPACE_VALUE = vert_space
    HORIZONTAL_BOUNDARY_MULTILINETEXT = horiz_boundary_multLineText #pixels, fixed in xy=(100, y_location)

    font_title = ImageFont.truetype('get_images/assets/verdanab.ttf', 50)
    
    font_type = ImageFont.truetype('get_images/assets/verdanab.ttf', 40)
    font_type_data = ImageFont.truetype('get_images/assets/verdanab.ttf', 30)

    #y_location variable is working like a "pointer", poiting to a specifically y_location

    last_item = len(json_obj)-1

    # Draw the title
    image = Image.new('RGB', (1080,1920), color=cl1)
    draw = ImageDraw.Draw(image)

    final_phrase = breakline_text(json_obj[last_item]['titulo'], HORIZONTAL_BOUNDARY_MULTILINETEXT)
    draw.multiline_text(xy=(70, 60), text=final_phrase, fill=(cl2), font=font_title, align="center", spacing=15)

    h_title = font_title.getsize_multiline(final_phrase)[1]


    #------
    y_location += h_title + VERTICAL_SPACE_VALUE

    start_y_selftext = y_location

    #Draw jsonTitle_text

    autor_size = font_type.getsize(json_obj[last_item]['autor']) #return (x,y) -> (comprimento, altura), se o texto for multile, usa getsize_multiline()
    

    # Draw the commment

    final_phrase = breakline_text(json_obj[last_item]['selftext'], HORIZONTAL_BOUNDARY_MULTILINETEXT)
    draw.multiline_text(xy=(100, y_location), text=final_phrase, fill=(cl2), font=font_type)

    selftext_height_size = font_type.getsize_multiline(final_phrase)[1]

    y_location += VERTICAL_SPACE_VALUE

    h_final = y_location + autor_size[1] + 1*VERTICAL_SPACE_VALUE + selftext_height_size
    
    h_final_ref = h_final # guardar em uma variável para usar como referencia como o tamanho final do selftext

    #image = image.crop((0, 20, 1040, h_final))



    ## breakimage (vetical limit)


    # Caso seja menor que o limite (o crop será no limite)
    if h_final <= VERTICAL_LIMIT:
        h_final = VERTICAL_LIMIT

    y_savePointer = start_y_selftext
    y_lastSavePointer = 0

    selftextLineHeight = font_type.getsize(json_obj[last_item]['selftext'])[1]


    print(selftextLineHeight)


    for i in range(ceil(h_final / VERTICAL_LIMIT)):



        print(y_lastSavePointer)
        print(y_savePointer)
        print()

        while y_savePointer + selftextLineHeight < VERTICAL_LIMIT:
            y_savePointer += selftextLineHeight
        
        print(y_savePointer)
        
        image.crop((0, y_lastSavePointer, 1040, y_savePointer)).save("get_images/images/image_selfText["+str(i)+"].jpeg")

        if y_savePointer + VERTICAL_LIMIT < 1920 : 
            y_lastSavePointer = y_savePointer
            y_savePointer += VERTICAL_LIMIT
        else:
            y_savePointer = h_final_ref
        
 
    ## ending of breakimage vetical limit




    


    y_location = 100


    for i in range(len(json_obj)-1):
        image = Image.new('RGB', (1080,1920), color=cl1)
        draw = ImageDraw.Draw(image)

        text_width_size = font_type.getsize(json_obj[i]['autor']) #return (x,y) -> (comprimento, altura), se o texto for multile, usa getsize_multiline()
        

        # Draw the commment
        draw.text(xy=(100, y_location), text=json_obj[i]['autor'], fill=(89, 161, 210), font=font_type, anchor='ls')
        draw.text(xy=(100+text_width_size[0]+HORIZONTAL_SPACE_VALUE, y_location), text=json_obj[i]['data'], fill=(110, 125, 135), font=font_type_data, anchor='ls')

        final_phrase = breakline_text(json_obj[i]['comentario'], HORIZONTAL_BOUNDARY_MULTILINETEXT)
        draw.multiline_text(xy=(100, y_location + VERTICAL_SPACE_VALUE), text=final_phrase, fill=(cl2), font=font_type)

        y_location += VERTICAL_SPACE_VALUE

        # Draw the 1(first) response
        y_location += font_type.getsize_multiline(final_phrase)[1] + VERTICAL_SPACE_VALUE + 70

        autorResp_width_size = font_type.getsize(json_obj[i]['respostas'][0]['autor_resp'])

        draw.text(xy=(200, y_location), text=json_obj[i]['respostas'][0]['autor_resp'], fill=(89, 161, 210), font=font_type, anchor='lt')
        draw.text(xy=(200+autorResp_width_size[0]+HORIZONTAL_SPACE_VALUE, y_location), text=json_obj[i]['respostas'][0]['data_resp'], fill=(110, 125, 135), font=font_type_data, anchor='lt')

        final_phrase_resp1 = breakline_text(json_obj[i]['respostas'][0]['comentario_resp'], HORIZONTAL_BOUNDARY_MULTILINETEXT)
        draw.multiline_text(xy=(200, y_location + 2*VERTICAL_SPACE_VALUE), text=final_phrase_resp1, fill=(cl2), font=font_type, anchor='la')

        # Draw the 2(second) response
        resp1_total_height = y_location + 2*VERTICAL_SPACE_VALUE + font_type.getsize(json_obj[i]['respostas'][0]['autor_resp'])[1] + font_type.getsize_multiline(final_phrase_resp1)[1]

        y_location = resp1_total_height

        draw.text(xy=(200, y_location), text=json_obj[i]['respostas'][1]['autor_resp'], fill=(89, 161, 210), font=font_type, anchor='lt')
        draw.text(xy=(200+autorResp_width_size[0]+HORIZONTAL_SPACE_VALUE, y_location), text=json_obj[i]['respostas'][1]['data_resp'], fill=(110, 125, 135), font=font_type_data, anchor='lt')

        final_phrase_resp2 = breakline_text(json_obj[i]['respostas'][1]['comentario_resp'], HORIZONTAL_BOUNDARY_MULTILINETEXT)
        draw.multiline_text(xy=(200, y_location + 2*VERTICAL_SPACE_VALUE), text=final_phrase_resp2, fill=(cl2), font=font_type, anchor='la')

        y_location_final = y_location + 2*VERTICAL_SPACE_VALUE
        
        #Draw Vertical line (aesthetic)
        #voltando para a altura do primeiro comentário (linha do resp1_total_height ...)

        y_location -= 2*VERTICAL_SPACE_VALUE + 2*font_type.getsize(json_obj[i]['respostas'][0]['autor_resp'])[1] + font_type.getsize_multiline(final_phrase_resp2)[1] + font_type.getsize_multiline(final_phrase_resp1)[1] #apontando para o fim do comentário(principal)
        
        h_initial = y_location + 2.5*VERTICAL_SPACE_VALUE
        h_final = y_location_final + 3*VERTICAL_SPACE_VALUE

        if final_phrase_resp1 == " ": h_final = h_initial
        if (final_phrase_resp2 == " ") and (final_phrase_resp1 != " "): h_final -= 6*VERTICAL_SPACE_VALUE

        draw.line(xy=[(120, h_initial), (120, h_final)], width=1, fill=(142, 145, 151))

        image = image.crop((0, 20, 1040, h_final))


        image.save("get_images/images/image_test" + str(i) +".jpeg")
        y_location = 100



# Opening JSON file
with open('comments_script.json', 'r') as openfile:
    json_object = load(openfile) #json.load()


drawImage(json_object)
"""

"""
