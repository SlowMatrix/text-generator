
        

if __name__ == "__main__":
    import os
    from train imoprt *
    from gemerate import *
    
    mn = input("model name: ")
    
    if mn != "":
        train(save=mn)
    
    seed = input("seed (если нажать Enter то сид выберется автоматичесски): ")
    
    if len(ld := [i for i in os.listdir() if i[-4:] == ".pkl"]) > 1:
        model = input(f"{', '.join(ld)}\nназвание используемой модели: ")
    else:
        model = ld[0]
    
    if seed == "":
        seed = None
    else:
        seed = tuple(seed.split())
    
    print(f'result:\n{generate_text(seed, model, int(input("длинна фразы в словах: ")), input("save name: "))}')
    
