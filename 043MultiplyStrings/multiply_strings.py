# TRICK -> In result DETERMINE the Postion as outer_loop-iter_number + inner_loop_iter_number
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
"""
Given two non-negative integers num1
and num2 represented as strings, return the product of num1 and num2.

Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.

You must not use any built-in BigInteger library or convert the inputs to integer directly.

"""

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


if __name__ == "__main__":
    print("Trying out github codedev first time")
    logger.debug("Trying out github codedev first time")

    num1 = "216"
    num2 = "335"

    # Both Equal
    result_array = [ 0 for x in range(0, (len(num1) + len(num2)))]
    print(result_array)
    print("".join(reversed(num1)))
    print("".join(reversed(num2)))
    rev_num1 = "".join(reversed(num1))
    rev_num2 = "".join(reversed(num2))
    for pos1,val1  in enumerate(rev_num1):
        operand1 = int(rev_num1[pos1])
        for pos2, val2 in enumerate(rev_num2):
            res_array_marker = pos1 + pos2
            operand2 = int(rev_num2[pos2])
            print(f"operand 1 --> {operand1} , operand 2 -> {operand2} \n")
            print(" ======================================****==============\n")
            run_res = (operand1 * operand2 ) + result_array[res_array_marker]
            print(f"\nrunning result -> {run_res}")
            pos_res = int(run_res % 10)
            pos_cover = int(run_res / 10)
            result_array[res_array_marker] = pos_res
            result_array[res_array_marker + 1] += pos_cover
            print(f"result array now -> {result_array} \n ")
            print("============= one iteration complete ===================== \n")
    print(f" final result -> {[str(x) for x in reversed(result_array)]}")
