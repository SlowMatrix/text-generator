def train(save=None, date_dir="date", nwm = 4, text_to_model=None): # функция для генерации модели
    """
    nwm ко скольки словам составлять список
    date_dir директория из которой брать файлы для обучения
    text_to_model если вы не хотите брать файл а хотите передать текст в формате стр передайте его сюда
    """
    import os # os для получения названия файлов в папке date
    import pickle # для сохранения модели
    model = {} # модель как словарь
    texts = [] # тексты это список для того чтобы последнее слово одного файла не крепилось к начальному другова

    if text_to_model != None: # провереяем задал ли пользователь текст
        texts.append(text) # дабавляем текст в тексты
        
    for i in os.listdir(date_dir): # роверяем какие файлы есть в деректории откуа мы берём обучающую выборку
        with open(f"{date_dir}\\{i}", encoding="utf-8") as f: # открываем файл
            texts.append(f.read().replace(".", " . ").replace(",", " , ").replace("?", " ? ").replace("  ", " ").strip().split()) # записываем его
            
    for text in texts:
        for word in range(nwm, len(text)):
            if (a := tuple(text[i-nwm+word-1] for i in range(4, 0, -1))) in model: # роверка на то есть ли сочетание слов(для примера: (" . ", "питон", люблю", "Я")) в модели
                if text[word] in model[a]: # проверка на то есть ли слово в сочетание слов  
                    model[a][text[word]] += 1 # если есть то просто добавим к ниму одно встречание
                else:
                    model[a][text[word]] = 1 # а если нет то добавим его туда
            else:
                model[a] = {text[word]: 1} # добавление сочитания слов к модели 
                
    if type(save) == str: # если надосохранить то сохраняем
        if not ".pkl" in save: # добовляем .pkl, если это нужно, для того что-бы небыло ошибок
            save += ".pkl"
        with open(save, 'wb') as f: # сохроняем
            pickle.dump(model, f)
    return model # возвращаем (навсякий случай, вдруг надо)