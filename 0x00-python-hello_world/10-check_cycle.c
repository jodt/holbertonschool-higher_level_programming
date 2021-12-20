#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer of a structure listint_t
 *
 * Return: 1 if linked has a cycle, else return 0
 */
int check_cycle(listint_t *list)
{
	listint_t *temp1, *temp2;

	temp1 = temp2 = list;

	while (temp2 && temp2->next)
	{
		temp1 = temp1->next;
		temp2 = temp2->next->next;
		if (temp1 == temp2)
			return (1);
	}
	return (0);
}
