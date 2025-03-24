# xkcdAnimator
A small python module for generation of animated XKCD plots with matplotlib

## Dependencies
- matplotlib
- PIL
- imageio

(you might ave to install fonts **xkcd**, **xkcd Script**, **Comic Neue** and **Comic Sans MS** for full styling but it will still work without them)

## Usage

Use it as a stand alone module.

```python
import xkcdanimator

def drawFunction(p):
    ...

xkcdanimator.animate(drawFunction, [p])
```

*Execute xkcdanimator as main for an example*