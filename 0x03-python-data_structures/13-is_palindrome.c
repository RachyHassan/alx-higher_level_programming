#include "lists.h"
listint_t *reverse_list(listint_t **head);
int palindrome(listint_t **head);

/**
 * reverse_list- a function to reverse the second half of a linked list
 * @head: pointer to the begining of the list
 * Return: pointer to head
 */

listint_t *reverse_list(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;
	
	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * palindrome - checks if the list is a palindrome
 * @head: a pointer to the begining of the list
 * Return: 0 if the list is not a palindrome
 * and 1 if it is a palindrome.
 */

int palindrome(listint_t **head)
{
	listint_t *tmp, *rev, *mid;

	size_t len = 0, n;

	if (*head == NULL || (*head)->next == NULL)
		return(1);

	tmp = *head;
	while (tmp)
	{
		len++;
		tmp = tmp->next;
	}

	tmp = *head;
	for (n = 0; n < (len / 2) - 1; n++)
		tmp = tmp->next;

	if ((len % 2) == 0 && tmp -> n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	rev = reverse_list(&tmp);
	mid = rev;

	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
	reverse_list(&mid);

	return (1);
}
