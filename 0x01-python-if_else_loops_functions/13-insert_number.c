#include"lists.h"
#include <stdio.h>
#include <stdlib.h>
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *ptr;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
		return(new);
	}
	if (number < 0)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	ptr = *head;
	while (number > ptr->n && ptr->next)
	{
		if (number < ptr->next->n)
			break;
		ptr = ptr->next;
	}
	new->next = ptr->next;
	ptr->next = new;
	return (new);
}
