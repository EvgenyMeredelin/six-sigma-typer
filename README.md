## __six-sigma-typer__

This is a single process data-only toy CLI for the [six-sigma](https://github.com/EvgenyMeredelin/six-sigma) app.

***
### __Installation__

```
$ pip install --user https://github.com/EvgenyMeredelin/six-sigma-typer/raw/refs/heads/main/dist/six_sigma_typer-0.1.0-py3-none-any.whl
```

```
$ uv pip install https://github.com/EvgenyMeredelin/six-sigma-typer/raw/refs/heads/main/dist/six_sigma_typer-0.1.0-py3-none-any.whl
```

***
### __Help__

```
$ six-sigma --help

 Usage: six-sigma [OPTIONS]

 Evaluate a single process with the "6 Sigma" approach. Calls https://six-sigma.containerapps.ru/
 under the hood.


╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                            │
│ --show-completion             Show completion for the current shell, to copy it or customize the   │
│                               installation.                                                        │
│ --help                        Show this message and exit.                                          │
╰────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Process parameters ───────────────────────────────────────────────────────────────────────────────╮
│ *  --tests  -t      INTEGER RANGE [x>=1]  Total number of tests [required]                         │
│ *  --fails  -f      INTEGER RANGE [x>=0]  Number of tests qualified as failed [required]           │
│    --name   -n      TEXT                  Name of the process [default: None]                      │
╰────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

***
### __Usage__

```
$ six-sigma -t 1500 -f 233 -n "Yet another process"
{
    'tests': 1500,
    'fails': 233,
    'name': 'Yet another process',
    'defect_rate': 0.15533333333333332,
    'sigma': 2.513824156021599,
    'label': 'YELLOW'
}
```

***
### __Reference__

* Typer: [Building a Package](https://typer.tiangolo.com/tutorial/package/)
* RealPython: [Building and Publishing Packages](https://realpython.com/python-uv/#building-and-publishing-packages)