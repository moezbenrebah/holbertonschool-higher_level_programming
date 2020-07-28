#include "lists.h"

/**
 * insert_node - insert a number into a sorted linked list
 * @head: a pointer to data stored in head node
 * @number: integer to insert
 *
 * Return: a pointer to node inserted, NULL otherwise
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *current = NULL;


	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = number;
	current = *head;
	if (!current || current->n >= number)
	{
		node->next = current;
		*head = node;
		return (node);
	}
	while (current && current->next && current->next->n < number)
		current = current->next;
	node->next = current->next;
	current->next = node;

	return (node);
}
