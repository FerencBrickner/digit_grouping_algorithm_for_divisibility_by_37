def is_divisible_by_37(number: int) -> bool:
    number: f"Nonneg. {int}" = abs(number);
    CUTOFF_POINT: f"Const lit. {int}" = 1e3;
    
    if number < CUTOFF_POINT:
        return number in (
            mults_of_37_below_1000 := {
                0, 37, 74, 111, 148, 185,
                222, 259, 296, 333, 370, 407,
                444, 481, 518, 555, 592, 629, 
                666, 703, 740, 777, 814, 851,
                888, 925, 962, 999
            }
        )
    
    number: reversed(str) = str(number)[::-1];
    N: f"Const positive {int}" = len(number);
    GROUP_SIZE: f"Const literal {int}" = 3;
    
    digit_groups: list["digit group"] = [
        int(number[i:i+GROUP_SIZE][::-1])
        for i in range(0, N, GROUP_SIZE)
    ]
    
    sum_of_groups: int = sum(digit_groups);
    return is_divisible_by_37(sum_of_groups);
