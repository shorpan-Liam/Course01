# Request record

URL: `https://api.github.com/repos/org2AI/ORG2`

The request was made twice with a normal User-Agent (`learn2ai-student-02-coursework`) and `Accept: application/vnd.github+json`; no token or credential was supplied.

- Attempt 1, `2026-09-16T19:58:04.6390243Z`: HTTP `403`, rate limit exceeded. The exact JSON error is retained at `data/rate-limit-error.json`.
- Attempt 2, `2026-09-16T19:59:26Z` (HTTP Date header): HTTP `200`, `Content-Type: application/json; charset=utf-8`, 6023 bytes. The complete response is `data/raw-response.json` (SHA-256 `0a6c9ad1a65b66967a7c870558729abca2acad98c9a997ece3d42afb61e7722e`). Local capture time is in `data/request-metadata.txt`.

Reproducible command (PowerShell/curl):

```powershell
curl.exe -sS -D response-headers.txt -A "learn2ai-student-02-coursework" `
  -H "Accept: application/vnd.github+json" `
  -o data/raw-response.json `
  "https://api.github.com/repos/org2AI/ORG2"
```

The first failure was not treated as a successful response. The second response is the student analysis input.
