# 验证记录

执行命令：

```powershell
$j = Get-Content -Raw -Encoding UTF8 data/raw-response.json | ConvertFrom-Json
[pscustomobject]@{ type=$j.GetType().FullName; name=$j.name; full_name=$j.full_name; private=$j.private; stargazers_count=$j.stargazers_count; forks_count=$j.forks_count; open_issues_count=$j.open_issues_count; default_branch=$j.default_branch }
```

实际输出：JSON 解析为 `PSCustomObject`；`name=ORG2`，`full_name=org2AI/ORG2`，`private=False`，`stargazers_count=2644`，`forks_count=126`，`open_issues_count=86`，`default_branch=develop`。

验证结论：响应是 JSON，所用字段存在且为数值（计数字段）或布尔/字符串类型；原始文件大小 6023 bytes，低于 1 MiB。教师基线 CSV/JSON 为 2647、126、85（2026-09-16），本次请求为 2644、126、86；时间变化可以解释数值变化，不能据此判定请求错误。

未执行项：没有额外 GitHub 认证请求或历史版本 API 请求，标记为 `NOT_RUN`；因此不推断更广泛的项目趋势。
