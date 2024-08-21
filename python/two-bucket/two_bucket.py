def pour(filler, filled, max_filled):
    if filler <= max_filled - filled:
        filled += filler
        filler = 0
    else:
        filler -= (max_filled - filled)
        filled = max_filled
    return filler, filled

def fill(capacity):
    return capacity

def measure(bucket_one, bucket_two, goal, start_bucket):

    if goal > bucket_one and goal > bucket_two:
        raise ValueError("The goal is greater than both buckets.")

    if start_bucket == "one":  # assign which is the start bucket
        first = [bucket_one] * 2  # in lists of [holding/capacity]
        second = [0, bucket_two]  # and giving the not starting one a name
        second_bucket = "two"
    else:
        first = [bucket_two] * 2
        second = [0, bucket_one]
        second_bucket = "one"

    actions = 1

    if second[1] == goal:  # if the second bucket it's the goal just fill it
        second[0] = goal
        actions += 1

    while first[0] != goal != second[0]:
        if actions == 50:
            raise ValueError(
                "You are probably stuck in a loop and I'm too lazy to check it")
        if first[0] == 0:  # fill first bucket if it's empty
            first[0] = first[1]
        elif second[0] == second[1]:  # empty second bucket if it's filled
            second[0] = 0
        else:  # else pour first into second bucket
            first[0], second[0] = pour(first[0], second[0], second[1])
        actions += 1
    # (actions, start bucket if it's the one with the goal else the other, liquid left in the other bucket)
    return actions, start_bucket if first[0] == goal else second_bucket, second[0] if first[0] == goal else first[0]
