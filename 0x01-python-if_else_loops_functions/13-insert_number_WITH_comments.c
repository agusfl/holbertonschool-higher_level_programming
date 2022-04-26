#include "lists.h"

/**
 *insert_node - insert a node into a sored sinlgy linked list
 *@head: pointer to the list
 *@number: number to add to the sorted list
 *Return: pointer to the sorted list

--> Esta es una funcion para insertar un numero en una lista ordenada osea si nos pasan el 27 se tiene que agregar entre
un numero menor al 27 y un numero mayor al 27, y si no hay ningun numero mayor tiene que ponerse al final y si no hay ningun
numero menor tiene que ponerse al principio.

 **/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *aux = *head, *last_node = NULL;
	/* Creamos 3 variables, un nuevo nodo (new_node) para almacenar el numero que hay que agregar en la lista ordenada 
	 Creamos una variable auxiliar (aux) para no perder puntero *head. */

	new_node = malloc(sizeof(listint_t)); /*space for the new node*/
	if (new_node == NULL) /*check there is no error assigning memory*/
		return (NULL);
	new_node->n = number; /* En caso que no se retorno null y no hay problemas de memoria asignamos el numero que nos
				 pasen al elemento 'n' de nuestro nuevo nodo: new_node. */
	if (*head == NULL)
	{
		*head = new_node;
		new_node->next = NULL;
	/* Si el head es null significa que la lista esta vacia por lo tanto agregamos el nuevo nodo a la lista, esto
	 * lo hacemos apuntando head (que es lo que apunta al inicio de la lista) al nuevo nodo y despues poniendo que el
	 * nuevo nodo apunte a NULL ya que no hay nada mas en la lista. */
	}
	else
	/* Si la lista no esta vacia entonces pasamos a analizar donde tenemos que agregar el nuevo nodo */
	{
		while (number > aux->n && aux->next != NULL)
		{
			last_node = aux;
			aux = aux->next;
		/* Aca hacemos un while para que se recorra siempre y cuando el numero sea mayor a lo que estas parado ahora
		 * ya que aux la habiamos igualado a head para iterar sobre aux y no sobre head. Y la otra condicion que
		 * ponemos es que el proximo nodo sea distinto de NULL, estas dos condiciones son para iterar toda la lista.
		 * Dentro del while ponemos que last_node (seria el nodo anterior, osea el numero mas chico del que queremos
		 * agregar, en el caso del ejemplo seria el 4 ya que el ultimo numero mas chico que 27 es el 4. */
		}
		if (number > aux->n) /* Esto para saber si se salio del while porque no se encontro un numero que fuese
		mas grande que nuestro "number" no es el caso del ejemplo (ya que es 27) pero si fuera 2500 el numero
		este seria mas grande que 1024 (que es el numero mas grande de la lista que ponen en el ejemplo del main)
		entonces lo que vamos a indicar es que el aux->next va a ser el nuevo nodo (ya que va a ser el final de
		la lista) y ponemos que el nuevo nodo apunte a NULL para indicar que es el final de la lista. */
		{
			aux->next = new_node;
			new_node->next = NULL;
		}
		else if (last_node == NULL) /* Si el last_node es NULL significa que nunca entro al while ya que una de las
		condiciones que habiamos puesto para que entre era: number > aux->n osea el numero (number) es menor al
		primer numero ordenado de la lista (ya que en el main los numeros que van agregando a la lista los ponen
		de forma ordenada de menor a  mayor) en este caso hay que agregar el nodo al inicio de la lista ya que
		va a ser el numero mas chico por lo tanto hacemos que el nuevo nodo apunte al inicio de la lista (head)
		y despues pones que el head (inicio de la lista) pase a ser el nuevo nodo, se tiene que hacer en este orden
		para no perder la referencia a la lista, porque si primero apuntaramos head al neuvo nodo perderiamos la
		referencia de toda la lista a la que viene apuntando head. */
		{
			new_node->next = *head;
			*head = new_node;
		}
		else /* Este es para el ulitmo caso que nos quedaria por analizar, osea que el numero no vaya ni al inicio ni
			al final (por ende en el medio). En dicho caso el nuevo nodo lo apuntamos al auxiliar (el auxiliar
			venia apuntando al nodo mas grande del numero que queremos agregar con el nuevo nodo y despues
			apuntamos el last_node al nuevo nodo para asi terminar de "cerrar" la linked lista, ya que el
			last_node venia apuntando al numero mas chico que el nuevo numero que queremos agregar con el
			nuevo nodo, de esta forma agregamos el nuevo nodo sin perder niguna parte de la lista. */
		{
			new_node->next = aux;
			last_node->next = new_node;
		}
	}
	return (*head); /* Por ultimo devolvemos un puntero al inicio de la lista que la misma contiene el nuevo nodo que
			   se agrego a la lista de forma ordenada de menor a mayor. */
}
