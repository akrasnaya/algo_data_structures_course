def GenerateBBSTArray(a):
    sorted_a = sorted(a)
    root_ind = len(a) // 2
    root = sorted_a[root_ind]
    bst_array = [None] * len(a)
    bst_array[0] = root


    def append_to_tree(ind, array, bst_ind):
        left_part = array[:ind]
        if len(left_part) > 0:
            left_centre = len(left_part) // 2
            bst_array[2 * bst_ind + 1] = left_part[left_centre]
        right_part = array[ind + 1:]
        if len(right_part) > 0:
            right_centre = len(right_part) // 2
            bst_array[2 * bst_ind + 2] = right_part[right_centre]
        if len(left_part) > 0:
            append_to_tree(left_centre, left_part, bst_array.index(left_part[left_centre]))
        if len(right_part) > 0:
            append_to_tree(right_centre, right_part, bst_array.index(right_part[right_centre]))

    append_to_tree(root_ind, sorted_a, 0)
    return bst_array
