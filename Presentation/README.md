## Installation

To install a stable version of this theme, please refer to update instructions
of your TeX distribution. Trigon has been on
[CTAN](https://ctan.org/pkg/beamertheme-trigon) since March 2021. For users of
typical TeX distributions (TexLive, MacTeX, MikTeX), simply updating your
package list should install Trigon on your system.

If you want to use the cutting-edge development version of Trigon, you can
install it manually by following these steps:

1. **Download the source** using a `git clone` of the [Trigon
   repository](https://gitlab.com/thlamb/beamertheme-trigon) or as a [zip
   archive](https://gitlab.com/thlamb/beamertheme-trigon/-/archive/master/beamertheme-trigon-master.zip)
2. **Compile the style files** by running `make sty` inside the downloaded
   directory. (Or run LaTeX directly on `source/trigontheme.ins`.)
3. **Move the resulting `*.sty` files** to the folder containing your
   presentation. To use Trigon with many presentations, run `make install` or
   move the `*.sty` files to a folder in your TeX path instead.
4. **Use the theme** by declaring `\usetheme{trigon}` in the preamble of your
   document.
