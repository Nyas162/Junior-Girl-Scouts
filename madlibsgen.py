class MadLibs: 
        def __init__(self, word_descriptions, template): 
            self.template = template 
            self.word.descriptions = word_descriptions
        

        #user input
        # 

def get_words_from_user(word_descriptions):
    words  = []
    print("Please provide the following words:")
    for desc in word_descriptions:
            user_input = input(desc + " ")
            words.append(user_input)
    return words



def build_story(template, words):
        story = template.format(*words)
        return story


template = "I have always enjoyed eating many {} kinds of foods. For breakfast, I usually have {} piece(s) of {}, a {} egg, a {} milk, and a glass of {} juice. From Monday to Friday, I eat lunch at my school. I love Wednesdays because we have {} pizza! At school, I sit with {} who always tells jokes about {}. My lunch lady's name is {}. When I get home from school, I eat a {}. I usually eat it with a {} apple or some {}. I think my favorite meal is dinner. My family {} together at the table. Sometimes my mom cooks {} or {}. But my favorite is when she makes {} cookies. They are {}. They are supeper gooey and oozing with {}. The next day at school, I cant stop {} about the cookies. Yum! Can't wait to eat {} {} tonight for dinner!"

words = get_words_from_user (["adjective", "number", "food", "adjective", "adjective", "fruit or vegetable", "animal",  
"Friend's Name", "noun", "Celebrity",  "animal", "adjective", "food", "verb,", "noun", 
"noun)", "flavor","adjective", "noun", "verb ending in -ing", "adjective", "noun"])


story = build_story(template, words)
print(story)