#include"lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list:pointer tosingly linked list to be checked.
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *myself = NULL;
	listint_t *mynext = NULL;

	if (list == NULL)
		return (0);
	while (list->next && myself !=NULL && mynext)
	{
		myself = list->next;
		mynext = myself->next;
		if (myself == mynext)
			return (1);
	}
	return (0);
}

