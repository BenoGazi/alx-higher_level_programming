#include "lists.h"

/**
 * check_cycle - checks if a list has a cycle\
 * @list: Param
 * Return: Always Success
 */

int check_cycle(listint_t *list)
{
	listint_t *i;
	listint_t *j;

	if (!list || !list->next)
	{
		return (0);
	}
	i = list;
	j = list;
	while (i != NULL && j != NULL && i->next != NULL)
	{
		j = j->next;
		i = i->next->next;
		if (j == i)
		{
			return (1);
		}
	}
	return (0);
}
