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


	if (!*head || !head)
		return (NULL);

	node = malloc(sizeof(listint_t));

	node->n = number;
	node->next = NULL;
	if (!*head || (*head)->n >= node->n)
	{
		node->next = *head;
		*head = node;
	}
	else
	{
		current = *head;
		while (current->next && current->next->n < node->n)
			current = current->next;
		node->next = current->next;
		current->next = node;
	}

	return (node);
}
