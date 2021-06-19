from spacy.lang.vi import Vietnamese
from spacy.lang.en import English
import spacy

# nlp_vn = Vietnamese()
# nlp_en = English()

nlp = spacy.load("en_core_web_md")
doc = nlp("100 football teams join the World Cup 2022 in Qatar")
# doc = nlp("I have a 10 million VND for buying startup company in Vietnam")

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

# doc_vn = nlp_vn("Tao có 100 nghìn việt nam đồng")

print("Index: ", [token.i for token in doc])
# print("Index_en: ", [token.i for token in doc_en])

print("Text: ", [i for i in doc])
# print("Text_vn: ", [i for i in doc_vn])

# print("is_alpha_vn: ", [token.i for token in doc_vn])
# print("is_alpha_en: ", [token.i for token in doc_en])

# nlp = spacy.load("en_core_web_sm")
#
# doc = nlp("She ate the pizza")
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)
#
# doc = nlp("Apple is looking at buying U.K. startup for 1$ billion")
# for ent in doc.ents:
#     print(ent.text, ent.label_)
#
# print(spacy.explain("GPE"))
# print(spacy.explain("NNP"))
# print(spacy.explain("dobj"))
#


# from spacy.matcher import Matcher
# nlp = spacy.load("en_core_web_sm")
# matcher = Matcher(nlp.vocab)
# pattern1 = [{"LOWER": "how"}, {"LOWER": "many"}, {"LOWER": "football"}, {"LOWER": "player"}, {"LOWER": "join"}, {"IS_PUNCT": True}]
# # pattern2 = [{"LOWER": "Football"}, {"LOWER": "Player"}, {"LOWER": "worldcup"}, {"IS_PUNCT": True}]
# # pattern3 = [{"LOWER": "football"}, {"LOWER": "player"}, {"LOWER": "worldcup"}, {"IS_PUNCT": False}]
# # pattern4 = [{"LOWER": "Football"}, {"LOWER": "Player"}, {"LOWER": "worldcup"}, {"IS_PUNCT": False}]
# # pattern5 = [{"LOWER": "football player"}, {"IS_PUNCT": True}]
# # pattern6 = [{"LOWER": "football player"}, {"IS_PUNCT": False}]
# # pattern7 = [{"LOWER": "football player"}, {"IS_PUNCT": False}]
# # pattern8 = [{"LOWER": "football player"}, {"LOWER": "asia"}, {"IS_PUNCT": True}]
# #
# matcher.add("football player", [pattern1])
# # doc = nlp("Tôi chọn ghi đè vào file có sẵn")
# # doc = nlp("Có bao nhiêu cầu thủ tham gia worldcup ở asia")
# doc = nlp("How many does football player join worldcup 2020 in asia?")
# matches = matcher(doc)
# for match_id, start, end in matches:
#     matched_span = doc[start: end]
#     print(match_id)
#     print(matched_span)
#     print(matched_span.text)



import spacy

# pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]
# pattern0 = [{"LEMMA": "that"}, {"LEMMA": "release"}, {"LEMMA": "iPhone"}]
# pattern0 = [{"LEMMA": "iphone"}, {"LEMMA": "X"}]
# # pattern1 = [{"LOWER": "leaked"}]
# # pattern1 = [{'LOWER':'solarpower'}]
# # pattern2 = [{'LOWER': 'solar'}, {'IS_PUNCT': True}, {'LOWER': 'power'}]
# # pattern3 = [{'LOWER': 'solar'}, {'LOWER': 'power'}]
# # matcher.add('Solar Power', [pattern1, pattern3, pattern2])
# # matcher.add('SolarPower', [pattern])
# matcher.add("iphone X", [pattern0])
# # doc = nlp("The Solar Power industry continues to grow a solar power increases. Solar-PoWer is good")
# # doc = nlp("here is your iPhone X that released iPhone leaked data")
# doc1 = nlp("the iPhone X released was leaked data out ")
# print([token.text for token in doc1])
# found_matches = matcher(doc1)
# print(found_matches)
# for match_id, start, end in found_matches:
#     string_id = nlp.vocab.strings[match_id]
#     span = doc1[start:end]
#     print(match_id, string_id, start, end, span.text)

# import spacy
# nlp = spacy.load('en_core_web_sm')
# from spacy.matcher import Matcher
#
# nlp_vn = Vietnamese()
# nlp_en = English()
# matcher = Matcher(nlp_vn.vocab)
# pattern = [{"IS_DIGIT": True},
#            {"LOWER": "fifa"},
#            {"LOWER": "world"},
#            {"LOWER": "cup"},
#            {"IS_PUNCT": True},
#            {"LOWER": "france"},
#            {"LOWER": "won"}]
# pattern1 = [{"TEXT": "2018"},
#            {"TEXT": "Fifa"}]
# pattern2 = [{"IS_DIGIT": True},
#            {"TEXT": "FIFA"}]
# pattern3 = [{"TEXT": "2018"},
#            {"TEXT": "fifa"}]
# pattern4 = [{"TEXT": "2018"},
#            {"TEXT": "FiFa"}]
# pattern5 = [{"IS_DIGIT": False},
#            {"TEXT": "FIFA"},
#             {"TEXT": "fifa"}]
# pattern6 = [{"TEXT": "Có"},
#             {"TEXT": "bao"},
#             {"TEXT": "nhiêu"},
#             {"TEXT": "đội"},
#             {"TEXT": "bóng"},
#             {"TEXT": "tham"},
#             {"TEXT": "gia"},
#             {"TEXT": "World"},
#             {"TEXT": "cup"},
#             {"TEXT": "2022"}]
#
# matcher.add("Có", [pattern6])
# #doc = nlp("Fifa FIFA fifa Cup: France Won!")
# doc = nlp_vn("Có bao nhiêu cầu thủ tham gia world cup ở asia")
# print(doc)
# matches = matcher(doc)
# print(matches)
# for i, start, end in matches:
#     span = doc[start: end]
#     print(span.text)


# Create an nlp object
# doc = nlp("He went to play basketball")
#
# # Iterate over the tokens
# print("\t >>> Part of Speech (POS) --> Loại từ: Danh từ, tính từ, động từ")
# for token in doc:
#     # Print the token and its part-of-speech tag
#     print(token.text, "-->", token.pos_)
#
# print("\t >>> Dependency (DEP) --> Sự phụ thuộc: \n"
#           " nsubj = động từ bổ nghĩa danh từ \n"
#           " amod = danh từ bổ nghĩa tính từ \n"
#           " compound = danh từ bổ nghĩa danh từ \n"
#           " dobj = động từ bổ nghĩa danh từ (đứng sau)\n"
#           " prep = động từ bổ nghĩa giới từ (đứng sau)\n"
#           " pobj = giới từ bổ nghĩa danh từ (đứng sau)\n")
# for token in doc:
#     print(token.text, "-->", token.pos_)
#
# print(spacy.explain("ADP"))

