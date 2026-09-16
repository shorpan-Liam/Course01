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
stargazers_count_int: PASS
forks_count_int: PASS
open_issues_count_int: PASS
fields:
  full_name='org2AI/ORG2' (str)
  private=False (bool)
  default_branch='develop' (str)
  stargazers_count=2646 (int)
  forks_count=125 (int)
  open_issues_count=85 (int)
  language='TypeScript' (str)
```

The script parses the saved JSON, checks object type, repository identity/public flag, expected field types, and prints the fields used in analysis. The rate-limit error was also preserved, but is not used as the success response.
