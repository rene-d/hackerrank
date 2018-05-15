// C > Structs and Enums > Boxes through a Tunnel
// Find the volume of short enough boxes.
//
// https://www.hackerrank.com/challenges/too-high-boxes/problem
//

#include <stdio.h>
#include <stdlib.h>
#define MAX_HEIGHT 41
// (skeliton_head) ----------------------------------------------------------------------

struct box
{
	/**
	* Define three fields of type int: length, width and height
	*/
    int     length;
    int     width;
    int     height;
};

typedef struct box box;

int get_volume(box b) {
	/**
	* Return the volume of the box
	*/
    return b.length * b.width * b.height;
}

int is_lower_than_max_height(box b) {
	/**
	* Return 1 if the box's height is lower than MAX_HEIGHT and 0 otherwise
	*/
    return b.height < MAX_HEIGHT;
}

// (skeliton_tail) ----------------------------------------------------------------------
int main()
{
	int n;
	scanf("%d", &n);
	box *boxes = malloc(n * sizeof(box));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &boxes[i].length, &boxes[i].width, &boxes[i].height);
	}
	for (int i = 0; i < n; i++) {
		if (is_lower_than_max_height(boxes[i])) {
			printf("%d\n", get_volume(boxes[i]));
		}
	}
	return 0;
}
