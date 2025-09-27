def solution(genres, plays):
    ranking = dict()
    ranking2 = dict()
    
    for i in range(len(genres)):
        if genres[i] in ranking:
            ranking[genres[i]] += plays[i]
            ranking2[genres[i]].append(i)
            ranking2[genres[i]] = sorted(ranking2[genres[i]], reverse=True, key=lambda idx: plays[idx])
        else:
            ranking[genres[i]] = plays[i]
            ranking2[genres[i]] = [i]

    ranking = sorted(ranking.items(), reverse=True, key=lambda item: item[1])

    answer = []
    for value in ranking:
        answer.extend(ranking2[value[0]][:2])
        
    return answer
