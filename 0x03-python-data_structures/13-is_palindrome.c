#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - check if linked list is a palindrome
 * @head: address of a pointer on the first element fo the list
 *
 * Return: 1 if the list is a plaindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *last, *first;
	int length = 1, count = 0, idx;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	last = first = *head;
	while (last->next)
	{
		last = last->next;
		length++;
	}
	while (first->n == last->n)
	{
		idx = 1;
		count++;
		first = first->next;
		last = *head;
		while (idx != length - count)
		{
			last = last->next;
			idx++;
		}
		if (idx - count == 0)
			return (1);
	}
	return (0);
}
