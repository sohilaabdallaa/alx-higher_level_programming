#include"lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list:pointer tosingly linked list to be checked.
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *myself = list;
	listint_t *mynext = list;

	if (list != NULL && list->next != NULL)
		return (0);
	while (mynext->next && myself != NULL && mynext-> != NULL)
	{
		myself = myself->next;
		mynext = mynext->next->next;
		if (myself == mynext)
			return (1);
	}
	return (0);
}

