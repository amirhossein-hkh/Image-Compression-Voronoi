# Image Compression Voronoi
A [Voronoi diagram](https://en.wikipedia.org/wiki/Voronoi_diagram) has many applications in computer science. This diagram partition the plane into regions. Each region has a site in it, which has a unique property. Each of the points in a particular region is closer to than site than the other sites. So the plane is divided into n regions if we have n sites.

One of its applications in computer science is image compression. To use the Voronoi diagram, first, we need to find our sites. There are multiple ways of doing so:
* Using random pixels in the image 
* Using gradients to figure out where are the edges
* Using inverse Voronoi

I used the second method. In this method, we should first compute the gradients of each image and use a threshold to make the image binary. Then, we should give non zero probability to the pixels around the edges and zero anywhere else. This way, only by having the row number, column number, and color of each site, we can restore the image.

| ![demo](docs/image.jpg) | 
|:--:| 
| *The right image was created with less than one-tenth of left image* |

## Todo
* Using optimise algorithms for constructing voronoi diagram (nlogn)
* Using more sophisticated ways for assigning probability to each pixel
