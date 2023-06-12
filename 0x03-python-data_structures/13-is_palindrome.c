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
	int tail = len - 1;
	int *arr = malloc(100 * sizeof(int));
	int i = 0;

	if (*head == NULL)
		return (1);
	while (counter != NULL)
	{
		len++;
		counter = counter->next;
	}
	printf("length = %d", len);
	arr = realloc(arr, (len * sizeof(int)));
	if (arr == NULL)
		return (1);
	counter = *head;
	while (counter)
	{
		arr[i] = counter->n;
		printf("array [%d] = %d \n", i, arr[i]);
		i++;
		counter = counter->next;
	}
	while (Head < tail)
	{
		if (arr[Head] != arr[tail])
		{
			free(arr);
			return(0);
		}
		Head++;
		tail--;
	}
	free(arr);
	return (1);
}
