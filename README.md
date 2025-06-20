## __six-sigma-typer__

This is a single process data-only toy CLI interface for the [six-sigma](https://github.com/EvgenyMeredelin/six-sigma) app.

***
### __Installation__

```
$ uv pip install six_sigma_typer-0.1.0-py3-none-any.whl
```

***
### __Help__

```
$ six-sigma --help

 Usage: six-sigma [OPTIONS]

 Evaluate a single process with the "6 Sigma" approach.


╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                               │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.        │
│ --help                        Show this message and exit.                                                             │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Process parameters ──────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *  --tests  -t      INTEGER RANGE [x>=1]  Total number of tests [required]                                            │
│ *  --fails  -f      INTEGER RANGE [x>=1]  Number of tests qualified as failed [required]                              │
│    --name   -n      TEXT                  Name of the process [default: None]                                         │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

***
### __Usage__

```
$ six-sigma -t 1500 -f 256 -n "My awesome process"
{
    "tests": 1500,
    "fails": 256,
    "name": "My awesome process",
    "defect_rate": 0.17066666666666666,
    "sigma": 2.4515340671620525,
    "label": "YELLOW",
}
```

***
### __Reference__

* Typer: [Building a Package](https://typer.tiangolo.com/tutorial/package/)
* RealPython: [Building and Publishing Packages](https://realpython.com/python-uv/#building-and-publishing-packages)