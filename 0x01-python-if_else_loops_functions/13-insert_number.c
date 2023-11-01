#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Function that add to a linked list
 * @head: The Pointer to head node
 * @number: The value to be added
 *
 * Return: the new Node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *temp, *move = NULL;

	if (*head == NULL)
		*head = malloc(sizeof(listint_t));
	temp = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;
	
	while (temp != NULL && temp->n < number)
	{
		move = temp;
		temp = temp->next;
	}

	if (move == NULL)
	{
		move->next = *head;
		*head = new;
	}
	else
	{
		move->next = new;
		new->next = temp;
	}

	return (new);
}
