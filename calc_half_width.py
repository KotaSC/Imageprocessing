import numpy as np
import cv2
import sys
args = sys.argv
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
from matplotlib import cycler

def main():

    colors = cycler('color', ['#EE6666', '#3388BB', '#9988DD', '#EECC55', '#88BB44', '#FFBBBB'])
    plt.rc('axes',  facecolor='#E6E6E6', edgecolor='black', axisbelow=True, grid=False, prop_cycle=colors)
    plt.rc('grid',  color='w', linestyle='solid')
    plt.rc('xtick', direction='in', color='black')
    plt.rc('ytick', direction='in', color='black')
    plt.rc('patch', edgecolor='#E6E6E6')
    plt.rc('lines', linewidth=2)
    
    plt.rcParams["xtick.major.size"] = 10
    plt.rcParams["xtick.minor.size"] = 5
    plt.rcParams["ytick.major.size"] = 10
    plt.rcParams["ytick.minor.size"] = 5
    plt.rcParams["font.size"]        = 14

    image_nonThinning = args[1]

    # 入力画像を読み込み
    img_nonthinning = cv2.imread( image_nonThinning )

    # グレースケール変換
    gray_nonThinning = cv2.cvtColor( img_nonthinning, cv2.COLOR_RGB2GRAY )
  
    # 画像の縦幅と横幅を求める
    height, width = gray_nonThinning.shape[0], gray_nonThinning.shape[1]

    val_NonThinning = calc_half_width( gray_nonThinning, height, width )

    plt.figure( figsize=(10, 8) )
    ax = plt.axes( facecolor='w')
    ax.set_axisbelow( True )

    ax.set_xlim([0, height])
    ax.set_ylim([0, 255])

    plt.xticks([5, 10, 15, 20, 25])

    ax.plot( val_NonThinning, color='black', marker='.', markersize=15 )
   
    # ax.legend( fontsize=20, flameon=True )

    ax.set_xlabel("Vertical component of the edge", fontsize=20, color='black')
    ax.set_ylabel("Pixel Value", fontsize=20, color='black')

    fig_name = args[2]

    plt.savefig( fig_name )
    plt.show()

def calc_half_width( gray, h, w ):

	value = []

	for y in range( h ):

		sumx = 0

		for x in range( w ):

			# x軸方向の画素値の合計を求める
			sumx += gray[ y, x ]

		value.append( sumx / w )

	return value

if __name__ == "__main__":
    main()