import pytest

from edits import edit_distance_bwd, edit_distance_fwd
from seamcarve import SeamCarve

def test_edits():
    # I think I have a good set of tests because I've considered a diverse
    # number of edge cases such as case insensitivity, one char change,
    # identical phrases, special chars, as well as running through
    # the 3 different choices for apple vs opal. I also have a few
    # more test examples (long, backwards, special chars, etc) to
    # ensure that my code is robust and works for all cases and for
    # both edit_distance_fwd and edit_distance_bwd.

    # Based on my original tests (before editing edits.py), it appeared
    # that my code was working for edit_distance_fwd (except case insensitivity) 
    # but not for edit_distance_bwd. I was able to fix my code by changing the
    # some of the indices which were off. In addition, the specific case
    # of case insensitivity was not working for both.
    
    # empty words test
    assert edit_distance_fwd("", "") == 0 
    # identical single word test
    assert edit_distance_fwd("test", "test") == 0
    # identical phrase test
    assert edit_distance_fwd("hello world", "hello world") == 0
    # one char change test
    assert edit_distance_fwd("ode", "ods") == 1
    # case insensitivity
    assert edit_distance_fwd("OPAL", "opal") == 0
    assert edit_distance_fwd("saturday", "sunday") == 3
    assert edit_distance_fwd("saturday", "Sunday") == 3
    # running through the 3 different choices for apple vs opal
    assert edit_distance_fwd("apple", "opal") == 3
    assert edit_distance_fwd("opple", "opal") == 2
    assert edit_distance_fwd("opale", "opal") == 1
    assert edit_distance_fwd("opal", "opal") == 0
    assert edit_distance_fwd("apple", "opal") == 3
    assert edit_distance_fwd("aople", "opal") == 3
    assert edit_distance_fwd("aopae", "opal") == 2
    assert edit_distance_fwd("aopal", "opal") == 1
    assert edit_distance_fwd("opal", "opal") == 0
    assert edit_distance_fwd("apple", "opal") == 3
    assert edit_distance_fwd("apple", "oppl") == 2
    assert edit_distance_fwd("apple", "opple") == 1
    assert edit_distance_fwd("apple", "apple") == 0
    # more test examples (long, backwards, special chars, etc)
    assert edit_distance_fwd("kitten", "sitting") == 3
    assert edit_distance_fwd("rosettacode", "raisethysword") == 8
    assert edit_distance_fwd("abcdefgh", "defghabc") == 6
    assert edit_distance_fwd("fleeting", "sleep") == 5
    assert edit_distance_fwd("sleep", "fleeting") == 5
    assert edit_distance_fwd("", "four") == 4
    assert edit_distance_fwd("12345", "54321") == 4
    assert edit_distance_fwd("%@# ", " _!#4") == 4
    assert edit_distance_fwd("apple", "banana") == 5


    # empty words test
    assert edit_distance_bwd("", "") == 0 
    # identical single word test
    assert edit_distance_bwd("test", "test") == 0
    # identical phrase test
    assert edit_distance_bwd("hello world", "hello world") == 0
    # one char change test
    assert edit_distance_bwd("ode", "ods") == 1
    # case insensitivity
    assert edit_distance_bwd("OPAL", "opal") == 0
    assert edit_distance_bwd("saturday", "sunday") == 3
    assert edit_distance_bwd("saturday", "Sunday") == 3
    # running through the 3 different choices for apple vs opal
    assert edit_distance_bwd("apple", "opal") == 3
    assert edit_distance_bwd("opple", "opal") == 2
    assert edit_distance_bwd("opale", "opal") == 1
    assert edit_distance_bwd("opal", "opal") == 0
    assert edit_distance_bwd("apple", "opal") == 3
    assert edit_distance_bwd("aople", "opal") == 3
    assert edit_distance_bwd("aopae", "opal") == 2
    assert edit_distance_bwd("aopal", "opal") == 1
    assert edit_distance_bwd("opal", "opal") == 0
    assert edit_distance_bwd("apple", "opal") == 3
    assert edit_distance_bwd("apple", "oppl") == 2
    assert edit_distance_bwd("apple", "opple") == 1
    assert edit_distance_bwd("apple", "apple") == 0
    # more test examples (long, backwards, special chars, etc)
    assert edit_distance_bwd("kitten", "sitting") == 3
    assert edit_distance_bwd("rosettacode", "raisethysword") == 8
    assert edit_distance_bwd("abcdefgh", "defghabc") == 6
    assert edit_distance_bwd("fleeting", "sleep") == 5
    assert edit_distance_bwd("sleep", "fleeting") == 5
    assert edit_distance_bwd("", "four") == 4
    assert edit_distance_bwd("12345", "54321") == 4
    assert edit_distance_bwd("%@# ", " _!#4") == 4
    assert edit_distance_bwd("apple", "banana") == 5

