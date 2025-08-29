def w_sum(vec1, vec2):
    assert(len(vec1) == len(vec2))

    output = 0

    for i in range(len(vec1)):
        output += vec1[i] * vec2[i]

    return output

def elem_mul(scal, vec):
    output = [0,0,0]

    assert(len(output) == len(vec))

    for i in range(len(vec)):
        output[i] = scal * vec[i]

def vec_mat_mult(vec, mat):
    assert(len(vec) == len(mat))

    output = [0,0,0]

    for i in range(len(vec)):
        output[i] = w_sum(vec, mat[i])

    return output

## weights 1 start
# weights = [
#     [0.1, 0.1, -0.3], # output 1
#     [0.1, 0.2, 0.0], # output 2
#     [0.0, 1.3, 0.1], # output 3
# ]
## weights 2 end
# weights = [[0.04781609303265233, 0.09600946593779106, -0.307367139807155], [0.10229379810845485, 0.20017540809064652, 0.00032383032119362546], [-0.09920676819067192, 1.2924136000795365, 0.08599433860837574]]

## weights 2 start
# weights = [
#     [0.5, -0.1, -0.4], # output 1
#     [0.9, 0.6, -0.2], # output 2
#     [1.7, -0.3, 0.0], # output 3
# ]
## weights 2 end
# weights = [[0.0865428909510146, -0.1316173083390401, -0.4583704153951509], [0.12010864312535348, 0.5403612491801739, -0.3101023092058325], [0.07656438874108504, -0.42414507615509345, -0.22919090982478801]]