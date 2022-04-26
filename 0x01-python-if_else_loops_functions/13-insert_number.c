#include "lists.h"

/**
 *insert_node - insert a node into a sored sinlgy linked list
 *@head: pointer to the list
 *@number: number to add to the sorted list
 *Return: pointer to the sorted list
 **/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *aux = *head, *last_node = NULL;

	new_node = malloc(sizeof(listint_t)); /*space for the new node*/
	if (new_node == NULL) /*check there is no error assigning memory*/
		return (NULL);
	new_node->n = number;
	if (*head == NULL)
	{
		*head = new_node;
		new_node->next = NULL;
	}
	else
	{
		while (number > aux->n && aux->next != NULL)
		{
			last_node = aux;
			aux = aux->next;
		}
		if (number > aux->n)
		{
			aux->next = new_node;
			new_node->next = NULL;
		}
		else if (last_node == NULL)
		{
			new_node->next = *head;
			*head = new_node;
		}
		else
		{
			new_node->next = aux;
			last_node->next = new_node;
		}
	}
	return (*head);
}
