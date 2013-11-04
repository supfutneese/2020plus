"""
The plot.py does the actual calling of plot commands from matplotlib.
Essentially, plot.py encapsulates all the minor tweaks needed in matplotlib
to make a reasonable looking plot.
"""

import matplotlib.pyplot as plt
import numpy as np


def heatmap(df, file_path, xlabel='', ylabel='', cmap=plt.cm.Blues):
    """Plot a heatmap from a pandas dataframe.

    Args:
        df (pandas.DataFrame): data for heatmap plotting
        file_path (str): path to save figure (png, pdf, etc.)

    Kwargs:
        xlabel (str): x-axis label
        ylabel (str): y-axis label
        cmap (cm): color scheme for heatmap

    Code from:
    http://stackoverflow.com/questions/14391959/heatmap-in-matplotlib-with-pcolor
    """
    df = df.fillna(0)  # fills missing values with 0's

    # make heatmap
    fig, ax = plt.subplots()
    hmap = ax.pcolor(df, cmap=cmap, alpha=0.8)

    fig = plt.gcf()
    fig.set_size_inches(8,11)

    # turn off the frame
    ax.set_frame_on(False)

    # put the major ticks at the middle of each cell
    ax.set_yticks(np.arange(df.shape[0])+0.5, minor=False)
    ax.set_xticks(np.arange(df.shape[1])+0.5, minor=False)

    # want a more natural, table-like display
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    # Set the labels
    labels = df.index
    ax.set_xticklabels(labels, minor=False)
    ax.set_yticklabels(df.index, minor=False)

    # rotate the
    plt.xticks(rotation=90)

    ax.grid(False)

    # Turn off all the ticks
    ax = plt.gca()

    for t in ax.xaxis.get_major_ticks():
        t.tick1On = False
        t.tick2On = False
    for t in ax.yaxis.get_major_ticks():
        t.tick1On = False
        t.tick2On = False

    # handle labels
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()

    # save figure
    plt.savefig(file_path)


def barplot(df, file_path, title='', xlabel='', ylabel='', stacked=False):
    """barplot generates/saves a bar plot from a pandas data frame.

    Args:
        df (pd.DataFrame): data frame for bar plot
        file_path (str): path to save bar plot figure

    Kwargs:
        Matplotlib options for plotting
    """
    df.plot(kind='bar', stacked=stacked)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(file_path)
    plt.clf()  # clear figure


def histogram(df,
              file_path,
              bins,
              log=False,
              title='',
              xlabel='',
              ylabel=''):
    """Plots a histogram using matplotlib.

    Args:
        df (pd.DataFrame): one dimensional data frame or series
        file_path (str): path to save figure
        bins (list): bin positions for histogram

    Kwargs:
        log (Bool): boolean for log scaling y-axis
        title (str): title of plot
        xlabel (str): label on x-axis
        ylabel (str): label on y-axis
    """
    df.hist(bins=bins, log=log)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(file_path)
    plt.clf()  # clear figure


def line(data,
         file_path,
         title='',
         xlabel='',
         ylabel='',
         logx=False,
         logy=False,
         vlines=[]):
    # plot data
    data.plot(kind='line')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # log scale if neccessary
    if logx:
        plt.xscale('log')
    if logy:
        plt.yscale('log')

    # plot vertical lines
    ymin, ymax = plt.ylim()  # get plotting range of y-axis
    for l in vlines:
        plt.vlines(l, ymin=ymin,
                   ymax=ymax,
                   color='red')

    plt.tight_layout()  # adjust plot margins
    plt.savefig(file_path)  # save figure
    plt.clf()  # clear figure


def scatter(x, y,
            file_path,
            colors='blue',
            size=20,
            title='',
            xlabel='',
            ylabel=''):
    """Create a 2D scatter plot. Many of the optional arguements
    deal with formatting the plot.

    Args:
        x (list|array): container for x-axis data
        y (list|array): container for y-axis data
        file_path (str): path to save figure

    Kwargs:
        colors (str|list): either single color (e.g. 'blue') or a list
        size (int|list): int for marker size or a list of ints
        title (str): title for plot
        xlabel (str): x-axis label
        ylabel (str): y-axis label
    """
    plt.scatter(x, y, c=colors, s=size)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(file_path)
    plt.clf()  # clear figure