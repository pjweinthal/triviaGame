from question import questionClass
def triviaQuestRet():
    questionList = []
    questionList.append(questionClass('How many days are in a lunar year?', '1. 354', '2. 365', '3. 243', '4. 379', '1'))
    questionList.append(questionClass('What is the largest planet?', '1. Mars', '2. Jupiter', '3. Earth', '4. Pluto', '2'))
    questionList.append(questionClass('What is the largest kind of whale?', '1. Orca whale', '2. Humpback whale', '3. Beluga whale ', '4. Blue whale ', '4'))
    questionList.append(questionClass('Which dinosaur could fly?', '1. Triceratops', '2. Tyrannosaurus Rex', '3. Pteranodon', '4. Diplodocus ', '3'))
    questionList.append(questionClass('Which of these Winnie the Pooh characters is a donkey? ', '1. Pooh', '2. Eeyore', '3. Piglet', '4. Kanga', '2'))
    questionList.append(questionClass('Which dinosaur had the largest brain compared to body size?', '1. Troodon', '2. Stegosaurus', '3. Ichthyosaurus', '4. Gigantoraptor', '1'))
    questionList.append(questionClass('What is the largest type of penguins?', '1. Chinstrap penguins', '2. Macaroni penguins', '3. Emperor penguins', '4. White-flippered penguins', '3'))
    questionList.append(questionClass('Which children''s story character is a monkey?', '1. Winnie the Pooh', '2. Curious George', '3. Horton', '4. Goofy ', '2'))
    questionList.append(questionClass('How long is a year on Mars?', '1. 550 Earth days', '2. 498 Earth days', '3. 126 Earth days', '4. 687 Earth days', '4'))
    questionList.append(questionClass('What is the hottest planet?', '1. Mars', '2. Pluto', '3. Earth', '4. Venus', '4'))
    return questionList