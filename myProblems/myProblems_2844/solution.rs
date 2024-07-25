use serde_json::{json, Value};

pub struct Solution;

impl Solution {
	pub fn minimum_operations(num: String) -> i32 {
		let mut ans = num.len() as i32;
		if num.contains('0'){ ans -= 1;}
		let ends = vec!["25","50","75","00"];
		ends.iter().for_each(|end|{
			ans = std::cmp::min(ans,Self::help(num.clone(),end.to_string().chars().into_iter().collect::<Vec<char>>()));
		});
		ans
	}
	fn help(num:String,end:Vec<char>) -> i32{
		let n = num.len() as i32;
		if let Some(i) = num.rfind(end[1]){
			return if let Some(j) = num[..i].rfind(end[0]) {
				n - j as i32 - 2
			} else {
				n
			}
		}
		n
	}
}

#[cfg(feature = "solution_2844")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let num: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::minimum_operations(num))
}
