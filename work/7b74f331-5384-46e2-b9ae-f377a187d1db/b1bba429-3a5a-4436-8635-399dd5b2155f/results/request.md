# Request record

URL: `https://api.github.com/repos/org2AI/ORG2`

The endpoint was requested twice as two independent unauthenticated attempts with a normal User-Agent (`learn2ai-student-02-coursework`) and `Accept: application/vnd.github+json`; no token or credential was supplied. Do not combine their statuses or timestamps.

- Attempt 1, `2026-09-16T19:58:04.6390243Z`: HTTP `403`, rate limit exceeded. Its error body is only evidence for this attempt and is retained at `data/rate-limit-error.json`; metadata is in `request-meta.txt`.
- Attempt 2, HTTP `Date: 2026-09-16T19:59:26Z` (local capture `2026-09-16T20:00:43.7442222Z`): HTTP `200`, `Content-Type: application/json; charset=utf-8`, 6023 bytes. The complete response is `data/raw-response.json` (SHA-256 `0a6c9ad1a65b66967a7c870558729abca2acad98c9a997ece3d42afb61e7722e`); headers and metadata are in `data/response-headers.txt` and `data/request-metadata.txt`.

Reproducible command (PowerShell/curl):

```powershell
curl.exe -sS -D response-headers.txt -A "learn2ai-student-02-coursework" `
  -H "Accept: application/vnd.github+json" `
  -o data/raw-response.json `
  "https://api.github.com/repos/org2AI/ORG2"
```

The first failure was not treated as a successful response. The second response is the student analysis input. Because both attempts were unauthenticated, rate-limit state, time, and network egress are reproduction prerequisites: a later or different-network run may legitimately return 403 or 200 and may observe different counters. Reproduction must preserve each attempt separately and must not overwrite the 403 with a later success.
