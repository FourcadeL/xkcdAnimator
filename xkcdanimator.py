import io
import random
import time
from PIL import Image
import imageio
import matplotlib.pyplot as plt



random.seed(time.time())


def animate(drawFun, drawArgs, saveFile="out.gif", nFrames=4,
            sScale=1, lScale=200, rScale=2,
            sBase=2, lBase=700, rBase=11,
            fps=5):
    """Plot animation function

    Animate a matplotlib drawing to a looping GIF using xkcd style
    Draws the sae function multiple times as xkcd variants

    Usage
    -----
    Pass a drawing function using matplotlib and its argument.
    For example :
    def drawPow(p):
        plt.plot([x**p for x in range(10)])

    and animate(drawPow, [2])
    will plot the x² graph as xkcd animation

    Parameters
    ----------
    drawFun : callable
        the drawing function, should only use pure matplotlib calls
    drawArgs : list[Any]
        the arguments as a list that should be passed to drawFun
    saveFile : str 
        the path for the generated gif
    nFrames : int, optional
        the number of frames to generate
    sScale : int, optional
        the variation parameter for xkcd scale
    lScale : int, optional
        the variation parameter for xkcd length
    rScale : int, optional
        the variation parameter for xkcd randomness
    sBase : int, optional
        the base parameter for xkcd scale
    lBase : int, optional
        the base parameter for xkcd length
    rBase : int, optional
        the base parameter for xkcd randomness
    fps : int, optional
        the number of frames per seconds for the GIF
    """

    with imageio.get_writer(saveFile, mode='I', format="gif", loop=0, fps=fps, subrectangles=True) as writer:
        for _ in range(nFrames):
            scale = sBase + sScale*random.uniform(-1, 1)
            length = lBase + lScale*random.uniform(-1, 1)
            rand = rBase + rScale*random.uniform(-1, 1)
            with plt.xkcd(scale=scale, length=length, randomness=rand): # temporary overwrite
                drawFun(*drawArgs)
                plt.tight_layout()
                buffer = io.BytesIO()
                plt.savefig(buffer, format='png')
                buffer.seek(0)
                writer.append_data(Image.open(buffer))
                buffer.close()
                plt.clf()
    return

def drawPow(p):
    plt.plot([x**p for x in range(10)])

def main():
    print("xkcdAnimator testing")
    animate(drawPow, [2])
    return

if __name__ =="__main__":
    main()