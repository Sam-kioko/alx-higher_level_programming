#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int count = 0, *arr, i = 0, left = 0;
	int right = count - 1;

	while (current != NULL)
	{
		count++;
		current = current->next;
	}

	arr = malloc(sizeof(int) * count);

	if (arr == NULL)
		return 0;

	current = *head;

	while (current != NULL)
	{
		 arr[i] = current->n;
		 i++;
		 current = current->next;
	}

	while (left < right)
	{
		if (arr[left] != arr[right])
		{
			free(arr);
			return 0;
		}
		left++;
		right--;
	}

	free(arr);
	return (-1);
}
