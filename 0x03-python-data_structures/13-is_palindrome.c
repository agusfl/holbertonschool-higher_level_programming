#include "lists.h"

/**
 * is_palindrome - determine if singly linked list is palindrome
 * @head: pointer to head of singly linked list
 * Return: 0 if not, 1 if palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *aux = *head;
	unsigned int size = 0, iter = 0, array[2000];

	if (head == NULL)
		return (0);

	if (*head == NULL)
		return (1);

	while (aux)
	{
		aux = aux->next;
		size += 1;
	}
	if (size == 1)
		return (1);

	aux = *head;
	while (aux)
	{
		array[iter++] = aux->n;
		aux = aux->next;
	}

	iter = 0;
	while (iter <= size / 2)
	{
		if (array[iter] == array[size - iter - 1])
			return (1);
		iter++;
	}
	return (0);
}
