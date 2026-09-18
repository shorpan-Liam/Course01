# Validation

Command executed:

```text
python results/validate.py
```

Recorded output (`results/validation-output.txt`):

```text
top_level_object: PASS
full_name: PASS
public: PASS
default_branch_string: PASS
stargazers_count_present_nonnegative: PASS
forks_count_present_nonnegative: PASS
open_issues_count_present_nonnegative: PASS
API facts (saved student response):
  full_name='org2AI/ORG2' (str)
  private=False (bool)
  default_branch='develop' (str)
  stargazers_count=2646 (int)
  forks_count=125 (int)
  open_issues_count=85 (int)
  language='TypeScript' (str)
```

The script parses only the saved student JSON, checks object type, repository identity/public flag, and that each counter is present as a real integer and non-negative (not merely truthy). Printed fields are API facts from that response; teacher baseline observations and inferences are discussed separately in `analysis.md`. The rate-limit error was also preserved, but is not used as the success response.
