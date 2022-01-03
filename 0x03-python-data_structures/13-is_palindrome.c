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
	listint_t *first, *last;
	int length = 0, i = 0, idx;

	if (*head)
	{
		first = last = *head;
		while (last->next)
		{
			last = last->next;
			length++;
		}
		while (i < ((length / 2)))
		{
			idx = 0;
			if (first->n != last->n)
				return (0);
			first = first->next;
			last = *head;
			i++;
			while (idx != length - i)
			{
				last = last->next;
				idx++;
			}
		}
	}
	return (1);
}
