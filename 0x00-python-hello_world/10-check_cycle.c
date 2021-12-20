#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer of a structure listint_t
 *
 * Return: 1 if linked has a cycle, else return 0
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;

	if (list == NULL)
		return (0);
	temp = list->next;
	while (list)
	{
		while (temp)
		{
			if (temp == list)
				return (1);
			temp = temp->next;
		}
		list = list->next;
	}
	return (0);
}
