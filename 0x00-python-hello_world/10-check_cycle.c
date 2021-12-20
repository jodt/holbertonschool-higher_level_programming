#include "lists.h"
int check_cycle(listint_t *list)
{
    listint_t *temp;
    temp = list->next;
    while (list)
    {
        while (temp)
        {
            if (temp == list)
                return 1;
            temp = temp->next;
        }
        list = list->next;
    }
    return 0;
}