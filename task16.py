def GenerateBBSTArray(a):
    sorted_a = sorted(a)
    root_ind = len(a) // 2
    root = sorted_a[root_ind]
    bst_array = []
    bst_array.append(root)

    def append_to_tree(ind, array):
        left_part = array[:ind]
        if len(left_part) > 0:
            left_centre = len(left_part) // 2
            bst_array.append(left_part[left_centre])
        right_part = array[ind + 1:]
        if len(right_part) > 0:
            right_centre = len(right_part) // 2
            bst_array.append(right_part[right_centre])
        if len(left_part) > 0:
            append_to_tree(left_centre, left_part)
        if len(right_part) > 0:
            append_to_tree(right_centre, right_part)

    append_to_tree(root_ind, sorted_a)
    return bst_array
