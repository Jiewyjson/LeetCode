const PROBLEM_FOLDER: &str = "myProblems";
const PROBLEM_ID: &str = "2740";

#[cfg(test)]
mod test {
	use solution_2740 as solution;
    use test_executor::run_test::run_test;

    use crate::{PROBLEM_FOLDER, PROBLEM_ID};

    #[test]
    fn test_solution() {
        println!("Run [Problem {}] Test Cases", PROBLEM_ID);
        run_test(PROBLEM_ID, PROBLEM_FOLDER, solution::solve);
    }
}
