# 请求记录

- URL: `https://api.github.com/repos/org2AI/ORG2`
- 请求时间: 2026-09-18（本地执行；响应头由同一请求保存于 `data/response-headers.txt`）
- 请求命令（无认证头）：`curl.exe -sS -D data/response-headers.txt -H "Accept: application/vnd.github+json" -H "User-Agent: learn2ai-student-analysis" -o data/raw-response.json -w "HTTP_STATUS=%{http_code}\nCONTENT_TYPE=%{content_type}\n" https://api.github.com/repos/org2AI/ORG2`
- 实际响应: HTTP `200 OK`，`Content-Type: application/json; charset=utf-8`
- 原始响应大小: 6023 bytes；SHA-256: `DEB716CA2172978ADB297EC1A010EDA60D5A25CC7C06C0ED7C45DA400A141F5C`
- `data/raw-response.json` 是本次请求的原始 JSON（未提交认证凭据）。请求元数据与完整响应头另存于 `data/`。

## 失败尝试

先用 PowerShell `Invoke-WebRequest` 发送同一 URL，收到真实 HTTP `403`，PowerShell 抛出“远程服务器返回错误: (403) 已禁止”。该失败没有被写成成功响应；随后用上述 `curl` 请求重新取得并保存实际 `200` 响应。
