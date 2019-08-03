def main():
    scores = {'骆昊':95, '白元芳':78, "狄仁杰":82}
    print(scores['骆昊'])
    print(scores['狄仁杰'])
    # 遍历
    for elem in scores:
        # print('%s\t--->\t%d' % (elem, scores[elem]))
        print(f"{elem}\t--->\t{scores[elem]}")
    # 更新
    scores['白元芳'] = 65
    scores['诸葛王朗'] = 71
    # scores['武则天'] = 82
    scores.update(冷面=67, 方启鹤=85)
    print(scores)
    if '武则天' in scores:
        print(scores['武则天'])
    print(scores.get('武则天'))
    print(scores.get('武则天', 60))
    # 删除
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('骆昊', 100))
    print(scores)
    # 清空
    scores.clear()
    print(scores)


if __name__ == "__main__":
    main()