def test_argmin():
    test_image = [[[255, 255, 255], [0, 0, 0], [125, 125, 125], [0, 0, 0],\
        [255, 255, 255]], [[0, 0, 0], [125, 125, 125], [0, 0, 0],
        [255, 255, 255], [0, 0, 0]], [[255, 255, 255], [125, 125, 125],
        [255, 255, 255], [0, 0, 0], [255, 255, 255]], [[0, 0, 0],
        [255, 255, 255], [125, 125, 125], [255, 255, 255], [0, 0, 0]], 
        [[255, 255, 255], [0, 0, 0], [255, 255, 255], [125, 125, 125],
        [255, 255, 255]]]
    my_sc = SeamCarve(image_matrix = test_image)
    # empty input list
    assert my_sc.argmin([]) == None
    # input list of size 1
    assert my_sc.argmin([5]) == 0
    # input list of size 2, where the first element is smaller
    assert my_sc.argmin([2, 5]) == 0
    # input list of size 2, where the second element is smaller
    assert my_sc.argmin([5, 2]) == 1
    # input list of size 3, where the first element is the smallest
    assert my_sc.argmin([1, 3, 5]) == 0
    # input list of size 3, where the second element is the smallest
    assert my_sc.argmin([5, 1, 9]) == 1
    # input list of size 3, where the third element is the smallest
    assert my_sc.argmin([7, 12, 2]) == 2
    # duplicate minimum values
    assert my_sc.argmin([1, 2, 5, 2]) == 1
    # all elements are equal
    assert my_sc.argmin([5, 5, 5, 5, 5, 5, 5, 5]) == 0
    # both positive and negative values
    assert my_sc.argmin([10, -5, 20, -10, 15]) == 3
    # all negative values
    assert my_sc.argmin([-2, -5, -10, -1, -8]) == 2


def test_seamcarve():
    # TODO: add more assertions and/or test functions to test seamcarve
    # cell E1 from 5x5 spreadsheet
    test_image = [[[255, 255, 255], [0, 0, 0], [125, 125, 125], [0, 0, 0],\
        [255, 255, 255]], [[0, 0, 0], [125, 125, 125], [0, 0, 0],
        [255, 255, 255], [0, 0, 0]], [[255, 255, 255], [125, 125, 125],
        [255, 255, 255], [0, 0, 0], [255, 255, 255]], [[0, 0, 0],
        [255, 255, 255], [125, 125, 125], [255, 255, 255], [0, 0, 0]], 
        [[255, 255, 255], [0, 0, 0], [255, 255, 255], [125, 125, 125],
        [255, 255, 255]]]

    expected_seam = [2, 1, 1, 2, 3]
    # from seamcarve computation spreadsheet
    expected_importance_vals = [[765.00, 505.00, 375.00, 635.00, 765.00],
                                [635.00, 281.25, 570.00, 765.00, 765.00],
                                [640.00, 292.50, 577.50, 765.00, 765.00],
                                [765.00, 577.50, 390.00, 577.50, 765.00],
                                [765.00, 765.00, 515.00, 390.00, 577.50]]

    my_sc = SeamCarve(image_matrix = test_image)

    importance_vals = my_sc.calculate_importance_values()
    assert importance_vals == expected_importance_vals
    calculated_seam = my_sc.find_least_important_seam(importance_vals)
    assert expected_seam == calculated_seam

# The reasoning behind this test case is to manually carve out the rest of the given
# test_image by manually computing importance values with help of seamcave computations spreadsheet
def test_seam_carved_out():
    test_image_carved1 = [[[255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255]], 
                        [[0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 0]], 
                        [[255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 255, 255]], 
                        [[0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0]], 
                        [[255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255]]]
    expected_seam1 = [1, 1, 1, 2, 2]
    my_sc1 = SeamCarve(image_matrix = test_image_carved1)
    importance_vals1 = my_sc1.calculate_importance_values()
    calculated_seam1 = my_sc1.find_least_important_seam(importance_vals1)
    assert expected_seam1 == calculated_seam1

    test_image_carved2 = [[[255, 255, 255], [0, 0, 0], [255, 255, 255]], 
                        [[0, 0, 0], [255, 255, 255], [0, 0, 0]], 
                        [[255, 255, 255], [0, 0, 0], [255, 255, 255]], 
                        [[0, 0, 0], [255, 255, 255], [0, 0, 0]], 
                        [[255, 255, 255], [0, 0, 0], [255, 255, 255]]]
    expected_seam2 = [0, 0, 0, 0, 0]
    my_sc2 = SeamCarve(image_matrix = test_image_carved2)
    importance_vals2 = my_sc2.calculate_importance_values()
    calculated_seam2 = my_sc2.find_least_important_seam(importance_vals2)
    assert expected_seam2 == calculated_seam2

    test_image_carved3 = [[[0, 0, 0], [255, 255, 255]],
                        [[255, 255, 255], [0, 0, 0]],
                        [[0, 0, 0], [255, 255, 255]],
                        [[255, 255, 255], [0, 0, 0]],
                        [[0, 0, 0], [255, 255, 255]]]
    expected_seam3 = [0, 0, 0, 0, 0]
    my_sc3 = SeamCarve(image_matrix = test_image_carved3)
    importance_vals3 = my_sc3.calculate_importance_values()
    calculated_seam3 = my_sc3.find_least_important_seam(importance_vals3)
    assert expected_seam3 == calculated_seam3
