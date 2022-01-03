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
	listint_t *last;
	int length = 1, i = 0;
	int *arr;

	if (*head == NULL)
		return (1);
	last = *head;
	while (last->next)
	{
		last = last->next;
		length++;
	}
	arr = malloc(sizeof(int) * length);
	while ((*head))
	{
		arr[i] = (*head)->n;
		*head = (*head)->next;
		i++;
	}
	i = 0;
	while (i < length / 2)
	{
		if (arr[i] != arr[length - 1 - i])
		{
			free(arr);
			return (0);
		}
		i++;
	}
	free(arr);
	return (1);
}
