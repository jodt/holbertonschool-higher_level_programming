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
			return (NULL);

	while (number > ptr->n)
		ptr = ptr->next;
	new = ptr;
	new->n = number;
	new->next = ptr->next;
	return (new);
}
