def bubblesort(lst : list[int]):
    state = []
    for i in range(len(lst)-1, 0, -1):
        for j in range(0, i):
            state.append(lst.copy())
            if lst[j+1] < lst[j]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return state

if __name__ == "__main__":
    lst = [5, 6, 2, 1, -5, 0, 0, 458, 4, -25, 58]
    all_states = bubblesort(lst)
    for i in range(len(all_states)):
        print(all_states[i])