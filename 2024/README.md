# Advent of Code 2024

Each day has a language-suffixed directory: `dayXX-go`, `dayXX-py`, `dayXX-js`.

Use the scaffold scripts from the repo root to create a new day:

```
./goday <day>   # creates 2024/dayXX-go/
./pyday <day>   # creates 2024/dayXX-py/
./jsday <day>   # creates 2024/dayXX-js/
```

All three download `input.txt` automatically (requires `$COOKIE`).

---

## Go (`dayXX-go/`)

### Run

```
cd dayXX-go
go run .
```

### Test

```
cd dayXX-go
go test .
```

Force a fresh run (bypass cache):

```
go test -count=1 .
```

Run all Go days from the 2024 root:

```
go test ./...
```

### Measure time

```
cd dayXX-go
time go run .
```

Or benchmark via the test binary:

```
go test -bench=. -benchtime=5s ./...
```

### Debug

Print values inline with `fmt.Println` or `fmt.Printf`.

Step through with `dlv` (Delve):

```
cd dayXX-go
dlv debug .
```

Common Delve commands inside the debugger:

| Command | Action |
|---|---|
| `break main.main` | set breakpoint at main |
| `break main.go:42` | set breakpoint at line 42 |
| `continue` | run until next breakpoint |
| `next` | step over |
| `step` | step into |
| `print <var>` | inspect a variable |
| `quit` | exit |

Debug a specific test:

```
dlv test -- -run TestPart1Sample
```

---

## Python (`dayXX-py/`)

### Run

```
cd dayXX-py
python day.py
```

Pass the sample file to test against the example:

```
python day.py sample.txt
```

### Test (pytest)

```
cd dayXX-py
pytest day.py
```

Or from the 2024 root:

```
pytest */day.py
```

### Measure time

```
time python day.py
```

---

## JavaScript (`dayXX-js/`)

### Run

```
cd dayXX-js
node day.js
```

Pass the sample file to test against the example:

```
node day.js sample.txt
```

### Measure time

```
time node day.js
```

---

## Debug in VS Code

Requires the [Go extension](https://marketplace.visualstudio.com/items?itemName=golang.go).

**Debug main:**
1. Open `dayXX/main.go`
2. Set breakpoints by clicking the gutter
3. Press `F5` — VS Code launches the debugger using the current file's package

**Debug a test:**
1. Open `dayXX/main_test.go`
2. Click **"debug test"** above any `TestXxx` function (shown by the Go extension)
3. Or open the Testing panel (`Cmd+Shift+P` → "Go: Test") and click the debug icon next to a test

**launch.json** — add to `.vscode/launch.json` for repeatable configs:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug day01",
      "type": "go",
      "request": "launch",
      "mode": "debug",
      "program": "${workspaceFolder}/day01-go"
    },
    {
      "name": "Debug day01 tests",
      "type": "go",
      "request": "launch",
      "mode": "test",
      "program": "${workspaceFolder}/day01-go",
      "args": ["-run", "TestPart1Sample"]
    }
  ]
}
```

The debugger runs with the package directory as the working directory, so `sample.txt` and `input.txt` are found automatically.

## Lint

`staticcheck` is installed and sufficient for AoC:

```
staticcheck .
```

Or across all days:

```
staticcheck ./...
```

For broader checks install `golangci-lint`:

```
brew install golangci-lint
golangci-lint run ./...
```

## Common patterns

### Read file into lines

Every day starts with this — it's already in the template as `readLines`:

```go
func readLines(path string) ([]string, error) {
    f, err := os.Open(path)
    if err != nil {
        return nil, err
    }
    defer f.Close()

    var lines []string
    s := bufio.NewScanner(f)
    s.Buffer(make([]byte, 0, 1024*1024), 1024*1024)
    for s.Scan() {
        lines = append(lines, s.Text())
    }
    return lines, s.Err()
}
```

### Parse values from each line

**Two integers per line:**

```go
for _, line := range lines {
    var a, b int
    fmt.Sscanf(line, "%d %d", &a, &b)
}
```

**Split on whitespace and convert:**

```go
import "strings"
import "strconv"

for _, line := range lines {
    parts := strings.Fields(line)   // splits on any whitespace
    n, _ := strconv.Atoi(parts[0])  // convert string to int
}
```

**Single character per cell (grid):**

```go
for _, line := range lines {
    for _, ch := range line {
        // ch is a rune, e.g. '.' or '#'
    }
}
```

### Frequency map

Count how many times each value appears:

```go
freq := make(map[int]int)
for _, v := range nums {
    freq[v]++  // missing keys default to 0, so first ++ goes 0→1
}
```

Look up a value (returns 0 if not present, no need to check existence):

```go
count := freq[42]
```

Check if a key exists:

```go
count, ok := freq[42]
if ok {
    // key was present
}
```

String frequency map works the same way — just change the key type:

```go
freq := make(map[string]int)
```
