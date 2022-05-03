#include "lists.h"

/**
 * is_palindrome - determine if singly linked list is palindrome
 * @head: pointer to head of singly linked list
 * Return: 0 if not, 1 if palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *aux = *head; /* Usamos una variable auxiliar para no tocar la lista (head) y no correr el
				* riesgo de perderla. */
	unsigned int size = 0, iter = 0, array[2000]; /* array le ponemos un valor fijo de 2000 para asegurarnos
						      * que tenga espacio */

	if (head == NULL) /* Si no existe la lista no es palindrome, return: 0 */
		return (0);

	if (*head == NULL) 
/**
 * Dereferenciamos la lista y nos fijamos si lo que esta adentro es NULL, en caso
 * de que sea NULL retornamos 1 ya que la letra nos dice que una lista vacia es considerada palindrome.
 */
		return (1);

	while (aux) /* Calculamos el tamaño de la linked list y lo guardamos en la variable: size */
	{
		aux = aux->next;
		size += 1;
	}
	if (size == 1) /* 1 solo nodo es considerado palindrome. */
		return (1);

	aux = *head;
	while (aux) /* Guardamos los valores de la lista en el array para luego compararlos. */
	{
		array[iter++] = aux->n; /* guardamos los datos */
		aux = aux->next; /* iteramos la linked list "aux" para ir guardando los datos en "array" */
	}

	iter = 0; /* seteamos iter en 0 */
	while (iter <= size / 2) /* se pone size/2 porque necesitas compararlo solo la mitad de las veces
				    porque se compara el primer elemento con el ultimo y asi hasta llegar a la mitad. */
        {
                if (array[iter] != array[size - iter - 1])
		/**
		 * Aca comparamos posiciones en el array, podemos hacer esto porque mas arriba copiamos la linked
		 * list dentro del "array". Comparamos la posicion 0 del array con la ultima posicion del array,
		 * ya que: array[size - iter - 1] en la primer iteracion es: 10 (size, el tamaño de la lista que nos
		 * pasan en el main) - 0 (iter arranca en 0) - 1 (esto es porque el size de la linked list te da 10
		 * pero en el array el ultimo elemento seria el 9 ya que se arranca a contar desde 0 en el "array"),
		 * por lo tanto daria: 9 y en la proxima iteracion: array[iter] seria: 1 y array[size - iter - 1] = 8
		 * y se van comparando los valores que estan en esas posiciones, si son distintos significa que no
		 * son palindromes, por lo tanto ponemos que se retorne 0. En caso que no sea palindrome ponemos afuera
		 * que retorne 1 ya que va a ser palindrome. */
                        return (0);
                iter++; /* incrementamos iter para ir iterando en el array */
        }
	return (1);
}
