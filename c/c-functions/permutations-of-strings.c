// C > Functions > Permutations of Strings
// Find all permutations of the string array.
//
// https://www.hackerrank.com/challenges/permutations-of-strings/problem
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int next_permutation(int n, char **s)
{
	/**
	* Complete this method
	* Return 0 when there is no next permutation and 1 otherwise
	* Modify array s to its next permutation
	*/

    if (n <= 1)
        return 0;

    // 1. Find the largest index k such that a[k] < a[k + 1]
	int i = n - 1;
	while (i > 0 && strcmp(s[i - 1], s[i]) >= 0)
		i--;

    // If no such index exists, the permutation is the last permutation
	if (i == 0)
		return 0;

	// 2. Find the largest index l greater than k such that a[k] < a[l]
	int j = n - 1;
	while (strcmp(s[j], s[i - 1]) <= 0)
		j--;

    // 3. Swap the value of a[k] with that of a[l].
	char *temp = s[i - 1];
	s[i - 1] = s[j];
	s[j] = temp;

	// 4. Reverse the sequence from a[k + 1] up to and including the final element a[n]
	j = n - 1;
	while (i < j)
    {
		temp = s[i];
		s[i] = s[j];
		s[j] = temp;
		i++;
		j--;
	}

	return 1;
}

// (skeliton_tail) ----------------------------------------------------------------------
int main()
{
	char **s;
	int n;
	scanf("%d", &n);
	s = calloc(n, sizeof(char*));
	for (int i = 0; i < n; i++)
	{
		s[i] = calloc(11, sizeof(char));
		scanf("%s", s[i]);
	}
	do
	{
		for (int i = 0; i < n; i++)
			printf("%s%c", s[i], i == n - 1 ? '\n' : ' ');
	} while (next_permutation(n, s));
	for (int i = 0; i < n; i++)
		free(s[i]);
	free(s);
	return 0;
}
