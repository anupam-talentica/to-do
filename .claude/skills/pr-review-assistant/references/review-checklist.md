# PR Review Checklist

## Security Review

- [ ] No hardcoded credentials, API keys, or secrets in code
- [ ] Passwords properly masked in logs and error messages
- [ ] Auth tokens not stored in plain text or localStorage
- [ ] Permission checks enforced at API boundaries
- [ ] Session management follows secure practices
- [ ] CORS policies properly configured (not overly permissive)
- [ ] SQL queries use parameterized statements (no string concatenation)
- [ ] User input properly validated and sanitized
- [ ] Output encoding applied for web content (prevent XSS)
- [ ] No use of eval(), exec(), or dynamic code execution
- [ ] No unsafe deserialization of untrusted data
- [ ] File uploads have size limits and type validation
- [ ] External dependencies pinned to known-safe versions
- [ ] No execution of arbitrary shell commands with user input

## Performance Review

- [ ] No N+1 query patterns
- [ ] Indexes properly utilized in queries
- [ ] Query results paginated for large datasets
- [ ] No unnecessary data retrieval (select specific columns)
- [ ] Database connections properly pooled
- [ ] No blocking operations on event loops
- [ ] Long-running operations are asynchronous or background tasks
- [ ] Caching implemented for frequently accessed data
- [ ] No repeated calculations in loops
- [ ] Memory leaks avoided (proper cleanup of resources)
- [ ] API responses appropriately paginated or limited
- [ ] Unnecessary API calls eliminated
- [ ] Request/response sizes reasonable
- [ ] Timeouts configured for external calls
- [ ] Retry logic has exponential backoff

## Code Quality

- [ ] Functions have clear, single responsibilities
- [ ] Complex logic documented or broken into smaller functions
- [ ] Variable and function names descriptive
- [ ] Duplicate code eliminated or extracted to shared functions
- [ ] Cyclomatic complexity reasonable (not deeply nested)
- [ ] Errors caught and handled appropriately
- [ ] Error messages descriptive for debugging
- [ ] Unhandled promise rejections prevented
- [ ] Failure modes considered and handled
- [ ] No silent failures (swallowed exceptions)

## Testing

- [ ] Changes include appropriate test coverage
- [ ] Edge cases considered in tests
- [ ] Breaking changes have migration paths
- [ ] Backward compatibility maintained where needed
- [ ] Integration points with other systems tested
- [ ] New functions/classes have docstrings or comments
- [ ] Complex algorithms documented
- [ ] API contracts clearly defined
- [ ] Configuration options documented
- [ ] Known limitations or TODOs tracked
