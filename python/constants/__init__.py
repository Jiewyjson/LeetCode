from .constant import *
from .daily_query import DAILY_QUERY
from .question_query import (QUESTION_INFO_QUERY, QUESTION_DESC_QUERY, QUESTION_DESC_CN_QUERY, QUESTION_CODE_QUERY,
                             QUESTION_TESTCASE_QUERY, QUESTION_KEYWORDS_QUERY)
from .plan_query import PLAN_QUERY, PLAN_PROGRESS_QUERY
from .submit_query import (RECENT_SUBMISSIONS_QUERY, RECENT_AC_SUBMISSIONS_QUERY, USER_PROFILE_QUESTIONS_QUERY,
                           PROGRESS_SUBMISSIONS_QUERY, MY_SUBMISSION_DETAIL_QUERY)
from .user_query import USER_PROFILE_PUBLIC_QUERY
from .code_templates import (TESTCASE_TEMPLATE_PYTHON, TESTCASE_TEMPLATE_PYTHON_TESTCASES,
                             SOLUTION_TEMPLATE_PYTHON, SOLUTION_TEMPLATE_GOLANG,
                             SOLUTION_TEMPLATE_GOLANG_MODIFY_IN_PLACE, TESTCASE_TEMPLATE_GOLANG,
                             SOLUTION_TEMPLATE_JAVA, SOLUTION_TEMPLATE_CPP, SOLUTION_TEMPLATE_TYPESCRIPT,
                             TESTCASE_TEMPLATE_CPP, SOLUTION_TEMPLATE_RUST, SOLUTIONS_TEMPLATE_RUST,
                            CARGO_TOML_TEMPLATE_SOLUTION)
from .display import (SUBMIT_BASIC_RESULT, SUBMIT_SUCCESS_RESULT, SUBMIT_FAIL_RESULT)
