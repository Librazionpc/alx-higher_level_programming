#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - Function that checks if a cycle exists in linked list
 *
 * @list: Pointer to the head pointer of the linked list
 *
 * Return: 1 on Success and 0 on Failure
 */

int check_cycle(listint_t *list)
{
	listint_t *head = NULL;
	listint_t *temp = NULL;

	if (list == NULL)
		return (0);

	while (temp != NULL && temp->next != NULL)
	{
		head = head->next;
		temp = temp->next->next;

		if (head == temp)
			return (1);
	}
	return (0);
}
