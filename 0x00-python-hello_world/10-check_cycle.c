#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if singly linked list is a cycle
 * Return: 0 if no cycle, 1 is yes
 */
int check_cycle(listint_t *list)
{
	/*
	 * Se crea dos variables para recorrer la lista "list" una itera de a 2
	 * y la otra de a 1
	 */
	listint_t *faster = list;
	listint_t *slow = list;

	if (!list)
	/*
	 * Chequeamos si la lista que nos pasan existe y sino existe la lista se
	 * retorna 0 y termina el prog
	 */
		return (0);

	while (1) /* Se crea un while infinito */
	{
		/* Traverse los nodos mientras que la linked list exista */
		if (faster->next != NULL && faster->next->next != NULL)
		{
			faster = faster->next->next; /* el mas rapido itera de a 2 */
			slow = slow->next; /* el mas lento itera de a 1 */

			if (faster == slow)
			/*
			 * si en algun momento son iguales retornar 1 ya que
			 * hay un ciclo
			 */
				return (1);
		}
		else
			return (0); /* Si no retornar 0 para salir del while infinito */
	}

}
