#include"lists.h"
#include <stdio.h>
#include <stdlib.h>
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *ptr;

	if (head == NULL || *head ==NULL)
		return (NULL);
	ptr = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return(NULL);
	new->n = number;
	while (number > ptr->n)
	{
		if (number < ptr->next->n)
			break;
		ptr = ptr->next;
	}
	new->next = ptr->next;
	ptr->next = new;
	return (new);
}
