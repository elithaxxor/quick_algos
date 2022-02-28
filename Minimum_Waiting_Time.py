def minimumWaitingTime(queries):
    len_queries=len(queries)
    query_pos= 0
    first_idx = queries[query_pos]
    second_idx = queries[query_pos+1]
    first_res = first_idx+second_idx
    print('first result',first_res)
    print('first,', first_idx)
    print('second,', second_idx)

    answer=[]
    for idx in range(0, len_queries):

        query_plus=queries[idx + 1]

        query_idx = queries[idx]

        #first_result = query_idx + idx
        result=first_res+query_plus
        after_result = result+query_plus

        print('result',result)
        print('after_result',after_result)
        answer.append(after_result)
        if query_plus > len_queries:
            return answer

    return answer
        #result=calculate(query_plus, query_idx, idx)
        #print(result)

    # Write your code here.
    #return 0

def calculate(query_plus, query_idx, idx):
    calc=query_idx+query_plus
    return calc


queries=[3,2,1,2,6]
result = minimumWaitingTime(queries)
print('FINAL_RESULT',result[-1])



## another try:
def minimumWaitingTime(queries):
    queries.sort()
    waiting_time = 0

    for idx, duration in enumerate(queries):
        queriesLeft = len(queries) - (idx + 1)
        waiting_time += duration * queriesLeft
    return waiting_time



