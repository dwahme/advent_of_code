
#[derive(Debug, Copy, Clone)]
struct Sub {
    x: i64,
    y: i64,
    aim: i64
}

impl Sub {

    fn down(&mut self, dist: i64) {
        self.aim += dist
    }

    fn up(&mut self, dist: i64) {
        self.aim -= dist
    }

    fn forward(&mut self, dist: i64) {
        self.y += self.aim * dist;
        self.x += dist
    }

    fn parse_direction(instructions: Vec<String>) {
        let mut sub = Sub { x: 0, y: 0, aim: 0 };

        for instr in instructions {
            let split: Vec<&str> = instr.split(" ").collect();

            let dir = split[0];
            let dist = split[1].parse::<i64>().unwrap();

            match dir {
                "up" => sub.up(dist),
                "down" => sub.down(dist),
                "forward" => sub.forward(dist),
                _ => println!("unmatched direction: {:?}", instr)
            }
        }

        println!("{:?} {:?}", sub, sub.x * sub.y)
    }
}

pub fn day2a() {
    let path = "inputs/day2.txt";
    let dirs = utils::get_input_lines::<&str>(path);

    Sub::parse_direction(dirs)
}