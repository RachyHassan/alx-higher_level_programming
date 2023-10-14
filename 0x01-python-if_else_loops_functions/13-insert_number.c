#include "lists.h"
#include <stddef.h>
#include <stdio.h>

/**
 * insert_node - this inserts a new number into a sorted linked list
 * @head: pointer to the begining of the list
 * @number: number to be added
 * Return: pointer to the new node if successful
 * otherwise, NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;
	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;
	new->next = node->next;
	node->next = new;

	return (new);
}
