# Gifs Gifs Everywhere (GGE)

Given a local file and currently an involved breakdown file,
make any number of gifs, sized and cropped the way you desire

## Getting Started

In the repository run cat breakdownFile.txt | python gge.py

### Prerequisites

You will need to have installed moviepi (https://zulko.github.io/moviepy/install)

### Installing
As of now clone into the repository. 


### Breakdown file

Included is a breakdown file. 
The important order is 
pathToVideo
True/False
x1 y1 x2 y2
t1 t2 .... tn

The True/False is if you wish to clip area of gif.
If True the next line should be the points to clip.

The last line are seconds included in each gif. 
t1 is the starting t2 ending of the first gif.
t2 t3 are the second gif. This follows.

The implication of this is that you are capturing everything between t1 and tn.

## Built With

* [MoviePi](https://zulko.github.io/moviepy/install) - Library Used

## Authors

* **Madeline Cook** - *Initial work* - [MadCook](https://github.com/MadCook)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Could not have done this without the help of this guide [Making animated gifs from video files with python](http://zulko.github.io/blog/2014/01/23/making-animated-gifs-from-video-files-with-python/)


