Install `uv` by running:
```
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

then, run:
```
$ uv sync
```

Now, you should have a fresh `.venv` directory. You can debug with `debugpy` as long as you link the proper interpreter, or you could directly call:
```
$ uv run main.py
```