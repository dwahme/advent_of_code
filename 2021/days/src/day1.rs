use utils;
use itertools::Itertools;

pub fn day1a() {
    let path = "inputs/day1.txt";
    let nums = utils::get_input_lines_int(path);

    let mut count = 0;

    let mut prev: Option<i32> = None;
    for curr in nums {
        match prev {
            Some(i) => {
                if curr > i {
                    count = count + 1;
                }
            },
            None => ()
        };

        prev = Some(curr)
    }

    println!("{:?}", count)
}

pub fn day1b() {
    let path = "inputs/day1.txt";
    let nums = utils::get_input_lines_int(path);

    let mut count = 0;

    let mut prev: Option<i32> = None;
    for (x, y, z) in nums.iter().tuple_windows::<(_, _, _)>() {
        let sum = x + y + z;

        match prev {
            Some(i) => {
                if sum > i {
                    count = count + 1;
                }
            },
            None => ()
        };

        prev = Some(sum)
    }

    println!("{:?}", count)
}