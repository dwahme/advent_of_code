
#[derive(Debug, Clone)]
struct Gamma {
    counts: Vec::<i32>
}

fn bin_to_int(vec: &Vec::<i32>) -> i32 {
    let mut clone = vec.clone();
    clone.reverse();
    
    let mut sum = 0;
    for (i, bit) in clone.into_iter().enumerate() {
        let power = i32::pow(2, i as u32);
        sum += bit * power;
    }

    sum
}


fn count_gamma(strs: Vec<String>) {
    let mut count = vec![(0, 0); strs[0].len()];

    for s in strs {
        for c in s.chars().enumerate() {
            match c {
                (i, '0') => count[i].0 += 1,
                (i, '1') => count[i].1 += 1,
                _ => panic!("Bad character count: {:?}", s)
            }
        }
    }

    let gamma = count.clone().into_iter().map(|(zero, one)| { if zero > one { 0 } else { 1 }}).collect();
    let epsilon = count.clone().into_iter().map(|(zero, one)| { if zero < one { 0 } else { 1 }}).collect();

    let gamma_num = bin_to_int(&gamma);
    let epsilon_num = bin_to_int(&epsilon);

    println!("{:?}\n{:?}\n{:?} * {:?} = {:?}", gamma, epsilon, gamma_num, epsilon_num, gamma_num * epsilon_num);
}

fn find_bit_counts(strs: Vec<String>, pos: usize) -> (i32, i32) {
    let mut counts: (i32, i32) = (0, 0);

    for s in strs {
        match s.as_bytes()[pos] as char {
            '0' => counts.0 += 1,
            '1' => counts.1 += 1,
            _ => panic!("Bad character count: {:?}", s)
        }
    }

    counts
}

fn expected_value(common: bool, zeroes: i32, ones: i32) -> char {
    if common {
        if ones >= zeroes {
            return '1'
        }
        else {
            return '0'
        }
    }
    else {
        if zeroes <= ones {
            return '0'
        }
        else {
            return '1'
        }
    }
}

fn find_diagnostic(strs: Vec<String>, common: bool) -> Vec::<i32> {
    let mut eligible_nums: Vec<String> = strs.clone();

    for i in 0..eligible_nums.len() {
        let (zeros, ones) = find_bit_counts(eligible_nums.clone(), i);

        eligible_nums = eligible_nums.into_iter().filter(
            |s| (s.as_bytes()[i] as char) == expected_value(common, zeros, ones)
        ).collect();

        println!("eligible: {:?}", eligible_nums);

        if eligible_nums.len() == 1 {
            break;
        }
    }

    assert!(eligible_nums.len() == 1);
    eligible_nums[0].chars().map(|c| c.to_digit(10).unwrap() as i32).collect()
}


pub fn day3a() {
    let path = "inputs/day3.txt";
    let nums = utils::get_input_lines::<&str>(path);

    count_gamma(nums)
}


pub fn day3b() {
    let path = "inputs/day3.txt";
    let nums0 = utils::get_input_lines::<&str>(path);
    let nums1 = utils::get_input_lines::<&str>(path);

    let o2 = find_diagnostic(nums0.clone(), true);
    let co2 = find_diagnostic(nums1.clone(), false);

    let o2_num = bin_to_int(&o2);
    let co2_num = bin_to_int(&co2);

    println!("{:?}\n{:?}\n{:?} * {:?} = {:?}", o2, co2, o2_num, co2_num, o2_num * co2_num);
}