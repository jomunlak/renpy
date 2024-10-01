


init -999 python:
    if not "zenpy_fonts" in renpy.session:
        renpy.session["zenpy_fonts"] = {}
    if not "old_get_font" in renpy.session:
        try:
            renpy.session["old_get_font"]  = renpy.text.font.get_font;
            def zenpy_get_font_hook(*args):
                if args[0].find("zen_fonts") == -1 and renpy.session["zenpy_fonts"] != None and _preferences.language in renpy.session["zenpy_fonts"] and 'Default' in renpy.session["zenpy_fonts"][_preferences.language]:
                    replace_font = renpy.session["zenpy_fonts"][_preferences.language]["Default"]
                    args = (replace_font,) + args[1:]
                return  renpy.session["old_get_font"](*args)
            renpy.text.font.get_font = zenpy_get_font_hook
        except:
            pass

translate ko_zenpy python:
    font_values = {
        "interface_text_font": "NanumBarunGothic.ttf",
        "button_text_font": "NanumBarunGothic.ttf",
        "choice_button_text_font": "NanumBarunGothic.ttf",
        "text_font": "NanumBarunGothic.ttf",
        "name_text_font": "NanumBarunGothic.ttf",
        "Default": "NanumBarunGothic.ttf"
    }
    if not "zenpy_fonts" in renpy.session:
        renpy.session["zenpy_fonts"] = {}
   
    if not "ko_zenpy" in renpy.session["zenpy_fonts"]:
        renpy.session["zenpy_fonts"]["ko_zenpy"]  = {}
        for k in font_values:
              
            if font_values[k].strip() != "" and k != "Default":
                font_values[k] = "tl/ko_zenpy/zen_fonts/" + font_values[k] ;
                renpy.session["zenpy_fonts"]["ko_zenpy"][k] = {"object": FontGroup().add(font_values[k], 0x5187, 0x5187).add(font_values[k], 0x5463, 0x5463).add(font_values[k], 0x5c44, 0x5c44).add(font_values[k], 0x5c4c, 0x5c4c).add(font_values[k], 0x808f, 0x808f).add(font_values[k], 0x6294, 0x6294).add(font_values[k], 0x2014, 0x201F).add(font_values[k], 0x2E80, 0xffff).add(font_values[k], 0x0000, 0xffff)}
            elif k == "Default":
                font_values[k] = "tl/ko_zenpy/zen_fonts/" + font_values[k];
                renpy.session["zenpy_fonts"]["ko_zenpy"]["Default"] = font_values[k]
    for k in renpy.session["zenpy_fonts"]["ko_zenpy"]:
        if hasattr(gui,k) and k != "Default":
            setattr(gui,k,renpy.session["zenpy_fonts"]["ko_zenpy"][k]["object"])






# Credits to anonymousException for help 
# https://github.com/anonymousException/renpy-translator/tree/main