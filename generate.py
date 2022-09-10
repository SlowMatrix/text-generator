def generate(seed=None, model="model.pkl", length=10, save="text.txt"): # функция для генерации текста на основе модели
    import pickle # модуль для сохранения модели
    from random import randint # рандом для выбора следующего слова
    
    if not ".pkl" in model: # устраняем возможную проблему импорта
            model += ".pkl"
            
    with open(model, 'rb') as f: # импортируем
        model = pickle.load(f)

    if seed != None: # если сид задан то переварачиваем его и преабразуем в кортедж (навсякий случай) а иначе берём его из модели 
        seed = tuple(reversed(seed))
    else:
        seed = tuple(model)[1]

    out = [*reversed(seed)] # добавляем сид в out чтобы избежать ошибок в смысле
    
    for i in range(length-len(seed)):
        if not seed in model:
            break

        n = []
        for i in range(len(model[seed])): # оздаём список n в котором будут лежать варианты следующего слова согластно их количеству
            z = model[seed][(s := list(model[seed])[i])]
            n += [s]*z
            
        out.append(n[randint(0, len(n)-1)]) # обавляем выбранное слово в out
        
        seed = tuple([out[-1]]+list(seed[0:-1])) # 

    out = " ".join(out).replace(" . ", ". ").replace(" ! ", "! ").replace(" ? ", "? ").replace(" ... ", "... ").replace(" , ", ", ")
                                                                            # исправляем некоторые косяки вроде:
    if not save in [None, ""]:                                              #что-то , что-то а в исправленном: что-то, что-то и тд. и тп. 
        with open(save, "w") as f:
            f.write(out)    
    return out