from PIL import Image, ImageDraw, ImageFont
from json import load
import textwrap

def drawImage(json_obj, y_location=100, horiz_space=20, vert_space=25, horiz_boundary_multLineText=820):

    cl1=(24,25,26)
    cl2=(211,233,233)

    HORIZONTAL_SPACE_VALUE = horiz_space
    VERTICAL_SPACE_VALUE = vert_space
    HORIZONTAL_BOUNDARY_MULTILINETEXT = horiz_boundary_multLineText # pixels, fixed in xy=(100, y_location)

    font_type = ImageFont.truetype('get_images/assets/verdanab.ttf', 40)
    font_type_data = ImageFont.truetype('get_images/assets/verdanab.ttf', 30)

    #y_location variable is working like a "pointer", poiting to a specifically y_location

    # Draw the title
    image = Image.new('RGB', (1080,1920), color=cl1)
    draw = ImageDraw.Draw(image)

    final_phrase = "\n".join(textwrap.wrap(text=json_obj[0]['titulo'], width=40))
    

    draw.multiline_text(xy=(70, 40), text=final_phrase, fill=(cl2), font=font_type, align="center", spacing=15)

    h_title = font_type.getsize_multiline(final_phrase)[1]
    w_title = font_type.getsize_multiline(final_phrase)[0]


    # crop and save title image
    image = image.crop((0, 0, 1040, h_title+80+VERTICAL_SPACE_VALUE)) #(left, top, right, bottom)

    image.save(f"get_images/images/image_test_title.jpeg")

    for i in range(len(json_obj)):
        image = Image.new('RGB', (1080,1920), color=cl1)
        draw = ImageDraw.Draw(image)

        text_width_size = font_type.getsize(json_obj[i]['autor']) #return (x,y) -> (comprimento, altura), se o texto for multile, usa getsize_multiline()
        

        # Draw the commment
        draw.text(xy=(100, y_location), text=json_obj[i]['autor'], fill=(89, 161, 210), font=font_type, anchor='ls')
        draw.text(xy=(100+text_width_size[0]+HORIZONTAL_SPACE_VALUE, y_location), text=json_obj[i]['data'], fill=(110, 125, 135), font=font_type_data, anchor='ls')

        final_phrase = "\n".join(textwrap.wrap(text=json_obj[i]['comentario'], width=35))

        draw.multiline_text(xy=(100, y_location + VERTICAL_SPACE_VALUE), text=final_phrase, fill=(cl2), font=font_type)

        y_location += VERTICAL_SPACE_VALUE

        # Draw the 1(first) response
        y_location += font_type.getsize_multiline(final_phrase)[1] + VERTICAL_SPACE_VALUE + 20

        autorResp_width_size = font_type.getsize(json_obj[i]['respostas'][0]['autor_resp'])

        draw.text(xy=(200, y_location), text=json_obj[i]['respostas'][0]['autor_resp'], fill=(89, 161, 210), font=font_type, anchor='lt')
        draw.text(xy=(200+autorResp_width_size[0]+HORIZONTAL_SPACE_VALUE, y_location), text=json_obj[i]['respostas'][0]['data_resp'], fill=(110, 125, 135), font=font_type_data, anchor='lt')

        final_phrase_resp1 = " ".join(textwrap.wrap(text=json_obj[i]['respostas'][0]['comentario_resp'], width=HORIZONTAL_BOUNDARY_MULTILINETEXT))

        draw.multiline_text(xy=(200, y_location + 2*VERTICAL_SPACE_VALUE), text=final_phrase_resp1, fill=(cl2), font=font_type, anchor='la')

        # Draw the 2(second) response
        resp1_total_height = y_location + VERTICAL_SPACE_VALUE + font_type.getsize(json_obj[i]['respostas'][0]['autor_resp'])[1] + font_type.getsize_multiline(final_phrase_resp1)[1]

        y_location = resp1_total_height

        draw.text(xy=(200, y_location), text=json_obj[i]['respostas'][1]['autor_resp'], fill=(89, 161, 210), font=font_type, anchor='lt')
        draw.text(xy=(200+autorResp_width_size[0]+HORIZONTAL_SPACE_VALUE, y_location), text=json_obj[i]['respostas'][1]['data_resp'], fill=(110, 125, 135), font=font_type_data, anchor='lt')

        final_phrase_resp2 = " ".join(textwrap.wrap(text=json_obj[i]['respostas'][1]['comentario_resp'], width=HORIZONTAL_BOUNDARY_MULTILINETEXT))

        draw.multiline_text(xy=(200, y_location + 2*VERTICAL_SPACE_VALUE), text=final_phrase_resp2, fill=(cl2), font=font_type, anchor='la')

        y_location_final = y_location
        
        #Draw Vertical line (aesthetic)
        #voltando para a altura do primeiro comentário (linha do resp1_total_height ...)

        y_location -= 2*VERTICAL_SPACE_VALUE + 2*font_type.getsize(json_obj[i]['respostas'][0]['autor_resp'])[1] + font_type.getsize_multiline(final_phrase_resp2)[1] + font_type.getsize_multiline(final_phrase_resp1)[1] #apontando para o fim do comentário(principal)
        
        h_initial = y_location + 2.5*VERTICAL_SPACE_VALUE
        h_final = y_location_final

        if final_phrase_resp1 == " ": h_final = h_initial
        if (final_phrase_resp2 == " ") and (final_phrase_resp1 != " "): h_final -= 6*VERTICAL_SPACE_VALUE

        image = image.crop((0, 20, 1040, h_final))

        image.save("get_images/images/image_test" + str(i) +".jpeg")
        y_location = 100

# Opening JSON file
with open('json_files/comments_script.json', 'r') as openfile:
    json_object = load(openfile) #json.load()


drawImage(json_object)
"""
"""

