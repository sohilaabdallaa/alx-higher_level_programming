#include"lists.h"
#include <stddef.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: double pointer to the head of list.
 * Return:0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *counter = *head;
	int len = 0;
	int Head = 0;
	int tail = 0;
	int *arr = malloc(100 * sizeof(int));
	int i = 0;

	if (*head == NULL)
		return (1);
	if (arr == NULL)
		return (1);

	while (counter != NULL)
	{
		len++;
		arr = realloc(arr, (len * sizeof(int)));
		arr[i] = counter->n;
		i++;
		counter = counter->next;
	}
	tail = len - 1;
	while (Head < tail)
	{
		if (arr[Head] != arr[tail])
		{
			free(arr);
			return (0);
		}
		else
		{
			Head++;
			tail--;
		}
	}
	free(arr);
	return (0);
}
