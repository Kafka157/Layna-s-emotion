yy_list = ['play_genshin', 'play_hongkai_starrail', 'play_FGO', 'facetime_Layna']
Layna_emotion_list = ['broke up with yy', 'disappointed', 'sad', 'bored','happy']
Layna_emotion_states = [0, 0, 0, 0]

Layna_emotion_mapping = {
    (1, 1, 1, 0): 0,   # 'broke up with yy'
    (1, 1, 0, 0): 1,   # 'disappointed'
    (1, 0, 1, 0): 1,   # 'disappointed'
    (0, 1, 1, 0): 1,   # 'disappointed'
    (1, 0, 0, 0): 2,   # 'sad'
    (0, 1, 0, 0): 2,   # 'sad'
    (0, 0, 1, 0): 2,   # 'sad'
    (0, 0, 1, 1): 3,   # 'boring'
    (0, 1, 0, 1): 3,   # 'boring'
    (1, 0, 0, 1): 3,   # 'boring'
    (0, 0, 0, 1): 4,   # 'happy'
}


def test():
    input_states = input("Enter four numbers (0 or 1) separated by spaces: ")
    Layna_emotion_states[:] = [int(num) for num in input_states.split()]
    if tuple(Layna_emotion_states) in Layna_emotion_mapping:
        emotion_index = Layna_emotion_mapping[tuple(Layna_emotion_states)]
        print(f"Layna is feeling: {Layna_emotion_list[emotion_index]}")
    else:
        print(f"Layna can't understand.")
test()
