#include "lists.h"

/**
*check_cycle - check if the singly list contain a cycle or not
*@list: pointer to a singly list
*
*Return: 1 if successed, otherwise 0
*/

int check_cycle(listint_t *list)
{
	listint_t *start, *new;

	if (list == NULL || list->next == NULL)
		return (0);

	start = new = list;
	while (start && new && new->next)
	{
		start = start->next;
		new = new->next->next;
		if (start == new)
			return (1);
	}
	return (0);
}
