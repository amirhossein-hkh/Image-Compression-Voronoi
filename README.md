# Image Compression Voronoi
Voronoi diagram has many applications in computer science. This diagram partition the plane into regions. Each region has a site in it, which has a special property. Each of the points in a particular region is closer to than site than the other sites. So the plane is divided into n regions, if we have n sites.

One of its application in computer science is image compression. To use Voronoi diagram, first, we need to find our sites. There are multiple ways of doing so:
* Using random pixels in the image 
* Using gradients to figure out where are the edges
* Using inverse Voronoi

I used the second method. In this method, we should first compute the gradients of each images and use threshold to make the image binary. Then, we should giving non zero probability to the pixels around the edges and zero anywhere else. This way only by having the row number, column number and color of each site, we are able to restore the image.
