from chop.hmm import Tokenizer as HMMTokenizer
import operator

# with open ("sample_book.txt") as file:
#     text = file.read()
text = "朋友圈里和社交媒体上，也充满了对医护人员的赞誉。平时的医护人员，就像空气一样被人忽略；疫情乍起，大家才意识到，医护人员也像空气一样不可或缺，在默默地为救人性命忙碌。掌声和鲜花当然重要。有了掌声和鲜花，社会才能进一步凝聚尊重医护人员的共识，也更好地意识到医护人员的贡献。如今在媒体和公众舆论场上，医护人员的形象已经基本定型，连曾经嚣张的医闹都变成了人人喊打。但掌声和鲜花绝不是全部。医护人员也是普通人，面临新型病毒和我们一样的脆弱。带着使命感和责任感奔赴前线的医护人员，有必要获得更坚实的保障。首先，“不计报酬”这话医生可以说，但医院不能说、卫生行政管理机构更不能说。医护人员面临的是未知的凶险，是信念和责任感支撑他们一路向前。为了大家的健康，医护人员做出了巨大贡献，也付出了巨大牺牲，医疗系统应当考虑给与相应的补偿。其次，“无论生死”是医生愿意牺牲的表现，但那不意味着医生应当牺牲。医生也有家，也有权利好好活着，我们也希望他们好好活着。武汉是此次疫情爆发地，希望当地政府能给力点，给去的医护人员、研究人员提供足够的防护，让他们在与未知的敌人作战时不用担太多的风险。最后，各地机构能做的事情还有很多。抗击疫情是个团队作业，医护人员解决的是医学问题，各地机构要解决的是社会学的问题，如何更好地控制人员流动、进行公共卫生知识普及、如何规范消毒，以防止疫情进一步扩散。医护人员集中在武汉攻关，已经很难了，希望能控制住疫情，别让医护人员再去别地攻关。明天就是除夕，但疫情凶险，这个年过得非比寻常。遥祝各地的医护人员一切安好，也希望患病的人们早日恢复健康。"

frequency_list = {}
high_frequency_list = {}
stop_words = ['.', '"', "'", "`", "，", ",", "。", ":", ";", "?", "!", "(", ")", "*", "/", "@", "-", "_000_", "「", "」", "、"]

def main(txt):
    HT = HMMTokenizer()
    tokenized = list(HT.cut(txt))

    for word in tokenized:
        if word in stop_words:
            pass
        elif word not in frequency_list:
            frequency_list[word] = 1
        elif word in frequency_list:
            frequency_list[word] += 1
    
    for key in frequency_list:
        if frequency_list[key] > 3:
            high_frequency_list[key] = frequency_list[key]

    list_of_tuples = sorted(high_frequency_list.items() , reverse=True, key=lambda x: x[1])
 
    print(list_of_tuples)
    print(len(list_of_tuples))

main(text)