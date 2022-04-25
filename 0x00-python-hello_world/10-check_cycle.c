#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if singly linked list is a cycle
 * Return: 0 if no cycle, 1 is yes
 */
int check_cycle(listint_t *list)
{
	listint_t *faster = list;
	listint_t *slow = list;

	if (!list) /* Si no existe la lista retornar 0*/
		return (0);

	while (1) /* while infinito */
	{
		/* Traverse los nodos mientras que la linked list exista */
		if (faster->next != NULL && faster->next->next != NULL)
		{
			faster = faster->next->next; /* el mas rapido itera de a 2 */
			slow = slow->next; /* itera de a 1 */

			if (faster == slow) /* si son iguales retornar 1 ya que hay un ciclo */
				return (1);
		}
		else
			return (0); /* Si no retornar 0 para salir del while infinito */
	}

}
